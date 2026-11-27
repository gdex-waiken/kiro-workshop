# 6.3 Trim the plan

**11:19 – 11:27 · Checkpoint 2 at 11:27.**

## Gate 2 · The code plan

About 2 minutes after you approve the requirements, Kiro writes:

```text
aidlc/spaces/default/intents/<date>-<name>/construction/code-generation/code-generation-plan.md
```

and stops with choices including **Approve Plan** and **Request Changes**. No code exists yet. This is the cheapest moment to say no.

## AI over-builds. Delete what nobody asked for

The Reviewer reads the plan's steps aloud. For each one, the team asks: **which line in the ticket or the contract asked for this?**

| What a plan may include | Your call |
|---|---|
| Submit, list newest first, open one idea | Keep: in the ticket |
| Tests written before the code | Keep: `technical-environment.md` says test-first. If the plan writes tests after the code, request a change |
| An extra test file for architecture rules, or 25+ tests | Trim: about one test per requirement is enough today |
| Voting or rankings | Not now: Feature 2, after the break |
| A database, Docker, login, an AI call, a new endpoint | Delete: `technical-environment.md` prohibits them |

Plans differ from run to run. In one reference run Kiro planned an extra architecture-test file and about 25 tests, and the team cut both; in another the plan had nothing to cut but wrote tests after the code. Note how many tests the plan promises: you'll compare at the next gate.

::: tip Prompt · Change the plan
```text
Request changes: <what to remove or change> because <the ticket or rule it breaks>. The rest of the plan is fine.
```
:::

Kiro revises the plan in about a minute and shows the same choices. Then:

::: tip Prompt 4 · Approve the plan
```text
Approve Plan
```
:::

::: info Checkpoint 2 (11:27)
You removed or questioned at least one thing in the plan, and said why. The Scribe noted it in `team-log.md` under **Gates**.
:::

**Next:** [6.4 Build and check](./4-construction)
