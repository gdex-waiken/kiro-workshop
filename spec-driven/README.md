# Hands-on 1: spec-driven development

**Time:** 10:00 – 10:30 AM · teams of 3–4 · one laptop per team · Kiro IDE

You build **Feature 1** of the Lumen Ideas service (submit and browse ideas) with Kiro's built-in **spec workflow**: Kiro writes `requirements.md`, `design.md` and `tasks.md`, you review each one, then it builds task by task. Feature 1 only.

In the room you go as far as `requirements.md` and hunt for the decisions the ticket never made. Design, tasks and the build are take-home. The full guide, with every prompt ready to copy, is on the workshop website: **Chapter 3, Spec-driven development**.

## What's in this folder

| File | What it is |
|---|---|
| `.kiro/steering/` | `product.md`, `tech.md`, `structure.md`: the rules Kiro reads with every request |
| `Lumen-Ideas-Client-Brief.docx` | The client's brief from Aina Rahman, Head of Innovation: business needs only, no tech or API. `.kiro/steering/product.md` was generated from it |
| `ticket.md` | What the innovation team asked for |
| `api-contract.md` | The fixed API the portal app already uses |
| `technical-environment.md` | The platform standards: stack, architecture, what is prohibited |
| `sample-data/` | The staff list, the categories and the answer keys |
| `check_ideas.py` | Replays the answer key against your running service |

There are **no stakeholder notes** in this folder, on purpose. Spec mode builds from what you give it. In Hands-on 2, AI-DLC builds the same Feature 1 and asks the questions this part never asks.

## Quick start

1. Open this `spec-driven` folder in Kiro IDE.
2. Kiro panel → **Specs** → **Create New Spec** (or pick **Spec** in the chat).
3. Paste the prompt from Chapter 3.1 on the website.
4. Review `requirements.md`, `design.md` and `tasks.md`, then run the tasks.
5. Start the service and check it:

```bash
python -m uvicorn app.main:app --port 8000      # terminal 1
python check_ideas.py                 # terminal 2: aim for "13/13 steps match the answer key"
```

If a step fails, write down which one and why. Some steps depend on decisions this folder never told Kiro about.
