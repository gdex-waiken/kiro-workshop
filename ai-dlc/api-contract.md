# API contract: cart service v1

Agreed with the mobile app team. **Do not change paths, field names or status codes.**

Base URL when running locally: `http://localhost:8000`

## Add a product to a cart

`POST /carts/{cart_id}/items`

Request body:

```json
{ "product_id": "SKU-001", "quantity": 2 }
```

- `cart_id` is chosen by the app (any non-empty string). A cart that does not exist yet is created by its first successful add.

| Result | Status | Body |
|---|---|---|
| Added | `201` | the full cart (below) |
| Unknown `product_id` | `404` | error |
| Request not allowed (for example a bad quantity) | `422` | error |

## Get a cart

`GET /carts/{cart_id}`

| Result | Status | Body |
|---|---|---|
| Found | `200` | the full cart |
| No such cart | `404` | error |

## Remove a product from a cart (stretch)

`DELETE /carts/{cart_id}/items/{product_id}`

| Result | Status | Body |
|---|---|---|
| Removed | `200` | the full cart, which may now be empty |
| No such cart, or product not in the cart | `404` | error |

## The cart

```json
{
  "cart_id": "c-123",
  "lines": [
    {
      "product_id": "SKU-001",
      "name": "A5 Notebook",
      "unit_price": "12.90",
      "quantity": 2,
      "line_total": "25.80"
    }
  ],
  "item_count": 2,
  "subtotal": "25.80"
}
```

- `lines` has one entry per product. The same product never appears twice.
- All money fields are strings with exactly 2 decimal places.
- `item_count` is the number the app shows on the cart badge.

## Errors

```json
{ "detail": "A human-readable message that names the product or cart" }
```

When a request fails, the cart must be exactly as it was before the request.
