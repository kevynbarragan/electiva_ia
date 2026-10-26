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


class DatasetVersion(Base):
    __tablename__ = "dataset_versions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    dataset_id: Mapped[str] = mapped_column(ForeignKey("datasets.id"), index=True)
    version: Mapped[int] = mapped_column(Integer)
    csv_text: Mapped[str] = mapped_column(Text)
    summary: Mapped[str] = mapped_column(Text, default="{}")
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class CleaningOperation(Base):
    __tablename__ = "cleaning_operations"
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    dataset_id: Mapped[str] = mapped_column(ForeignKey("datasets.id"), index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    idempotency_key: Mapped[str] = mapped_column(String(100), index=True)
    source_version: Mapped[int] = mapped_column(Integer)
    action: Mapped[str] = mapped_column(String(50))
    column_name: Mapped[str] = mapped_column(String(255), default="")
    row_ids_json: Mapped[str] = mapped_column(Text, default="[]")
    params_json: Mapped[str] = mapped_column(Text, default="{}")
    preview_json: Mapped[str] = mapped_column(Text, default="{}")
    result_json: Mapped[str] = mapped_column(Text, default="{}")
    status: Mapped[str] = mapped_column(String(40), default="preview")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    confirmed_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class AnalysisExclusion(Base):
    __tablename__ = "analysis_exclusions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    dataset_id: Mapped[str] = mapped_column(ForeignKey("datasets.id"), index=True)
    version: Mapped[int] = mapped_column(Integer)
    operation_id: Mapped[str] = mapped_column(String(36), index=True)
    row_ids_json: Mapped[str] = mapped_column(Text, default="[]")
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
    # Detect possible type inconsistencies conservatively; categorical codes are not converted automatically.
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]) or pd.api.types.is_bool_dtype(df[col]):
            continue
        nonblank = df[col].dropna().astype("string").str.strip()
        nonblank = nonblank[nonblank.ne("")]
        if len(nonblank) < 4:
            continue
        parsed = pd.to_numeric(nonblank, errors="coerce")
        valid_n = int(parsed.notna().sum())
        invalid_n = int(parsed.isna().sum())
        if valid_n >= 3 and invalid_n > 0 and valid_n / len(nonblank) >= 0.5:
            recs.append({"id": f"invalid_type:{col}", "action": "review_invalid_type", "column": str(col), "count": invalid_n, "label": f"Revisar {invalid_n} valores incompatibles con número en «{col}»", "reason": "La columna mezcla valores convertibles a número y valores no convertibles. Puede ser un tipo inconsistente o una variable categórica; no se convertirá automáticamente."})
    duplicates = int(df.duplicated().sum())
    if duplicates:
        recs.append({"id": "duplicates:all", "action": "drop_duplicates", "column": None, "count": duplicates, "label": f"Eliminar {duplicates} filas idénticas duplicadas", "reason": "Son filas completamente iguales. Confirma que una fila idéntica no represente una repetición válida del negocio."})
    categorical_code_names = {"browser", "region", "traffictype", "operatingsystems", "operating_systems", "month", "specialday", "visitor_type", "visitortype", "weekend"}
    for col in df.select_dtypes(include=np.number).columns:
        if str(col).strip().lower().replace(" ", "") in categorical_code_names:
            continue
        s = df[col].dropna()
        if len(s) >= 4:
            q1, q3 = s.quantile([.25,.75])
            n = int(((s < q1 - 1.5*(q3-q1)) | (s > q3 + 1.5*(q3-q1))).sum())
            if n:
                recs.append({"id": f"outliers:{col}", "action": "review_outliers", "column": str(col), "count": n, "label": f"Revisar {n} posibles valores atípicos en «{col}»", "reason": "Candidatos identificados mediante el rango intercuartílico (IQR). No se eliminan automáticamente porque podrían ser observaciones reales."})
    total = max(len(df), 1)
    for rec in recs:
        rec["affected_percent"] = round(rec["count"] / total * 100, 2)
        rec["dtype"] = str(df[rec["column"]].dtype) if rec.get("column") in df.columns else "fila completa"
        rec["detection_method"] = "Valores nulos/blancos, duplicidad exacta o límites IQR (1,5 × rango intercuartílico)."
        rec["risk"] = "La acción puede modificar la distribución o eliminar información; inspecciona los registros antes de confirmar."
        rec["status"] = "Detectada"
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

