# kiro-workshop: one cart, built twice

Hands-on material for the **Kiro developer workshop** (1:00 – 5:00 PM, 4 hours).

You build one small **cart API** for a fictional online store, KedaiKu, twice:

1. **Part 1, spec-driven development** (`spec-driven/`): Kiro writes requirements, design and tasks; you approve each one; then it builds.
2. **Part 2, AI-DLC** (`ai-dlc/`): Kiro asks questions in files, plans, and waits for your approval at every stage. The stakeholders don't all agree, so your team decides, records why, and proves the result against an answer key.

Then you compare the two results. Everything runs **locally** on your laptop: no cloud account, no database, no Docker.

## The workshop website

The step-by-step guide, chapter by chapter with every prompt ready to copy, is a small website in [`site/`](site/).

```bash
cd site
npm install
npm run dev        # http://localhost:5173
npm run build      # static site in site/.vitepress/dist
```

To host it on Vercel, import this repo and set the **Root Directory** to `site`. The settings are in `site/vercel.json`.

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
├── site/                       # the workshop website (VitePress)
├── spec-driven/                # PART 1 workspace: open Kiro here first
│   ├── .kiro/steering/         # product, tech and structure rules
│   ├── ticket.md, api-contract.md
│   ├── sample-data/            # catalog + the answer key
│   └── check_cart.py           # replays the answer key against your service
├── ai-dlc/                     # PART 2 workspace: open Kiro here after the break
│   ├── README.md               # the AI-DLC guide in one file
│   ├── ticket.md, vision-document.md, api-contract.md, technical-environment.md
│   ├── stakeholder-notes.md    # what people said (they disagree)
│   ├── sample-data/, check_cart.py
│   ├── team-log.md             # you fill in: roles, decisions and why
│   └── traceability-worksheet.md
└── spec-demo/                  # a finished, lean reference spec for the facilitator
```

## Agenda

| Time | Chapter |
|---|---|
| 1:00 – 1:20 | **1 · Meet Kiro:** IDE, CLI, Web, Mobile and Crew, and which one to use when |
| 1:20 – 1:35 | **2 · The scenario:** the KedaiKu ticket, the rules, teams and roles |
| 1:35 – 2:35 | **3 · Spec-driven development** (hands-on, `spec-driven/`) |
| 2:35 – 2:50 | Break |
| 2:50 – 3:50 | **4 · AI-DLC** (hands-on, `ai-dlc/`) |
| 3:50 – 4:05 | Break |
| 4:05 – 4:25 | **5 · Which way to build?** Compare the two results |
| 4:25 – 4:45 | **6 · Extend Kiro:** MCP, skills, powers, and what agents really cost |
| 4:45 – 5:00 | **7 · Wrap-up:** governance, retro and next steps |

## The one rule

**Kiro proposes, you approve.** Read before you continue, and in AI-DLC, answer in the question files, never in chat.

## Sources

- AI-DLC: *AI-Driven Development Lifecycle (AI-DLC) Method Definition*, Raja SP, AWS; rules from github.com/awslabs/aidlc-workflows (release v1.0.1)
- Kiro documentation: kiro.dev/docs
- User stories adapted from the AWS workshop *Kiro – Getting Started*, Code Challenge (catalog.workshops.aws/q-zero2hero)
- Workshop format inspired by the AI-DLC Workshop kit at github.com/tongzahub/AI-DLC-Workshop
