# FASE 3 - Validacion (6/6 Tests)

**Estudiante:** IVAN RAMOS 090-21-804

## Resultado Final

```
============================================
   TEST SUITE COMPLETO
============================================

>>> VALIDACION CAG:
test_ask_uses_context_to_influence_later_response ... ok
test_retrieves_context_for_user ... ok
test_saves_context_for_user ... ok
----------------------------------------------------------------------
Ran 3 tests in 0.614s
OK

>>> BASE:
test_ask_answers_from_knowledge_base ... ok
test_ask_requires_user_and_question ... ok
test_health_returns_ok ... ok
----------------------------------------------------------------------
Ran 3 tests in 0.597s
OK
```

## Comandos para reproducir

```powershell
cd C:\Users\alext\Downloads\final_project_AI_CUSTOM-main\final_project_AI_CUSTOM-main
$env:PYTHONPATH = "."

# Pruebas base
python -m unittest discover -s tests/base -p "test_*.py" -v

# Pruebas validacion CAG
python -m unittest discover -s tests/validation -p "test_*.py" -v
```

## Resumen

| Suite | Tests | Pasaron |
|-------|-------|---------|
| Base | 3 | 3 |
| Validacion CAG | 3 | 3 |
| **Total** | **6** | **6** |
