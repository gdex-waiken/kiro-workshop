# Hands-on: build the KedaiKu cart with AI-DLC

**Time:** 2:50 – 3:50 PM · teams of 3–4 · one laptop per team · the full guide with every prompt is on the workshop website, Chapter 4

You build the same cart API as in Part 1 (`spec-driven/`), this time the AI-DLC way. Kiro leads with the **AI-DLC** workflow: it asks questions in files, plans, and stops at a gate before every stage. You answer, challenge and approve. At the end, your service must reproduce the numbers in `sample-data/cart-scenario.csv`.

> **Read this file first.** It takes you from setup to a running workflow.

---

## 1 · Set up (15 minutes, before you type anything at Kiro)

### 1.1 Install the AI-DLC rules (v1.0.1) into this folder

**Git Bash, macOS or Linux:**

```bash
cd ai-dlc
curl -fsSL -o ai-dlc-rules-v1.0.1.zip https://github.com/awslabs/aidlc-workflows/releases/download/v1.0.1/ai-dlc-rules-v1.0.1.zip
unzip ai-dlc-rules-v1.0.1.zip
mkdir -p .kiro/steering
cp -R aidlc-rules/aws-aidlc-rules .kiro/steering/
cp -R aidlc-rules/aws-aidlc-rule-details .kiro/
rm -rf ai-dlc-rules-v1.0.1.zip aidlc-rules
```

**Windows PowerShell:**

```powershell
cd ai-dlc
Invoke-WebRequest -Uri https://github.com/awslabs/aidlc-workflows/releases/download/v1.0.1/ai-dlc-rules-v1.0.1.zip -OutFile ai-dlc-rules-v1.0.1.zip
Expand-Archive ai-dlc-rules-v1.0.1.zip -DestinationPath .
New-Item -ItemType Directory -Force .kiro\steering | Out-Null
Copy-Item -Recurse aidlc-rules\aws-aidlc-rules .kiro\steering\
Copy-Item -Recurse aidlc-rules\aws-aidlc-rule-details .kiro\
Remove-Item -Recurse -Force ai-dlc-rules-v1.0.1.zip, aidlc-rules
```

You should now have `.kiro/steering/aws-aidlc-rules/` and `.kiro/aws-aidlc-rule-details/`.

### 1.2 Check your toolchain

```bash
python --version          # Python 3.12.x
python check_cart.py      # "Cannot reach http://localhost:8000 ... Is the service running?"
```

That message is correct for now: there is no service yet. It proves the checker runs.

### 1.3 Assign roles (write them in `team-log.md`)

| Role | Job |
|---|---|
| **Driver** | Types into Kiro. Never answers a question alone |
| **Product Owner** | Owns the documents, settles conflicts, has the final say at gates |
| **Reviewer** | Opens and reads every artifact before a gate |
| **Scribe** | Keeps `team-log.md` up to date: decisions **and why** |

Swap the Driver at the break.

---

## 2 · Your trigger phrase

Open this `ai-dlc` folder in **Kiro IDE** (or run `kiro-cli chat` here). Start a **new Vibe session** and paste exactly:

```
Using AI-DLC, build the KedaiKu cart service described in ticket.md: Feature 1 (add items to cart and view the cart) only. Follow vision-document.md, stakeholder-notes.md, technical-environment.md and api-contract.md. The service must pass check_cart.py. This is a greenfield project.
```

You should get the AI-DLC welcome message, and an `aidlc-docs/` folder appears with `aidlc-state.md` and `audit.md`. Then let the workflow lead.

---

## 3 · What to read, in this order

| # | File | Why |
|---|---|---|
| 1 | `ticket.md` | What the Product team asked for |
| 2 | `vision-document.md` | Why, for whom, what is in and out of scope |
| 3 | `stakeholder-notes.md` | **The real requirements.** People disagree here on purpose |
| 4 | `api-contract.md` | The fixed contract the app team already built against |
| 5 | `technical-environment.md` | Stack, architecture and what is prohibited |
| 6 | `sample-data/` | The product catalog and **the answer key** your service must reproduce |

Read 1–3 **before** Kiro asks its first question. Not every answer is written down as a fact. Some are in what people said, and some people contradict each other.

---

## 4 · How to work (five rules)

1. **Answer in files, not in chat.** Kiro writes questions to a file with lettered options and an `[Answer]:` tag. Type after the tag, save, then tell Kiro: `I've answered the questions, please proceed`.
2. **Read before you approve.** Every stage ends at a gate (**Request Changes / Continue**). Open the files it points to. A gate you click without reading is a gate you did not use.
3. **Trim the plan.** AI over-builds: ask for a cart and it may plan a whole shop (login, checkout, database, admin pages). At Workflow Planning and before Code Generation, delete every stage, story or task the ticket didn't ask for, and say why at the gate. For a feature this small, a lean plan is right.
4. **Record the why.** "We chose b" is worth nothing. "We chose b because Siti said customers must never have their quantity changed silently" is worth everything.
5. **No vibe coding.** Don't edit files outside the workflow. If you do, tell Kiro what you changed.

---

## 5 · Timeline and checkpoints

| Time | You should be… | Checkpoint |
|---|---|---|
| 2:50 – 3:00 | Rules installed, roles set, trigger phrase answered | |
| 3:00 – 3:15 | **Requirements Analysis:** question files answered, extension decision recorded, conflicts settled | **CP1 3:15:** every conflict in `stakeholder-notes.md` has a recorded decision |
| 3:15 – 3:30 | **Workflow Planning** challenged, **Application Design** approved | **CP2 3:30:** the plan was argued with, not just clicked |
| 3:30 – 3:50 | **Construction:** code and tests, then `check_cart.py` | **CP3 3:50:** `check_cart.py` result on screen |

Behind schedule? Tell the facilitator. You may be given a ready-made `aidlc-docs/` so you can jump to Construction.

---

## 6 · Definition of done

- `pytest` passes.
- `python check_cart.py` prints **15/15 steps match the answer key**, with the service running on port 8000.
- Every conflict in `stakeholder-notes.md` has a decision and a reason in `team-log.md`.
- `traceability-worksheet.md` has at least one complete chain.
- `aidlc-docs/` shows a gate approval for every stage that ran.

---

## 7 · What you show in the comparison at 4:05 (a few minutes per team)

1. Run `check_cart.py` live.
2. Pick **one number** it checks (for example `54.00` or `16`) and walk it back, out loud: the number → the test → the design → the requirement → your answer in a question file → the sentence a stakeholder said.
3. Say where your chain broke, if it did.

---

## 8 · When you are stuck

| Symptom | Do this |
|---|---|
| No welcome message, no `aidlc-docs/` | The rules are in the wrong folder. Check §1.1, then start a **new** session |
| Kiro suggests switching to Spec mode | Decline. Stay in Vibe mode: AI-DLC replaces the spec workflow |
| Kiro keeps asking the same thing | Your answer was vague. The follow-up file is the system working. Be more specific |
| Kiro proposes a database, Docker, login or a new endpoint | Reject it at the gate and point to `technical-environment.md` |
| You can't find the answer in the documents | Record an assumption, say it's an assumption, move on. Timebox it to 2 minutes |
| `check_cart.py` says "Cannot reach" | Start the service: `uvicorn app.main:app --port 8000` |
| `check_cart.py` fails a step | Read the step's `what_happens` column, then find the stakeholder sentence it depends on |
| You're running out of Kiro credits | Stop asking for explanations in chat. Read the files instead |
