# 6.5 Read the record

**A few minutes before the break.**

## What AI-DLC kept

| File | Holds |
|---|---|
| `aidlc-docs/audit.md` | Every question, answer and approval, with a timestamp, including your first prompt |
| `aidlc-docs/aidlc-state.md` | Which stages ran, which were skipped, and the extensions you chose |
| `aidlc-docs/inception/…` | Requirements, the execution plan and the design |

These files are the AI's "context memory", and yours: a new session, or a new teammate, can continue without any chat history. You'll keep this record when you start Feature 2 in [Chapter 7](../07-brownfield).

## Walk one result back to a sentence

Pick a result the checker tests, for example the `409` at step 3 (a duplicate title is refused), and trace it back:

1. **The result** the checker tests
2. **The test** that would fail if the decision flipped
3. **The design decision**, in `aidlc-docs/`
4. **The requirement**, in `aidlc-docs/`
5. **Your answer** in a question file
6. **The sentence** a stakeholder said, in `stakeholder-notes.md`

For step 3, the chain should end at Aina's Tuesday message: "Same title, ignoring capitals and spaces at the ends, is refused." Other good ones: the `422` at step 5 (Daniel: "Reject it and let them shorten it, don't cut it") and the `422` at step 8 (Aina: "Every idea needs a staff ID from the staff list").

Write the chain in `traceability-worksheet.md`. Where it breaks is the most useful thing you'll learn today.

::: tip Prompt: help tracing a result
```text
Trace the 409 at step 3 of sample-data/ideas-scenario.csv back through the code, the tests, the design and the requirements in aidlc-docs/ to the stakeholder sentence it depends on. Quote each file and line.
```
:::

**Break: 12:35 – 12:50.** Then [Chapter 7: Brownfield](../07-brownfield).
