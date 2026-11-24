# 5.2 Review the requirements

**About 10 minutes.** The Reviewer reads `requirements.md` aloud; the Product Owner decides.

## Every criterion has the same shape

```text
WHEN [condition or event]
THE SYSTEM SHALL [expected behavior]
```

This is **EARS** (Easy Approach to Requirements Syntax). One sentence, one behavior, easy to test.

## What to look for

| Check | Why |
|---|---|
| Every acceptance criterion from `ticket.md` is there | Nothing got lost |
| Each criterion is testable | You can't check "fast" or "user-friendly" |
| Anything Kiro added that nobody asked for | AI over-builds. Remove it now, not after it's coded |
| What happens on bad input: a blank title, a category not on the list, a staff ID not in `staff.csv` | The contract says `422`. Make sure the spec agrees |
| What happens for an idea that doesn't exist | The contract says `404` |
| Where the name and department come from | `staff.csv`, never the request. Check the spec doesn't accept them from the client |
| What counts as "too long" or "the same idea" | The ticket doesn't say. Write down what Kiro assumed |

## Ask for changes in plain words

You don't edit the file by hand. Tell Kiro, and it revises `requirements.md` and comes back to the same review point.

::: tip Prompt: request a change
```text
Update requirements.md: remove anything not in ticket.md or api-contract.md, and add acceptance criteria for a blank title (422), a category that is not in categories.csv (422), a staff ID that is not in staff.csv (422) and an unknown idea id (404). Keep the EARS format.
```
:::

::: tip Prompt: move on
```text
The requirements look good. Continue to the design phase.
```
:::

**Next:** [5.3 Design and tasks](./3-design-and-tasks)
