# AI-DLC cheat sheet

> Keep this open all morning. It's the map; `ai-dlc/README.md` is the route.

## The golden rule

**Kiro proposes, you approve.** Every stage ends at a gate. Read the files before you choose **Continue**.

## The stages

| Phase | Stage | What it produces | Today |
|---|---|---|---|
| Inception | Workspace Detection | Spots whether there is existing code | runs |
| | Reverse Engineering | Docs for existing code | skipped (no code yet) |
| | **Requirements Analysis** | Requirements + the extension question | **runs: the big one** |
| | User Stories | Stories with acceptance criteria | Kiro may propose it; keep it short |
| | **Workflow Planning** | The execution plan: which stages run or skip | **challenge it** |
| | Application Design | Components and boundaries | runs, keep it small |
| | Units Generation | Splits work into units | one unit is enough today |
| Construction | Functional / NFR design | Detailed design per unit | lean |
| | **Code Generation** | Code and tests | runs |
| | **Build and Test** | Full test run, verification | runs, then `check_cart.py` |

Everything lands in `aidlc-docs/`: `aidlc-state.md` (where you are) and `audit.md` (every question, answer and approval).

## Trim the plan

AI over-builds. Ask for a cart and it may plan login, checkout, a database and an admin page. Before you approve a plan, **delete everything the ticket didn't ask for**, and say why at the gate. Every task you delete is code you don't have to review, and credits you don't spend.

## Question files, not chat

1. Kiro writes questions to a `.md` file with lettered options and an `[Answer]:` tag.
2. Type your letter (or a short answer) after each tag. Answer **every** question.
3. Save the file.
4. Tell Kiro: `I've answered the questions, please proceed`.

A vague answer gets a follow-up file. That's the system working.

## Extensions (asked during Requirements Analysis)

| Extension | Adds | Today |
|---|---|---|
| Security baseline | Security rules checked at every gate | your call: record why |
| Resiliency | Failure-mode analysis | your call: record why |
| Property-Based Testing | Generated-input tests | your call: record why |

Each one you enable adds work. A "no" only counts if it's written down with a reason.

## Roles (swap the Driver at the break)

**Driver:** types, never answers alone · **Product Owner:** final say, settles conflicts · **Reviewer:** reads every file before a gate · **Scribe:** keeps `team-log.md` live

## Saving credits

- Read the generated files instead of asking Kiro to explain them in chat.
- Don't ask for optional or stretch work until Feature 1 passes `check_cart.py`.
- One session per team. Don't open parallel sessions on the same work.

## Done means

`pytest` passes · `check_cart.py` shows **15/15** · every conflict has a recorded decision · one traceability chain written
