---
inclusion: always
---

# Product: KedaiKu cart service

## Purpose
The backend for the shopping cart in the KedaiKu mobile app. A workshop MVP: small, correct and easy to extend.

## Users
- **Customer**, through the mobile app: adds products to a cart and views it.
- **Developer** (workshop participant): runs and extends the service locally.

## Features
| Feature | Status |
|---|---|
| Add a product with a quantity to a cart | MVP, build first |
| View a cart: lines, item count, subtotal | MVP |
| Remove a product from a cart | Stretch, only after the MVP passes |
| Checkout, payment, login, promotions, database | Out of scope |

## Rules we already know
- The API is fixed: follow `api-contract.md` exactly.
- Product names and prices come from `sample-data/catalog.csv`, never from the client.
- A cart never has two lines for the same product.
- Money is exact: strings with 2 decimal places in JSON.

## Do not
- Add features that are not in the current spec.
- Add optional tasks unless asked.
