---
inclusion: always
---

# Tech stack and rules

## Stack
- Python 3.12
- FastAPI + Pydantic v2 for the HTTP layer, served by uvicorn
- pytest, with FastAPI `TestClient` for API tests
- No database: in-memory storage behind repository interfaces
- No cloud or infrastructure code. Everything runs locally.

## Architecture: Clean Architecture
- Three layers: `domain` -> `application` -> `adapters`. Dependencies point inward only.
- `domain`: entities and business rules. Standard library only. No FastAPI, no Pydantic.
- `application`: use cases. They talk to storage only through ports (abstract base classes).
- `adapters`: FastAPI routes, Pydantic schemas, in-memory repositories.
- Wire concrete adapters together in one place: `create_app()`.

## Coding rules
- Money is `decimal.Decimal`, never `float`. Return money in JSON as strings with 2 decimals (`"19.98"`).
- Type hints on every function and method.
- Domain errors are plain exceptions. Map them to HTTP status codes only in the HTTP adapter.
- Validate input at the boundary (Pydantic) **and** protect invariants in the domain.
- Keep `requirements.txt` up to date with every dependency.

## Working rules
- Test-Driven Development: write a failing test, run it and see it fail, make it pass, then refactor.
- Run `pytest` before you mark a task done.
- Do not add libraries that are not listed above without asking.
