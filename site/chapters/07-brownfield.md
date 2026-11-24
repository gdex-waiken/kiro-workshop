# 7. Brownfield: add Feature 2 to existing code

**12:50 – 1:15 · Hands-on, 25 minutes · Kiro IDE.** Same `ai-dlc` folder, same team, swap the Driver. Now the folder has code in it: your Feature 1 service. You add **Feature 2, vote and rank**, with AI-DLC again.

## What changes

| | Feature 1 (greenfield, Chapter 6) | Feature 2 (brownfield, now) |
|---|---|---|
| **Workspace Detection** | Finds an empty folder | **Finds your Feature 1 code** |
| **Reverse Engineering** | Skipped | **Runs:** documents the code that's already there |
| **The answer key** | `check_ideas.py`: 13 steps | `check_ideas.py --feature 2`: 14 steps, **and** `check_ideas.py` must still pass |
| **The risk** | Building the wrong thing | Breaking what already works |

Most real work is brownfield. This is where a written record pays off: Kiro, and a new teammate, can understand the code before changing it.

## Feature 2 in one paragraph

A staff member votes for an idea. Each idea shows how many votes it has. The portal shows a ranked list, most votes first. Two endpoints from `api-contract.md`, nothing else:

| Endpoint | Does |
|---|---|
| `POST /ideas/{idea_id}/votes` with `{ "voter": "E1003" }` | Counts a vote and returns the idea with its new `vote_count` |
| `GET /rankings?limit=10` | Returns the top ideas, most votes first. `limit` from 1 to 50, 10 if left out |

## Step 1: Put the Feature 1 record aside

Rename the finished `aidlc-docs/` folder to `aidlc-docs-feature1/`. That keeps the Feature 1 record for your traceability chain, and stops AI-DLC from picking up the old workflow where it left off. Leave `app/`, `tests/` and everything else where they are.

::: code-group

```bash [Git Bash / macOS / Linux]
cd kiro-workshop/ai-dlc
mv aidlc-docs aidlc-docs-feature1
```

```powershell [Windows PowerShell]
cd kiro-workshop\ai-dlc
Rename-Item aidlc-docs aidlc-docs-feature1
```

:::

Then start a **new** chat session. Don't continue the Feature 1 chat.

## Step 2: Paste the brownfield trigger phrase

In the same `ai-dlc` folder, the one with `app/` in it, paste exactly:

::: tip Copy this
```text
Using AI-DLC, add Feature 2 from ticket.md (vote for an idea and see a ranked list) to the existing Pelita Ideas service in this folder. Follow stakeholder-notes.md and api-contract.md. The service must pass check_ideas.py --feature 2 and still pass check_ideas.py. This is a brownfield project.
```
:::

You should see a new `aidlc-docs/` folder, and Workspace Detection reporting existing code.

## Step 3: Read the Reverse Engineering output

Reverse Engineering writes what Kiro thinks your code does: its structure, its components, its rules. **Read it before you continue.** If it gets your code wrong, the Feature 2 plan builds on the mistake.

| Check | Look for |
|---|---|
| The three layers | `domain`, `application`, `adapters`, as you built them |
| Your Feature 1 rules | The 80-character limit, the duplicate rule, the fixed categories, staff from `staff.csv` |
| Nothing invented | No database, login or endpoint that isn't there |

## Step 4: Settle the voting conflicts

Read `stakeholder-notes.md` again, this time for voting, and `sample-data/votes-scenario.csv`. Answer the question files as before, and record each decision and why in `team-log.md`.

- **A double tap:** what happens when someone votes for the same idea twice?
- **Your own idea:** can you vote for it?
- **Managers:** should some people's votes count more?
- **Ties:** when two ideas have the same number of votes, which ranks first?

::: details Stuck? Hints, one per conflict
| Topic | Who disagrees | What settles it | The answer key checks |
|---|---|---|---|
| Double vote | Daniel (ignore it and say OK) vs Aina (one person, one vote) | Aina, Wednesday: one person, one vote per idea | Step 3: `409`, and the count stays at 2 |
| Own idea | Farid asks for the rule | Aina, Wednesday: "Farid is right about own ideas" | Step 4: `422` |
| Managers' votes count three times | Farid vs Aina | Aina, Wednesday: "Everyone's vote counts the same" | Nothing to check: refuse it **on record** in `team-log.md` |
| Ties | Nobody raised it at the kick-off | Aina, Wednesday: the idea submitted first ranks higher | Step 10: A ranks above B |
:::

## Step 5: Keep the plan lean

You have 25 minutes. Feature 2 is one endpoint to vote and one to rank. At Workflow Planning, delete anything else: weighted votes, vote history, notifications, a leaderboard of people, a database. Say why at the gate.

## Step 6: Build and check both features

::: code-group

```bash [Terminal 1: the service]
uvicorn app.main:app --port 8000
```

```bash [Terminal 2: the checkers]
python check_ideas.py --feature 2
python check_ideas.py
```

:::

```text
PASS  step  1  E1002 votes for idea A               (the first vote)
PASS  step  2  E1003 votes for idea A               (a second person votes)
PASS  step  3  E1002 votes for idea A               (the same person votes again: refused and the count stays)
PASS  step  4  E1001 votes for idea A               (voting for your own idea)
...
PASS  step 14  rankings, limit 0                    (a limit outside 1 to 50)

14/14 steps match the answer key (Feature 2).
```

The Feature 2 checker first submits four ideas of its own, so Feature 1 has to work before it can start.

## Done means (Feature 2)

- `pytest` passes, old tests and new.
- `python check_ideas.py --feature 2` prints **14/14**.
- `python check_ideas.py` **still** prints **13/13**.
- Every voting conflict has a decision and a reason in `team-log.md`, including the managers' votes you refused.

## When you are stuck

| Symptom | Do this |
|---|---|
| Reverse Engineering is skipped | Kiro didn't see your code. Check you opened the `ai-dlc` folder with `app/` in it, then start a **new** session |
| Kiro carries on with the Feature 1 workflow | The old `aidlc-docs/` is still there. Rename it (Step 1), then start a **new** session |
| `check_ideas.py --feature 2` says "Setup failed" | Feature 1 is broken. Make `check_ideas.py` pass first |
| Feature 2 broke a Feature 1 step | Tell Kiro which step of `check_ideas.py` fails and let it fix it inside the workflow |
| Rankings look crowded after many checker runs | Restart the service. Every run adds ideas |
| Running low on Kiro credits | Stop asking for explanations in chat. Read the files instead |

::: tip Prompt: a failing checker step
```text
check_ideas.py --feature 2 fails step <n> (<what_happens>): <paste the problem lines>. Find the requirement and the stakeholder decision behind this step in aidlc-docs/, then fix the code with a failing test first, and confirm check_ideas.py still passes.
```
:::

**Next:** [Chapter 8: Wrap-up](./08-wrap-up)
