# 2. Kiro spec mode and steering

This chapter matches the 10-minute live demo. The files are in the repo's [`spec-demo/`](https://github.com/gdex-waiken/kiro-workshop/tree/main/spec-demo) folder.

## What spec mode produces

From one prompt, Kiro writes three files in `.kiro/specs/<feature>/`:

| File | Holds |
|---|---|
| `requirements.md` | User stories and acceptance criteria in **EARS** form: `WHEN … THE SYSTEM SHALL …` |
| `design.md` | Components, data, errors and the test plan |
| `tasks.md` | A short checklist, each task linked to the requirements it covers |

You review each file before Kiro moves on, then start the tasks one by one.

::: warning Every task is a separate run
Each task reloads the steering files and the spec. Five tasks cost about five times the context, so **fewer, bigger tasks win**. Ask for "at most 5 tasks, no optional tasks".
:::

## Steering: the rules Kiro reads for you

Steering files live in `.kiro/steering/`. A small front-matter block says when each one is loaded.

| File | Loaded | Holds |
|---|---|---|
| `product.md` | always | Purpose, users, scope, business rules |
| `tech.md` | always | Stack and hard technical rules |
| `structure.md` | always | Folders, naming, where new code goes |
| `testing.md`, `api-conventions.md` | when a matching file is open | Detail that only matters there |
| `code-review.md` | when you type `#code-review` | A checklist on demand |

```yaml
---
inclusion: always            # or: fileMatch, manual
fileMatchPattern: "tests/**/*.py"   # only with fileMatch
---
```

## Good practice

- **Have all three always-on files.** Without `product.md` and `structure.md`, every task rediscovers the purpose and the folder layout by reading files: more requests, more credits.
- **Keep them short.** Always-on files are sent with every request. Aim for under 150 lines across the three.
- **Rules, not essays.** One line per rule. No history.
- **Push detail into `fileMatch` or `manual` files**, so it loads only when it's relevant.

### A good `product.md`, in brief

```markdown
---
inclusion: always
---
# Product: Shopping Cart API

## Purpose
A backend API that lets a customer build a shopping cart. Workshop MVP.

## Features
| Feature | Status |
|---|---|
| Add an item with a quantity | MVP, build first |
| View a cart: lines, item count, subtotal | MVP |
| Checkout, payment, login, database | Out of scope |

## Do not
- Add features that are not in the current spec.
- Add optional tasks unless asked.
```

The full set (six steering files and a lean 4-task spec) is in [`spec-demo/`](https://github.com/gdex-waiken/kiro-workshop/tree/main/spec-demo).
