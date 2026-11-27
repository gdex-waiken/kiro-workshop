# 7. Brownfield: add Feature 2 to existing code

**12:10 – 12:50 · Hands-on 3 · Kiro IDE.** Same `ai-dlc` folder, same team, **swap the Driver**. The folder now has your Feature 1 service in it. Add **Feature 2, vote and rank**, with AI-DLC again. Feature 1 must keep working.

## What changes

| | Greenfield (Chapter 6) | Brownfield (now) |
|---|---|---|
| The folder | Documents only | Documents plus your Feature 1 code and its record |
| First stage | Requirements Analysis | **Reverse Engineering**: Kiro reads your code and documents it before it plans anything |
| Gates | 4 | 5 |
| Done means | Feature 1 passes | Feature 2 passes **and** Feature 1 still passes |

::: tip Verify the artifacts, not the diff
On existing code a diff is long and noisy. Read what AI-DLC wrote instead: its picture of your code, the requirements, the plan, the code summary. Check those against the documents. As Lauren Tan, whose products are mostly brownfield, puts it: use AI to verify artifacts, not diffs.
:::

You don't move or rename anything. Feature 1's record stays in its own folder under `aidlc/spaces/default/intents/`; the new request starts a second one next to it.

## The plan for these 40 minutes

| Time | Step | Gate |
|---|---|---|
| 12:10 | Step 1 · New chat, send Prompt 1 (we do it together) | |
| 12:11 | Step 2 · While Kiro reads your code (about 6 min): the trainer explains Reverse Engineering, then you re-read the voting notes | |
| 12:17 | Step 3 · Read what Kiro thinks your code does | **1** Reverse Engineering |
| 12:20 | Step 4 · Answer the voting questions | **2** Requirements |
| 12:27 | Step 5 · Check the plan | **3** Code plan |
| 12:31 | Step 6 · Kiro builds (8–11 min) | **4** Code Generation |
| 12:43 | Step 7 · Build and test both features | **5** Build and Test |

## Step 1 · Start a new chat

1. Stop any service you still have running (**Ctrl + C**).
2. Start a **new chat** and pick the **aidlc** agent again.
3. Send:

::: tip Prompt 1 · Start Feature 2
```text
/aidlc express --plan-approval on --project-type brownfield --skip deployment-pipeline,deployment-execution,observability-setup Add Feature 2 from ticket.md (vote for an idea and see a ranked list) to the existing Lumen Ideas service in this folder. Follow stakeholder-notes.md, technical-environment.md and api-contract.md, and build test-first. The service must pass check_ideas.py --feature 2 and still pass check_ideas.py. We will answer your questions by editing the question files.
```
:::

`--project-type brownfield` tells AI-DLC the code is yours and must be kept. "build test-first" saves a plan revision: AI-DLC's default is to write tests after the code.

## Step 2 · While Kiro reads your code

Reverse Engineering takes about 5–6 minutes. Listen to the trainer, then re-read `stakeholder-notes.md` for **voting**, and `sample-data/votes-scenario.csv`:

- **A double tap:** what happens when someone votes for the same idea twice?
- **Your own idea:** can you vote for it?
- **Managers:** should some votes count more?
- **Ties:** with the same number of votes, which idea ranks first?

## Step 3 · Gate 1: read what Kiro thinks your code does

Kiro writes its picture of your code to `aidlc/spaces/default/codekb/<folder-name>/` (probably `codekb/ai-dlc/`) and stops. The Reviewer opens `business-overview.md` (your Feature 1 rules) and `architecture.md` (the layers and the files Feature 2 will touch).

| Check | Look for |
|---|---|
| The three layers | `domain`, `application`, `adapters`, as Kiro built them for Feature 1 |
| Your Feature 1 rules | The 80-character limit, the duplicate rule, the fixed categories, staff from `staff.csv` |
| The files Feature 2 will touch | Named, and nothing outside them |
| Nothing invented | No database, login or endpoint that isn't there |

If it gets your code wrong, the plan builds on the mistake. Say so now. Otherwise:

::: tip Prompt 2 · Approve Reverse Engineering
```text
Approve
```
:::

## Step 4 · Gate 2: answer the voting questions

