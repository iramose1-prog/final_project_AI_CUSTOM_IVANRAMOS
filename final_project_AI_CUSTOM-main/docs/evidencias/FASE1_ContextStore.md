# FASE 1 - ContextStore

**Estudiante:** IVAN RAMOS 090-21-804

## Archivo modificado: `backend/context_store.py`

```python
class ContextStore:
    def __init__(self):
        self._data = {}

    def save(self, user_id, key, value):
        if user_id not in self._data:
            self._data[user_id] = []
        existing = [item for item in self._data[user_id] if item["key"] == key]
        if existing:
            existing[0]["value"] = value
        else:
            self._data[user_id].append({"key": key, "value": value})
        return True

    def list_for_user(self, user_id):
        return self._data.get(user_id, [])
```

## Archivo nuevo: `backend/store.py`

```python
from backend.context_store import ContextStore
context_store = ContextStore()
```

## Pruebas que pasan en esta fase

```
test_saves_context_for_user ... ok
test_retrieves_context_for_user ... ok
```

## Endpoints habilitados

| Metodo | Ruta | Resultado |
|--------|------|-----------|
| POST | /api/context | 201 {"saved": true} |
| GET | /api/context?user_id=X | 200 con lista de contexto |
