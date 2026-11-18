# Vision: KedaiKu cart service

> KedaiKu is a fictional online store selling stationery and everyday items in Malaysia. Every company, person and quote in this workshop is invented.

## Why we are building this

KedaiKu's mobile app is being rebuilt. The app team has already designed its cart screen against an agreed API contract (`api-contract.md`). They need a backend that honours that contract so they can start testing.

Today, carts live inside the old monolith. It has two known problems the business wants gone:

1. Cart totals sometimes show amounts like `RM 0.30000000004` because money is stored as floating point.
2. The app silently changed quantities during last year's Hari Raya sale, which caused a wave of complaints and refunds.

## Who uses it

| Who | How |
|---|---|
| Customers | Through the KedaiKu mobile app: add products, see the cart badge, see the cart screen |
| Mobile app team | Calls the API exactly as described in `api-contract.md` |
| Customer service | Reads carts when a customer calls about a wrong total |

## In scope for this release

- Add a product with a quantity to a cart
- View a cart: its lines, item count and subtotal
- Remove a product from a cart (stretch, only if time allows)

## Out of scope for this release

- Promotions, discounts, vouchers, bundles
- Checkout, payment, tax, shipping
- Stock levels and reservations
- Customer accounts and login
- A real database and any cloud deployment

## What success looks like

- The mobile app team can run its cart screen against this API without changing their code.
- Every amount is exact to the sen.
- Replaying `sample-data/cart-scenario.csv` with `check_cart.py` passes every step.
