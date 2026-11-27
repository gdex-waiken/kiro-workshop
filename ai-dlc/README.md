# Hands-on 2 and 3: build Lumen Ideas with AI-DLC

**Time:** 11:00 – 11:50 AM (Feature 1, greenfield) and 12:10 – 12:50 PM (Feature 2, brownfield) · teams of 3–4 · one laptop per team · Kiro IDE

Kiro leads with AI-DLC: it reads these documents, asks what they don't settle in a question file, and stops at a gate after every stage. You answer, trim and approve. Your service must reproduce every result in `sample-data/ideas-scenario.csv` (Feature 1) and `votes-scenario.csv` (Feature 2).

Step-by-step guide, with every prompt: the workshop website, **Chapter 6** and **Chapter 7**, and the **Prompts** page.

## At 11:00, before the first message

1. Turn off Kiro **Workflows**: Settings → `@id:kiroAgent.workflows.enabled` → untick (or Command Palette → **Kiro: Disable Workflows**).
2. Open this folder in Kiro, trust it, and in its terminal:

```bash
aidlc config --harness kiro --yes
aidlc doctor
```

3. **Developer: Reload Window**, new chat, agent picker → **aidlc**.

## What's in this folder

| File | What it is |
|---|---|
| `Lumen-Ideas-Client-Brief.docx` | The client's brief from Aina Rahman, Head of Innovation: business needs only |
| `ticket.md` | The two features and their acceptance criteria |
| `vision-document.md` | Why, for whom, in and out of scope |
| `stakeholder-notes.md` | What people said. **They disagree.** Read it as a team on the day |
| `api-contract.md` | The fixed API: paths, fields, status codes |
| `technical-environment.md` | Stack, architecture and what is prohibited. A copy sits in `aidlc/spaces/default/knowledge/aidlc-shared/` so AI-DLC reads it at every stage |
| `sample-data/` | Staff list, categories and the answer keys |
| `check_ideas.py` | Replays the answer key against your running service |
| `team-log.md` | Your Scribe fills it in: roles, decisions, reasons, gates |
| `traceability-worksheet.md` | Walk one result back to a stakeholder sentence |

## The first message (Feature 1)

New chat → agent **aidlc** →

```text
/aidlc express --plan-approval on --skip deployment-pipeline,deployment-execution,observability-setup Build the Lumen Ideas service described in ticket.md: Feature 1 (submit and browse ideas) only. Follow vision-document.md, stakeholder-notes.md, technical-environment.md and api-contract.md, and build test-first. The service must pass check_ideas.py. This is a greenfield project. We will answer your questions by editing the question files.
```

## Check it

```bash
python -m uvicorn app.main:app --port 8000   # terminal 1
python check_ideas.py                        # terminal 2: 13/13
python check_ideas.py --feature 2            # after Feature 2: 14/14
```

## The one rule

**Kiro proposes, you approve.** Read before you approve. Answer in the question file, not in the chat.
