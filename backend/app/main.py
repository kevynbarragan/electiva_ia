from __future__ import annotations
import os, io, uuid, json
from pathlib import Path
from datetime import datetime, timedelta, timezone
from typing import Optional

import numpy as np
import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import create_engine, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session
from passlib.context import CryptContext
from jose import jwt, JWTError

load_dotenv()
ROOT = Path(__file__).resolve().parent.parent
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./insightbuy.db")
CONNECT_ARGS = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=CONNECT_ARGS, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
JWT_SECRET = os.getenv("JWT_SECRET", "DEV_ONLY_CHANGE_THIS_SECRET")
JWT_ALGORITHM = "HS256"
TOKEN_MINUTES = int(os.getenv("ACCESS_TOKEN_MINUTES", "720"))
MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", "25"))
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    password_hash: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Dataset(Base):
    __tablename__ = "datasets"
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    filename: Mapped[str] = mapped_column(String(255))
    raw_csv: Mapped[str] = mapped_column(Text)
    working_csv: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Decision(Base):
    __tablename__ = "cleaning_decisions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dataset_id: Mapped[str] = mapped_column(ForeignKey("datasets.id"), index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    action: Mapped[str] = mapped_column(String(100))
    details: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def read_csv_text(text: str) -> pd.DataFrame:
    try:
        return pd.read_csv(io.StringIO(text), low_memory=False)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"No se pudo leer el CSV. Verifica separador y codificación. Detalle: {e}")

def profile_df(df: pd.DataFrame) -> dict:
    rows, cols = df.shape
    missing = []
    for col in df.columns:
        nulls = int(df[col].isna().sum())
        blanks = int(df[col].astype("string").str.strip().eq("").fillna(False).sum())
        total_missing = int((df[col].isna() | df[col].astype("string").str.strip().eq("").fillna(False)).sum())
        missing.append({"column": str(col), "missing": total_missing, "missing_percent": round(total_missing / max(rows, 1) * 100, 2), "blank_cells": blanks, "dtype": str(df[col].dtype)})
    numeric = df.select_dtypes(include=np.number)
    numeric_stats = {}
    for col in numeric.columns:
        s = numeric[col].replace([np.inf, -np.inf], np.nan).dropna()
        if len(s):
            q1, q3 = s.quantile([.25, .75]).tolist()
            numeric_stats[str(col)] = {
                "count": int(s.count()), "mean": round(float(s.mean()), 4),
                "median": round(float(s.median()), 4), "std": round(float(s.std()), 4) if len(s)>1 else 0,
                "min": round(float(s.min()), 4), "q1": round(float(q1), 4),
                "q3": round(float(q3), 4), "max": round(float(s.max()), 4),
                "outlier_candidates_iqr": int(((s < q1 - 1.5*(q3-q1)) | (s > q3 + 1.5*(q3-q1))).sum())
            }
    cat_stats = {}
    for col in df.columns:
        if col not in numeric.columns:
            vc = df[col].astype("string").fillna("(nulo)").value_counts().head(8)
            cat_stats[str(col)] = [{"value": str(k), "count": int(v)} for k,v in vc.items()]
    return {
        "rows": int(rows), "columns": int(cols), "duplicate_rows": int(df.duplicated().sum()),
        "column_names": [str(c) for c in df.columns], "missing": missing,
        "numeric_stats": numeric_stats, "categorical_stats": cat_stats,
        "memory_bytes": int(df.memory_usage(deep=True).sum())
    }

def recommendations(df: pd.DataFrame) -> list[dict]:
    recs = []
    blank_cols = []
    for col in df.columns:
        blank = df[col].astype("string").str.strip().eq("").fillna(False)
        missing = df[col].isna() | blank
        n = int(missing.sum())
        if n:
            recs.append({"id": f"missing:{col}", "action": "fill_missing_median" if pd.api.types.is_numeric_dtype(df[col]) else "fill_missing_mode", "column": str(col), "count": n, "label": f"Tratar {n} valores faltantes en «{col}»", "reason": "Los valores vacíos o nulos pueden afectar estadísticas y modelos. Se propone mediana para columnas numéricas y moda para columnas no numéricas."})
    duplicates = int(df.duplicated().sum())
    if duplicates:
        recs.append({"id": "duplicates:all", "action": "drop_duplicates", "column": None, "count": duplicates, "label": f"Eliminar {duplicates} filas idénticas duplicadas", "reason": "Son filas completamente iguales. Confirma que una fila idéntica no represente una repetición válida del negocio."})
    for col in df.select_dtypes(include=np.number).columns:
        s = df[col].dropna()
        if len(s) >= 4:
            q1, q3 = s.quantile([.25,.75])
            n = int(((s < q1 - 1.5*(q3-q1)) | (s > q3 + 1.5*(q3-q1))).sum())
            if n:
                recs.append({"id": f"outliers:{col}", "action": "review_outliers", "column": str(col), "count": n, "label": f"Revisar {n} posibles valores atípicos en «{col}»", "reason": "Candidatos identificados mediante el rango intercuartílico (IQR). No se eliminan automáticamente porque podrían ser observaciones reales."})
    return recs

