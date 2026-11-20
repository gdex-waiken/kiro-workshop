# 3. Spec-driven development

**10:05 – 11:05 · Hands-on, 1 hour · Kiro IDE.** Plan it, approve it, build it, check it, fix it.

![Kiro IDE with the kedaiku-cart spec open](/images/kiro-ide-spec.png){.shot .wide}

*What you'll have by 11:05: the steering files and the three spec files in the explorer, `tasks.md` open with **Start task** and **Run all tasks**, and the chat on the right.*

## A spec-driven workspace has two layers

| Layer | Folder | Who writes it | How long it lives |
|---|---|---|---|
| **Steering:** the project's standing rules | `.kiro/steering/` | You (or Kiro, with **Generate Steering Docs**), once per project | As long as the project |
| **Spec:** the plan for one feature | `.kiro/specs/<feature>/` | Kiro writes it, you approve each file | One per feature or bug fix |

```text
spec-driven/
├── .kiro/
│   ├── steering/                 ← already there: Kiro reads these with every request
│   │   ├── product.md            what we build, for whom, what's in and out of scope
│   │   ├── tech.md               the stack and the hard technical rules
│   │   └── structure.md          folders, naming, run commands
│   └── specs/
│       └── kedaiku-cart/         ← Kiro creates this in 3.1 to 3.3, you approve each file
│           ├── requirements.md   1. what the cart must do
│           ├── design.md         2. how it will be built
│           └── tasks.md          3. the step-by-step build list
├── ticket.md                     the request from the Product team
├── api-contract.md               the API the app team already built against
├── sample-data/                  the catalog and the answer key
└── check_cart.py                 replays the answer key against your service
```

## Steering: the three foundation files

Kiro sends these with **every** request, so it follows your stack and conventions without being told each time.

| File | Holds | In this workshop |
|---|---|---|
| `product.md` | Purpose, users, key features, scope | KedaiKu's cart: add items and view the cart. Checkout, payment, login and a database are out of scope |
| `tech.md` | Frameworks, libraries, hard rules | Python 3.12, FastAPI, pytest, in-memory storage, money as `Decimal` |
| `structure.md` | Folders, naming, run commands | `app/` (domain, application, adapters) and `tests/`. Run with `uvicorn app.main:app --port 8000` |

Each file starts with a front matter block that says when Kiro loads it:

```yaml
---
inclusion: always            # or: fileMatch (with fileMatchPattern), manual
---
```

::: details In your own projects: let Kiro write the first draft
Kiro panel → **Steering** → **Generate Steering Docs** (or **+** → **Foundation steering files**). Kiro reads your code and creates `product.md`, `tech.md` and `structure.md`. Review them like any other file: they steer every request after that.
:::

::: tip Keep steering short
Always-on files are sent with every request. Short files cost less and keep Kiro focused.
:::

## The spec: three files you approve, in order

Instead of jumping to code, Kiro writes three markdown files in `.kiro/specs/<name>/` and pauses for your review after each one. The tabs at the top of the editor (**1 Requirements › 2 Design › 3 Task list**) show where you are.

| # | File | Holds | You check |
|---|---|---|---|
| 1 | `requirements.md` | User stories and acceptance criteria in **EARS** form: `WHEN … THE SYSTEM SHALL …` | Is every criterion testable? Did Kiro add anything you didn't ask for? |
| 2 | `design.md` | Components, data, errors and the test plan | Do the decisions point back to the requirements? Does it follow `tech.md`? |
| 3 | `tasks.md` | A short checklist, each task linked to the requirements it covers | Small enough to review? Tests first? |

A bug fix uses the same three steps, with `bugfix.md` in place of `requirements.md`.

## Why work from a spec?

- **Shared understanding.** Everyone can read and agree on the goal before code exists.
- **A North Star for the agent.** It can take on larger work without losing the plot.
- **It catches bugs.** In the AWS lab, a test written from one requirement caught a bug that vibe coding would have shipped.

## The plan for this hour

| Step | Page | Time |
|---|---|---|
| Create the spec | [3.1](./1-create-the-spec) | 10 min |
| Review the requirements | [3.2](./2-requirements) | 10 min |
| Review design and tasks | [3.3](./3-design-and-tasks) | 10 min |
| Build, run and check | [3.4](./4-build-and-check) | 20 min |
| Fix what fails | [3.5](./5-fix-errors) | 10 min |

::: info Sources
AWS workshop *Kiro – Getting Started*, Lab 12 Part 1 · kiro.dev/docs/specs · kiro.dev/docs/steering
:::
