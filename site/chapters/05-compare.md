# 5. Which way to build?

**12:35 – 12:55 · Discussion.** You've built the same cart twice. Now put the two results side by side.

## Compare your two builds

From the repo root:

```bash
# What each process left on disk
ls spec-driven/.kiro/specs/ ai-dlc/aidlc-docs/

# What AI-DLC recorded about itself
head -40 ai-dlc/aidlc-docs/audit.md
```

| Question | Spec-driven (`spec-driven/`) | AI-DLC (`ai-dlc/`) |
|---|---|---|
| Your `check_cart.py` score | | |
| Who stated the requirements? | Kiro drafted, you corrected | Kiro asked, you answered, then it drafted |
| Where are the decisions recorded? | `requirements.md`, `design.md` | `aidlc-docs/`, `audit.md`, `team-log.md` |
| Which failing steps did the stakeholder notes fix? | | |

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

## Discuss

::: tip Three questions for your team
1. Which failing step from Chapter 3 did AI-DLC get right, and which sentence in `stakeholder-notes.md` fixed it?
2. Where did you disagree with Kiro, and was that disagreement recorded?
3. Six months from now, which project could a new teammate pick up with confidence?
:::

::: info Source
AWS workshop *Kiro – Getting Started*, Lab 12 Part 3 (the comparison and the timings come from its Sudoku runs).
:::