class RegisterIn(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)

class LoginIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=72)

class CleanIn(BaseModel):
    actions: list[str] = Field(default_factory=list)

app = FastAPI(title="INSIGHTBUY API", version="1.0.0", description="API para calidad de datos y análisis exploratorio.")
origins = [x.strip() for x in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",") if x.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def token_for(user: User):
    exp = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_MINUTES)
    return jwt.encode({"sub": str(user.id), "email": user.email, "exp": exp}, JWT_SECRET, algorithm=JWT_ALGORITHM)

def current_user(authorization: Optional[str] = Header(default=None), db: Session = Depends(get_db)) -> User:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Debes iniciar sesión.")
    token = authorization.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = int(payload.get("sub", ""))
    except (JWTError, ValueError, TypeError):
        raise HTTPException(status_code=401, detail="Sesión inválida o vencida.")
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado.")
    return user

def owned_dataset(dataset_id: str, user: User, db: Session) -> Dataset:
    ds = db.get(Dataset, dataset_id)
    if not ds or ds.user_id != user.id:
        raise HTTPException(status_code=404, detail="Dataset no encontrado.")
    return ds

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "INSIGHTBUY API"}

@app.post("/api/auth/register")
def register(data: RegisterIn, db: Session = Depends(get_db)):
    email = data.email.lower().strip()
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=409, detail="Ya existe una cuenta con ese correo.")
    user = User(name=data.name.strip(), email=email, password_hash=pwd_context.hash(data.password))
    db.add(user); db.commit(); db.refresh(user)
    return {"token": token_for(user), "user": {"id": user.id, "name": user.name, "email": user.email}}

