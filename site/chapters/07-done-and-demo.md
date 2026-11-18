# 7. Done, demo and traceability

## Done means 15 out of 15

Start your service in one terminal, then run the checker in another, from the `ai-dlc` folder:

```bash
uvicorn app.main:app --port 8000
python check_cart.py
```

```text
PASS  step  1  add 2 x SKU-001 to cart A            (first add creates the cart)
...
PASS  step 15  get cart A                           (first cart is untouched)

15/15 steps match the answer key.
```

The checker replays every step in `sample-data/cart-scenario.csv` with fresh cart ids, so you can run it as often as you like.

### Definition of done

- `pytest` passes.
- `check_cart.py` prints **15/15**.
- Every conflict in `stakeholder-notes.md` has a decision and a reason in `team-log.md`.
- `traceability-worksheet.md` has at least one complete chain.
- `aidlc-docs/` shows a gate approval for every stage that ran.

::: info Why the answer key ships with you
Building software that reproduces a known-correct number is the exercise. Guessing what the number should be is not.
:::

## Walk one number back to a sentence

Pick a number the checker tests, and trace it back:

1. **The number:** for example `54.00`, cart A's subtotal at step 9
2. **The test** that would fail if the decision flipped
3. **The design decision**, in `aidlc-docs/`
4. **The requirement**, in `aidlc-docs/`
5. **Your answer** in a question file
6. **The sentence** a stakeholder said, in `stakeholder-notes.md`

Where the chain breaks is the most useful thing you'll learn today. Write it in [`traceability-worksheet.md`](https://github.com/gdex-waiken/kiro-workshop/blob/main/ai-dlc/traceability-worksheet.md).

## Your demo: 5 minutes

1. **Run it:** start the service and run `check_cart.py` live.
2. **Trace it:** walk one number back, out loud, to the sentence that caused it.
3. **Be honest:** say where your chain broke, and what you'd do differently.

After the demos, we put a few teams' workflow plans side by side. Same documents, same rules, but different answers lead to different plans.
