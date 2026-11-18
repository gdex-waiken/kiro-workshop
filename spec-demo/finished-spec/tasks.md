# Implementation plan: Add items to cart

Four tasks. Each one is a full red -> green -> refactor slice of one layer, so it can be checked on its own with `pytest`.

- [ ] 1. Domain: cart rules with tests
  - Set up `requirements.txt`, `pytest.ini` and the empty `app/` and `tests/` packages from `structure.md`
  - Write failing tests in `tests/domain/test_cart.py`, then implement `Product`, `Cart`, `CartItem` and the domain errors
  - Cover: new line, merging a repeated product, item count, `Decimal` subtotal (2 x 9.99 + 1 x 1.50 = 21.48), quantity 0 and -1 rejected with the cart unchanged
  - _Requirements: 1.1, 1.2, 2.2, 2.3, 3.1_

- [ ] 2. Application: ports and use cases with tests
  - Write failing tests in `tests/application/` using in-test fakes, then implement `ports.py`, `dtos.py`, `AddItemToCart` and `GetCart`
  - Cover: new cart created on first add, name and price come from the catalog, unknown product raises and saves nothing, unknown cart raises
  - _Requirements: 1.3, 1.4, 2.1, 2.4, 3.2_

- [ ] 3. Adapters: in-memory storage and FastAPI with API tests
  - Write failing tests in `tests/adapters/test_api.py`, then implement the in-memory repository and catalog, the schemas, routes, error handlers and `create_app()`
  - Cover every row of the API table in `design.md`, including money as 2-decimal strings
  - _Requirements: 1.1–1.4, 2.1–2.4, 3.1, 3.2_

- [ ] 4. README and final check
  - Write install, test and run instructions with one `curl` example for add and one for get
  - Run the full `pytest` suite and fix any failure
  - _Requirements: all_
