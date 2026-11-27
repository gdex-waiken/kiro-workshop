# 3. Spec-driven development

**10:00 – 10:30 · Hands-on 1 · Kiro IDE.** The trainer builds a spec live, the room starts one together, then your team hunts for the decisions the ticket never made. You plan **Feature 1** of Lumen Ideas: submit and browse ideas.

![Kiro IDE with a spec open](/images/kiro-ide-spec.png){.shot .wide}

*Where a spec ends up: the steering files and the three spec files in the explorer, `tasks.md` open with **Start task** and **Run all tasks**, and the chat on the right. Today you go as far as `requirements.md`; the rest is take-home.*

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
│       └── lumen-ideas/         ← Kiro creates this; you approve each file
│           ├── requirements.md   1. what the service must do
│           ├── design.md         2. how it will be built
│           └── tasks.md          3. the step-by-step build list
├── Lumen-Ideas-Client-Brief.docx  the client's brief: business needs only
├── ticket.md                     the two features, with acceptance criteria
├── api-contract.md               the API the app team already built against
├── technical-environment.md      the platform standards and what is prohibited
├── sample-data/                  the staff list, the categories and the answer keys
└── check_ideas.py                replays the answer key against your service
```

## Where steering comes from

On a client project nobody hands you steering files. You get a **Word document** from the client: business needs, the problems, who uses it, what's in and out. No technology, no API. Your team adds what you agreed internally: the stack and the house rules.

| Source | Becomes |
|---|---|
| The client's brief, `Lumen-Ideas-Client-Brief.docx` (business needs) | `product.md`, written by Kiro from the brief |
| Your internal standards, `technical-environment.md` | `tech.md` and `structure.md` |
| The app team's `api-contract.md` | Stays a document; you hand it to Kiro with the ticket |

The trainer does this live at 10:00 with one prompt. Kiro opens the `.docx` itself:

```text
Read Lumen-Ideas-Client-Brief.docx (the client's brief) and turn it into a Kiro steering file .kiro/steering/product.md: what the product is, who uses it, the problems it solves, release 1 scope and what is out of scope, the business rules, and the open questions. Business only: no technology, no API design. Keep it short.
```

The `product.md` in your `spec-driven` folder was made exactly this way.

## Steering: the three foundation files

Kiro sends these with **every** request, so it follows your stack and conventions without being told each time.

| File | Holds | In this workshop |
|---|---|---|
| `product.md` | Purpose, users, key features, scope | Lumen Ideas: submit ideas, list them newest first, open one. Voting comes later. Comments, login, a database and AI features are out of scope |
| `tech.md` | Frameworks, libraries, hard rules | Python 3.12, FastAPI, pytest, in-memory storage, times in UTC ending in `Z` |
| `structure.md` | Folders, naming, run commands | `app/` (domain, application, adapters) and `tests/`. Run with `python -m uvicorn app.main:app --port 8000`, check with `python check_ideas.py` |

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
| 1 | `requirements.md` | Requirements and acceptance criteria in **EARS** form: `WHEN … THE SYSTEM SHALL …` | Is every criterion testable? Did Kiro add anything you didn't ask for? |
| 2 | `design.md` | Components, data, errors and the test plan | Do the decisions point back to the requirements? Does it follow `tech.md`? |
| 3 | `tasks.md` | A short checklist, each task linked to the requirements it covers | Small enough to review? Tests first? |

A bug fix uses the same three steps, with `bugfix.md` in place of `requirements.md`.

## Why work from a spec?

- **Shared understanding.** Everyone can read and agree on the goal before code exists.
- **Gives direction.** The agent knows where it's going, so it can take on larger work without losing the plot.
- **It catches bugs.** In the AWS lab, a test written from one requirement caught a bug that vibe coding would have shipped.

## The plan for these 30 minutes

| Min | Who | What | Page |
|---|---|---|---|
| 10:00 | **Trainer** (I do) | Turns the client's `.docx` into steering, then builds a spec: requirements → design → tasks | — |
| 10:10 | **Everyone** (we do) | Opens `spec-driven/`, starts a spec with the same prompt, together | [3.1](./1-create-the-spec) |
| 10:15 | **Your team** (you do) | Reads `requirements.md` and hunts for the decisions the ticket never made | [3.2](./2-requirements) |
| 10:27 | **Two teams** | Share what they found | — |

Design, tasks, build and check are take-home pages: [design and tasks](./3-design-and-tasks), [build and check](./4-build-and-check), [fix errors](./5-fix-errors).

::: info Sources
AWS workshop *Kiro – Getting Started*, Lab 12 Part 1 · kiro.dev/docs/specs · kiro.dev/docs/steering
:::
