---
inclusion: manual
---

# Code review checklist (type #code-review in chat to use it)

Review the current changes against this list. Reply with a short table: item, pass/fail, file:line for each failure.

1. Every acceptance criterion in the spec has a test, and `pytest` passes.
2. The domain layer imports only the standard library.
3. No `float` anywhere money is handled.
4. Routes are thin: no business rules in `app/adapters/api.py`.
5. Error cases leave the cart unchanged, and a test proves it.
6. No feature, dependency or file that the spec did not ask for.
7. README run instructions still work.
