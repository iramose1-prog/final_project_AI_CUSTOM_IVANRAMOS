# FASE 4 - Demo Final

**Estudiante:** IVAN RAMOS 090-21-804

## Frontend Interfaz Web

Archivo: `frontend/index.html`

### Diseno
- Tema oscuro azul/pizarra
- Acentos en celeste (#38bdf8)
- Tipografia: Segoe UI + Courier New
- Grid de 2 columnas responsive

### Nombre visible
**IVAN RAMOS 090-21-804** en el encabezado de la pagina

## Demo Paso a Paso

### 1. Iniciar backend
```powershell
cd C:\Users\alext\Downloads\final_project_AI_CUSTOM-main\final_project_AI_CUSTOM-main
$env:PYTHONPATH = "."
python -m backend.server
# → http://127.0.0.1:8000
```

### 2. Abrir frontend
```
Abrir: frontend/index.html en el navegador
```

### 3. Probar sin contexto
- Usuario: student-01
- Pregunta: "Que es CAG?"
- Resultado: `context_used: []`

### 4. Guardar contexto
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/context" `
  -Method POST -ContentType "application/json" `
  -Body '{"user_id":"student-01","key":"audience","value":"explicar como principiante"}'
```

### 5. Probar con CAG activo
- Recargar frontend (F5)
- Usuario: student-01
- Pregunta: "Que es CAG?"
- Resultado: `context_used: ["audience"]`
- answer: "Explicado para explicar como principiante: ..."

## Evidencias de Archivos

| Archivo | Descripcion |
|---------|-------------|
| backend/context_store.py | Almacenamiento en memoria de contexto |
| backend/store.py | Singleton compartido |
| backend/cag.py | Logica de adaptacion de respuestas |
| backend/assistant.py | Integracion CAG + ContextStore |
| backend/server.py | Endpoints API |
| frontend/index.html | Interfaz de usuario |
| frontend/styles.css | Estilos con diseno personalizado |
| frontend/app.js | Logica del frontend |
