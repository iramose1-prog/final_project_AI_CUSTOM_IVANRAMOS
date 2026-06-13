# FASE 2 - Logica CAG

**Estudiante:** IVAN RAMOS 090-21-804

## Archivo modificado: `backend/cag.py`

```python
def apply_context(user_id, question, base_answer, context_items):
    if not context_items:
        return base_answer, []

    answer = base_answer
    keys_used = []

    for item in context_items:
        key = item["key"]
        value = item["value"]

        if key == "audience":
            answer = f"Explicado para {value}: {answer}"
            keys_used.append(key)
        elif key == "preferred_style":
            style_phrases = {
                "explicaciones con analogias": "Para explicarlo con una analogia: ",
            }
            prefix = style_phrases.get(value)
            if prefix:
                answer = f"{prefix}{answer}"
                keys_used.append(key)

    return answer, keys_used
```

## Archivo modificado: `backend/assistant.py`

```python
from backend.cag import apply_context
from backend.knowledge import retrieve_snippets
from backend.store import context_store

def answer_question(user_id, question):
    snippets = retrieve_snippets(question)
    if not snippets:
        base_answer = "No encontre informacion suficiente..."
        context_items = context_store.list_for_user(user_id)
        answer, context_used = apply_context(user_id, question, base_answer, context_items)
        return {"answer": answer, "context_used": context_used, ...}

    source_text = " ".join(item["content"] for item in snippets)
    base_answer = f"Segun la base de conocimiento del curso: {source_text}"
    context_items = context_store.list_for_user(user_id)
    answer, context_used = apply_context(user_id, question, base_answer, context_items)
    return {"answer": answer, "context_used": context_used, "sources": [...], ...}
```

## Prueba que pasa en esta fase

```
test_ask_uses_context_to_influence_later_response ... ok
```

## Demo: Sin CAG vs Con CAG

**Sin contexto:** `context_used: []`
**Con contexto (audience=principiante):** `context_used: ["audience"]`
  - answer: "Explicado para explicar como principiante: Segun la base de conocimiento..."
