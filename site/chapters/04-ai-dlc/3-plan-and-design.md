# 4.3 Plan and design

**3:15 – 3:30 · Checkpoint 2 at 3:30.**

## Every stage ends at a gate

Kiro does the work, writes a file to `aidlc-docs/`, prints **REVIEW REQUIRED**, and waits. You choose **Request Changes** or **Continue**.

A gate you click without reading is a gate you didn't use. The Reviewer opens every file it points to.

::: tip Prompt: continue after you've read the files
```text
proceed
```
:::

## Trim the plan

**AI over-builds.** Ask for a cart and it may plan a whole shop.

| What Kiro might plan | Your call |
|---|---|
| Add items to the cart | Keep: in the ticket |
| View the cart and subtotal | Keep: in the ticket |
| Remove items from the cart | Later: stretch goal |
| User login and accounts | Delete: out of scope |
| Checkout and payment | Delete: out of scope |
| A database | Delete: prohibited |

::: tip Prompt: request changes to the plan
```text
Request changes: remove <stage or task> from the execution plan. It isn't in ticket.md, and technical-environment.md prohibits it. Keep Feature 1 only, with one unit.
```
:::

## Approve a small design

| Check | Look for |
|---|---|
| Three layers | `domain`, `application`, `adapters` |
| Money | `Decimal`, never `float` |
| Storage | In memory, behind a repository interface |
| Nothing prohibited | No database, Docker, login or new endpoint |

## Code generation is gated twice

First Kiro shows a **code-generation plan**, and only after you approve it does it write code. Check the plan as carefully as the code: a wrong approach is cheapest to fix here.

::: info Checkpoint 2 (3:30)
You deleted or questioned at least one thing in the plan, and said why at the gate. The design has no database, Docker or login.
:::

**Next:** [4.4 Construction](./4-construction)
