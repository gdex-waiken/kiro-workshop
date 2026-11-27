# 3.2 Hunt for the gaps

**10:15 – 10:27 · Your team.** The Reviewer reads `requirements.md` aloud; everyone hunts.

::: tip The race
The first team to post **three decisions the ticket doesn't settle** in the chat, each with the line in `requirements.md` where Kiro guessed, wins. Examples of the kind of thing to look for: what makes two ideas "the same", what happens to a title that's too long.
:::

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

## Stop here

Leave the spec where it is. At 10:27 two teams share what they found; the trainer writes the list on the board. You'll see the same questions again at 11:00, asked by AI-DLC.

::: details Take-home: carry on to the build
```text
The requirements look good. Continue to the design phase.
```
Then follow [design and tasks](./3-design-and-tasks), [build and check](./4-build-and-check) and [fix errors](./5-fix-errors).
:::

**Next:** [4. Who asks the questions?](../04-bridge)
