# 2. The scenario: the KedaiKu cart

**9:50 – 10:05 · Talk.** You'll build the same small cart API twice this morning: first with a spec, then with AI-DLC.

## The ticket

KedaiKu is a fictional online store in Malaysia. Its mobile app team has already built a cart screen against a fixed API. You build the service behind it.

> **As a customer, I want to add items to my shopping cart, so that I can collect items I intend to purchase.**

| Done means | |
|---|---|
| Add an item | with a specified quantity |
| Item count | updated each time |
| Item details | product name, price, quantity |
| Subtotal | calculated for you |

Feature 2, removing items, is a stretch goal: only once Feature 1 works.

## The files you'll use

| File | In `spec-driven/` | In `ai-dlc/` | What it is |
|---|:---:|:---:|---|
| `ticket.md` | ✓ | ✓ | What Product asked for |
| `api-contract.md` | ✓ | ✓ | The fixed API: paths, fields, status codes |
| `sample-data/` | ✓ | ✓ | The product catalog and **the answer key** |
| `check_cart.py` | ✓ | ✓ | Replays the answer key against your service |
| `.kiro/steering/` | ✓ | | Product, tech and structure rules for spec mode |
| `vision-document.md` | | ✓ | Why, for whom, in and out of scope |
| `stakeholder-notes.md` | | ✓ | What people said. **They disagree** |
| `technical-environment.md` | | ✓ | Stack, architecture and what is prohibited |
| `team-log.md`, `traceability-worksheet.md` | | ✓ | You fill these in |

::: warning Spec mode gets less, on purpose
The `spec-driven/` folder has no stakeholder notes. Spec mode builds from what you give it. In Chapter 4, AI-DLC builds the same cart and asks the questions the spec never asked.
:::

## The rules Kiro must follow

| Rule | Detail |
|---|---|
| Language | Python 3.12 |
| HTTP | FastAPI, served locally by uvicorn on port **8000** |
| Architecture | Clean Architecture: `domain` → `application` → `adapters` |
| Tests | pytest, test first: red, green, refactor |
| Money | `decimal.Decimal` in code, strings with 2 decimals in JSON (`"12.90"`) |
| Storage | In memory, behind a repository interface |
| Prohibited | Database, Docker, cloud deployment, login |

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
User stories adapted from the AWS workshop *Kiro – Getting Started*, Code Challenge. Permission rules: AWS workshop Labs 10 and 15. KedaiKu is fictional.
:::
