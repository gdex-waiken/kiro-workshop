---
inclusion: fileMatch
fileMatchPattern: "app/adapters/**/*.py"
---

# HTTP API conventions (loaded only when an adapter file is in context)

- Resource paths are plural nouns: `/ideas`, `/ideas/{idea_id}`.
- `POST` that creates something returns **201** with the full new resource.
- `GET` returns **200**. A list comes back as `{"ideas": [...], "count": 2}`.
- Error status codes:
  | Domain error | HTTP |
  |---|---|
  | `InvalidIdeaError` | 422 |
  | `IdeaNotFoundError` | 404 |
- Error body: `{"detail": "<human-readable message that says what was wrong>"}`.
- Times are strings: UTC, ISO 8601, ending in `Z`.
- Routes never contain business logic. Parse input, call one use case, map the result to a response schema.
