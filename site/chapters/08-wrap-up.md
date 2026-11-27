# 8. Show, trace and roll out

**12:50 – 1:30 · Show, then talk and Q&A.**

<img src="/images/kiro-ghost.png" alt="The Kiro ghost" class="mascot-float" />

## Show it: 2 minutes per team (12:50)

Start the service in one terminal, then run both checkers in another and read the totals out:

```bash
python -m uvicorn app.main:app --port 8000
```

```bash
python check_ideas.py
python check_ideas.py --feature 2
```

The trainer writes them on the scoreboard.

## The trace challenge: 60 seconds per team

The trainer picks one checker step. Your team walks it back, out loud, using only the files:

```text
the checker step
  └─ the test that would fail if the decision flipped        tests/…
      └─ the requirement                                      …/requirements.md
          └─ your answer, or the decisions table              …/requirements-analysis-questions.md
              └─ the sentence a stakeholder said              stakeholder-notes.md
```

| Good steps to be asked | Ends at |
|---|---|
| Feature 1, step 3: `409` for "&nbsp;&nbsp;REUSABLE PARCEL BAGS&nbsp;&nbsp;" | Aina, Tuesday |
| Feature 1, step 5: `422` for 81 characters | Daniel, Tuesday |
| Feature 1, step 8: `422` with no staff ID | Aina, Tuesday |
| Feature 2, step 3: `409` for a second vote | Aina, Wednesday |
| Feature 2, step 10: A ranks above B on a tie | Aina, Wednesday |

Nobody wrote that audit trail by hand. AI-DLC kept it while you worked.

## Compare the three ways you worked

| | Spec (Hands-on 1) | AI-DLC greenfield (Hands-on 2) | AI-DLC brownfield (Hands-on 3) |
|---|---|---|---|
| Who found the open decisions? | You, if you noticed | Kiro asked, or decided and showed you | Kiro read the code, then asked |
| Where are decisions recorded? | `requirements.md` | Question file, `requirements.md`, `audit/`, `team-log.md` | Same, in a second record folder |
| Your result | Gaps found: __ | `check_ideas.py`: __/13 | `--feature 2`: __/14, still __/13 |

::: tip The question that matters
**In six months, which project could a new teammate pick up without asking you?**
:::

## Roll it out {#roll-it-out}

### Which way, when

| Situation | Use |
|---|---|
| A quick fix, a throwaway script | Chat (vibe) |
| A clear feature in a project you know | Spec |
| Fuzzy needs, people who disagree, a team sharing one repo, audit needs | AI-DLC |
| You know the outcome, not the steps | Goal |

### Three layers of governance

| Layer | What it controls |
|---|---|
| **Kiro console** | Which models, MCP servers, web tools and sign-in methods your organization allows; prompt logging |
| **Dashboards** | Who uses what, and how many credits |
| **Repo guardrails** | Steering, hooks, `.kiroignore` and permission rules that travel with the repo |

Kiro can only reach what your credentials and your machine can reach. IAM, device management and network rules set the real limits.

### Habits to take home

1. **Give Kiro documents, not one-liners.** The client's brief as steering, a ticket, a contract, the rules.
2. **Read before you approve.** A gate you click without reading is a gate you didn't use.
3. **Trim the plan.** AI over-builds by default.
4. **Verify the artifacts, not the diff.** Requirements, plan and code summary tell you what changed and why; the diff only tells you what.
5. **Answer in files.** If it isn't in the record, it didn't happen.
6. **Keep your `.kiro/` and `aidlc/` folders in git.** They explain why your code does what it does.

## Retro: three, three, one

In `team-log.md`, then share one item each: **3** things that worked, **3** frictions, **1** thing you'd change before using this on a real project.

## Clean up

- Stop the service (**Ctrl + C**).
- Keep the repo: your records are worth reading again.

## Next steps

- **Monday:** pick one real ticket and run it with `/aidlc express …`, with the people who'd normally answer your questions filling in the question file.
- **Take-home:** finish the spec build from [Chapter 3](./03-spec/3-design-and-tasks) and compare its checker score with your AI-DLC build.
- **Read:** the AI-DLC user guide at [awslabs.github.io/aidlc-workflows](https://awslabs.github.io/aidlc-workflows/guide/01-getting-started/).

::: info Sources
Governance: kiro.dev/docs/enterprise (settings and governance) · AWS workshop *Kiro – Getting Started*, Lab 15. AI-DLC: awslabs.github.io/aidlc-workflows.
:::
