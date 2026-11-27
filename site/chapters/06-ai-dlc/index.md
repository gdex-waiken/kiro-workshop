# 6. AI-DLC: Kiro leads, people approve

**11:00 – 12:00 · Hands-on 2 · Kiro IDE.** Build Feature 1 from an empty folder: a **greenfield** project. This time Kiro reads the stakeholder notes, asks what they don't settle, and stops at a gate after every stage.

![The AI-DLC loop: AI plans, AI asks, you validate, AI implements](/images/aidlc-loop.svg){.diagram}

## What runs today

We use AI-DLC's **express** scope with the plan gate switched on. Four stages, four gates:

| # | Stage | Kiro does | You do at the gate |
|---|---|---|---|
| 1 | **Requirements Analysis** | Reads every document, writes a question file, then `requirements.md` | Answer the questions in the file. Check every decision against `stakeholder-notes.md`. **Approve** |
| 2 | **Code plan** | Writes `code-generation-plan.md`: what it will build and which tests | Delete what the ticket didn't ask for. **Approve Plan** |
| 3 | **Code Generation** | Writes the code and tests, test-first. About 8 minutes, mostly silent | Read `code-summary.md`. **Approve** |
| 4 | **Build and Test** | Runs the tests and `check_ideas.py` | Run the checker yourselves. **Approve** |

Everything is written under `aidlc/` in your folder: the questions, your answers, every approval. That's the **record**.

## The plan for this hour

| Time | Page | Checkpoint |
|---|---|---|
| 11:00 – 11:06 | [6.1 Start the workflow](./1-set-up): turn off Workflows, set up AI-DLC (we do it together) | Kiro is reading your documents |
| 11:06 – 11:19 | [6.2 Questions and conflicts](./2-inception) | **CP1:** every decision checked against a stakeholder, requirements approved |
| 11:19 – 11:27 | [6.3 Trim the plan](./3-plan-and-design) | **CP2:** you removed or questioned something in the plan |
| 11:27 – 11:50 | [6.4 Build and check](./4-construction) · [6.5 Read the record](./5-the-record) | **CP3:** `check_ideas.py` shows 13/13 on your screen |
| 11:50 – 12:00 | Two teams show their result on the big screen | |

## Roles

| Role | Job right now |
|---|---|
| **Driver** | Types into Kiro. Never answers a question alone |
| **Product Owner** | Decides every answer. Has the final say |
| **Reviewer** | Opens and reads every file before anyone types Approve |
| **Scribe** | Writes each decision, the reason and the source in `team-log.md` |

::: tip Behind schedule?
Ask the trainer. Every stage of a finished reference run is tagged in the repo, so your team can jump ahead and still do the trace at the end.
:::

::: info Sources
*AI-Driven Development Lifecycle (AI-DLC) Method Definition*, Raja SP, AWS · AI-DLC user guide, awslabs.github.io/aidlc-workflows (scopes, interaction modes, state and audit) · measured in a reference run of this exercise with `aidlc` 2.11.4
:::
