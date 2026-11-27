# 5. The stakeholders: who decides?

**10:50 – 11:00 · Talk.** You met the project at 10:00: the client's brief, the ticket, the contract. Now you meet the six people behind it, and they don't agree. You'll build Feature 1 with AI-DLC, then add Feature 2 to that code.

## The company and the problem

Velox Group is a fictional logistics company in Malaysia. It asks staff for improvement ideas, but they arrive by email, in WhatsApp groups and in corridor chats. Three things go wrong:

1. **Ideas get lost.** Nobody can see what was already suggested.
2. **The same idea arrives again and again.** "Reusable parcel bags" came in five times last quarter.
3. **Nobody knows why an idea was picked.** Staff want to see which ideas their colleagues back.

The app team has already designed the portal screens against a fixed API. You build the service behind it: **Lumen Ideas**.

## The brief from Product

Aina Rahman, Head of Innovation, sent the client's brief: **`Lumen-Ideas-Client-Brief.docx`**, in both workshop folders. You met it at 10:00 when it became `product.md`. It covers business needs only: the problems, who uses the portal, the scope, what's out, and who to talk to.

::: tip Hand Kiro documents, not a one-line prompt
On a real project nobody gets a one-sentence request. You get a client brief, a ticket, a contract and some standards. Today you work the same way: point Kiro at the documents and let it read them. The better the documents, the less Kiro has to guess.
:::

The brief ends with a warning worth reading twice: questions on **title length, duplicates, anonymous ideas and voting rules** are still being discussed with Design, People and Culture, Operations and Finance.

## The ticket

The ticket is short on purpose. Two features, built one at a time.

| Feature | What it does | When |
|---|---|---|
| **1 · Submit and browse ideas** | A staff member submits an idea with a title, a short description and a category. The portal lists every idea, newest first, with who submitted it and their department. Anyone can open one idea and see all its details | Chapter 3 (spec, requirements only) and Chapter 6 (AI-DLC, greenfield) |
| **2 · Vote and rank** | A staff member votes for an idea. Each idea shows its vote count. The portal shows a ranked list, most votes first | Chapter 7 (brownfield: added to the code you already have) |

## The files you'll use

| File | In `spec-driven/` | In `ai-dlc/` | What it is |
|---|:---:|:---:|---|
| `Lumen-Ideas-Client-Brief.docx` | ✓ | ✓ | **The brief from Product:** scope, constraints, done means |
| `ticket.md` | ✓ | ✓ | The two features and their acceptance criteria |
| `api-contract.md` | ✓ | ✓ | The fixed API: paths, fields, status codes |
| `sample-data/` | ✓ | ✓ | `staff.csv`, `categories.csv` and **the answer keys** (`ideas-scenario.csv`, `votes-scenario.csv`) |
| `check_ideas.py` | ✓ | ✓ | Replays the answer key against your service |
| `technical-environment.md` | ✓ | ✓ | Stack, architecture and what is prohibited |
| `.kiro/steering/` | ✓ | | Product, tech and structure rules for spec mode |
| `vision-document.md` | | ✓ | Why, for whom, in and out of scope |
| `stakeholder-notes.md` | | ✓ | What people said. **They disagree** |
| `team-log.md`, `traceability-worksheet.md` | | ✓ | You fill these in |

::: warning Spec mode gets less, on purpose
The `spec-driven/` folder has no stakeholder notes. Spec mode builds from what you give it, which is why your requirements in Chapter 3 had gaps. In Chapter 6, AI-DLC builds the same feature and asks the questions the spec never asked.
:::

## How you'll know it works

```bash
python -m uvicorn app.main:app --port 8000      # terminal 1: your service
python check_ideas.py                 # terminal 2: Feature 1, 13 steps
python check_ideas.py --feature 2     # Feature 2, 14 steps (Chapter 7)
```

The checker replays every step of the answer key against your running service and compares the status code, the idea count, the order and the vote count. A perfect run ends with **13/13 steps match the answer key** (or **14/14** for Feature 2).

## The rules Kiro must follow

| Rule | Detail |
|---|---|
| Language | Python 3.12 |
| HTTP | FastAPI, served locally by uvicorn on port **8000** |
| Architecture | Clean Architecture: `domain` → `application` → `adapters` |
| Tests | pytest, test first: red, green, refactor |
| Time | `submitted_at` is UTC, ISO 8601, ending in `Z` (`"2026-12-09T03:31:07Z"`) |
| Reference data | Names and departments come from `staff.csv`, never from the client. Categories come from `categories.csv` |
| Storage | In memory, behind a repository interface |
| Prohibited | Database, Docker, cloud deployment, login, calls to outside services (AI models included) |

## Safe from day one

Two layers decide what Kiro can do on your machine and in your accounts.

| Layer | Decides | How |
|---|---|---|
| **What Kiro may run** | Which commands and file writes need your approval | Permission rules: **deny > ask > allow**. A deny always wins |
| **What credentials can reach** | Which accounts and systems Kiro can touch | Kiro inherits the credentials on your machine. IAM sets the real limit |

```yaml
# ~/.kiro/settings/permissions.yaml (an example)
rules:
  - capability: shell
    effect: deny
    match: ["rm -rf *", "sudo *"]
  - capability: fs_write
    effect: deny
    match: ["**/*.env", "**/*.pem"]
```

::: danger Trust-all mode
`--trust-all-tools` skips every approval. Use it only in a throwaway sandbox, never on a machine with real data or credentials.
:::

## Teams and roles

Teams of 3–4, one laptop per team. Swap the Driver at each break.

| Role | Job |
|---|---|
| **Driver** | Types into Kiro. Never answers a question alone |
| **Product Owner** | Owns the documents, settles conflicts, has the final say |
| **Reviewer** | Opens and reads every file before you approve |
| **Scribe** | Writes down decisions **and why** |

::: info Sources
Permission rules: AWS workshop *Kiro – Getting Started*, Labs 10 and 15. Velox Group and everyone in it are fictional.
:::
