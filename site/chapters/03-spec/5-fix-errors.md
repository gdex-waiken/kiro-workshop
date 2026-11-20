# 3.5 Fix errors

**About 10 minutes.**

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
check_cart.py fails step 5: "quantity zero", expected status 422 and an unchanged cart. Show me the requirement that covers this, then add a failing test for it, make it pass, and run the full test suite.
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

- Commit your work, or note your `check_cart.py` score.
- Keep the list of failing steps. They're the bridge to Chapter 4.

::: info Source
Tips and troubleshooting adapted from the AWS workshop *Kiro – Getting Started*, Code Challenge.
:::

**Break: 2:35 – 2:50.** Then [Chapter 4: AI-DLC](../04-ai-dlc/).