Kiro writes `inception/requirements-analysis/requirements-analysis-questions.md` in the new record folder. Answer in the file, with the source, save it, then:

::: tip Prompt 3 · Answers are in the file
```text
done
```
:::

If Kiro asks how you want to answer (Guide me / I'll edit the file / Chat), send `2. The answers are in the file, done.`

Kiro may ask about the voting disagreements, or settle them itself and ask only about edge cases nobody discussed, such as which error wins when both the idea and the voter are wrong. For those the **Product Owner decides** from `api-contract.md` and writes `PO decision:` and the reason.

Then Kiro writes `requirements.md`. The decisions may be in a table or written into the requirements themselves. Check each one against `stakeholder-notes.md`, then:

::: tip Prompt 4 · Approve the requirements
```text
Approve
```
:::

::: details Stuck on a voting question? Hints
| Topic | What settles it | The checker tests |
|---|---|---|
| Double vote | Aina, Wednesday: one person, one vote per idea; the contract says `409` | Step 3: `409`, the count stays at 2 |
| Own idea | Aina, Wednesday: "Farid is right about own ideas" | Step 4: `422` |
| Voter not on the staff list | Same rule as submitters: staff from `staff.csv` | Step 9: `422` |
| Managers count three times | Aina, Wednesday: "Everyone's vote counts the same" | Steps 10–12. Refuse it **on record** in `team-log.md` |
| Ties | Aina, Wednesday: the idea submitted first ranks higher | Step 10: A above B |
| Ideas with no votes | `votes-scenario.csv` step 10 expects idea D with 0 votes in the ranking | Step 10 |
:::

## Step 5 · Gate 3: check the plan

Feature 2 is one endpoint to vote and one to rank. Delete anything else: weighted votes, vote history, notifications, a leaderboard of people, a database. Check that the steps write the tests first. A "Testing Contract" block in the plan may still say `test-after`: the steps are what count.

::: tip Prompt 5 · Approve the plan
```text
Approve Plan
```
:::

Or `Request changes: <what> because <why>. The rest of the plan is fine.`

## Step 6 · Gate 4: Kiro builds

About 8–11 minutes. Kiro changes the existing files it named in Step 3 and adds tests, then runs both checkers. Leave port 8000 free. When it stops, read `construction/code-generation/code-summary.md`: which **existing** files changed?

::: tip Prompt 6 · Approve the code
```text
Approve
```
:::

## Step 7 · Gate 5: build and test both features

When Kiro stops at Build and Test, prove it yourselves:

::: code-group

```bash [Terminal 1: the service]
python -m uvicorn app.main:app --port 8000
```

```bash [Terminal 2: both checkers]
python check_ideas.py --feature 2
python check_ideas.py
```

:::

```text
PASS  step  1  E1002 votes for idea A               (the first vote)
PASS  step  2  E1003 votes for idea A               (a second person votes)
PASS  step  3  E1002 votes for idea A               (the same person votes again: refused and the count stays)
...
PASS  step 14  rankings, limit 0                    (a limit outside 1 to 50)

14/14 steps match the answer key (Feature 2).
```

::: tip Prompt 7 · Approve Build and Test
```text
Approve
```
:::

## Done means

- `python check_ideas.py --feature 2` prints **14/14**.
- `python check_ideas.py` **still** prints **13/13**.
- `team-log.md` has every voting decision with a reason and a source, including the manager votes you refused.

## When you are stuck

| Symptom | Do this |
|---|---|
| Kiro carries on with Feature 1's workflow | You're in the old chat. New chat, pick **aidlc**, send Prompt 1 |
| No Reverse Engineering, Kiro starts from scratch | `--project-type brownfield` is missing. Send Prompt 1 again, exactly |
| "Setup failed: submitting idea A returned …" | The Feature 2 checker submits four ideas first. Feature 1 must pass before Feature 2 can |
| Feature 1 now fails | Tell Kiro which step fails and ask for a fix with a failing test first, as in [6.4](./06-ai-dlc/4-construction#when-a-step-fails) |
| It's 12:40 and Kiro is still planning | Ask the trainer for the finished reference. You'll still do the trace at 12:50 |

**Next:** [8. Show, trace and roll out](./08-wrap-up)
