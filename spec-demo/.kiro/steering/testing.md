---
inclusion: fileMatch
fileMatchPattern: "tests/**/*.py"
---

# Testing rules (loaded only when a test file is in context)

- One behaviour per test. The test name says the behaviour.
- Arrange / Act / Assert, separated by a blank line.
- Domain tests: build entities directly. No fakes, no FastAPI.
- Application tests: write small fakes in the test file that implement the ports, including a fixed clock. Do not use the in-memory adapters here.
- API tests: a pytest fixture calls `create_app()` for a fresh app per test, wrapped in `TestClient`.
- Test the title limits at the edges: 1 and 100 characters pass, empty, only spaces and 101 characters fail.
- For every error case, also assert that state did not change (the list is the same as before).
- No sleeps, no network, no randomness.
