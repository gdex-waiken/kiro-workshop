# 6.4 Build and check

**11:27 – 11:50 · Checkpoint 3 at 11:50.**

## Gate 3 · Code Generation (about 8 minutes)

After **Approve Plan**, Kiro writes the code and the tests, test-first, in `app/` and `tests/`. It runs `pip install`, starts the service, runs `check_ideas.py` and stops it again.

::: warning It's working, even when the chat is quiet
Code Generation runs for about 8 minutes with little to read in the chat. New files appearing under `app/` and `tests/` show it's working. Don't send messages while it builds, and don't start your own service on port 8000 yet: Kiro is using it.
:::

Use the wait without typing in the chat: read [6.5 Read the record](./5-the-record) and fill in the requirement, answer and stakeholder rows of `traceability-worksheet.md`. The test row comes after this gate, once the tests exist.

When it stops, the Reviewer reads `construction/code-generation/code-summary.md` in the record folder and skims `app/`. The layers should be `app/domain`, `app/application`, `app/adapters`, wired in `app/main.py`. Compare the number of tests with what the plan promised: if it built far more, ask why before you approve.

::: tip Prompt 5 · Approve the code
```text
Approve
```
:::

## Gate 4 · Build and Test (about 2 minutes)

Kiro runs every test and the checker on a fresh service, writes `construction/build-and-test/test-results.md` and stops at the last gate.

**Before you approve, prove it yourselves** in two terminals (**Terminal → New Terminal**, twice):

::: code-group

```bash [Terminal 1: the service]
python -m uvicorn app.main:app --port 8000
```

```bash [Terminal 2: the checker]
python check_ideas.py
```

:::

```text
PASS  step  1  submit 'Weekly route review with'    (the first idea)
PASS  step  2  submit 'Reusable parcel bags'        (a second idea)
PASS  step  3  submit 'REUSABLE PARCEL BAGS'        (the same title again in capitals with extra spaces)
...
PASS  step 13  get an unknown idea                  (an idea nobody submitted)

13/13 steps match the answer key (Feature 1).
```

::: tip Prompt 6 · Approve Build and Test
```text
Approve
```
:::

Kiro closes the workflow and prints a summary. Stop your service (**Ctrl + C** in Terminal 1) before the break.

## When a step fails

::: tip Prompt · A failing checker step
```text
check_ideas.py fails step <n> (<what_happens>): <paste the problem lines>. Find the requirement and the stakeholder decision behind this step, then fix the code with a failing test first.
```
:::

| Symptom | Do this |
|---|---|
| "Cannot reach … Is the service running?" | Start it in Terminal 1: `python -m uvicorn app.main:app --port 8000` |
| `uvicorn` is not recognised | Use `python -m uvicorn app.main:app --port 8000`, as written above |
| `No module named fastapi` | `python -m pip install fastapi uvicorn httpx pytest` |
| "Address already in use" on port 8000 | Another service is still running. Close the other terminal, or wait for Kiro to finish Build and Test |
| Kiro offers to switch to Spec mode | Decline. Stay in AI-DLC |
| The chat is nearly full | `/aidlc park`, start a new chat, pick **aidlc**, then `/aidlc --resume` |

::: info Checkpoint 3 (11:50)
`check_ideas.py` shows **13/13** on your screen and the workflow is complete. At 11:50 two teams run it on the big screen.
:::

**Next:** [6.5 Read the record](./5-the-record)
