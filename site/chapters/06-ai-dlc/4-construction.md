# 6.4 Construction

**12:15 – 12:35 · Checkpoint 3 at 12:35.**

## Let Kiro build, then check it yourself

Kiro writes the code and the tests, then runs Build and Test. When it reports done, check it against the answer key yourself.

::: code-group

```bash [Terminal 1: the service]
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8000
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

## Definition of done

- `pytest` passes.
- `check_ideas.py` prints **13/13**.
- Every conflict has a decision and a reason in `team-log.md`.
- `aidlc-docs/` shows a gate approval for every stage that ran.

## When a step fails

::: tip Prompt: a failing checker step
```text
check_ideas.py fails step <n> (<what_happens>): <paste the problem lines>. Find the requirement and the stakeholder decision behind this step in aidlc-docs/, then fix the code with a failing test first.
```
:::

| Symptom | Do this |
|---|---|
| "Cannot reach" | Start the service: `uvicorn app.main:app --port 8000` |
| A step fails | Read its `what_happens` column, then find the stakeholder sentence behind it |
| Kiro suggests switching to Spec mode | Decline. AI-DLC replaces the spec workflow |
| Kiro plans a database, Docker or login | Delete it at the gate and point to `technical-environment.md` |
| Running low on Kiro credits | Stop asking for explanations in chat. Read the files instead |

::: info Checkpoint 3 (12:35)
The `check_ideas.py` result is on screen. Compare it with your Chapter 5 score.
:::

**Next:** [6.5 Read the record](./5-the-record)
