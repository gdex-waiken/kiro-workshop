# Part 1: spec-driven development

**Time:** 10:05 – 11:05 AM · teams of 3–4 · one laptop per team · Kiro IDE

You build the KedaiKu cart service with Kiro's built-in **spec workflow**: Kiro writes `requirements.md`, `design.md` and `tasks.md`, you review each one, then it builds task by task.

The full guide, with every prompt ready to copy, is on the workshop website: **Chapter 3, Spec-driven development**.

## What's in this folder

| File | What it is |
|---|---|
| `.kiro/steering/` | `product.md`, `tech.md`, `structure.md`: the rules Kiro reads with every request |
| `ticket.md` | What the Product team asked for |
| `api-contract.md` | The fixed API the mobile app already uses |
| `sample-data/` | The product catalog and the answer key |
| `check_cart.py` | Replays the answer key against your running service |

There are **no stakeholder notes** in this folder, on purpose. Spec mode builds from what you give it. In Part 2, AI-DLC builds the same cart and asks the questions this part never asks.

## Quick start

1. Open this `spec-driven` folder in Kiro IDE.
2. Kiro panel → **Specs** → **Create New Spec** (or pick **Spec** in the chat).
3. Paste the prompt from Chapter 3.1 on the website.
4. Review `requirements.md`, `design.md` and `tasks.md`, then run the tasks.
5. Start the service and check it:

```bash
uvicorn app.main:app --port 8000      # terminal 1
python check_cart.py                  # terminal 2
```

If a step fails, write down which one and why. Some steps depend on decisions this folder never told Kiro about.
