# 4.4 Construction

**3:30 – 3:50 · Checkpoint 3 at 3:50.**

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
python check_cart.py
```

:::

```text
PASS  step  1  add 2 x SKU-001 to cart A             (first add creates the cart)
...
PASS  step 15  get cart A                            (first cart is untouched)

15/15 steps match the answer key.
```

## Definition of done

- `pytest` passes.
- `check_cart.py` prints **15/15**.
- Every conflict has a decision and a reason in `team-log.md`.
- `aidlc-docs/` shows a gate approval for every stage that ran.

## When a step fails

::: tip Prompt: a failing checker step
```text
check_cart.py fails step <n> (<what_happens>): <paste the problem lines>. Find the requirement and the stakeholder decision behind this step in aidlc-docs/, then fix the code with a failing test first.
```
:::

| Symptom | Do this |
|---|---|
| "Cannot reach" | Start the service: `uvicorn app.main:app --port 8000` |
| A step fails | Read its `what_happens` column, then find the stakeholder sentence behind it |
| Kiro suggests switching to Spec mode | Decline. AI-DLC replaces the spec workflow |
| Kiro plans a database, Docker or login | Delete it at the gate and point to `technical-environment.md` |
| Running low on Kiro credits | Stop asking for explanations in chat. Read the files instead |

::: info Checkpoint 3 (3:50)
The `check_cart.py` result is on screen. Compare it with your Chapter 3 score.
:::

**Next:** [4.5 Read the record](./5-the-record)
