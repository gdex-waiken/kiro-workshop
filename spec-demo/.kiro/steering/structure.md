---
inclusion: always
---

# Project structure

```
app/
├── domain/
│   ├── models.py          # Product, CartItem, Cart
│   └── errors.py          # DomainError and its subclasses
├── application/
│   ├── ports.py           # CartRepository, ProductCatalog (ABCs)
│   ├── dtos.py            # CartView, CartLineView (read models)
│   └── use_cases.py       # AddItemToCart, GetCart, ...
└── adapters/
    ├── repositories.py    # InMemoryCartRepository, InMemoryProductCatalog, seed products
    ├── api.py             # Pydantic schemas, APIRouter, error handlers
    └── main.py            # create_app() and module-level `app`
tests/
├── domain/                # pure unit tests, no fakes needed
├── application/           # use case tests with in-test fakes for the ports
└── adapters/              # API tests with TestClient
```

## Where things go
- New business rule -> `app/domain/`, with a test in `tests/domain/`.
- New user action -> one use case class in `app/application/use_cases.py`.
- New endpoint -> `app/adapters/api.py`. Keep routes thin: parse, call a use case, return a schema.
- Tests mirror the `app/` layer they test.

## Naming
- Modules and functions: `snake_case`. Classes: `PascalCase`.
- Use cases are verbs: `AddItemToCart`, `RemoveItemFromCart`. One public method: `execute(...)`.
- Errors end in `Error`: `ProductNotFoundError`.
- Test files: `test_<subject>.py`. Test names say the behaviour: `test_adding_same_product_twice_merges_lines`.

## Run commands
- Tests: `pytest`
- Server: `uvicorn app.adapters.main:app --reload`
