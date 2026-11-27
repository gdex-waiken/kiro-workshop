# Take-home: build, run and check

**Take-home, about 10–20 minutes.** Do this after the workshop if you want to see the spec build all the way to running code.

## Run the tests

::: tip Prompt: tests and progress
```text
Run the full test suite with pytest and fix anything that fails. Then tell me exactly how to start the service on port 8000.
```
:::

## Start the service and replay the answer key

Open two terminals in the `spec-driven` folder.

::: code-group

```bash [Terminal 1: the service]
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --port 8000
```

```bash [Terminal 2: the checker]
python check_ideas.py
```

:::

`check_ideas.py` replays the 13 steps in `sample-data/ideas-scenario.csv` against your service. At every step it compares the status code, the number of ideas in the list, the order, and the fields of each idea (name and department from `staff.csv`, `submitted_at` in UTC ending in `Z`).

```text
PASS  step  1  submit 'Weekly route review with'    (the first idea)
PASS  step  2  submit 'Reusable parcel bags'        (a second idea)
FAIL  step  3  submit 'REUSABLE PARCEL BAGS'        (the same title again in capitals with extra spaces)
          - status 201, expected 409
PASS  step  4  submit '(blank)'                     (a blank title)
FAIL  step  5  submit '<81>'                        (a title one character too long: refused and not cut)
          - status 201, expected 422
PASS  step  6  submit '<80>'                        (a title of exactly 80 characters)
...

11/13 steps match the answer key (Feature 1).
```

Each failing step points at one missing decision: see [5.5](./5-fix-errors). A perfect run ends with **13/13 steps match the answer key (Feature 1).** You may not get there in this chapter, and that's the point.

## Write down what failed

Some steps depend on decisions the spec never had: what counts as the same idea, how long a title may be, and what happens when it's too long. Write each failing step and your guess at the reason in the team's notes. These are the decisions AI-DLC asks about in Chapter 6.

| Step | What happened | Why we think it failed |
|---|---|---|
| | | |

::: info Done for this part
`pytest` passes, the service runs, and you know your score on `check_ideas.py`, even if it isn't 13/13.
:::

**Next:** [Fix errors](./5-fix-errors)
