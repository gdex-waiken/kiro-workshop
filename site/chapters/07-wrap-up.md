# 7. Roll it out to the team

**4:45 – 5:00 · Talk and Q&A.**

<img src="/images/kiro-ghost.png" alt="The Kiro ghost" class="mascot-float" />

## Three layers of Kiro governance

| Layer | What it controls |
|---|---|
| **Console policy** | Which models, MCP servers and sign-in methods your organization allows |
| **Dashboards and exports** | Who is using what, and how much |
| **Repo guardrails** | Hooks, steering, `.kiroignore` and permission rules that travel with the repo |

Kiro inherits what your credentials and machine can already reach. IAM, device management, network rules and secrets handling set the real limits.

## Retro: three, three, one

Write it down as a team, then share one item from each:

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

- **Finish Feature 2** (remove items) as a new AI-DLC request, and see whether Kiro proposes a leaner plan now that code exists.
- **Try a brownfield change** on code you already have: AI-DLC starts with Reverse Engineering.
- **Bring it to a real ticket**, with the people you'd normally wait for answering the question files together.

::: info Source
Governance layers: AWS workshop *Kiro – Getting Started*, Lab 15.
:::
