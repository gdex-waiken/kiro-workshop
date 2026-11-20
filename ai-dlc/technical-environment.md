# Technical environment

The platform standards for every KedaiKu service. Your Application Design must follow them. If the AI proposes something this page prohibits, reject it at the gate and point to the rule.

## Platform standards

| Standard | Detail |
|---|---|
| Language | Python 3.12 |
| HTTP | FastAPI, served locally by uvicorn on port **8000** |
| Architecture | Clean Architecture: `domain` → `application` (use cases) → `adapters`. Dependencies point inward only |
| Storage | In-memory, behind a repository interface (port), so a real database can be added later as a new adapter |
| Tests | pytest. Test-Driven Development: write a failing test, see it fail, make it pass, then refactor |
| Money | `decimal.Decimal` in code. Strings with exactly 2 decimal places in JSON (`"12.90"`) |
| Catalog | Loaded at startup from `sample-data/catalog.csv`. The cart never accepts a name or price from the client |
| Contract | `api-contract.md` is fixed. The mobile app team has already built against it |

## Prohibitions

- **No database, no Docker, no cloud deployment.** Everything runs on the laptop.
- **No login or authentication** in this release.
- **No new endpoints or fields** beyond `api-contract.md` without the Product Owner's approval.
- **No hand edits outside the workflow.** If you change a file yourself, tell the AI so its documents stay true.

## How the service is checked

```bash
uvicorn app.main:app --port 8000          # in one terminal
python check_cart.py                      # in another, from this folder
```

`check_cart.py` replays every step in `sample-data/cart-scenario.csv` against the running service and compares the result with the expected status, item count and subtotal. It uses only the Python standard library.
