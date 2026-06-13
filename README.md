# Proyecto Examen Final - Módulo 3 IVAN RAMOS

Proyecto base para la evaluación práctica del módulo 3. Los requisitos oficiales están en `Enunciado en la serie II de la evaluación final`.

## Inicio rápido

1. Abra la carpeta `ProyectoExamen`.
2. Ejecute las pruebas base.
3. Levante el backend.
4. Abra el frontend para revisar el estado inicial.

## Estructura

| Ruta | Contenido |
|---|---|
| `backend/` | Código del servidor y lógica base del asistente. |
| `frontend/` | Interfaz web estática para interactuar con el backend. |
| `data/` | Base de conocimiento inicial del proyecto. |
| `tests/base/` | Pruebas base que deben pasar desde el inicio. |
| `tests/validation/` | Pruebas de validación de la entrega final. |
| `docs/` | Espacio para documentación técnica y evidencias del estudiante. |

## Ejecutar pruebas base

```bash
./scripts/run_base_tests.sh
```

Estas pruebas validan que el proyecto inicial funciona correctamente.

## Ejecutar backend

```bash
PYTHONPATH=. python3 -m backend.server
```

El backend queda disponible en `http://127.0.0.1:8000`.

## Abrir frontend

Abra `frontend/index.html` en un navegador. También puede servir la carpeta con un servidor estático local si lo prefiere.

## Validación final

```bash
./test.sh
```

En el proyecto base, la validación final está destinada a fallar. Debe utilizarse como autoevaluación cuando el trabajo solicitado en el enunciado esté completo.

Sprint 1 — ContextStore (3 días)
Objetivo: Implementar la capa de persistencia de contexto.

Tarea	Archivo	Criterio de Aceptación
Implementar save(user_id, key, value) en memoria	context_store.py:9-15	POST /api/context → 201 {"saved": true}
Implementar list_for_user(user_id)	context_store.py:17-19	GET /api/context?user_id=X → 200 con lista de items
Probar manualmente con curl o el frontend	—	Items persisten entre requests
Definition of Done: test_saves_context_for_user y test_retrieves_context_for_user pasan.

Sprint 2 — Lógica CAG (3 días)
Objetivo: Implementar la adaptación de respuestas según contexto.

Tarea	Archivo	Criterio de Aceptación
Implementar apply_context() que modifique el answer según contexto	cag.py:5-6	La respuesta incluye palabras clave del contexto
Integrar apply_context en assistant.py::answer_question()	assistant.py:10-16	context_used se llena con las claves de contexto usadas
Conectar cag.py con context_store.py	ambos	apply_context recibe contexto real, no placeholder
Definition of Done: test_ask_uses_context_to_influence_later_response pasa.

Sprint 3 — Integración y Validación (2 días)
Objetivo: Pasar la suite completa de validación.

Tarea	Criterio
Ejecutar test.sh y verificar 3/3 tests verdes	Ran 3 tests in ... OK
Probar casos borde: usuario sin contexto, contexto vacío	Sin errores
Verificar que pruebas base sigan pasando	test_base_api.py → OK
Definition of Done: ./test.sh reporta 0 fallos.

Sprint 4 — Demo y Evidencias (2 días)
Objetivo: Documentar y presentar resultados.

Tarea	Archivo
Capturar pantallas del frontend funcionando	docs/evidencias/
Documentar arquitectura CAG implementada	docs/
Demostrar: "Qué es CAG?" con audience=principiante	Frontend + backend
