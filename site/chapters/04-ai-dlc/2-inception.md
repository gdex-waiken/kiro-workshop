# 4.2 Questions and conflicts

**11:30 – 11:45 · Checkpoint 1 at 11:45.**

## Read first, as a team

| # | File | Why |
|---|---|---|
| 1 | `ticket.md` | What Product asked for |
| 2 | `vision-document.md` | Why, for whom, what's in and out of scope |
| 3 | `stakeholder-notes.md` | **The real requirements.** People disagree here on purpose |
| 4 | `api-contract.md` | The fixed contract the app already uses |
| 5 | `technical-environment.md` | Stack, architecture, what is prohibited |

## Answer in files, not in chat

Kiro writes its questions to a `.md` file, usually `aidlc-docs/inception/requirements/requirement-verification-questions.md`, and **stops and waits**.

1. Open the file.
2. Type your answer after each `[Answer]:` tag, and say where it came from.
3. **Save the file.** Kiro reads it from disk.
4. Tell Kiro you're done.

```markdown
## Question 4
How are cart ids created?

A) The app chooses the id
B) The server generates the id
C) Other (please describe)

[Answer]: A, api-contract.md says so
```

::: tip Prompt: after you've saved your answers
```text
I've answered the questions, please proceed
```
:::

Answers in chat don't reach the audit trail. A vague answer earns a follow-up question file: that's the system working.

## The stakeholders don't agree

Four topics pull in different directions:

- **The cart badge:** what number should it show?
- **How many is too many:** is there a limit per product?
- **When it's too many:** what happens to the customer's request?
- **A launch promotion:** does it belong in this release?

Don't settle these by vote. Look for **who has the authority** and what else they said. The Product Owner decides; the Scribe writes the decision, the reason and the source in `team-log.md`. Refusing a request on record counts.

## The extension question

Kiro asks whether to enable **Security baseline**, **Resiliency** and **Property-Based Testing**. Each one adds work. Whatever you choose, write down why.

::: info Checkpoint 1 (11:45)
Every conflict has a decision, a reason and a source in `team-log.md`. The extension decision is recorded. Answers are in the question files, not the chat.
:::

**Next:** [4.3 Plan and design](./3-plan-and-design)
