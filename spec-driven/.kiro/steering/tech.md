---
inclusion: always
---

# Shopping cart API: technical rules

- Language: Python 3.12.
- Follow Clean Architecture. Keep three layers:
  - `domain`: entities and business rules. No framework or storage imports.
  - `application`: use cases that work with the domain through interfaces (ports).
  - `adapters`: the FastAPI HTTP layer and the in-memory repository.
- Follow Test-Driven Development. Write a failing test first, show it failing, make it pass, then refactor. Never skip the failing step.
- Use pytest for all tests.
- Expose the API with FastAPI and run it locally with uvicorn.
- Store carts in an in-memory repository behind a repository interface, so a real database can be added later as a new adapter.
- Everything runs locally. Do not add any cloud deployment or infrastructure code.
- Build one feature at a time. Start with "add items to cart".
- Keep a `requirements.txt` with every dependency, and a short README that says how to install, test and run the app.
