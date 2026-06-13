# Arquitectura del Modulo CAG

## Diagrama de Flujo

```
Usuario (Frontend)
    │
    ▼
POST /api/ask {user_id, question}
    │
    ▼
server.py ──► assistant.py ──► knowledge.py ──► knowledge_base.json
    │              │                    │
    │              │                    ▼
    │              │            retrieve_snippets()
    │              │            (keyword matching)
    │              │                    │
    │              │                    ▼
    │              │         base_answer construida
    │              │                    │
    │              ▼                    ▼
    │       context_store.py ──► cag.py::apply_context()
    │       (ContextStore)        │
    │         list_for_user()     │
    │              │              ├─ audience=principiante → prefijo
    │              │              └─ preferred_style → analogia
    │              │              │
    │              ▼              ▼
    │       (answer_modificada, context_used)
    │                    │
    └────────────────────┘
         Response JSON
```

## Componentes

### 1. ContextStore (`backend/context_store.py`)
- Almacenamiento en memoria: `{user_id: [{key, value}, ...]}`
- `save(user_id, key, value)` → guarda/actualiza contexto
- `list_for_user(user_id)` → devuelve lista de contexto

### 2. CAG Engine (`backend/cag.py`)
- `apply_context(user_id, question, base_answer, context_items)`
- Adapta respuesta segun contexto del usuario
- Retorna (answer_modificada, keys_usadas)

### 3. Integracion (`backend/assistant.py`)
- Obtiene snippets de knowledge_base
- Obtiene contexto del usuario via ContextStore
- Aplica CAG y devuelve respuesta contextualizada

### 4. Singleton Compartido (`backend/store.py`)
- Instancia unica de ContextStore para todo el backend
- Asegura que contexto guardado via API sea visible al asistente

## Endpoints API

| Metodo | Ruta | Proposito |
|--------|------|-----------|
| GET | /health | Health check |
| POST | /api/ask | Preguntar al asistente (con CAG) |
| POST | /api/context | Guardar contexto de usuario |
| GET | /api/context?user_id=X | Recuperar contexto de usuario |

## Caso de Uso: "Explicar como principiante"

1. POST /api/context → `{user_id: "luis", key: "audience", value: "explicar como principiante"}`
2. POST /api/ask → `{user_id: "luis", question: "Que es CAG?"}`
3. Respuesta incluye: "Explicado para explicar como principiante: Segun la base de conocimiento..."
4. `context_used`: ["audience"]
