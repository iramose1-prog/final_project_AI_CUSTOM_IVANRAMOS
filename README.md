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

# Planificación Scrum

## Sprint 1 – Implementación del Context Store

**Objetivo:** Implementar la persistencia de contexto para que el sistema pueda almacenar información asociada a cada usuario.

### Actividades

* Analizar el funcionamiento actual del endpoint `/api/context`.
* Implementar `save(user_id, key, value)` en `context_store.py`.
* Implementar `list_for_user(user_id)` en `context_store.py`.
* Realizar pruebas manuales mediante API y frontend.

### Criterios de aceptación

* POST `/api/context` retorna `201 {"saved": true}`.
* GET `/api/context?user_id=X` retorna los elementos almacenados.
* Los datos persisten entre solicitudes.

### Resultado esperado

Las pruebas `test_saves_context_for_user` y `test_retrieves_context_for_user` deben ejecutarse exitosamente.

### Observación personal

Este sprint es fundamental porque constituye la base del CAG. Sin almacenamiento de contexto no es posible recuperar información en consultas futuras.

---

## Sprint 2 – Implementación de la lógica CAG

**Objetivo:** Incorporar el contexto almacenado en la generación de respuestas.

### Actividades

* Implementar `apply_context()` en `cag.py`.
* Integrar la lógica CAG en `assistant.py`.
* Conectar el módulo CAG con `context_store.py`.

### Criterios de aceptación

* Las respuestas reflejan información previamente almacenada.
* `context_used` contiene las claves de contexto utilizadas.
* El contexto recuperado proviene del almacenamiento real.

### Resultado esperado

La prueba `test_ask_uses_context_to_influence_later_response` debe aprobarse.

### Observación personal

La diferencia principal entre RAG y CAG es que el sistema comienza a utilizar información específica del usuario, mejorando la personalización de las respuestas.

---

## Sprint 3 – Integración y Validación

**Objetivo:** Verificar que la integración funcione correctamente sin afectar el comportamiento existente.

### Actividades

* Ejecutar pruebas de validación.
* Verificar casos sin contexto.
* Verificar casos con contexto vacío.
* Ejecutar nuevamente las pruebas base.

### Criterios de aceptación

* Todas las pruebas de validación deben aprobarse.
* No deben existir regresiones en las funcionalidades originales.

### Resultado esperado

La suite de pruebas debe finalizar sin errores ni fallos.

### Observación personal

Esta fase permite comprobar que el nuevo módulo se integra correctamente con la arquitectura existente y mantiene la estabilidad del sistema.

---

## Sprint 4 – Evidencias y Entrega

**Objetivo:** Preparar la documentación y evidencias requeridas para la evaluación final.

### Actividades

* Capturar evidencias del funcionamiento.
* Documentar la arquitectura implementada.
* Completar README.md.
* Completar PROMPTS.md.
* Crear Pull Request y realizar merge.

### Criterios de aceptación

* Evidencias disponibles en `docs/evidencias/`.
* Documentación actualizada.
* Pull Request creado y fusionado.

### Resultado esperado

Repositorio listo para entrega con evidencia verificable de todo el proceso.

### Observación personal

La documentación y las evidencias permiten demostrar no solo el resultado final, sino también el proceso seguido para llegar a la solución.


Tarea	Archivo
Capturar pantallas del frontend funcionando	docs/evidencias/
Documentar arquitectura CAG implementada	docs/
Demostrar: "Qué es CAG?" con audience=principiante	Frontend + backend
