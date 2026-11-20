# 3.4 Build, run and check

**About 20 minutes.**

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
uvicorn app.main:app --port 8000
```

```bash [Terminal 2: the checker]
python check_cart.py
```

:::

`check_cart.py` replays the 15 steps in `sample-data/cart-scenario.csv` against your service and compares the status code, item count and subtotal at every step.

```text
PASS  step  1  add 2 x SKU-001 to cart A             (first add creates the cart)
FAIL  step  2  add 1 x SKU-002 to cart A             (two notebooks and one pen)
          - item_count is 2, expected 3
...
13/15 steps match the answer key.
```

## Write down what failed

Some steps depend on decisions the spec never had: what the badge counts, whether there's a limit, what happens when someone asks for too much. Write each failing step and your guess at the reason in the team's notes. You'll meet these decisions again in Chapter 4.

| Step | What happened | Why we think it failed |
|---|---|---|
| | | |

::: info Done for this part
`pytest` passes, the service runs, and you know your score on `check_cart.py`, even if it isn't 15/15.
:::

**Next:** [3.5 Fix errors](./5-fix-errors)
