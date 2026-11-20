# 4. AI-DLC: Kiro leads, people approve

**2:50 – 3:50 · Hands-on, 1 hour · Kiro IDE.** Same cart, built again. This time Kiro asks before it assumes.

## Reverse the conversation

In the **AI-assisted** way of working, people do the thinking and prompt the AI task by task. **AI-DLC** (AI-Driven Development Life Cycle) turns that around: the AI proposes the plan, asks the questions and recommends options, and **people approve, choose and decide** at every critical point.

> Humans set the destination, the intent. AI gives the step-by-step directions, and people keep oversight along the way. — AWS AI-DLC method definition

## One loop, repeated for every step

![The AI-DLC loop](/images/aidlc-loop.svg){.diagram}

Every check you make works like a safety net: it catches a wrong turn early, before it snowballs into code. Iterations are called **Bolts**, and they last hours or days instead of weeks.

## From intent to running code

![The AI-DLC core framework](/images/aidlc-framework.png){.figure}

| Artefact | What it is |
|---|---|
| **Intent** | A high-level goal: a feature, a business need, a technical outcome |
| **Unit** | A self-contained, loosely coupled piece of the intent, like an epic |
| **Bolt** | A short build cycle that delivers a Unit |

## Three phases, nine steps

![The AI-DLC workflow](/images/aidlc-workflow.png){.figure}

| Phase | Team ritual | What happens | Today |
|---|---|---|---|
| **Inception** | Mob Elaboration | Intent → user stories, NFRs, risks, Units and Bolts | Yes |
| **Construction** | Mob Construction | Domain design → logical design → code and tests | Yes |
| **Operations** | AI watches, people approve | Deploy, then monitor metrics, logs and incidents | After the workshop |

Each step builds richer context for the next, and every artefact is saved, so the AI (and your teammates) can always find out why something was decided.

## Who does what

<div class="split">
<div>

| Who | Does |
|---|---|
| **AI** | Asks, elaborates, recommends designs, writes code and tests, watches production |
| **Product Owner and developers** | Set the intent, verify each step, make the decisions |

</div>
<img src="/images/aidlc-greenfield.png" alt="Who does what in an AI-DLC green-field project" class="figure tall" />
</div>

## AI-DLC in Kiro

AI-DLC comes as a set of rules from [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows). Copied into `.kiro/steering/`, they turn Kiro into a disciplined teammate: it asks before it assumes, plans before it builds, and stops at a **gate** after every stage. Today we use release **v1.0.1**.

| Stage | Produces | Today |
|---|---|---|
| Workspace Detection | Spots existing code | runs |
| **Requirements Analysis** | Requirements and the extension question | the big one |
| User Stories | Stories with acceptance criteria | keep it short |
| **Workflow Planning** | Which stages run and which are skipped | **trim it** |
| Application Design | Components and boundaries | keep it small |
| **Code Generation** | A plan, then code and tests | gated twice |
| **Build and Test** | Full test run | then `check_cart.py` |

## The plan for this hour

| Time | Page | Checkpoint |
|---|---|---|
| 2:50 – 3:00 | [4.1 Set up](./1-set-up) | Welcome message appears |
| 3:00 – 3:15 | [4.2 Questions and conflicts](./2-inception) | **CP1:** every conflict has a recorded decision |
| 3:15 – 3:30 | [4.3 Plan and design](./3-plan-and-design) | **CP2:** you deleted or questioned something in the plan |
| 3:30 – 3:50 | [4.4 Construction](./4-construction) · [4.5 The record](./5-the-record) | **CP3:** checker result on screen |

::: tip Behind schedule?
Ask the facilitator for a ready-made `aidlc-docs/` up to an approved design, and jump straight to Construction.
:::

::: info Sources
*AI-Driven Development Lifecycle (AI-DLC) Method Definition*, Raja SP, Amazon Web Services (figures reproduced from it) · AWS workshop *Kiro – Getting Started*, Lab 12 Part 2 · github.com/awslabs/aidlc-workflows
:::
