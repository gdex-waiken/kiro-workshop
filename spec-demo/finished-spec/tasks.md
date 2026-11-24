# Implementation plan: Submit and list ideas

Four tasks. Each one is a full red -> green -> refactor slice of one layer, so it can be checked on its own with `pytest`.

- [ ] 1. Domain: idea rules with tests
  - Set up `requirements.txt`, `pytest.ini` and the empty `app/` and `tests/` packages from `structure.md`
  - Write failing tests in `tests/domain/test_idea.py`, then implement `Idea`, `Idea.create` and `InvalidIdeaError`
  - Cover: titles of 1 and 100 characters accepted; empty, only spaces and 101 characters rejected; description of 1 and 1000 characters accepted, empty and 1001 rejected; title kept exactly as typed
  - _Requirements: 1.1, 1.3, 3.1, 3.2_

- [ ] 2. Application: ports and use cases with tests
  - Write failing tests in `tests/application/` using in-test fakes and a fixed clock, then implement `ports.py`, `dtos.py`, `SubmitIdea` and `ListIdeas`
  - Cover: new ids in order, `created_at` from the clock, a rejected idea adds nothing, list newest first with its count, empty list with count 0
  - _Requirements: 1.2, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2_

- [ ] 3. Adapters: in-memory storage and FastAPI with API tests
  - Write failing tests in `tests/adapters/test_api.py`, then implement the in-memory repository, `SystemClock`, the schemas, routes, error handlers and `create_app()`
  - Cover every row of the API table in `design.md`, including `created_at` ending in `Z` and two ideas sent in the same second listed in the right order
  - _Requirements: 1.1–1.3, 2.1–2.4, 3.1, 3.2_

- [ ] 4. README and final check
  - Write install, test and run instructions with one `curl` example for submit and one for list
  - Run the full `pytest` suite and fix any failure
  - _Requirements: all_
