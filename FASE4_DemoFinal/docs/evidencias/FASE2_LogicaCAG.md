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

Integra `apply_context` y `context_store` para obtener el contexto del usuario y adaptar la respuesta.

## Prueba que pasa

```
test_ask_uses_context_to_influence_later_response ... ok
```

## Demo

**Sin contexto:** `context_used: []`
**Con contexto (audience=principiante):** `context_used: ["audience"]`
- answer: "Explicado para explicar como principiante: Segun la base de conocimiento..."
