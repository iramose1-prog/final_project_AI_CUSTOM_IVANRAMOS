# Proyecto Examen Final - Módulo 3 IVAN RAMOS

Descripción del Proyecto

Este proyecto corresponde a la evaluación práctica del módulo 3 y consiste en la integración de un mecanismo de Context-Augmented Generation (CAG) sobre una arquitectura existente basada en Retrieval-Augmented Generation (RAG).

El objetivo principal fue permitir que el asistente pueda almacenar, recuperar y reutilizar contexto asociado a cada usuario para generar respuestas más personalizadas y coherentes entre diferentes interacciones.

Durante el desarrollo se implementó:

Persistencia de contexto por usuario.
Recuperación de contexto almacenado.
Integración del contexto dentro del flujo de generación de respuestas.
Pruebas de validación para garantizar el correcto funcionamiento.
Documentación del proceso utilizando Scrum, SDD, BDD y TDD.

Funcionalidades Implementadas
Persistencia de Contexto

Permite almacenar información asociada a un usuario mediante el endpoint:

POST /api/context

Ejemplo:

{
  "user_id": "ana",
  "key": "audience",
  "value": "explicar como principiante"
}
Recuperación de Contexto

Permite consultar el contexto almacenado para un usuario:

GET /api/context?user_id=ana
Aplicación de Contexto

El sistema utiliza la información almacenada para adaptar futuras respuestas.

Ejemplos:

Explicar conceptos para principiantes.
Adaptar el estilo de respuesta.
Reutilizar preferencias previamente registradas.

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

Metodología de Desarrollo

El proyecto fue desarrollado utilizando Scrum en cuatro sprints:

Sprint 1: Análisis del proyecto base y validación inicial.
Sprint 2: Implementación del Context Store.
Sprint 3: Integración de la lógica CAG.
Sprint 4: Validación, documentación y evidencias.

Documentar arquitectura CAG implementada	docs/
Demostrar: "Qué es CAG?" con audience=principiante	Frontend + backend
