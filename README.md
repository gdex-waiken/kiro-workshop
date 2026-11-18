# kiro-workshop: AI-DLC with Kiro

Hands-on material for the **Kiro AI-DLC workshop** (1:00 – 5:00 PM, 4 hours).

You build one small **cart API** for a fictional online store, KedaiKu, using the **AI-DLC** methodology in Kiro: Kiro asks questions in files, plans, and waits for your approval at every stage before it builds. The stakeholders do not all agree, so your team decides, records why, and proves the result against an answer key.

Everything runs **locally** on your laptop. No cloud account, no database, no Docker.

## Before the workshop

Do everything in [`Pre-Workshop-Checklist.md`](Pre-Workshop-Checklist.md) at home, on the laptop your team will use.

```bash
git clone https://github.com/gdex-waiken/kiro-workshop.git
cd kiro-workshop
```

## What's in this repo

```
kiro-workshop/
├── Pre-Workshop-Checklist.md   # do this 2–3 days before
├── AI-DLC-Cheat-Sheet.md       # one-page map: stages, gates, rules
├── spec-demo/                  # facilitator's 10-minute Kiro spec demo (you watch)
└── ai-dlc/                     # YOUR WORKSPACE: open Kiro here
    ├── README.md               # step-by-step guide: start here
    ├── ticket.md               # what Product asked for
    ├── vision-document.md      # why, for whom, in and out of scope
    ├── stakeholder-notes.md    # what people said (they disagree)
    ├── api-contract.md         # the fixed API the mobile app expects
    ├── technical-environment.md# stack, architecture, prohibitions
    ├── sample-data/            # product catalog + the answer key
    ├── check_cart.py           # replays the answer key against your service
    ├── team-log.md             # you fill in: roles, decisions and why
    └── traceability-worksheet.md # you fill in: one number traced back to a sentence
```

## Agenda

| Time | What |
|---|---|
| 1:00 – 1:20 | **Why AI-DLC.** Vibe coding, spec-driven development and AI-DLC. Live Kiro spec demo. What multi-agent runs really cost |
| 1:20 – 1:35 | **Set up.** Teams and roles, install the AI-DLC rules, paste the trigger phrase |
| 1:35 – 2:30 | **Inception: requirements.** Answer the question files, settle the stakeholder conflicts. *Checkpoint 1* |
| 2:30 – 2:40 | Break |
| 2:40 – 3:25 | **Inception: plan and design.** Challenge the workflow plan, approve the design. *Checkpoint 2* |
| 3:25 – 4:20 | **Construction.** Code and tests, then `check_cart.py`. *Checkpoint 3* |
| 4:20 – 4:50 | **Demos.** Each team runs the checker and walks one number back to the sentence that caused it |
| 4:50 – 5:00 | **Retro and wrap-up** |

## The one rule

**Kiro proposes, you approve.** Never let it skip a gate, and never answer its questions in chat: answers go in the question files.

## Sources

- AI-DLC workflows: github.com/awslabs/aidlc-workflows (release v1.0.1)
- Kiro documentation: kiro.dev/docs
- User stories adapted from the AWS workshop *Kiro – Getting Started*, Code Challenge (catalog.workshops.aws/q-zero2hero)
- Workshop format inspired by the AI-DLC Workshop kit at github.com/tongzahub/AI-DLC-Workshop
