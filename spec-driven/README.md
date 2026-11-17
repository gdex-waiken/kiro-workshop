# Part 1 – Spec-driven development

**Time:** 1:35 – 2:35 PM (1 hour, hands-on)

Kiro first writes three documents for you to review: **requirements.md** (what to build and why), **design.md** (how to build it) and **tasks.md** (a step-by-step plan). Only after you approve all three does it write code.

## 1. Start Kiro in this folder

```bash
cd spec-driven
kiro-cli chat
```

Kiro loads `.kiro/steering/tech.md` automatically, so it already knows the technical rules.

> On your own laptop, approve tool calls as Kiro asks for them. Only use `--trust-all-tools` in a throwaway sandbox.

## 2. Create the spec

```
/spec new shopping-cart-api
```

When Kiro asks:

- **New feature or bugfix?** → `Build a Feature (recommended)`
- **Start with?** → `Requirements (recommended)`

When Kiro asks what the spec should cover, paste:

```
A shopping cart API for an e-commerce system. Start with "add items to cart" only.
User story: As a customer, I want to add items to my shopping cart, so that I can collect items I intend to purchase.
Acceptance criteria:
- I can add an item with a specified quantity to my cart
- The cart should display the updated item count
- The cart should show the item details (product name, price, quantity)
- The cart should calculate and display the subtotal
Keep it an MVP: at most 10 tasks, and skip optional tasks.
```

## 3. Review the requirements

Open `.kiro/specs/shopping-cart-api/requirements.md`.

- Each acceptance criterion follows the EARS pattern: `WHEN ... THE SYSTEM SHALL ...`
- Look for decisions Kiro made that you didn't ask for. Change them by typing feedback in plain words.
- Happy? Choose **1. Continue to design phase**.

## 4. Review the design

Open `.kiro/specs/shopping-cart-api/design.md`.

- Check the three Clean Architecture layers: domain, application, adapters.
- Check that design decisions point back to the requirements.
- Happy? Choose **1. Continue to tasks phase**.

## 5. Review and run the tasks

Open `.kiro/specs/shopping-cart-api/tasks.md`. Each task links back to the requirements it covers.

Choose **1. Run required tasks**.

- `ctrl+g` opens the agent monitor; `ctrl+o` expands a sub-agent's output.
- `tasks.md` marks each task `[x]` as it completes.
- You can stop at any time and resume later with `/spec run shopping-cart-api`.

## 6. Check the result

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Then ask Kiro:

```
How do I run this API locally, and how do I call the add-item endpoint with curl?
```

## 7. Stretch goal – Feature 2

Create a second spec for removing items:

```
/spec new shopping-cart-remove-item
```

Use the Feature 2 story in [`../docs/user-story.md`](../docs/user-story.md).

---
Steps adapted from the AWS workshop *Kiro – Getting Started*, Lab 12 Part 1 (spec-driven development), and the Code Challenge.
