# 6.3 Plan and design

**12:00 – 12:15 · Checkpoint 2 at 12:15.**

## Every stage ends at a gate

Kiro does the work, writes a file to `aidlc-docs/`, prints **REVIEW REQUIRED**, and waits. You choose **Request Changes** or **Continue**.

A gate you click without reading is a gate you didn't use. The Reviewer opens every file it points to.

::: tip Prompt: continue after you've read the files
```text
proceed
```
:::

## Trim the plan

**AI over-builds.** Ask for an idea list and it may plan login, comments, an admin page, a database and AI tagging. Delete everything the ticket didn't ask for, at the gate.

| What Kiro might plan | Your call |
|---|---|
| Submit an idea | Keep: in the ticket |
| List ideas newest first, open one idea | Keep: in the ticket |
| Vote and rank | Later: Feature 2, in [Chapter 7](../07-brownfield) |
| Login and user accounts | Delete: out of scope |
| Comments, editing, attachments | Delete: out of scope |
| An admin page | Delete: nobody asked for it |
| AI tagging or summaries | Delete: out of scope, and no calls to outside services |
| A database | Delete: prohibited |

::: tip Prompt: request changes to the plan
```text
Request changes: remove <stage or task> from the execution plan. It isn't in ticket.md, and technical-environment.md prohibits it. Keep Feature 1 only, with one unit.
```
:::

## Approve a small design

| Check | Look for |
|---|---|
| Three layers | `domain`, `application`, `adapters` |
| Time | `submitted_at` in UTC, ISO 8601, ending in `Z` |
| Reference data | Names and departments come from `staff.csv`, never from the client. Categories from `categories.csv` |
| Storage | In memory, behind a repository interface |
| Your decisions | The 80-character limit, the duplicate rule and the fixed category list each appear in the design |
| Nothing prohibited | No database, Docker, login, outside calls or new endpoint |

## Code generation is gated twice

First Kiro shows a **code-generation plan**, and only after you approve it does it write code. Check the plan as carefully as the code: a wrong approach is cheapest to fix here.

::: info Checkpoint 2 (12:15)
You deleted or questioned at least one thing in the plan, and said why at the gate. The design has no database, Docker or login.
:::

**Next:** [6.4 Construction](./4-construction)
