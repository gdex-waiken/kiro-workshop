# 6.2 Questions and conflicts

**11:06 – 11:19 · Checkpoint 1 at 11:19.**

## Answer in the file, not in the chat

Kiro wrote its questions to:

```text
aidlc/spaces/default/intents/<date>-<name>/inception/requirements-analysis/requirements-analysis-questions.md
```

1. Open the file. The **Product Owner** decides each answer; the **Scribe** writes it in `team-log.md` with the source.
2. Type the letter after `[Answer]:`, then **who said so**.
3. **Save the file.**
4. Send:

::: tip Prompt 2 · Answers are in the file
```text
done
```
:::

What a good answer looks like (the format, not the answer to your question):

```markdown
## Q1. [Product owner] <a question Kiro asks>

- A. <option>
- B. <option>
- X. Other (please specify)

[Answer]: B. Aina, Tuesday: "<her sentence>".
```

Kiro may ask different questions from the team next to you. That's normal: it asks only about what your documents don't settle.

::: tip When no stakeholder said anything about it
Kiro often asks about gaps nobody discussed, such as rules for the description. Then the **Product Owner decides**, using the ticket and `api-contract.md`, and writes `PO decision:` and the reason, for example `[Answer]: A. PO decision: the ticket says "a short description" and sets no limit, so we don't invent one.`
:::

## The stakeholders don't agree

`stakeholder-notes.md` has five disagreements for Feature 1:

- **Long titles:** cut them to 80 characters, or refuse?
- **Anonymous ideas:** let shy staff submit without a name?
- **Duplicates:** refuse a repeat, or allow it and merge later?
- **An "Other" category:** add one so nobody gets stuck?
- **An AI summary of each idea:** "basically one API call"?

Kiro either asks you about these, or decides them itself and shows the decisions in `requirements.md`. **Either way, your job is the same: check each decision against the person who has the authority.** Read the follow-up messages: some people changed their minds.

## Gate 1 · Requirements

About a minute after `done`, Kiro writes `requirements.md` in the same folder and stops at the gate. The **Reviewer** reads it aloud. Look for the table **Decisions on stakeholder disagreements**:

| Disagreement | Decision | Source |
|---|---|---|
| Cut long titles vs reject | Reject with `422`, never cut | Daniel Wong, Siti Hassan |
| Allow anonymous ideas | Refused; staff ID required | Aina Rahman (Tuesday) |
| … | … | … |

*From the reference run. Yours may be worded differently.*

For each row, find the sentence in `stakeholder-notes.md`. If one is wrong, say so in words:

::: tip Prompt · Request a change to the requirements
```text
Request changes: <the decision> is wrong. <Who> said <what> in stakeholder-notes.md (<day>). Change the requirement and the decisions table.
```
:::

When every row checks out:

::: tip Prompt 3 · Approve the requirements
```text
Approve
```
:::

::: details Stuck on a disagreement? Hints
| Topic | What settles it | The checker tests |
|---|---|---|
| Long titles | Daniel's Tuesday follow-up: "Reject it and let them shorten it, don't cut it" | Step 5: 81 characters → `422`. Step 6: exactly 80 → `201` |
| Anonymous ideas | Aina, Tuesday: every idea needs a staff ID from the staff list | Steps 8 and 9 → `422` |
| Duplicates | Aina, Tuesday: same title, ignoring capitals and spaces at the ends, is refused | Step 3 → `409` |
| "Other" category | Aina, kick-off: the committee reports by category, the list is fixed | Step 7 → `422` |
| AI summary | Out of scope in `vision-document.md`; `technical-environment.md` forbids outside calls | Nothing: refuse it **on record** in `team-log.md` |
:::

::: info Checkpoint 1 (11:19)
Requirements approved. `team-log.md` has every disagreement with a decision, a reason and a source, including the AI summary you refused.
:::

**Next:** [6.3 Trim the plan](./3-plan-and-design)
