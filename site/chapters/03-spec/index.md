# 3. Spec-driven development

**10:05 – 11:05 · Hands-on, 1 hour · Kiro IDE.** Plan it, approve it, build it, check it, fix it.

![Kiro IDE with a spec open](/images/kiro-ide.png){.shot}

## A spec is three files you approve

Instead of jumping to code, Kiro first writes three markdown files in `.kiro/specs/<name>/`, and pauses for your review after each one.

| File | Holds | You check |
|---|---|---|
| `requirements.md` | User stories and acceptance criteria in **EARS** form: `WHEN … THE SYSTEM SHALL …` | Is every criterion testable? Did Kiro add anything you didn't ask for? |
| `design.md` | Components, data, errors and the test plan | Do the decisions point back to the requirements? |
| `tasks.md` | A short checklist, each task linked to the requirements it covers | Small enough to review? Tests first? |

## Why work from a spec?

- **Shared understanding.** Everyone can read and agree on the goal before code exists.
- **A North Star for the agent.** It can take on larger work without losing the plot.
- **It catches bugs.** In the AWS lab, a test written from one requirement caught a bug that vibe coding would have shipped.

## Steering: rules Kiro reads with every request

Your `spec-driven/.kiro/steering/` folder already has three short files:

| File | Holds |
|---|---|
| `product.md` | What we build, for whom, what's in and out of scope |
| `tech.md` | The stack and the hard technical rules |
| `structure.md` | Folders, naming, run commands |

```yaml
---
inclusion: always            # or: fileMatch, manual
---
```

::: tip Keep steering short
Always-on files are sent with every request. Short files cost less and keep Kiro focused.
:::

## The plan for this hour

| Step | Page | Time |
|---|---|---|
| Create the spec | [3.1](./1-create-the-spec) | 10 min |
| Review the requirements | [3.2](./2-requirements) | 10 min |
| Review design and tasks | [3.3](./3-design-and-tasks) | 10 min |
| Build, run and check | [3.4](./4-build-and-check) | 20 min |
| Fix what fails | [3.5](./5-fix-errors) | 10 min |

::: info Sources
AWS workshop *Kiro – Getting Started*, Lab 12 Part 1 · kiro.dev/docs/specs
:::
