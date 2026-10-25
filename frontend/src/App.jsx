import React, { useEffect, useMemo, useState } from 'react'

const API = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'
const fmt = n => new Intl.NumberFormat('es-CO').format(n ?? 0)

export default function App() {
  const [token, setToken] = useState(localStorage.getItem('ib_token') || '')
  const [user, setUser] = useState(null)
  const [mode, setMode] = useState('login')
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [dataset, setDataset] = useState(null)
  const [file, setFile] = useState(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')
  const [notice, setNotice] = useState('')
  const [selected, setSelected] = useState([])
  const [view, setView] = useState('overview')
  const [eda, setEda] = useState(null)
  const [history, setHistory] = useState([])

  async function request(path, options = {}) {
    const headers = { ...(options.headers || {}) }
    if (token) headers.Authorization = `Bearer ${token}`
    if (options.body && !(options.body instanceof FormData)) headers['Content-Type'] = 'application/json'
    const res = await fetch(`${API}${path}`, { ...options, headers })
    const data = await res.json().catch(() => ({}))
    if (!res.ok) throw new Error(data.detail || `Error HTTP ${res.status}`)
    return data
  }

  useEffect(() => {
    if (!token) return
    request('/api/auth/me').then(setUser).catch(() => logout())
  }, [token])

  function logout() {
    localStorage.removeItem('ib_token'); setToken(''); setUser(null); setDataset(null); setEda(null); setHistory([])
  }

  async function auth(e) {
    e.preventDefault(); setError(''); setNotice(''); setBusy(true)
    try {
      const path = mode === 'register' ? '/api/auth/register' : '/api/auth/login'
      const body = mode === 'register' ? { name, email, password } : { email, password }
      const data = await request(path, { method: 'POST', body: JSON.stringify(body) })
      localStorage.setItem('ib_token', data.token); setToken(data.token); setUser(data.user); setNotice('Sesión iniciada correctamente.')
    } catch (err) { setError(err.message) } finally { setBusy(false) }
  }

  async function upload(e) {
    e.preventDefault(); if (!file) return
    setError(''); setNotice(''); setBusy(true)
    try {
      const form = new FormData(); form.append('file', file)
      const data = await request('/api/datasets/upload', { method: 'POST', body: form })
      setDataset(data); setSelected([]); setEda(null); setView('quality')
      setNotice(`CSV analizado: ${data.profile.rows} filas y ${data.profile.columns} columnas.`)
    } catch (err) { setError(err.message) } finally { setBusy(false) }
  }

  async function openDataset(id) {
    setBusy(true); setError('')
    try {
      const data = await request(`/api/datasets/${id}`)
      setDataset(data); setSelected([]); setEda(null); setView('quality')
    } catch (err) { setError(err.message) } finally { setBusy(false) }
  }

  async function applyCleaning() {
    if (!dataset || !selected.length) return
    setBusy(true); setError(''); setNotice('')
    try {
      const data = await request(`/api/datasets/${dataset.id}/clean`, { method: 'POST', body: JSON.stringify({ actions: selected }) })
      setDataset(prev => ({ ...prev, profile: data.profile, recommendations: data.recommendations }))
      setSelected([]); setNotice('Acciones confirmadas aplicadas a la copia de trabajo.')
    } catch (err) { setError(err.message) } finally { setBusy(false) }
  }

  async function openEda() {
    if (!dataset) { setError('Primero carga un CSV o abre uno del historial.'); return }
    setBusy(true); setError('')
    try {
      setEda(await request(`/api/datasets/${dataset.id}/eda`)); setView('eda')
    } catch (err) { setError(err.message) } finally { setBusy(false) }
  }

  async function loadHistory() {
    try { setHistory(await request('/api/datasets')); setView('history') } catch (err) { setError(err.message) }
  }

  async function download() {
    try {
      const res = await fetch(`${API}/api/datasets/${dataset.id}/download`, { headers: { Authorization: `Bearer ${token}` } })
      if (!res.ok) throw new Error('No se pudo descargar el CSV.')
      const blob = await res.blob(); const url = URL.createObjectURL(blob)
      const a = document.createElement('a'); a.href = url; a.download = `limpio_${dataset.filename}`; a.click(); URL.revokeObjectURL(url)
    } catch (err) { setError(err.message) }
  }

  if (!token || !user) return <div className="auth-shell">
    <section className="auth-brand"><div className="brand-mark">IB</div><span className="eyebrow">DATA INTELLIGENCE</span><h1>Convierte tus datos en decisiones.</h1><p>InsightBuy ayuda a revisar, preparar y comprender tus CSV antes de construir modelos predictivos.</p><div className="auth-points"><span>✓ Diagnóstico real de calidad</span><span>✓ Limpieza bajo tu aprobación</span><span>✓ Análisis exploratorio verificable</span></div></section>
    <form className="auth-card" onSubmit={auth}><span className="eyebrow">{mode === 'register' ? 'CREAR CUENTA' : 'BIENVENIDO DE NUEVO'}</span><h2>{mode === 'register' ? 'Crea tu espacio' : 'Inicia sesión'}</h2><p className="muted">Accede a tu espacio de análisis de datos.</p>
      {mode === 'register' && <label>Nombre completo<input value={name} onChange={e=>setName(e.target.value)} required minLength="2" placeholder="Tu nombre"/></label>}
      <label>Correo electrónico<input type="email" value={email} onChange={e=>setEmail(e.target.value)} required placeholder="correo@ejemplo.com"/></label>
      <label>Contraseña<input type="password" value={password} onChange={e=>setPassword(e.target.value)} required minLength="8" maxLength="72" placeholder="Mínimo 8 caracteres"/></label>
      {error && <div className="alert error">{error}</div>}{notice && <div className="alert success">{notice}</div>}
      <button className="primary full" disabled={busy}>{busy ? 'Procesando…' : mode === 'register' ? 'Crear cuenta' : 'Entrar a InsightBuy'}</button>
      <p className="switch">{mode === 'register' ? '¿Ya tienes cuenta?' : '¿Aún no tienes cuenta?'} <button type="button" className="link" onClick={()=>{setMode(mode==='register'?'login':'register');setError('')}}>{mode==='register'?'Inicia sesión':'Regístrate'}</button></p>
    </form>
  </div>

  return <div className="app-shell">
    <aside className="sidebar"><div className="brand"><div className="brand-mark">IB</div><div><b>INSIGHTBUY</b><small>DATA WORKSPACE</small></div></div><div className="side-label">ESPACIO DE TRABAJO</div>
      <button className={view==='overview'?'nav active':'nav'} onClick={()=>setView('overview')}>◫ <span>Inicio</span></button>
      <button className={view==='quality'?'nav active':'nav'} onClick={()=>setView('quality')}>▤ <span>Calidad de datos</span></button>
      <button className={view==='eda'?'nav active':'nav'} onClick={openEda}>◌ <span>Análisis exploratorio</span></button>
      <button className={view==='history'?'nav active':'nav'} onClick={loadHistory}>◷ <span>Mis datasets</span></button>
      <div className="sidebar-bottom"><div className="user-mini"><div className="avatar">{(user.name||user.email).slice(0,1).toUpperCase()}</div><div><b>{user.name||user.email}</b><small>{user.email}</small></div></div><button className="nav logout" onClick={logout}>↪ <span>Cerrar sesión</span></button></div>
    </aside>
    <main className="main"><header className="topbar"><div><span className="eyebrow">ANÁLISIS DE DATOS · WORKSPACE</span><h1>{view==='overview'?'Resumen general':view==='quality'?'Calidad y preparación':view==='eda'?'Análisis exploratorio':view==='history'?'Mis datasets':'InsightBuy'}</h1></div><div className="status"><i/> Sistema disponible</div></header>
      {error && <div className="alert error">{error}<button onClick={()=>setError('')}>×</button></div>}{notice && <div className="alert success">{notice}<button onClick={()=>setNotice('')}>×</button></div>}
      {view==='overview' && <><section className="hero"><div><span className="eyebrow">TU ESPACIO DE ANÁLISIS</span><h2>Hola, {user.name?.split(' ')[0] || 'bienvenido'} 👋</h2><p>Sube un archivo CSV para evaluar su calidad y descubrir patrones en tus datos.</p><form className="upload-row" onSubmit={upload}><label className="file-pick">＋ <span>{file?file.name:'Seleccionar archivo CSV'}</span><input type="file" accept=".csv,text/csv" onChange={e=>setFile(e.target.files?.[0]||null)}/></label><button className="primary" disabled={!file||busy}>{busy?'Analizando…':'Analizar dataset'}</button></form><small className="muted">Límite configurado por el servidor · CSV únicamente</small></div><div className="hero-art"><div className="orb">✳</div><div className="floating f1">▥ &nbsp; Datos listos</div><div className="floating f2">↗ &nbsp; Insights</div><div className="bars"><i/><i/><i/><i/><i/><i/><i/></div></div></section>
        <section className="section-head"><div><h2>Flujo de trabajo</h2><p>Del archivo original al entendimiento de tus datos.</p></div></section><div className="workflow"><article><span className="step">01</span><h3>Cargar dataset</h3><p>Valida la estructura y revisa que el archivo se pueda interpretar.</p></article><article><span className="step">02</span><h3>Revisar calidad</h3><p>Detecta nulos, duplicados y candidatos a valores atípicos.</p></article><article><span className="step">03</span><h3>Explorar datos</h3><p>Consulta estadísticas, distribuciones y correlaciones numéricas.</p></article></div>
        {dataset && <section className="panel"><div className="panel-title"><div><h2>Dataset actual</h2><p>{dataset.filename}</p></div><button className="secondary" onClick={()=>setView('quality')}>Abrir análisis →</button></div><Stats profile={dataset.profile}/></section>}
      </>}
      {view==='quality' && <>{!dataset ? <section className="empty panel"><div className="empty-icon">▤</div><h2>Aún no hay un dataset abierto</h2><p>Regresa al inicio y selecciona un archivo CSV para comenzar.</p><button className="primary" onClick={()=>setView('overview')}>Cargar dataset</button></section> : <><section className="panel"><div className="panel-title"><div><span className="eyebrow">DATASET ACTUAL</span><h2>{dataset.filename}</h2><p>El archivo original se conserva; las acciones afectan la copia de trabajo.</p></div><button className="secondary" onClick={download}>↓ Descargar CSV de trabajo</button></div><Stats profile={dataset.profile}/></section><section className="panel"><div className="panel-title"><div><h2>Asistente de calidad</h2><p>Las reglas detectan problemas. Tú decides qué acciones aplicar.</p></div><span className="pill">{dataset.recommendations?.length||0} recomendaciones</span></div>{!dataset.recommendations?.length ? <div className="empty-small">No hay recomendaciones automáticas pendientes en el perfil actual.</div> : <div className="recommendations">{dataset.recommendations.map(r=><label className="recommendation" key={r.id}><input type="checkbox" checked={selected.includes(r.id)} onChange={e=>setSelected(prev=>e.target.checked?[...prev,r.id]:prev.filter(x=>x!==r.id))}/><div><b>{r.label}</b><p>{r.reason}</p><small>{r.action==='review_outliers'?'Solo revisión; no modifica los valores':`Acción propuesta: ${r.action}`}</small></div><span className="count">{fmt(r.count)}</span></label>)}</div>}<div className="action-row"><span className="muted">Seleccionadas: {selected.length}</span><button className="primary" disabled={!selected.length||busy} onClick={applyCleaning}>{busy?'Aplicando…':'Aplicar seleccionadas'}</button></div></section><section className="panel"><div className="panel-title"><div><h2>Vista previa</h2><p>Primeras 10 filas de la copia de trabajo.</p></div><button className="secondary" onClick={openEda}>Ir al análisis exploratorio →</button></div><DataTable rows={dataset.preview||[]}/></section></>}</>}
      {view==='eda' && <>{!eda ? <section className="empty panel"><div className="empty-icon">◌</div><h2>Explora tu dataset</h2><p>Abre el análisis del dataset actual para calcular estadísticas y correlaciones.</p><button className="primary" onClick={openEda}>Calcular análisis exploratorio</button></section> : <><section className="panel"><div className="panel-title"><div><h2>Hallazgos iniciales</h2><p>Calculados sobre la copia de trabajo actual.</p></div><button className="secondary" onClick={download}>↓ Descargar CSV</button></div><div className="findings">{eda.findings.map((x,i)=><div key={i} className="finding"><span>{String(i+1).padStart(2,'0')}</span>{x}</div>)}</div></section><section className="panel"><div className="panel-title"><div><h2>Estadísticas descriptivas</h2><p>Resumen de las columnas numéricas.</p></div></div><NumericTable stats={eda.profile.numeric_stats}/></section><section className="panel"><div className="panel-title"><div><h2>Distribuciones</h2><p>Frecuencias agrupadas para variables numéricas.</p></div></div>{Object.entries(eda.distributions||{}).length ? <div className="distribution-grid">{Object.entries(eda.distributions).map(([col,bins])=><div className="dist-card" key={col}><h3>{col}</h3>{bins.map((b,i)=><div className="bar-row" key={i}><small>{b.range}</small><div className="bar-track"><i style={{width:`${Math.max(2,b.count/Math.max(...bins.map(x=>x.count),1)*100)}%`}}/></div><b>{b.count}</b></div>)}</div>)}</div>:<p className="muted">No hay columnas numéricas para graficar.</p>}</section><section className="panel"><div className="panel-title"><div><h2>Matriz de correlación</h2><p>Correlación de Pearson entre variables numéricas. No implica causalidad.</p></div></div><Correlation data={eda.correlation}/></section><section className="panel"><div className="panel-title"><div><h2>Primeras filas</h2><p>Vista tabular de los datos analizados.</p></div></div><DataTable rows={eda.preview||[]}/></section></>}</>}
      {view==='history' && <section className="panel"><div className="panel-title"><div><h2>Datasets cargados</h2><p>Archivos asociados a tu cuenta.</p></div><button className="secondary" onClick={loadHistory}>↻ Actualizar</button></div>{history.length ? <div className="history-list">{history.map(x=><button className="history-item" key={x.id} onClick={()=>openDataset(x.id)}><span className="file-icon">CSV</span><span><b>{x.filename}</b><small>{new Date(x.created_at).toLocaleString('es-CO')}</small></span><span>→</span></button>)}</div>:<div className="empty-small">No hay datasets cargados. Sube un CSV desde Inicio.</div>}</section>}
      <footer>INSIGHTBUY · Análisis de datos responsable <span>Resultados calculados sobre el archivo cargado</span></footer>
    </main>
  </div>
}

function Stats({profile:p}) {
  if(!p) return null
  const missing=p.missing?.reduce((s,x)=>s+x.missing,0)||0
  return <div className="stats-grid"><div className="stat"><span>Filas</span><b>{fmt(p.rows)}</b><small>Registros del dataset</small></div><div className="stat"><span>Columnas</span><b>{fmt(p.columns)}</b><small>Variables detectadas</small></div><div className="stat"><span>Valores faltantes</span><b>{fmt(missing)}</b><small>Incluye celdas en blanco</small></div><div className="stat"><span>Duplicados exactos</span><b>{fmt(p.duplicate_rows)}</b><small>Filas idénticas completas</small></div></div>
}
function DataTable({rows}) {
  if(!rows?.length) return <div className="empty-small">No hay filas para mostrar.</div>
  const cols=Object.keys(rows[0])
  return <div className="table-wrap"><table><thead><tr>{cols.map(c=><th key={c}>{c}</th>)}</tr></thead><tbody>{rows.map((r,i)=><tr key={i}>{cols.map(c=><td key={c}>{r[c]===null||r[c]===undefined?'—':String(r[c])}</td>)}</tr>)}</tbody></table></div>
}
function NumericTable({stats}) {
  const entries=Object.entries(stats||{})
  if(!entries.length) return <div className="empty-small">No se detectaron columnas numéricas. Revisa si los números están guardados como texto.</div>
  return <div className="table-wrap"><table><thead><tr><th>Variable</th><th>Conteo</th><th>Media</th><th>Mediana</th><th>Desv. estándar</th><th>Mínimo</th><th>Q1</th><th>Q3</th><th>Máximo</th><th>Atípicos IQR</th></tr></thead><tbody>{entries.map(([k,s])=><tr key={k}><td>{k}</td><td>{s.count}</td><td>{s.mean}</td><td>{s.median}</td><td>{s.std}</td><td>{s.min}</td><td>{s.q1}</td><td>{s.q3}</td><td>{s.max}</td><td>{s.outlier_candidates_iqr}</td></tr>)}</tbody></table></div>
}
function Correlation({data}) {
  if(!data?.columns?.length || data.columns.length<2) return <div className="empty-small">Se requieren al menos dos columnas numéricas para calcular correlaciones.</div>
  const color = v => v===null ? '#eef2f7' : `rgba(${v<0?'220,85,85':'26,143,110'},${Math.min(.9,Math.abs(v)*.85+.1)})`
  return <div className="table-wrap"><table className="corr"><thead><tr><th></th>{data.columns.map(c=><th key={c}>{c}</th>)}</tr></thead><tbody>{data.matrix.map((row,i)=><tr key={i}><th>{data.columns[i]}</th>{row.map((v,j)=><td key={j} style={{background:color(v),color:v!==null&&Math.abs(v)>.58?'white':'#172033'}} title={v===null?'No calculable':`Correlación: ${v}`}>{v===null?'—':Number(v).toFixed(2)}</td>)}</tr>)}</tbody></table><div className="legend"><span><i className="neg"/> Negativa</span><span><i className="pos"/> Positiva</span><span>−1 a +1 · asociación lineal, no causalidad</span></div></div>
}