class CleanPreviewIn(BaseModel):
    action: str = Field(pattern="^(missing|outliers|duplicates|invalid_type)$")
    column: str = ""
    row_ids: list[int] = Field(default_factory=list)
    params: dict = Field(default_factory=dict)
    source_version: int = Field(ge=1)
    idempotency_key: str = Field(default_factory=lambda: str(uuid.uuid4()), min_length=8, max_length=100)

class CleanConfirmIn(BaseModel):
    operation_id: str


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
    db.add(ds); db.flush()
    db.add(DatasetVersion(dataset_id=ds_id, version=1, csv_text=ds.working_csv, summary=json.dumps({"event":"initial_upload"}), created_by=user.id))
    db.commit()
    return {"id": ds_id, "filename": filename, "version": 1, "profile": profile_df(df), "recommendations": recommendations(df), "preview": df.head(10).replace({np.nan: None}).to_dict(orient="records")}

@app.get("/api/datasets")
def list_datasets(user: User = Depends(current_user), db: Session = Depends(get_db)):
    rows = db.query(Dataset).filter(Dataset.user_id == user.id).order_by(Dataset.created_at.desc()).all()
    return [{"id": x.id, "filename": x.filename, "created_at": x.created_at.isoformat(), "version": _version_number(db, x.id)} for x in rows]

def _recommendations_for_dataset(db: Session, ds: Dataset, df: pd.DataFrame) -> list[dict]:
    recs = recommendations(df)
    operations = db.query(CleaningOperation).filter(CleaningOperation.dataset_id==ds.id).order_by(CleaningOperation.created_at.desc()).all()
    for rec in recs:
        expected_action = "missing" if rec["id"].startswith("missing:") else "outliers" if rec["id"].startswith("outliers:") else "duplicates" if rec["id"] == "duplicates:all" else "invalid_type" if rec["id"].startswith("invalid_type:") else ""
        match = next((o for o in operations if o.action == expected_action and o.column_name == (rec.get("column") or "") and o.status in ("applied", "reviewed")), None)
        if match:
            rec["status"] = "Problema todavía presente" if match.status == "applied" else "Revisada sin cambios"
            rec["last_operation_id"] = match.id
        else:
            rec["status"] = "Detectada"
    return recs

