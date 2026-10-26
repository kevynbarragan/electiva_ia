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
  const [activeRec, setActiveRec] = useState(null)
  const [records, setRecords] = useState([])
  const [recordPage, setRecordPage] = useState(1)
  const [recordPages, setRecordPages] = useState(1)
  const [recordTotal, setRecordTotal] = useState(0)
  const [recordSearch, setRecordSearch] = useState('')
  const [selectedRows, setSelectedRows] = useState([])
  const [cleanMethod, setCleanMethod] = useState('review')
  const [customValue, setCustomValue] = useState('')
  const [previewResult, setPreviewResult] = useState(null)
  const [operations, setOperations] = useState([])
  const [versions, setVersions] = useState([])

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
      setDataset(data); setSelected([]); setEda(null); setView('quality'); loadAudit(data.id)
      setNotice(`CSV analizado: ${data.profile.rows} filas y ${data.profile.columns} columnas.`)
    } catch (err) { setError(err.message) } finally { setBusy(false) }
  }

  async function openDataset(id) {
    setBusy(true); setError('')
    try {
      const data = await request(`/api/datasets/${id}`)
      setDataset(data); setSelected([]); setEda(null); setView('quality'); loadAudit(data.id)
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

  function recommendationKind(rec) {
    if (rec.id.startsWith('missing:')) return { action: 'missing', column: rec.column || rec.id.slice(8) }
    if (rec.id === 'duplicates:all') return { action: 'duplicates', column: '' }
    if (rec.id.startsWith('outliers:')) return { action: 'outliers', column: rec.column || rec.id.slice(9) }
    if (rec.id.startsWith('invalid_type:')) return { action: 'invalid_type', column: rec.column || rec.id.slice(13) }
    return { action: 'invalid_type', column: rec.column || '' }
  }

  async function inspectRecommendation(rec) {
    if (!dataset) return
    const kind = recommendationKind(rec)
    setBusy(true); setError(''); setActiveRec({ ...rec, ...kind }); setSelectedRows([]); setPreviewResult(null); setRecordPage(1); setRecordSearch('')
    setCleanMethod(kind.action === 'missing' ? (['int64','float64','Int64','Float64'].includes(rec.dtype) && !['browser','region','traffictype','operatingsystems','month','specialday','weekend'].includes(String(rec.column || '').toLowerCase().replaceAll(' ','')) ? 'median' : 'mode') : kind.action === 'duplicates' ? 'drop_rows' : 'review')
    try {
      const data = await request(`/api/datasets/${dataset.id}/records?action=${kind.action}&column=${encodeURIComponent(kind.column)}&page=1&page_size=25`)
      setRecords(data.records || []); setRecordPages(data.pages || 1); setRecordTotal(data.total || 0)
      const ops = await request(`/api/datasets/${dataset.id}/operations`)
      setOperations(ops)
      const vers = await request(`/api/datasets/${dataset.id}/versions`)
      setVersions(vers)
    } catch (err) { setError(err.message); setActiveRec(null) } finally { setBusy(false) }
  }

  async function searchRecords(page = 1) {
    if (!dataset || !activeRec) return
    setBusy(true); setError('')
    try {
      const q = new URLSearchParams({ action: activeRec.action, column: activeRec.column || '', page: String(page), page_size: '25', search: recordSearch })
      const data = await request(`/api/datasets/${dataset.id}/records?${q.toString()}`)
      setRecords(data.records || []); setRecordPage(data.page); setRecordPages(data.pages); setRecordTotal(data.total)
    } catch (err) { setError(err.message) } finally { setBusy(false) }
  }

  async function createCleaningPreview() {
    if (!dataset || !activeRec || !selectedRows.length) return
    const params = { method: cleanMethod }
    if (['missing', 'outliers'].includes(activeRec.action)) {
      if (cleanMethod === 'custom') params.value = customValue
      if (activeRec.action === 'outliers') { params.bounds = 'iqr'; params.factor = 1.5 }
    }
    if (activeRec.action === 'invalid_type') { params.expected_type = 'numeric'; if (cleanMethod === 'custom') params.value = customValue }
    setBusy(true); setError(''); setPreviewResult(null)
    try {
      const data = await request(`/api/datasets/${dataset.id}/clean/preview`, { method: 'POST', body: JSON.stringify({ action: activeRec.action, column: activeRec.column || '', row_ids: selectedRows, params, source_version: dataset.version || 1, idempotency_key: crypto.randomUUID() }) })
      setPreviewResult(data)
    } catch (err) { setError(err.message) } finally { setBusy(false) }
  }

  async function confirmCleaningPreview() {
    if (!dataset || !previewResult?.operation_id) return
    setBusy(true); setError(''); setNotice('')
    try {
      const data = await request(`/api/datasets/${dataset.id}/clean/confirm`, { method: 'POST', body: JSON.stringify({ operation_id: previewResult.operation_id }) })
      const fresh = await request(`/api/datasets/${dataset.id}`)
      setDataset(fresh); setEda(null); setPreviewResult(null); setActiveRec(null); setSelectedRows([])
      setNotice(`${data.status === 'reviewed' ? 'Revisión registrada sin cambios' : 'Limpieza aplicada y guardada'}. Versión actual: ${data.version}.`)
      setOperations(await request(`/api/datasets/${dataset.id}/operations`))
      setVersions(await request(`/api/datasets/${dataset.id}/versions`))
    } catch (err) { setError(err.message) } finally { setBusy(false) }
  }

  async function loadAudit(datasetId = dataset?.id) {
    if (!datasetId) return
    try {
      const [ops, vers] = await Promise.all([request(`/api/datasets/${datasetId}/operations`), request(`/api/datasets/${datasetId}/versions`)])
      setOperations(ops); setVersions(vers)
    } catch (err) { setError(err.message) }
  }

  async function downloadVersion(version) {
    if (!dataset) return
    try {
      const res = await fetch(`${API}/api/datasets/${dataset.id}/versions/${version}/download`, { headers: { Authorization: `Bearer ${token}` } })
      if (!res.ok) throw new Error('No se pudo descargar esa versión.')
      const blob = await res.blob(); const url = URL.createObjectURL(blob)
      const a = document.createElement('a'); a.href = url; a.download = `version_${version}_${dataset.filename}`; a.click(); URL.revokeObjectURL(url)
    } catch (err) { setError(err.message) }
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
      {view==='quality' && <>{!dataset ? <section className="empty panel"><div className="empty-icon">▤</div><h2>Aún no hay un dataset abierto</h2><p>Regresa al inicio y selecciona un archivo CSV para comenzar.</p><button className="primary" onClick={()=>setView('overview')}>Cargar dataset</button></section> : <><section className="panel"><div className="panel-title"><div><span className="eyebrow">DATASET ACTUAL</span><h2>{dataset.filename}</h2><p>El archivo original se conserva; las acciones afectan la copia de trabajo.</p></div><button className="secondary" onClick={download}>↓ Descargar CSV de trabajo</button></div><Stats profile={dataset.profile}/></section><section className="panel"><div className="panel-title"><div><h2>Asistente de calidad</h2><p>Versión {dataset.version || 1}. Inspecciona los registros antes de decidir qué hacer.</p></div><span className="pill">{dataset.recommendations?.length||0} hallazgos</span></div>{!dataset.recommendations?.length ? <div className="empty-small">No se detectaron problemas en las reglas básicas actuales.</div> : <div className="recommendations">{dataset.recommendations.map(r=><article className="recommendation" key={r.id}><div className="rec-content"><b>{r.label}</b><p>{r.reason}</p><small>Estado: {r.status || 'Detectada'} · {r.detection_method} · {r.column ? `Columna: ${r.column} (${r.dtype})` : 'Filas completas'} · {r.affected_percent}% del dataset. {r.risk}</small></div><span className="count">{fmt(r.count)}</span><button className="secondary" disabled={busy} onClick={()=>inspectRecommendation(r)}>Ver registros</button></article>)}</div>}</section><section className="panel"><div className="panel-title"><div><h2>Vista previa</h2><p>Primeras 10 filas de la copia de trabajo.</p></div><button className="secondary" onClick={openEda}>Ir al análisis exploratorio →</button></div><DataTable rows={dataset.preview||[]}/></section><section className="panel"><div className="panel-title"><div><h2>Historial y versiones</h2><p>Operaciones registradas y archivos de trabajo guardados.</p></div><button className="secondary" onClick={()=>loadAudit(dataset.id)}>Actualizar historial</button></div><h3 className="audit-heading">Versiones del dataset</h3>{versions.length ? versions.map(v=><div className="audit-row" key={v.version}><span><b>Versión {v.version}</b><small>{new Date(v.created_at).toLocaleString('es-CO')}</small></span><button className="secondary" onClick={()=>downloadVersion(v.version)}>Descargar</button></div>) : <p className="muted">No hay versiones disponibles todavía.</p>}<h3 className="audit-heading">Operaciones de limpieza</h3>{operations.length ? operations.map(o=><div className="audit-row" key={o.id}><span><b>{o.action} {o.column ? `· ${o.column}` : ''}</b><small>{new Date(o.created_at).toLocaleString('es-CO')} · versión origen {o.source_version}</small></span><span className="pill">{o.status}</span></div>) : <p className="muted">Todavía no hay operaciones registradas.</p>}</section></>}</>}
      {view==='eda' && <>{!eda ? <section className="empty panel"><div className="empty-icon">◌</div><h2>Explora tu dataset</h2><p>Abre el análisis del dataset actual para calcular estadísticas y correlaciones.</p><button className="primary" onClick={openEda}>Calcular análisis exploratorio</button></section> : <><section className="panel"><div className="panel-title"><div><h2>Hallazgos iniciales</h2><p>Dataset: {dataset?.filename} · versión {eda.version}. Excluidos solo del análisis: {eda.excluded_rows_from_analysis || 0}.</p></div><button className="secondary" onClick={download}>↓ Descargar CSV</button></div><div className="findings">{eda.findings.map((x,i)=><div key={i} className="finding"><span>{String(i+1).padStart(2,'0')}</span>{x}</div>)}</div></section><section className="panel"><div className="panel-title"><div><h2>Estadísticas descriptivas</h2><p>Resumen de las columnas numéricas.</p></div></div><NumericTable stats={eda.profile.numeric_stats}/></section><section className="panel"><div className="panel-title"><div><h2>Distribuciones</h2><p>Frecuencias agrupadas para variables numéricas.</p></div></div>{Object.entries(eda.distributions||{}).length ? <div className="distribution-grid">{Object.entries(eda.distributions).map(([col,bins])=><div className="dist-card" key={col}><h3>{col}</h3>{bins.map((b,i)=><div className="bar-row" key={i}><small>{b.range}</small><div className="bar-track"><i style={{width:`${Math.max(2,b.count/Math.max(...bins.map(x=>x.count),1)*100)}%`}}/></div><b>{b.count}</b></div>)}</div>)}</div>:<p className="muted">No hay columnas numéricas para graficar.</p>}</section><section className="panel"><div className="panel-title"><div><h2>Matriz de correlación</h2><p>Correlación de Pearson entre variables numéricas. No implica causalidad.</p></div></div><Correlation data={eda.correlation}/></section><section className="panel"><div className="panel-title"><div><h2>Primeras filas</h2><p>Vista tabular de los datos analizados.</p></div></div><DataTable rows={eda.preview||[]}/></section></>}</>}
      {view==='history' && <section className="panel"><div className="panel-title"><div><h2>Datasets cargados</h2><p>Archivos asociados a tu cuenta.</p></div><button className="secondary" onClick={loadHistory}>↻ Actualizar</button></div>{history.length ? <div className="history-list">{history.map(x=><button className="history-item" key={x.id} onClick={()=>openDataset(x.id)}><span className="file-icon">CSV</span><span><b>{x.filename}</b><small>{new Date(x.created_at).toLocaleString('es-CO')}</small></span><span>→</span></button>)}</div>:<div className="empty-small">No hay datasets cargados. Sube un CSV desde Inicio.</div>}</section>}
      {activeRec && <div className="modal-backdrop"><section className="panel cleaning-modal"><div className="panel-title"><div><span className="eyebrow">INSPECCIÓN DE REGISTROS · VERSIÓN {dataset?.version || 1}</span><h2>{activeRec.label}</h2><p>{recordTotal} registros coinciden con la regla. Selecciona únicamente los que deseas tratar.</p></div><button className="secondary" onClick={()=>{setActiveRec(null);setPreviewResult(null)}}>Cerrar</button></div>
        {!previewResult ? <><div className="record-tools"><input value={recordSearch} onChange={e=>setRecordSearch(e.target.value)} placeholder="Buscar en los registros afectados…"/><button className="secondary" onClick={()=>searchRecords(1)} disabled={busy}>Buscar</button><button className="secondary" onClick={()=>setSelectedRows(prev=>Array.from(new Set([...prev, ...records.map(r=>r.__row_id)])))}>Seleccionar página</button><button className="link" onClick={()=>setSelectedRows([])}>Limpiar selección</button></div>
          <p className="muted">Seleccionados: {selectedRows.length} · Página {recordPage} de {recordPages}</p><div className="table-wrap"><table><thead><tr><th>Elegir</th><th>Fila de origen</th>{records[0] && Object.keys(records[0]).filter(k=>k!=='__row_id').map(k=><th key={k}>{k}</th>)}</tr></thead><tbody>{records.map(r=><tr key={r.__row_id}><td><input type="checkbox" checked={selectedRows.includes(r.__row_id)} onChange={e=>setSelectedRows(prev=>e.target.checked?[...prev,r.__row_id]:prev.filter(x=>x!==r.__row_id))}/></td><td>{r.__row_id + 1}</td>{Object.keys(r).filter(k=>k!=='__row_id').map(k=><td key={k}>{r[k]===null?'—':String(r[k])}</td>)}</tr>)}</tbody></table></div>
          <div className="record-pagination"><button className="secondary" disabled={recordPage<=1||busy} onClick={()=>searchRecords(recordPage-1)}>Anterior</button><button className="secondary" disabled={recordPage>=recordPages||busy} onClick={()=>searchRecords(recordPage+1)}>Siguiente</button></div>
          <div className="clean-config"><label>Acción para los registros seleccionados<select value={cleanMethod} onChange={e=>setCleanMethod(e.target.value)}>{activeRec.action==='missing' && <><option value="median">Reemplazar por mediana (numérico)</option><option value="mean">Reemplazar por media (numérico)</option><option value="mode">Reemplazar por moda</option><option value="custom">Usar valor personalizado</option><option value="drop_rows">Eliminar filas de la versión de trabajo</option><option value="exclude_analysis">Excluir del análisis (conservar CSV)</option><option value="keep">Conservar sin cambios</option><option value="review">Marcar como revisado</option></>}{activeRec.action==='outliers' && <><option value="review">Solo revisar, sin cambios</option><option value="keep">Conservar valores</option><option value="mean">Reemplazar por media</option><option value="median">Reemplazar por mediana</option><option value="capping">Limitar extremos (capping IQR)</option><option value="drop_rows">Eliminar filas de la versión de trabajo</option><option value="exclude_analysis">Excluir del análisis (conservar CSV)</option></>}{activeRec.action==='duplicates' && <><option value="drop_rows">Eliminar duplicados seleccionados</option><option value="exclude_analysis">Excluir del análisis (conservar CSV)</option><option value="review">Solo revisar, sin cambios</option><option value="keep">Conservar duplicados</option></>}{activeRec.action==='invalid_type' && <><option value="review">Solo revisar</option><option value="custom">Corregir con valor personalizado</option><option value="drop_rows">Eliminar filas seleccionadas</option><option value="exclude_analysis">Excluir del análisis</option></>}</select></label>{['custom'].includes(cleanMethod) && <label>Valor personalizado<input value={customValue} onChange={e=>setCustomValue(e.target.value)} placeholder="Escribe el valor"/></label>}</div>
          <div className="action-row"><span className="muted">La vista previa no modifica el dataset.</span><button className="primary" disabled={!selectedRows.length||busy} onClick={createCleaningPreview}>{busy?'Calculando…':'Previsualizar cambios'}</button></div></> : <><h3>Vista previa calculada por el backend</h3><Stats profile={previewResult.preview?.before_profile}/><div className="preview-summary"><p><b>Acción:</b> {previewResult.preview?.method}</p><p><b>Filas antes/después:</b> {fmt(previewResult.preview?.source_rows)} / {fmt(previewResult.preview?.result_rows)}</p><p><b>Celdas modificadas:</b> {fmt(previewResult.preview?.cells_changed)}</p><p><b>Filas que se eliminarían:</b> {fmt(previewResult.preview?.rows_removed)}</p><p><b>Registros excluidos del análisis:</b> {fmt(previewResult.preview?.rows_excluded_from_analysis)}</p>{(previewResult.preview?.warnings||[]).map((w,i)=><p className="muted" key={i}>{w}</p>)}</div>{previewResult.preview?.changes?.length>0 && <><h3>Valores originales y propuestos</h3><DataTable rows={previewResult.preview.changes}/></>}<div className="action-row"><button className="secondary" onClick={()=>setPreviewResult(null)}>Volver y cambiar</button><button className="primary" disabled={busy} onClick={confirmCleaningPreview}>{busy?'Guardando…':'Confirmar y guardar versión'}</button></div></>}
        <div className="panel history-subpanel"><h3>Historial reciente de limpieza</h3>{operations.length ? operations.slice(0,5).map(o=><p key={o.id}><b>{o.action}</b> · {o.column || 'filas completas'} · {o.status} · versión origen {o.source_version}</p>) : <p className="muted">Aún no hay operaciones registradas.</p>}<h3>Versiones guardadas</h3>{versions.map(v=><p key={v.version}>Versión {v.version} · {new Date(v.created_at).toLocaleString('es-CO')}</p>)}</div>
      </section></div>}
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
