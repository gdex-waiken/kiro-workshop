# 1. Why AI-DLC

## Three ways to work with AI

| Approach | Who does what | What goes wrong |
|---|---|---|
| **AI-managed** | AI builds and maintains the software alone, with little or no human involvement | It seldom works. The result is unreliable, and nobody can explain the code |
| **AI-assisted** | People do the heavy thinking; AI helps with narrow tasks such as writing a function | Time saved in coding is lost again in handoffs, reviews and waiting |
| **AI-driven** (AI-DLC) | AI plans and builds; people verify the plan and the outcome at every step | Only works if people really verify. Clicking "Continue" without reading turns it back into AI-managed |

## Where the time really goes

In most teams, writing code is not the slow part. **Waiting** is: for a test environment, a database change, a security review, a performance test. Every team waits for another team.

AI-DLC tackles this by putting the decisions in one place and one moment. The people who would normally be waited on answer the AI's questions together (AWS calls these sessions *mob elaboration* and *mob construction*), and every answer is written down.

## The operating model

Every stage of AI-DLC runs the same loop:

1. **AI** creates the plan
2. **You** verify the plan
3. **AI** refines the plan
4. **AI** executes the plan
5. **You** verify the outcome

In Kiro, each "verify" is a **gate**. That's where you trim, correct and approve. Each stage builds richer context for the next one.

## Three ways to work in Kiro

| Mode | How it works | Use it when |
|---|---|---|
| **Vibe** | You chat, Kiro codes | Prototypes and small fixes |
| **Spec** | Kiro writes requirements, design and tasks; you review; then it builds | The feature is clear and small |
| **AI-DLC** | Kiro asks first in question files, plans which stages to run, and stops at a gate before each one | Requirements are unclear, or people disagree |

AI-DLC runs inside Kiro's Vibe mode, using the AI-DLC rules as steering. It **replaces** the spec workflow, so if Kiro offers to switch to Spec mode during the hands-on, decline.

::: tip Source
The three approaches, the operating model and the phase names come from the AWS talk on the AI-Driven Development Lifecycle: [watch it on YouTube](https://www.youtube.com/watch?v=1HNUH6j5t4A).
:::