@app.get("/api/datasets/{dataset_id}")
def get_dataset(dataset_id: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    ds = owned_dataset(dataset_id, user, db)
    df = read_csv_text(ds.working_csv)
    _ensure_version(db, ds, user.id)
    return {"id": ds.id, "filename": ds.filename, "version": _version_number(db, ds.id), "profile": profile_df(df), "recommendations": _recommendations_for_dataset(db, ds, df), "preview": df.head(10).replace({np.nan: None}).to_dict(orient="records")}

@app.post("/api/datasets/{dataset_id}/clean")
def clean_dataset_legacy(dataset_id: str, data: CleanIn, user: User = Depends(current_user), db: Session = Depends(get_db)):
    owned_dataset(dataset_id, user, db)
    raise HTTPException(status_code=409, detail="La limpieza directa fue deshabilitada para proteger los datos. Usa /clean/preview y luego /clean/confirm para inspeccionar, previsualizar y guardar una versión.")

@app.get("/api/datasets/{dataset_id}/download")
def download_dataset(dataset_id: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    ds = owned_dataset(dataset_id, user, db)
    return StreamingResponse(io.BytesIO(ds.working_csv.encode("utf-8-sig")), media_type="text/csv; charset=utf-8", headers={"Content-Disposition": f'attachment; filename="limpio_{Path(ds.filename).stem}.csv"'})

@app.get("/api/datasets/{dataset_id}/eda")
def eda(dataset_id: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    ds = owned_dataset(dataset_id, user, db)
    df = read_csv_text(ds.working_csv).reset_index(drop=True)
    version = _version_number(db, ds.id)
    exclusion_rows = db.query(AnalysisExclusion).filter(AnalysisExclusion.dataset_id==ds.id, AnalysisExclusion.version==version).all()
    excluded_ids = set()
    for exclusion in exclusion_rows:
        excluded_ids.update(int(x) for x in json.loads(exclusion.row_ids_json))
    excluded_positions = {x-1 for x in excluded_ids if 1 <= x <= len(df)}
    analysis_df = df.drop(index=list(excluded_positions)).reset_index(drop=True) if excluded_positions else df.copy()
    numeric = analysis_df.select_dtypes(include=np.number)
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
    for col in analysis_df.columns:
        if col not in numeric.columns:
            vc = analysis_df[col].astype("string").fillna("(nulo)").value_counts().head(10)
            categorical[str(col)] = [{"value": str(k), "count": int(v)} for k,v in vc.items()]
    findings = []
    p = profile_df(analysis_df)
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
    return {"profile": p, "version": version, "excluded_rows_from_analysis": len(excluded_positions), "correlation": corr, "distributions": distributions, "categorical": categorical, "findings": findings, "preview": analysis_df.head(15).replace({np.nan: None}).to_dict(orient="records")}


def _ensure_version(db: Session, ds: Dataset, user_id: int):
    first = db.query(DatasetVersion).filter(DatasetVersion.dataset_id == ds.id, DatasetVersion.version == 1).first()
    if not first:
        db.add(DatasetVersion(dataset_id=ds.id, version=1, csv_text=ds.working_csv,
                              summary=json.dumps({"event":"initial"}), created_by=user_id))
        db.commit()

def _version_number(db: Session, dataset_id: str) -> int:
    row = db.query(DatasetVersion).filter(DatasetVersion.dataset_id == dataset_id).order_by(DatasetVersion.version.desc()).first()
    return row.version if row else 1

def _profile_safe(df: pd.DataFrame) -> dict:
    # Convert pandas/numpy scalars into JSON-safe values.
    return json.loads(json.dumps(profile_df(df), default=lambda x: None if pd.isna(x) else x.item() if hasattr(x, "item") else str(x)))

def _mask_for_action(df: pd.DataFrame, action: str, column: str, params: dict):
    if action == "missing":
        if column not in df: raise HTTPException(status_code=422, detail="La columna no existe.")
        return df[column].isna() | df[column].astype("string").str.strip().eq("").fillna(False)
    if action == "duplicates":
        return df.duplicated(keep=False)
    if action == "outliers":
        categorical_codes = {"browser", "region", "traffictype", "operatingsystems", "operating_systems", "month", "specialday", "visitor_type", "visitortype", "weekend"}
        normalized_column = str(column).strip().lower().replace(" ", "")
        if column not in df or not pd.api.types.is_numeric_dtype(df[column]) or normalized_column in categorical_codes:
            raise HTTPException(status_code=422, detail="Los valores atípicos por IQR solo se calculan en variables numéricas continuas; los códigos categóricos deben revisarse como categorías.")
        values = pd.to_numeric(df[column], errors="coerce")
        valid = values.dropna()
        if len(valid) < 4: return pd.Series(False, index=df.index)
        method = params.get("bounds", "iqr")
        if method == "percentile":
            lp = float(params.get("lower_percentile", 0.01)); up = float(params.get("upper_percentile", 0.99))
            if not 0 <= lp < up <= 1: raise HTTPException(status_code=422, detail="Los percentiles deben cumplir 0 ≤ inferior < superior ≤ 1.")
            low, high = valid.quantile(lp), valid.quantile(up)
        else:
            factor = float(params.get("factor", 1.5))
            if factor < 0: raise HTTPException(status_code=422, detail="El factor IQR no puede ser negativo.")
            q1, q3 = valid.quantile([.25, .75]); low, high = q1-factor*(q3-q1), q3+factor*(q3-q1)
        return (values < low) | (values > high)
    if action == "invalid_type":
        if column not in df: raise HTTPException(status_code=422, detail="La columna no existe.")
        typ = params.get("expected_type", "numeric")
        if typ == "numeric": converted = pd.to_numeric(df[column], errors="coerce")
        elif typ == "datetime": converted = pd.to_datetime(df[column], errors="coerce")
        else: raise HTTPException(status_code=422, detail="Tipo esperado no compatible.")
        return converted.isna() & df[column].notna() & df[column].astype("string").str.strip().ne("")
    raise HTTPException(status_code=422, detail="Tipo de problema no válido.")

def _apply_selected(df: pd.DataFrame, action: str, column: str, row_ids: list[int], params: dict):
    if not row_ids: raise HTTPException(status_code=422, detail="Selecciona al menos un registro afectado.")
    if any(i < 0 or i >= len(df) for i in row_ids): raise HTTPException(status_code=409, detail="Una fila seleccionada ya no pertenece a la versión actual.")
    result = df.copy().reset_index(drop=True)
    mask = _mask_for_action(result, action, column, params).fillna(False)
    selected = sorted(set(row_ids))
    not_affected = [i for i in selected if not bool(mask.iloc[i])]
    if not_affected:
        raise HTTPException(status_code=409, detail="Algunas filas seleccionadas ya no cumplen el criterio. Vuelve a generar la vista previa.")
    method = params.get("method", "review")
    changes=[]; removed=[]; excluded=[]
    before_rows=len(result)
    if action == "missing":
        if method in ("mean", "median"):
            categorical_codes = {"browser", "region", "traffictype", "operatingsystems", "operating_systems", "month", "specialday", "visitor_type", "visitortype", "weekend"}
            if str(column).strip().lower().replace(" ", "") in categorical_codes or pd.api.types.is_bool_dtype(result[column]):
                raise HTTPException(status_code=422, detail="Media/mediana no son apropiadas para códigos categóricos o booleanos. Usa moda, valor personalizado o revisión.")
            original_values = result[column].replace(r"^\s*$", np.nan, regex=True)
            numeric = pd.to_numeric(original_values, errors="coerce")
            nonempty = original_values.notna()
            if numeric[nonempty].isna().any():
                raise HTTPException(status_code=422, detail="Media y mediana solo se permiten cuando los valores existentes de la columna son numéricos. Usa moda o un valor personalizado.")
            result[column] = numeric
            fill = numeric.mean() if method=="mean" else numeric.median()
            if pd.isna(fill): raise HTTPException(status_code=422, detail="No existen valores numéricos válidos para imputar.")
        elif method == "mode":
            mode=result.loc[~mask,column].mode(dropna=True)
            if mode.empty: raise HTTPException(status_code=422, detail="No hay moda válida para esta columna.")
            fill=mode.iloc[0]
        elif method == "custom":
            fill=params.get("value")
            if fill is None or str(fill).strip()=="": raise HTTPException(status_code=422, detail="Escribe el valor personalizado.")
            if pd.api.types.is_numeric_dtype(result[column]):
                try: fill=float(fill)
                except (ValueError,TypeError): raise HTTPException(status_code=422, detail="El valor debe ser numérico.")
        elif method in ("drop_rows", "exclude_analysis", "review", "keep"): fill=None
        else: raise HTTPException(status_code=422, detail="Tratamiento de nulos no válido.")
        if method in ("mean","median","mode","custom"):
            for i in selected:
                changes.append({"row_id":i+1,"column":column,"original":None if pd.isna(result.at[i,column]) else str(result.at[i,column]),"proposed":fill.item() if hasattr(fill,"item") else fill})
                result.at[i,column]=fill
        elif method=="drop_rows":
            removed=[i+1 for i in selected]; result=result.drop(index=selected).reset_index(drop=True)
        elif method=="exclude_analysis": excluded=[i+1 for i in selected]
    elif action == "outliers":
        valid=pd.to_numeric(result[column],errors="coerce").dropna()
        if params.get("bounds")=="percentile": low,high=valid.quantile(float(params.get("lower_percentile",.01))),valid.quantile(float(params.get("upper_percentile",.99)))
        else:
            q1,q3=valid.quantile([.25,.75]); factor=float(params.get("factor",1.5)); low,high=q1-factor*(q3-q1),q3+factor*(q3-q1)
        if method in ("mean","median"):
            reference = valid.drop(index=[i for i in selected if i in valid.index], errors="ignore")
            if reference.empty:
                raise HTTPException(status_code=422, detail="No quedan valores de referencia válidos fuera de los atípicos seleccionados para calcular media/mediana.")
            fill=float(reference.mean() if method=="mean" else reference.median())
            for i in selected:
                changes.append({"row_id":i+1,"column":column,"original":float(result.at[i,column]),"proposed":fill}); result.at[i,column]=fill
        elif method=="capping":
            for i in selected:
                old=float(result.at[i,column]); new=float(min(max(old,low),high)); changes.append({"row_id":i+1,"column":column,"original":old,"proposed":new}); result.at[i,column]=new
        elif method=="drop_rows": removed=[i+1 for i in selected]; result=result.drop(index=selected).reset_index(drop=True)
        elif method=="exclude_analysis": excluded=[i+1 for i in selected]
        elif method not in ("review","keep"): raise HTTPException(status_code=422,detail="Acción para atípicos no válida.")
    elif action == "duplicates":
        if method=="drop_rows":
            keep_id=params.get("keep_row_id")
            if keep_id is not None:
                keep_id=int(keep_id)-1
                if keep_id not in selected: raise HTTPException(status_code=422,detail="La fila que deseas conservar debe estar seleccionada.")
                remove=[i for i in selected if i != keep_id]
            else:
                remove=[]; seen=set()
                for i in selected:
                    key=tuple(str(x) for x in result.iloc[i].tolist())
                    if key in seen: remove.append(i)
                    else: seen.add(key)
            removed=[i+1 for i in remove]; result=result.drop(index=remove).reset_index(drop=True)
        elif method=="exclude_analysis": excluded=[i+1 for i in selected]
        elif method not in ("review","keep"): raise HTTPException(status_code=422,detail="Acción para duplicados no válida.")
    elif action == "invalid_type":
        typ=params.get("expected_type","numeric")
        if method=="custom":
            value=params.get("value")
            for i in selected:
                proposed=value
                if typ=="numeric":
                    try: proposed=float(value)
                    except (ValueError,TypeError): raise HTTPException(status_code=422,detail="El valor personalizado debe ser numérico.")
                changes.append({"row_id":i+1,"column":column,"original":str(result.at[i,column]),"proposed":str(proposed)}); result.at[i,column]=proposed
        elif method=="drop_rows": removed=[i+1 for i in selected]; result=result.drop(index=selected).reset_index(drop=True)
        elif method=="exclude_analysis": excluded=[i+1 for i in selected]
        elif method not in ("review","keep"): raise HTTPException(status_code=422,detail="Acción para tipo incorrecto no válida.")
    summary={"action":action,"column":column or None,"method":method,"parameters":params,"selected_rows":len(selected),"source_rows":before_rows,"result_rows":len(result),"rows_removed":len(removed),"rows_excluded_from_analysis":len(excluded),"cells_changed":len(changes),"changes":changes[:500],"removed_row_ids":removed,"excluded_row_ids":excluded,"before_profile":_profile_safe(df),"after_profile":_profile_safe(result),"warnings":["Revisa el efecto sobre la distribución y el posible sesgo."] if changes or removed or excluded else ["Revisión registrada sin modificar los valores."]}
    return result, summary

@app.get("/api/datasets/{dataset_id}/records")
def dataset_records(dataset_id: str, page: int=1, page_size: int=25, search: str="", action: str="", column: str="", user: User=Depends(current_user), db: Session=Depends(get_db)):
    ds=owned_dataset(dataset_id,user,db); _ensure_version(db,ds,user.id)
    df=read_csv_text(ds.working_csv).reset_index(drop=True)
    mask=_mask_for_action(df,action,column,{}) if action else pd.Series(True,index=df.index)
    filtered=df.loc[mask.fillna(False)].copy()
    if search:
        sm=filtered.astype("string").apply(lambda c:c.str.contains(search,case=False,na=False,regex=False)).any(axis=1); filtered=filtered[sm]
    page=max(1,page); page_size=min(max(1,page_size),100); total=len(filtered); start=(page-1)*page_size
    records=[]
    for i,row in filtered.iloc[start:start+page_size].iterrows():
        item={str(k):(None if pd.isna(v) else v.item() if hasattr(v,"item") else v) for k,v in row.items()}; item["__row_id"]=int(i); records.append(item)
    return {"dataset_id":ds.id,"version":_version_number(db,ds.id),"page":page,"page_size":page_size,"total":total,"pages":max(1,(total+page_size-1)//page_size),"records":records}

@app.post("/api/datasets/{dataset_id}/clean/preview")
def preview_clean(dataset_id: str, data: CleanPreviewIn, user: User=Depends(current_user), db: Session=Depends(get_db)):
    ds=owned_dataset(dataset_id,user,db); _ensure_version(db,ds,user.id); version=_version_number(db,ds.id)
    if data.source_version != version: raise HTTPException(status_code=409,detail="La versión del dataset cambió. Actualiza los datos y vuelve a intentarlo.")
    old=db.query(CleaningOperation).filter(CleaningOperation.user_id==user.id,CleaningOperation.dataset_id==ds.id,CleaningOperation.idempotency_key==data.idempotency_key).first()
    if old: return {"operation_id":old.id,"status":old.status,"source_version":old.source_version,"preview":json.loads(old.preview_json)}
    df=read_csv_text(ds.working_csv).reset_index(drop=True)
    result,summary=_apply_selected(df,data.action,data.column,data.row_ids,data.params)
    op_id=str(uuid.uuid4()); op=CleaningOperation(id=op_id,dataset_id=ds.id,user_id=user.id,idempotency_key=data.idempotency_key,source_version=version,action=data.action,column_name=data.column,row_ids_json=json.dumps(sorted(set(data.row_ids))),params_json=json.dumps(data.params,ensure_ascii=False),preview_json=json.dumps(summary,ensure_ascii=False,default=str))
    db.add(op); db.commit()
    return {"operation_id":op_id,"status":"preview","source_version":version,"preview":summary}

@app.post("/api/datasets/{dataset_id}/clean/confirm")
def confirm_clean(dataset_id: str, data: CleanConfirmIn, user: User=Depends(current_user), db: Session=Depends(get_db)):
    ds=owned_dataset(dataset_id,user,db); op=db.get(CleaningOperation,data.operation_id)
    if not op or op.dataset_id!=ds.id or op.user_id!=user.id: raise HTTPException(status_code=404,detail="Operación no encontrada.")
    if op.status in ("applied","reviewed"):
        return {"message":"Esta operación ya fue procesada; no se repitió.","status":op.status,"operation_id":op.id,"version":_version_number(db,ds.id),"result":json.loads(op.result_json)}
    if op.status!="preview": raise HTTPException(status_code=409,detail="La operación no está pendiente de confirmación.")
    version=_version_number(db,ds.id)
    if version!=op.source_version: op.status="stale"; db.commit(); raise HTTPException(status_code=409,detail="El dataset cambió después de la vista previa. Genera otra.")
    df=read_csv_text(ds.working_csv).reset_index(drop=True); rows=json.loads(op.row_ids_json); params=json.loads(op.params_json)
    result,summary=_apply_selected(df,op.action,op.column_name,rows,params)
    if summary["cells_changed"] or summary["rows_removed"]:
        new_version=version+1; csv=result.to_csv(index=False); ds.working_csv=csv
        db.add(DatasetVersion(dataset_id=ds.id,version=new_version,csv_text=csv,summary=json.dumps({"operation_id":op.id,"result":summary},ensure_ascii=False,default=str),created_by=user.id)); op.status="applied"
    else:
        summary["note"]="La decisión fue registrada sin modificar los valores del CSV original ni de la copia de trabajo."; op.status="reviewed"; new_version=version
    if summary.get("rows_excluded_from_analysis"):
        db.add(AnalysisExclusion(dataset_id=ds.id, version=new_version, operation_id=op.id,
                                row_ids_json=json.dumps(summary.get("excluded_row_ids", []))))
    op.result_json=json.dumps(summary,ensure_ascii=False,default=str); op.confirmed_at=datetime.utcnow()
    db.add(Decision(dataset_id=ds.id,user_id=user.id,action=op.action,details=json.dumps({"operation_id":op.id,"status":op.status,"summary":summary},ensure_ascii=False,default=str)))
    db.commit(); current=read_csv_text(ds.working_csv)
    return {"message":"Operación procesada y registrada.","status":op.status,"operation_id":op.id,"version":new_version,"result":summary,"profile":_profile_safe(current),"recommendations":_recommendations_for_dataset(db, ds, current)}

@app.get("/api/datasets/{dataset_id}/versions")
def dataset_versions(dataset_id: str,user: User=Depends(current_user),db: Session=Depends(get_db)):
    ds=owned_dataset(dataset_id,user,db); _ensure_version(db,ds,user.id)
    return [{"version":v.version,"created_at":v.created_at.isoformat(),"summary":json.loads(v.summary)} for v in db.query(DatasetVersion).filter(DatasetVersion.dataset_id==ds.id).order_by(DatasetVersion.version.desc()).all()]

@app.get("/api/datasets/{dataset_id}/versions/{version}/download")
def download_dataset_version(dataset_id: str,version: int,user: User=Depends(current_user),db: Session=Depends(get_db)):
    ds=owned_dataset(dataset_id,user,db); v=db.query(DatasetVersion).filter(DatasetVersion.dataset_id==ds.id,DatasetVersion.version==version).first()
    if not v: raise HTTPException(status_code=404,detail="Versión no encontrada.")
    return StreamingResponse(io.BytesIO(v.csv_text.encode("utf-8-sig")),media_type="text/csv; charset=utf-8",headers={"Content-Disposition":f'attachment; filename="version_{version}_{Path(ds.filename).name}"'})

@app.get("/api/datasets/{dataset_id}/operations")
def dataset_operations(dataset_id: str,user: User=Depends(current_user),db: Session=Depends(get_db)):
    ds=owned_dataset(dataset_id,user,db)
    return [{"id":o.id,"action":o.action,"column":o.column_name,"status":o.status,"source_version":o.source_version,"params":json.loads(o.params_json),"result":json.loads(o.result_json),"created_at":o.created_at.isoformat()} for o in db.query(CleaningOperation).filter(CleaningOperation.dataset_id==ds.id,CleaningOperation.user_id==user.id).order_by(CleaningOperation.created_at.desc()).all()]


@app.get("/api/datasets/{dataset_id}/decisions")
def decisions(dataset_id: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    owned_dataset(dataset_id, user, db)
    rows = db.query(Decision).filter(Decision.dataset_id == dataset_id, Decision.user_id == user.id).order_by(Decision.created_at.desc()).all()
    return [{"id": x.id, "action": x.action, "details": json.loads(x.details), "created_at": x.created_at.isoformat()} for x in rows]
