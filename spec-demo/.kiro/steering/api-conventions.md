---
inclusion: fileMatch
fileMatchPattern: "app/adapters/**/*.py"
---

# HTTP API conventions (loaded only when an adapter file is in context)

- Resource paths are plural nouns: `/carts/{cart_id}/items`.
- `POST` that changes a cart returns **201** with the full updated cart.
- `GET` returns **200**. `DELETE` of an item returns **200** with the updated cart.
- Error status codes:
  | Domain error | HTTP |
  |---|---|
  | `InvalidQuantityError` | 422 |
  | `ProductNotFoundError` | 404 |
  | `CartNotFoundError` | 404 |
  | `ItemNotInCartError` | 404 |
- Error body: `{"detail": "<human-readable message that names the id>"}`.
- Money fields are strings with exactly 2 decimals.
- Routes never contain business logic. Parse input, call one use case, map the result to a response schema.
