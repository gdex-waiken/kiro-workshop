# 4.5 Read the record

**A few minutes before the break.**

## What AI-DLC kept

| File | Holds |
|---|---|
| `aidlc-docs/audit.md` | Every question, answer and approval, with a timestamp, including your first prompt |
| `aidlc-docs/aidlc-state.md` | Which stages ran, which were skipped, and the extensions you chose |
| `aidlc-docs/inception/…` | Requirements, stories, the execution plan and the design |

These files are the AI's "context memory", and yours: a new session, or a new teammate, can continue without any chat history.

## Walk one number back to a sentence

Pick a number the checker tests, for example `54.00` (cart A's subtotal at step 9), and trace it back:

1. **The number** the checker tests
2. **The test** that would fail if the decision flipped
3. **The design decision**, in `aidlc-docs/`
4. **The requirement**, in `aidlc-docs/`
5. **Your answer** in a question file
6. **The sentence** a stakeholder said, in `stakeholder-notes.md`

Write the chain in `traceability-worksheet.md`. Where it breaks is the most useful thing you'll learn today.

::: tip Prompt: help tracing a number
```text
Trace the subtotal 54.00 at step 9 of sample-data/cart-scenario.csv back through the code, the tests, the design and the requirements in aidlc-docs/ to the stakeholder sentence it depends on. Quote each file and line.
```
:::

**Break: 3:50 – 4:05.** Then [Chapter 5: Which way to build?](../05-compare)
