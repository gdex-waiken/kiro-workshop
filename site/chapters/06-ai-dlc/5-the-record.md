# 6.5 Read the record

**While Code Generation runs, about 8 minutes.**

## What AI-DLC kept

Everything is in `aidlc/spaces/default/intents/<date>-<name>/`:

| File | Holds |
|---|---|
| `project-description.json` | Your request, the words after the `/aidlc …` options |
| `aidlc-state.md` | Which stages ran, which were skipped, and why |
| `inception/requirements-analysis/requirements-analysis-questions.md` | Kiro's questions and your answers |
| `inception/requirements-analysis/requirements.md` | The requirements, numbered, and the decisions table |
| `construction/code-generation/code-generation-plan.md` | The plan you trimmed and approved |
| `construction/code-generation/code-summary.md` | What was built, file by file |
| `construction/build-and-test/test-results.md` | The test run and the checker result |
| `audit/` | One entry per event: every stage start, question, answer and approval, with a time |

A new chat, or a new teammate, can carry on from these files without the chat history. Ask Kiro where it is at any time:

```text
/aidlc --status
```

## Walk one result back to a sentence

Fill in `traceability-worksheet.md`. Pick a checker step, for example **step 5**: a title of 81 characters is refused with `422`, not cut.

```text
step 5 in sample-data/ideas-scenario.csv: 81 characters → 422
  └─ the test in tests/ that checks 81 characters are refused
      └─ the requirement in requirements.md (the 80-character rule)
          └─ the row in "Decisions on stakeholder disagreements", or your answer in the question file
              └─ Daniel, Tuesday: "Reject it and let them shorten it, don't cut it."
```

Other good ones: step 3, the `409` for a duplicate (Aina, Tuesday), and step 8, the `422` for no staff ID (Aina, Tuesday).

::: tip Prompt · Help tracing a result
```text
Trace step 5 of sample-data/ideas-scenario.csv back through the tests, the code and the requirements in this workflow's record to the stakeholder sentence it depends on. Quote each file and line.
```
:::

Where the chain breaks is the most useful thing you'll learn today. At 12:50 the trainer picks a step and your team walks it in 60 seconds.

**Break: 12:00 – 12:10.** Then [Chapter 7: Brownfield](../07-brownfield).
