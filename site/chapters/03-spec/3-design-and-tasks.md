# 3.3 Review the design and the tasks

**About 10 minutes.**

## design.md

| Check | Look for |
|---|---|
| Three layers | `domain`, `application`, `adapters`, as `tech.md` says |
| Money | `Decimal`, never `float` |
| Decisions point back to requirements | Each design choice names the criterion it satisfies |
| Nothing extra | No database, login, checkout or new endpoint |

::: tip Prompt: approve the design
```text
The design looks good. Continue to the tasks phase. Keep it to at most 5 tasks, tests first, no optional tasks.
```
:::

## tasks.md

Each task is a checkbox, with a `_Requirements: x.y_` line linking it back to `requirements.md`.

| Check | Why |
|---|---|
| 5 tasks or fewer | Every task reloads the steering and the spec. Fewer, bigger tasks cost less |
| Each task starts with a failing test | That's the TDD rule in `tech.md` |
| No "optional" tasks | They add time and credits you don't need today |

## Run the tasks

::: code-group

```text [Kiro IDE]
In tasks.md, click "Start task" above task 1.
When it's done, review the change, then start the next one.
Or run all required tasks at once.
```

```text [Kiro CLI]
Choose "Run required tasks" at the review question.
Resume later with:  /spec run kedaiku-cart
```

:::

::: warning One task at a time while you're learning
You see what each task changes, and what it costs. Running everything at once on a long plan recreates the "more agents, more tokens" problem from Chapter 6.
:::

**Next:** [3.4 Build and check](./4-build-and-check)
