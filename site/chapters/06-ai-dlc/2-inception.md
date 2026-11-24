# 6.2 Questions and conflicts

**11:45 – 12:00 · Checkpoint 1 at 12:00.**

## Read first, as a team

| # | File | Why |
|---|---|---|
| 1 | `Pelita-Ideas-Proposal.pdf` | The brief from Product: scope, constraints, done means |
| 2 | `ticket.md` | What the innovation team asked for |
| 3 | `vision-document.md` | Why, for whom, what's in and out of scope |
| 4 | `stakeholder-notes.md` | **The real requirements.** People disagree here on purpose |
| 5 | `api-contract.md` | The fixed contract the app team already uses |
| 6 | `technical-environment.md` | Stack, architecture, what is prohibited |

## Answer in files, not in chat

Kiro writes its questions to a `.md` file, usually `aidlc-docs/inception/requirements/requirement-verification-questions.md`, and **stops and waits**.

1. Open the file.
2. Type your answer after each `[Answer]:` tag, and say where it came from.
3. **Save the file.** Kiro reads it from disk.
4. Tell Kiro you're done.

```markdown
## Question 4
What should happen when a title is longer than 80 characters?

A) Cut it to 80 characters and add "..."
B) Refuse it with 422 and let the person shorten it
C) Other (please describe)

[Answer]: B. Daniel's follow-up on Tuesday: "Reject it and let them shorten it, don't cut it."
```

::: tip Prompt: after you've saved your answers
```text
I've answered the questions, please proceed
```
:::

Answers in chat don't reach the audit trail. A vague answer earns a follow-up question file: that's the system working.

## The stakeholders don't agree

Five topics pull in different directions:

- **Long titles:** the card shows 80 characters. Cut the rest, or refuse?
- **Anonymous ideas:** should shy staff be able to submit without a name?
- **Duplicates:** refuse an idea that's already there, or allow it and merge later?
- **An "Other" category:** add one so nobody gets stuck?
- **An AI summary of each idea:** "basically one API call". Does it belong in this release?

Don't settle these by vote. Look for **who has the authority**, and read the **follow-up messages**: some people changed their minds. The Product Owner decides; the Scribe writes the decision, the reason and the source in `team-log.md`. Refusing a request on record counts.

::: details Stuck? Hints, one per conflict
| Topic | Who disagrees | What settles it | The answer key checks |
|---|---|---|---|
| Long titles | Daniel (cut it with "...") vs Siti (never change what someone wrote) | Daniel's Tuesday follow-up: reject it, don't cut it | Step 5: 81 characters → `422`. Step 6: exactly 80 → `201` |
| Anonymous ideas | Siti (let them) vs Aina (not this release) | Aina, Tuesday: every idea needs a staff ID from the staff list | Step 8: no staff ID → `422` |
| Duplicates | Priya (refuse) vs Marcus (allow, merge later) | Aina, Tuesday: Priya is right. Same title, ignoring capitals and spaces at the ends, is refused | Step 3: "&nbsp;&nbsp;REUSABLE PARCEL BAGS&nbsp;&nbsp;" → `409` |
| "Other" category | Marcus (add it) vs Aina (the fixed list of five) | Aina, kick-off: the committee reports by category, so the list is fixed | Step 7: "Other" → `422` |
| AI summary | Marcus asks, twice | Out of scope in `vision-document.md`; `technical-environment.md` forbids calls to outside services | Nothing to check: refuse it **on record** in `team-log.md` |
:::

## The extension question

Kiro asks whether to enable **Security baseline**, **Resiliency** and **Property-Based Testing**. Each one adds work. Whatever you choose, write down why.

::: info Checkpoint 1 (12:00)
Every conflict has a decision, a reason and a source in `team-log.md`, including the AI summary you refused. The extension decision is recorded. Answers are in the question files, not the chat.
:::

**Next:** [6.3 Plan and design](./3-plan-and-design)
