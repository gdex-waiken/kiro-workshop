---
inclusion: always
---

# Product: Shopping Cart API

## Purpose
A backend API that lets a customer build a shopping cart for an e-commerce store. It is a workshop MVP: small, correct and easy to extend.

## Users
- **Customer** (through a web or mobile front end): adds, views and removes items in a cart.
- **Developer** (workshop participant): runs and extends the API locally.

## Features
| Feature | Status |
|---|---|
| Add an item with a quantity to a cart | MVP, build first |
| View a cart: lines, item count, subtotal | MVP |
| Remove an item from a cart | Next |
| Checkout, payment, tax, discounts, shipping | Out of scope |
| User accounts, login, persistent database | Out of scope |

## Business rules
- Quantity is a whole number of 1 or more.
- Adding a product that is already in the cart increases its quantity. A cart never has two lines for the same product.
- Item count = sum of all line quantities.
- Subtotal = sum of unit price x quantity, exact to 2 decimal places.
- Product names and prices come from the product catalog, never from the client.
- One currency only.

## Definition of done
- Every acceptance criterion has a passing test.
- `pytest` passes with no skipped tests.
- The README says how to install, test and run the API.

## Do not
- Add features that are not in the current spec.
- Add "nice to have" or optional tasks unless asked.
