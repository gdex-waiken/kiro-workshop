# 5.5 Fix errors

**About 10 minutes.**

## Why some steps fail, whatever you do

The `spec-driven/` folder has **no stakeholder notes**, on purpose. Some steps in the answer key depend on decisions people made in meetings and messages that only the `ai-dlc/` folder has. Your spec can't know them unless someone tells it.

| Step | Expected | The decision behind it | Who made it |
|---|---|---|---|
| 3 | `409` | The same title, ignoring capitals and spaces at the ends, is a duplicate and is refused | Priya asked, Aina decided |
| 5 | `422` | A title over 80 characters is refused, not cut short | Daniel, after Siti objected |
| 6 | `201` | A title of exactly 80 characters is fine | Daniel |

Steps 7 to 9 (a category not on the list, no staff ID, an unknown staff ID) usually pass: the steering files and the contract already say names come from `staff.csv` and categories from `categories.csv`.

::: tip One wrong answer fails one step
When a submit that should have been refused gets `201`, the checker allows for the extra idea in the steps after it. So each `FAIL` points at its own missing decision.
:::

That's the lesson to take into Chapter 6: the spec did what it was told. The gaps came from what nobody told it.

## Four habits

| Habit | In practice |
|---|---|
| **Start slow** | One task at a time. Stop, verify, then respond |
| **Give context** | Paste the exact error, the step number, the command you ran |
| **Reset when it's tangled** | Start a new chat session, or delete the generated code and run the tasks again |
| **Fix the spec, not just the code** | If a requirement was wrong, change `requirements.md` first, then the tasks |

## Prompts for common problems

::: tip Prompt: a failing checker step
```text
check_ideas.py fails step 4: "a blank title", expected status 422 and no new idea. Show me the requirement that covers this, then add a failing test for it, make it pass, and run the full test suite.
```
:::

::: tip Prompt: the service won't start
```text
uvicorn app.main:app --port 8000 fails with this error: <paste the error>. Find the cause, fix it, and tell me the command to start the service.
```
:::

::: tip Prompt: a wrong requirement
```text
Requirement 2 is wrong: <say what's wrong>. Update requirements.md, then update design.md and tasks.md to match, and list the tasks that need to run again.
```
:::

::: warning Don't hand-edit outside the spec
If you change code yourself, tell Kiro what you changed, so the spec and the code stay in step.
:::

## Before the break

- Commit your work, or note your `check_ideas.py` score.
- Keep the list of failing steps. They're the bridge to Chapter 6.

::: info Source
Tips and troubleshooting adapted from the AWS workshop *Kiro – Getting Started*, Code Challenge.
:::

**Break: 11:20 – 11:35.** Then [Chapter 6: AI-DLC](../06-ai-dlc/).
