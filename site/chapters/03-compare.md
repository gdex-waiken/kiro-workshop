# 3. Vibe, spec or AI-DLC?

**10:00 – 10:10 · Discussion.** Three ways to build with Kiro, and when to use which. You'll try two of them this morning on the same feature, so decide now what you expect to see.

## Vibe coding, spec or AI-DLC: at a glance

| | Vibe coding | Spec-driven | AI-DLC |
|---|---|---|---|
| **Who drives** | You, one prompt at a time | You and Kiro, phase by phase | AI directs, you validate |
| **Requirements** | Implicit, in the chat | EARS criteria in `requirements.md` | Gathered through question files |
| **Left on disk** | Just the code | `.kiro/specs/` + code | `aidlc-docs/` + audit trail + code |
| **Time in the AWS lab** (Sudoku app) | 2–4 min | ~50 min | ~12 min |

More ceremony did not mean more time: in the AWS lab, AI-DLC skipped stages that added no value and finished well ahead of a 50-task spec run.

## When to use which

| Situation | Use |
|---|---|
| Prototypes, throwaway scripts, small fixes in familiar code | **Vibe coding** |
| A clear feature in an ongoing project, or work that needs stakeholder review first | **Spec-driven** |
| Fuzzy requirements, people who disagree, audit or compliance needs, end-to-end projects | **AI-DLC** |

They're not mutually exclusive: use a spec or AI-DLC for the big picture, then vibe-code fast iterations inside it.

## What you'll do this morning

| Chapter | Way of working | What you build | Where |
|---|---|---|---|
| [5](./05-spec/) | **Spec-driven** | Feature 1: submit and browse ideas | `spec-driven/` |
| [6](./06-ai-dlc/) | **AI-DLC, greenfield** | Feature 1 again, from an empty folder | `ai-dlc/` |
| [7](./07-brownfield) | **AI-DLC, brownfield** | Feature 2: vote and rank, added to your Chapter 6 code | `ai-dlc/` |

Same ticket, same contract, same answer key. What changes is how much Kiro asks, and how much it writes down. You compare the results in [Chapter 8](./08-wrap-up).

## Discuss

::: tip Three questions for your team, before you start
1. Which of the three do you use today, and for what kind of work?
2. The spec folder gets no stakeholder notes; the AI-DLC folder does. Which build do you expect to score higher on the checker, and why?
3. Six months from now, which project would you rather hand to a new teammate?
:::

::: info Source
AWS workshop *Kiro – Getting Started*, Lab 12 Part 3 (the comparison and the timings come from its Sudoku runs).
:::
