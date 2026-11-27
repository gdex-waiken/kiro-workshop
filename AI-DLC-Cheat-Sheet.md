# AI-DLC cheat sheet

> Keep this open all morning. Every prompt, in order, is on the website's **Prompts** page.

## The golden rule

**Kiro proposes, you approve.** Every stage ends at a gate. Read the files before you type **Approve**.

## Every new chat

1. New chat → agent picker → **aidlc**.
2. Start with `/aidlc express --plan-approval on …` (the full message is on the Prompts page).

## The stages today (`express` scope)

| # | Stage | You check | Feature 1 | Feature 2 |
|---|---|---|---|---|
| – | Reverse Engineering | What Kiro thinks your code does | skipped (no code yet) | **gate 1** |
| 1 | **Requirements Analysis** | Your answers, and the decisions table against `stakeholder-notes.md` | gate 1 | gate 2 |
| 2 | **Code plan** | Anything the ticket didn't ask for: delete it | gate 2 | gate 3 |
| 3 | **Code Generation** (8–11 min) | `code-summary.md`: which files changed, how many tests | gate 3 | gate 4 |
| 4 | **Build and Test** | Run the checker yourselves | gate 4 | gate 5 |

## What you type at a gate

| You want to | Type |
|---|---|
| Continue | `Approve` (at the code plan: `Approve Plan`) |
| Change something | `Request changes: <what> because <why>.` |
| Say your answers are in the file | `done` |
| See where you are | `/aidlc --status` |
| Stop for a break / carry on | `/aidlc park` / `/aidlc --resume` (pick **aidlc** in the new chat first) |

## Question files, not chat

1. Kiro writes questions to `…/inception/requirements-analysis/requirements-analysis-questions.md`.
2. Type the letter after each `[Answer]:`, then who said so (or `PO decision:` and why, if nobody did).
3. Save the file, then send `done`.

## Where the record lives

`aidlc/spaces/default/intents/<date>-<name>/`

| File | Holds |
|---|---|
| `project-description.json` | Your request |
| `aidlc-state.md` | Stages run and skipped |
| `inception/requirements-analysis/` | Questions, answers, `requirements.md` |
| `construction/code-generation/` | The plan you approved, `code-summary.md` |
| `construction/build-and-test/` | Test results |
| `audit/` | Every question, answer and approval, with a time |

Feature 2's Reverse Engineering writes to `aidlc/spaces/default/codekb/<folder-name>/`.

## Roles (swap the Driver at each break)

**Driver:** types, never answers alone · **Product Owner:** final say · **Reviewer:** reads every file before a gate · **Scribe:** keeps `team-log.md` live

## Saving credits

- Read the files instead of asking Kiro to explain them in chat.
- Don't send messages while Kiro is building.
- New chat for Feature 2. Don't drag the Feature 1 conversation along.

## Done means

**Feature 1:** `check_ideas.py` shows **13/13** · every disagreement has a recorded decision · one traceability chain written

**Feature 2:** `check_ideas.py --feature 2` shows **14/14** · `check_ideas.py` **still** shows 13/13 · the voting decisions are recorded
