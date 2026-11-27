# kiro-workshop: one idea portal, built twice, then extended

Hands-on material for the **Sweetmag AWS Kiro Training** (Wednesday 9 December, 9:30 AM – 1:30 PM GMT+8, 4 hours).

You build the backend for **Lumen Ideas**, the staff idea portal of Velox Group, a fictional logistics company in Malaysia. Staff submit improvement ideas, browse them and, later, vote.

1. **Hands-on 1 · Spec** (`spec-driven/`): the trainer builds a spec live, then your team turns the client's brief into requirements for Feature 1 and hunts for the decisions the ticket never made.
2. **Hands-on 2 · AI-DLC, greenfield** (`ai-dlc/`): Feature 1 (submit and browse ideas) from an empty folder. Kiro asks questions in files and waits at a gate after every stage. The stakeholders don't agree, so your team decides, records why, and proves the result against an answer key.
3. **Hands-on 3 · AI-DLC, brownfield** (same `ai-dlc/` folder): add Feature 2 (vote and rank) to the code you built. AI-DLC reads the existing code first.

At the end each team runs the checker and walks one line of code back to the stakeholder who caused it. Everything runs **locally**: no cloud account, no database, no Docker.

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

Do **Session 0 · Setup** (Mon 7 Dec, 30 minutes online): [`Pre-Workshop-Checklist.md`](Pre-Workshop-Checklist.md), or the Setup page on the website.

## What's in this repo

```
kiro-workshop/
├── Pre-Workshop-Checklist.md   # Session 0: do this before the day
├── AI-DLC-Cheat-Sheet.md       # one-page map: stages, gates, rules
├── site/                       # the workshop website (VitePress)
├── spec-driven/                # Hands-on 1 workspace
│   ├── .kiro/steering/         # product, tech and structure rules
│   ├── Lumen-Ideas-Client-Brief.docx   # the one-page brief you hand to Kiro with ticket.md
│   ├── ticket.md, api-contract.md
│   ├── sample-data/            # staff list, categories + the answer keys
│   └── check_ideas.py          # replays the answer key against your service
├── ai-dlc/                     # Hands-on 2 and 3 workspace
│   ├── README.md               # the AI-DLC guide in one file
│   ├── Lumen-Ideas-Client-Brief.docx   # the same one-page brief
│   ├── ticket.md, vision-document.md, api-contract.md, technical-environment.md
│   ├── stakeholder-notes.md    # what people said (they disagree)
│   ├── sample-data/, check_ideas.py
│   ├── team-log.md             # you fill in: roles, decisions and why
│   └── traceability-worksheet.md
```

## Agenda

| Time | Block |
|---|---|
| Mon 7 Dec | **Session 0 · Setup**, 30 min online: sign in, install, `aidlc doctor` |
| 9:30 – 10:00 | **Meet Kiro:** live demo, IDE and Crew in depth, the building blocks |
| 10:00 – 10:30 | **Hands-on 1 · Spec:** watch it, then plan Feature 1 and hunt for the gaps (`spec-driven/`) |
| 10:30 – 10:40 | **Who asks the questions?** From spec to AI-DLC |
| 10:40 – 10:50 | Break |
| 10:50 – 11:00 | **The scenario:** Lumen Ideas, six stakeholders who don't agree |
| 11:00 – 12:00 | **Hands-on 2 · AI-DLC greenfield:** Feature 1 (`ai-dlc/`), then a checkpoint |
| 12:00 – 12:10 | Break |
| 12:10 – 12:50 | **Hands-on 3 · AI-DLC brownfield:** add Feature 2 to the same code |
| 12:50 – 1:30 | **Show, trace, roll out:** run the checkers, trace one line of code, Q&A |

## The one rule

**Kiro proposes, you approve.** Read before you continue. In AI-DLC, answer in the question files, not in the chat.

## Sources

- AI-DLC: *AI-Driven Development Lifecycle (AI-DLC) Method Definition*, Raja SP, AWS; the `aidlc` command 2.11.x from github.com/awslabs/aidlc-workflows, guide at awslabs.github.io/aidlc-workflows
- Kiro documentation: kiro.dev/docs
- Workshop format inspired by the AI-DLC Workshop kit at github.com/tongzahub/AI-DLC-Workshop
