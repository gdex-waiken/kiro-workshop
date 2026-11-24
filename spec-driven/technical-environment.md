# Technical environment

The platform standards for every Pelita Group service. Your Application Design must follow them. If the AI proposes something this page prohibits, reject it at the gate and point to the rule.

## Platform standards

| Standard | Detail |
|---|---|
| Language | Python 3.12 |
| HTTP | FastAPI, served locally by uvicorn on port **8000** |
| Architecture | Clean Architecture: `domain` → `application` (use cases) → `adapters`. Dependencies point inward only |
| Storage | In-memory, behind a repository interface (port), so a real database can be added later as a new adapter |
| Tests | pytest. Test-Driven Development: write a failing test, see it fail, make it pass, then refactor |
| Time | `submitted_at` is UTC, ISO 8601, ending in `Z` (`"2026-12-09T03:31:07Z"`) |
| Reference data | Staff list and categories are loaded at startup from `sample-data/staff.csv` and `sample-data/categories.csv`. The service never accepts a name or department from the client |
| Contract | `api-contract.md` is fixed. The app team has already built against it |

## Prohibitions

- **No database, no Docker, no cloud deployment.** Everything runs on the laptop.
- **No login or authentication** in this release.
- **No new endpoints or fields** beyond `api-contract.md` without the Product Owner's approval.
- **No calls to outside services**, including AI models.
- **No hand edits outside the workflow.** If you change a file yourself, tell the AI so its documents stay true.

## How the service is checked

```bash
uvicorn app.main:app --port 8000          # in one terminal
python check_ideas.py                     # in another: Feature 1
python check_ideas.py --feature 2         # once Feature 2 is built
```

`check_ideas.py` replays every step in `sample-data/ideas-scenario.csv` (or `votes-scenario.csv`) against the running service and compares each result with the expected status, idea count, order and vote count. It uses only the Python standard library.
