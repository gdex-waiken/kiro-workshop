---
inclusion: always
---

# Project structure

```
app/
├── domain/          # Cart, CartLine, errors
├── application/     # ports and use cases: AddItemToCart, GetCart
├── adapters/        # FastAPI routes and schemas, in-memory repository, catalog loader
└── main.py          # create_app() and the module-level `app`
tests/               # mirrors app/: domain, application, adapters
```

## Where things go
- New business rule -> `app/domain/`, with a test in `tests/domain/`.
- New user action -> one use case in `app/application/`.
- New endpoint -> `app/adapters/`. Keep routes thin: parse, call a use case, return a schema.

## Run commands
- Tests: `pytest`
- Service: `uvicorn app.main:app --port 8000`
- Answer key: `python check_cart.py` (with the service running)
