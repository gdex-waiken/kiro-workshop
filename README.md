# kiro-workshop: one idea portal, built twice, then extended

Hands-on material for the **Sweetmag AWS Kiro Training** (Wednesday 9 December, 9:30 AM – 1:30 PM GMT+8, 4 hours).

You build the backend for **Pelita Ideas**, the staff idea portal of Pelita Group, a fictional logistics company in Malaysia. Staff submit improvement ideas, browse them and, later, vote. You build it in three steps:

1. **Part 1, spec-driven development** (`spec-driven/`): Feature 1 (submit and browse ideas). Kiro writes requirements, design and tasks; you approve each one; then it builds.
2. **Part 2, AI-DLC, greenfield** (`ai-dlc/`): Feature 1 again, from an empty folder. Kiro asks questions in files, plans, and waits for your approval at every stage. The stakeholders don't all agree, so your team decides, records why, and proves the result against an answer key.
3. **Part 3, AI-DLC, brownfield** (same `ai-dlc/` folder): add Feature 2 (vote and rank) to the code you built in Part 2. This time AI-DLC finds existing code and documents it first.

At the wrap-up, each team runs the checker and walks one decision back to the stakeholder who caused it. Everything runs **locally** on your laptop: no cloud account, no database, no Docker.

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

Do everything in [`Pre-Workshop-Checklist.md`](Pre-Workshop-Checklist.md) at home, on the laptop your team will use. The website has the same list in Chapter 0, Before you start.

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
│   ├── Pelita-Ideas-Proposal.pdf   # the one-page brief you hand to Kiro with ticket.md
│   ├── ticket.md, api-contract.md
│   ├── sample-data/            # staff list, categories + the answer keys
│   └── check_ideas.py          # replays the answer key against your service
├── ai-dlc/                     # PARTS 2 and 3 workspace: open Kiro here after the first break
│   ├── README.md               # the AI-DLC guide in one file
│   ├── Pelita-Ideas-Proposal.pdf   # the same one-page brief
│   ├── ticket.md, vision-document.md, api-contract.md, technical-environment.md
│   ├── stakeholder-notes.md    # what people said (they disagree)
│   ├── sample-data/, check_ideas.py
│   ├── team-log.md             # you fill in: roles, decisions and why
│   └── traceability-worksheet.md
└── spec-demo/                  # a finished, lean reference spec for the facilitator demo
```

## Agenda

| Time | Chapter |
|---|---|
| 9:30 – 9:50 | **1 · Meet Kiro:** IDE, CLI, Web, Mobile and Crew, and a live demo of the spec workflow (`spec-demo/`) |
| 9:50 – 10:00 | **2 · Extend Kiro:** MCP, skills, powers |
| 10:00 – 10:10 | **3 · Compare:** vibe vs spec vs AI-DLC |
| 10:10 – 10:20 | **4 · The scenario:** Pelita Ideas, the rules, teams and roles |
| 10:20 – 11:20 | **5 · Spec-driven development** (hands-on core 1: Feature 1 in `spec-driven/`) |
| 11:20 – 11:35 | Break |
| 11:35 – 12:35 | **6 · AI-DLC** (hands-on core 2: Feature 1 again in `ai-dlc/`, greenfield) |
| 12:35 – 12:50 | Break |
| 12:50 – 1:15 | **7 · Brownfield** (hands-on core 3: add Feature 2, vote and rank, to the AI-DLC code with AI-DLC) |
| 1:15 – 1:30 | **8 · Wrap-up and Q&A:** each team runs the checker and walks one traceability chain out loud |

## The one rule

**Kiro proposes, you approve.** Read before you continue, and in AI-DLC, answer in the question files, never in chat.

## Sources

- AI-DLC: *AI-Driven Development Lifecycle (AI-DLC) Method Definition*, Raja SP, AWS; rules from github.com/awslabs/aidlc-workflows (release v1.0.1)
- Kiro documentation: kiro.dev/docs
- Workshop format inspired by the AI-DLC Workshop kit at github.com/tongzahub/AI-DLC-Workshop