@app.post("/api/auth/login")
def login(data: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email.lower().strip()).first()
    if not user or not pwd_context.verify(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos.")
    return {"token": token_for(user), "user": {"id": user.id, "name": user.name, "email": user.email}}

@app.get("/api/auth/me")
def me(user: User = Depends(current_user)):
    return {"id": user.id, "name": user.name, "email": user.email}

@app.post("/api/datasets/upload")
async def upload_dataset(file: UploadFile = File(...), user: User = Depends(current_user), db: Session = Depends(get_db)):
    filename = Path(file.filename or "dataset.csv").name
    if not filename.lower().endswith(".csv"):
        raise HTTPException(status_code=415, detail="Solo se admiten archivos .csv.")
    raw = await file.read(MAX_UPLOAD_MB * 1024 * 1024 + 1)
    if len(raw) > MAX_UPLOAD_MB * 1024 * 1024:
        raise HTTPException(status_code=413, detail=f"El archivo supera el límite de {MAX_UPLOAD_MB} MB.")
    if not raw:
        raise HTTPException(status_code=422, detail="El archivo está vacío.")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        try: text = raw.decode("latin-1")
        except Exception: raise HTTPException(status_code=422, detail="No se pudo decodificar el archivo.")
    df = read_csv_text(text)
    if df.empty or len(df.columns) == 0:
        raise HTTPException(status_code=422, detail="El CSV no contiene filas o columnas utilizables.")
    ds_id = str(uuid.uuid4())
    ds = Dataset(id=ds_id, user_id=user.id, filename=filename, raw_csv=text, working_csv=df.to_csv(index=False))
    db.add(ds); db.commit()
    return {"id": ds_id, "filename": filename, "profile": profile_df(df), "recommendations": recommendations(df), "preview": df.head(10).replace({np.nan: None}).to_dict(orient="records")}

@app.get("/api/datasets")
def list_datasets(user: User = Depends(current_user), db: Session = Depends(get_db)):
    rows = db.query(Dataset).filter(Dataset.user_id == user.id).order_by(Dataset.created_at.desc()).all()
    return [{"id": x.id, "filename": x.filename, "created_at": x.created_at.isoformat()} for x in rows]

@app.get("/api/datasets/{dataset_id}")
def get_dataset(dataset_id: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    ds = owned_dataset(dataset_id, user, db)
    df = read_csv_text(ds.working_csv)
    return {"id": ds.id, "filename": ds.filename, "profile": profile_df(df), "recommendations": recommendations(df), "preview": df.head(10).replace({np.nan: None}).to_dict(orient="records")}

@app.post("/api/datasets/{dataset_id}/clean")
def clean_dataset(dataset_id: str, data: CleanIn, user: User = Depends(current_user), db: Session = Depends(get_db)):
    ds = owned_dataset(dataset_id, user, db)
    df = read_csv_text(ds.working_csv)
    recs = recommendations(df)
    allowed = {r["id"]: r for r in recs}
    selected = [allowed[x] for x in data.actions if x in allowed]
    if not selected:
        raise HTTPException(status_code=400, detail="Selecciona al menos una recomendación válida.")
    applied = []
    for rec in selected:
        action, col = rec["action"], rec["column"]
        if action == "fill_missing_median":
            df[col] = df[col].replace(r"^\s*$", np.nan, regex=True)
            df[col] = pd.to_numeric(df[col], errors="coerce")
            median = df[col].median()
            if pd.notna(median): df[col] = df[col].fillna(median)
            else: applied.append({"id": rec["id"], "status": "omitida", "reason": "No se pudo calcular una mediana válida."}); continue
        elif action == "fill_missing_mode":
            df[col] = df[col].replace(r"^\s*$", np.nan, regex=True)
            mode = df[col].mode(dropna=True)
            fill = mode.iloc[0] if len(mode) else "Sin dato"
            df[col] = df[col].fillna(fill)
        elif action == "drop_duplicates":
            before = len(df); df = df.drop_duplicates().reset_index(drop=True)
            applied.append({"id": rec["id"], "status": "aplicada", "rows_removed": before-len(df)})
            continue
        elif action == "review_outliers":
            applied.append({"id": rec["id"], "status": "solo_revisada", "reason": "No se modificaron valores atípicos automáticamente."})
            continue
        applied.append({"id": rec["id"], "status": "aplicada"})
    ds.working_csv = df.to_csv(index=False)
    for item in applied:
        db.add(Decision(dataset_id=ds.id, user_id=user.id, action=item["id"], details=json.dumps(item, ensure_ascii=False)))
    db.commit()
    return {"message": "Proceso finalizado. Revisa el resultado antes de continuar.", "applied": applied, "profile": profile_df(df), "recommendations": recommendations(df)}

@app.get("/api/datasets/{dataset_id}/download")
def download_dataset(dataset_id: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    ds = owned_dataset(dataset_id, user, db)
    return StreamingResponse(io.BytesIO(ds.working_csv.encode("utf-8-sig")), media_type="text/csv; charset=utf-8", headers={"Content-Disposition": f'attachment; filename="limpio_{Path(ds.filename).stem}.csv"'})

@app.get("/api/datasets/{dataset_id}/eda")
def eda(dataset_id: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    ds = owned_dataset(dataset_id, user, db)
    df = read_csv_text(ds.working_csv)
    numeric = df.select_dtypes(include=np.number)
    corr = {}
    if len(numeric.columns) >= 2:
        matrix = numeric.corr(numeric_only=True).round(4).replace({np.nan: None})
        corr = {"columns": [str(c) for c in matrix.columns], "matrix": matrix.values.tolist()}
    distributions = {}
    for col in numeric.columns[:12]:
        s = numeric[col].dropna()
        if len(s):
            counts, edges = np.histogram(s, bins=min(10, max(3, int(np.sqrt(len(s))))))
            distributions[str(col)] = [{"range": f"{edges[i]:.3g} – {edges[i+1]:.3g}", "count": int(counts[i])} for i in range(len(counts))]
    categorical = {}
    for col in df.columns:
        if col not in numeric.columns:
            vc = df[col].astype("string").fillna("(nulo)").value_counts().head(10)
            categorical[str(col)] = [{"value": str(k), "count": int(v)} for k,v in vc.items()]
    findings = []
    p = profile_df(df)
    if p["duplicate_rows"]:
        findings.append(f"Se detectan {p['duplicate_rows']} filas completamente duplicadas; valida si son registros repetidos legítimos.")
    for m in p["missing"]:
        if m["missing"]:
            findings.append(f"La columna «{m['column']}» tiene {m['missing']} valores faltantes ({m['missing_percent']}%).")
    for col, stats in p["numeric_stats"].items():
        if stats["outlier_candidates_iqr"]:
            findings.append(f"«{col}» tiene {stats['outlier_candidates_iqr']} candidatos a valores atípicos por IQR; deben revisarse con contexto.")
    if not findings:
        findings.append("No se detectaron faltantes ni duplicados exactos en el perfil básico. Revisa los gráficos y el contexto del negocio.")
    return {"profile": p, "correlation": corr, "distributions": distributions, "categorical": categorical, "findings": findings, "preview": df.head(15).replace({np.nan: None}).to_dict(orient="records")}

@app.get("/api/datasets/{dataset_id}/decisions")
def decisions(dataset_id: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    owned_dataset(dataset_id, user, db)
    rows = db.query(Decision).filter(Decision.dataset_id == dataset_id, Decision.user_id == user.id).order_by(Decision.created_at.desc()).all()
    return [{"id": x.id, "action": x.action, "details": json.loads(x.details), "created_at": x.created_at.isoformat()} for x in rows]
