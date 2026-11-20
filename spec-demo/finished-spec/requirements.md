# Requirements: Add items to cart

## Introduction
A customer adds a product with a quantity to a cart and gets back the updated cart: its lines, item count and subtotal. This spec covers adding and viewing only. Removing items is a separate spec.

## Glossary
- **Cart**: a set of lines, identified by a client-chosen `cart_id`.
- **Line**: one product in the cart with its quantity.
- **Catalog**: the source of product name and unit price.
- **Item count**: sum of the quantities of all lines.
- **Subtotal**: sum of unit price x quantity over all lines.

## Requirement 1: Add an item
**User story:** As a customer, I want to add a product with a quantity to my cart, so that I can collect items I intend to buy.

**Acceptance criteria**
1. WHEN a customer adds a catalog product with quantity 1 or more THE SYSTEM SHALL add a line with that product and quantity.
2. WHEN the product is already in the cart THE SYSTEM SHALL increase that line's quantity and SHALL NOT create a second line.
3. WHEN the `cart_id` does not exist yet THE SYSTEM SHALL create the cart, then add the item.
4. WHEN an item is added THE SYSTEM SHALL return the full updated cart.

## Requirement 2: Show cart details
**User story:** As a customer, I want to see what is in my cart, so that I can check what I am buying.

**Acceptance criteria**
1. WHEN a cart is returned THE SYSTEM SHALL include, for each line, `product_id`, `name`, `unit_price` and `quantity`.
2. WHEN a cart is returned THE SYSTEM SHALL include the item count.
3. WHEN a cart is returned THE SYSTEM SHALL include the subtotal, calculated with `Decimal` and shown with 2 decimals.
4. WHEN a customer requests a cart that does not exist THE SYSTEM SHALL return a not-found error.

## Requirement 3: Reject bad input
**User story:** As a customer, I want clear errors for bad input, so that my cart never holds wrong data.

**Acceptance criteria**
1. IF the quantity is less than 1 THEN THE SYSTEM SHALL return a validation error and leave the cart unchanged.
2. IF the `product_id` is not in the catalog THEN THE SYSTEM SHALL return a not-found error that names the id and leave the cart unchanged.

## Out of scope
Removing items, changing quantity directly, stock checks, checkout, login, persistent storage.
