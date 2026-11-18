# Design: Add items to cart

Follows `tech.md` (Clean Architecture, Decimal money, TDD) and `structure.md` (file locations).

## API
| Method | Path | Body | Success | Errors |
|---|---|---|---|---|
| POST | `/carts/{cart_id}/items` | `{"product_id": "sku-1", "quantity": 2}` | 201 + cart | 422 bad quantity, 404 unknown product |
| GET | `/carts/{cart_id}` | none | 200 + cart | 404 unknown cart |

Cart response:
```json
{
  "cart_id": "c1",
  "items": [{"product_id": "sku-1", "name": "Notebook", "unit_price": "9.99", "quantity": 2, "line_total": "19.98"}],
  "item_count": 2,
  "subtotal": "19.98"
}
```

## Components
| Layer | Component | Responsibility | Requirements |
|---|---|---|---|
| Domain | `Product` | Frozen: `product_id`, `name`, `price` | 2.1 |
| Domain | `Cart` | `add_item(product, qty)` merges lines; `item_count`; `subtotal` | 1.1, 1.2, 2.2, 2.3, 3.1 |
| Domain | errors | `InvalidQuantityError`, `ProductNotFoundError`, `CartNotFoundError` | 2.4, 3.1, 3.2 |
| Application | ports | `CartRepository.get/save`, `ProductCatalog.get` | 1.3 |
| Application | `AddItemToCart` | Look up product, load or create cart, add, save, return `CartView` | 1.1–1.4, 3.2 |
| Application | `GetCart` | Load cart or raise `CartNotFoundError` | 2.4 |
| Adapters | in-memory repo and catalog | Dict stores; seed `sku-1` Notebook 9.99, `sku-2` Pen 1.50, `sku-3` Backpack 49.90 | 1.3 |
| Adapters | `api.py`, `main.py` | Schemas (`quantity: int = Field(ge=1)`), routes, error mapping, `create_app()` | all |

## Key decisions
- Name and price are copied from the catalog into the line when added.
- Validation happens twice: Pydantic (`ge=1`) at the boundary, and `Cart.add_item` in the domain.
- `save` is called only after every check passes, so errors never change state.
- Subtotal is quantized to `0.01` with `ROUND_HALF_UP`.

## Testing
- Domain: merge lines, item count, subtotal with `Decimal`, invalid quantity leaves cart unchanged.
- Application: fakes for the ports; unknown product and invalid quantity save nothing.
- API: 201 on add, merged lines, 2-decimal strings, 422, 404 product, 200 and 404 on GET.
