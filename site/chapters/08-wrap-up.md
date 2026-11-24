# 8. Wrap-up and roll-out

**1:15 – 1:30 · Talk and Q&A.**

<img src="/images/kiro-ghost.png" alt="The Kiro ghost" class="mascot-float" />

## Show it: a few minutes per team

1. **Run the checkers live:** `python check_ideas.py` and `python check_ideas.py --feature 2`.
2. **Walk one traceability chain, out loud.** Pick one result, for example the `409` at step 3 or the `422` at step 5, and take it back: the result → the test → the design → the requirement → your answer in a question file → the sentence a stakeholder said.
3. **Say where your chain broke**, if it did.

## Compare your builds

From the repo root:

```bash
# What each process left on disk
ls spec-driven/.kiro/specs/ ai-dlc/aidlc-docs-feature1/ ai-dlc/aidlc-docs/

# What AI-DLC recorded about itself
head -40 ai-dlc/aidlc-docs-feature1/audit.md
```

| Question | Spec-driven (Chapter 5) | AI-DLC greenfield (Chapter 6) | AI-DLC brownfield (Chapter 7) |
|---|---|---|---|
| Your checker score | `check_ideas.py`: __/13 | `check_ideas.py`: __/13 | `--feature 2`: __/14, and still __/13 |
| Who stated the requirements? | Kiro drafted, you corrected | Kiro asked, you answered, then it drafted | Kiro read the code first, then asked |
| Where are the decisions recorded? | `requirements.md`, `design.md` | `aidlc-docs-feature1/`, `team-log.md` | `aidlc-docs/`, `team-log.md` |
| Which failing steps did the stakeholder notes fix? | | | |

::: tip The question that matters
**In six months, which project could a new teammate pick up with confidence?** The one with the code alone, the one with a spec, or the one with every question, answer and approval on record?
:::

## Three layers of Kiro governance

| Layer | What it controls |
|---|---|
| **Console policy** | Which models, MCP servers and sign-in methods your organization allows |
| **Dashboards and exports** | Who is using what, and how much |
| **Repo guardrails** | Hooks, steering, `.kiroignore` and permission rules that travel with the repo |

Kiro inherits what your credentials and machine can already reach. IAM, device management, network rules and secrets handling set the real limits.

## Retro: three, three, one

Write it down as a team in `team-log.md`, then share one item from each:

- **3** things that worked
- **3** frictions you hit
- **1** thing you'd change before using this on a real project

## Habits to take home

1. **Verify the plan, verify the outcome.** Those two human steps are the whole method.
2. **Trim before you approve.** AI over-builds by default.
3. **Answer in files.** If it isn't in the record, it didn't happen.
4. **Record the why**, with the source.
5. **Fewer, bigger tasks.** Every task re-sends its context.
6. **Keep steering short:** `product.md`, `tech.md`, `structure.md`.
7. **Keep your `.kiro/` and `aidlc-docs/` folders.** They explain why your code does what it does.

## Clean up

- Stop the uvicorn services (`Ctrl+C`).
- Remove any recurring Kiro Crew jobs you created.
- Keep the repo: your specs and AI-DLC records are reusable.

## Next steps

- **Add Feature 2 to the spec build too**, and compare how a spec handles existing code with how AI-DLC's Reverse Engineering did.
- **Try a brownfield change on your own code:** AI-DLC starts by documenting what's already there.
- **Bring it to a real ticket**, with the people you'd normally wait for answering the question files together.

::: info Source
Governance layers: AWS workshop *Kiro – Getting Started*, Lab 15.
:::
