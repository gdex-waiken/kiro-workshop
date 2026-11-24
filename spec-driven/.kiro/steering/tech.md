---
inclusion: always
---

# Tech stack and rules

## Stack
- Python 3.12
- FastAPI + Pydantic v2, served by uvicorn on port 8000
- pytest, with FastAPI `TestClient` for API tests
- In-memory storage behind repository interfaces. No database, no Docker, no cloud.

## Architecture: Clean Architecture
- Three layers: `domain` -> `application` -> `adapters`. Dependencies point inward only.
- `domain`: entities and business rules. Standard library only.
- `application`: use cases. They reach storage only through ports (abstract base classes).
- `adapters`: FastAPI routes, Pydantic schemas, in-memory repositories, the CSV loaders.

## Coding rules
- Times are UTC, ISO 8601, ending in `Z`.
- Type hints on every function.
- Domain errors are plain exceptions, mapped to HTTP status codes only in the HTTP adapter.
- A failed request leaves everything exactly as it was.
- Keep `requirements.txt` up to date.

## Working rules
- Test-Driven Development: write a failing test, see it fail, make it pass, then refactor.
- Run `pytest` before you mark a task done.
