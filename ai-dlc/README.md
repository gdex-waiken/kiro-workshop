# Hands-on: build Pelita Ideas with AI-DLC

**Time:** 11:35 AM – 12:35 PM (Feature 1, greenfield) and 12:50 – 1:15 PM (Feature 2, brownfield) · teams of 3–4 · one laptop per team · the full guide with every prompt is on the workshop website, Chapter 6, AI-DLC, and Chapter 7, Brownfield

You build the same Feature 1 as in Part 1 (`spec-driven/`), this time the AI-DLC way, from an empty folder. Kiro leads with the **AI-DLC** workflow: it asks questions in files, plans, and stops at a gate before every stage. You answer, challenge and approve. At the end, your service must reproduce every result in `sample-data/ideas-scenario.csv`.

After the second break you stay in this folder and add Feature 2 (vote and rank) to the code you just built. That's brownfield: see §7.

> **Read this file first.** It takes you from setup to a running workflow.

---

## 1 · Set up (10 minutes, before you type anything at Kiro)

### 1.0 Turn off Kiro Workflows (do this first)

AI-DLC must lead the chat itself. If Kiro's **Workflows** feature is on, Kiro can run your AI-DLC request as its own background workflow and skip AI-DLC's questions and gates.

1. Kiro IDE: **Ctrl + ,** (Cmd + , on macOS) → **User** tab → search `workflows` → **untick Kiro Agent › Workflows: Enabled**.
   Or Command Palette (**Ctrl + Shift + P**) → **Kiro: Disable Workflows**.
2. Command Palette → **Developer: Reload Window**, then start a **new** chat.
3. Kiro CLI: `/settings` → **Features** → **Workflows** off, then restart `kiro-cli`.

It's one setting for the whole computer, not per project. Pictures: workshop website, Chapter 6.1.

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
python check_ideas.py     # "Cannot reach http://127.0.0.1:8000 ... Is the service running?"
```

That message is correct for now: there is no service yet. It proves the checker runs.

### 1.3 Assign roles (write them in `team-log.md`)

| Role | Job |
|---|---|
| **Driver** | Types into Kiro. Never answers a question alone |
| **Product Owner** | Owns the documents, settles conflicts, has the final say at gates |
| **Reviewer** | Opens and reads every artifact before a gate |
| **Scribe** | Keeps `team-log.md` up to date: decisions **and why** |

Swap the Driver at each break.

---

## 2 · Your trigger phrase

Open this `ai-dlc` folder in **Kiro IDE** (or run `kiro-cli chat` here). Start a **new Vibe session** and paste exactly:

```
Using AI-DLC, build the Pelita Ideas service described in ticket.md: Feature 1 (submit and browse ideas) only. Follow vision-document.md, stakeholder-notes.md, technical-environment.md and api-contract.md. The service must pass check_ideas.py. This is a greenfield project.
```

You should get the AI-DLC welcome message, and an `aidlc-docs/` folder appears with `aidlc-state.md` and `audit.md`. Then let the workflow lead.

---

## 3 · What to read, in this order

| # | File | Why |
|---|---|---|
| 1 | `Pelita-Ideas-Proposal.pdf` | The one-page product proposal from Aina Rahman, Head of Innovation. It's the brief you hand to Kiro with `ticket.md`: a document, not a one-line prompt |
| 2 | `ticket.md` | What the innovation team asked for |
| 3 | `vision-document.md` | Why, for whom, what is in and out of scope |
| 4 | `stakeholder-notes.md` | **The real requirements.** People disagree here on purpose |
| 5 | `api-contract.md` | The fixed contract the app team already built against |
| 6 | `technical-environment.md` | Stack, architecture and what is prohibited |
| 7 | `sample-data/` | The staff list, the categories and **the answer keys** your service must reproduce |

Read 1–4 **before** Kiro asks its first question. Not every answer is written down as a fact. Some are in what people said, and some people contradict each other.

---

## 4 · How to work (five rules)

1. **Answer in files, not in chat.** Kiro writes questions to a file with lettered options and an `[Answer]:` tag. Type after the tag, save, then tell Kiro: `I've answered the questions, please proceed`.
2. **Read before you approve.** Every stage ends at a gate (**Request Changes / Continue**). Open the files it points to. A gate you click without reading is a gate you did not use.
3. **Trim the plan.** AI over-builds: ask for an idea list and it may plan login, comments, an admin page, a database and AI tagging. At Workflow Planning and before Code Generation, delete every stage, story or task the ticket didn't ask for, and say why at the gate. For a feature this small, a lean plan is right.
4. **Record the why.** "We chose b" is worth nothing. "We chose b because Siti said never change what someone wrote without telling them" is worth everything.
5. **No vibe coding.** Don't edit files outside the workflow. If you do, tell Kiro what you changed.

---

## 5 · Timeline and checkpoints (Feature 1)

| Time | You should be… | Checkpoint |
|---|---|---|
| 11:35 – 11:45 | Rules installed, roles set, trigger phrase answered | |
| 11:45 – 12:00 | **Requirements Analysis:** question files answered, extension decision recorded, conflicts settled | **CP1 12:00:** every conflict in `stakeholder-notes.md` has a recorded decision |
| 12:00 – 12:15 | **Workflow Planning** challenged, **Application Design** approved | **CP2 12:15:** the plan was argued with, not just clicked |
| 12:15 – 12:35 | **Construction:** code and tests, then `check_ideas.py` | **CP3 12:35:** `check_ideas.py` result on screen |

Behind schedule? Tell the facilitator. You may be given a ready-made `aidlc-docs/` so you can jump to Construction.

---

## 6 · Definition of done (Feature 1)

- `pytest` passes.
- `python check_ideas.py` prints **13/13 steps match the answer key**, with the service running on port 8000.
- Every conflict in `stakeholder-notes.md` has a decision and a reason in `team-log.md`.
- `traceability-worksheet.md` has at least one complete chain (finish it before the wrap-up at 1:15).
- `aidlc-docs/` shows a gate approval for every stage that ran.

---

## 7 · Brownfield: add Feature 2 (12:50 – 1:15)

Now the folder has code in it. You add Feature 2 from `ticket.md` (vote for an idea and see a ranked list) to the service you built for Feature 1, with AI-DLC again.

### 7.1 What changes

| | Feature 1 (greenfield) | Feature 2 (brownfield) |
|---|---|---|
| **Workspace Detection** | Finds an empty folder | **Finds your Feature 1 code** |
| **Reverse Engineering** | Skipped | **Runs:** documents the code that is already there. Read it before you continue: if it gets your code wrong, the Feature 2 plan builds on the mistake |
| **The answer key** | `check_ideas.py`: 13 steps | `check_ideas.py --feature 2`: 14 steps, **and** `check_ideas.py` must still pass |
| **The risk** | Building the wrong thing | Breaking what already works |

### 7.2 Your brownfield trigger phrase

Stay in this `ai-dlc` folder. First rename the finished `aidlc-docs/` folder to `aidlc-docs-feature1/`: that keeps the Feature 1 record, and stops AI-DLC from resuming the old workflow. Then start a **new** session (don't continue the Feature 1 chat) and paste exactly:

```
Using AI-DLC, add Feature 2 from ticket.md (vote for an idea and see a ranked list) to the existing Pelita Ideas service in this folder. Follow stakeholder-notes.md and api-contract.md. The service must pass check_ideas.py --feature 2 and still pass check_ideas.py. This is a brownfield project.
```

### 7.3 What to settle

Read `stakeholder-notes.md` again, this time for voting, and `sample-data/votes-scenario.csv`. The questions below all have an answer in the notes, and some people disagree. Record each decision and why in `team-log.md`.

- What happens when someone taps vote twice?
- Can you vote for your own idea?
- Do some people's votes count more than others?
- When two ideas have the same number of votes, which one ranks first?

Only 25 minutes, so keep the plan lean: Feature 2 is one endpoint to vote and one to rank, nothing else.

### 7.4 Done means (Feature 2)

- `pytest` passes, old tests and new.
- `python check_ideas.py --feature 2` prints **14/14 steps match the answer key**.
- `python check_ideas.py` **still** prints **13/13**.
- Every voting conflict has a decision and a reason in `team-log.md`.

---

## 8 · What you show at the wrap-up at 1:15 (a few minutes per team)

1. Run `check_ideas.py` and `check_ideas.py --feature 2` live.
2. Pick **one result** it checks (for example the `409` at step 3 or the `422` at step 5) and walk it back, out loud: the result → the test → the design → the requirement → your answer in a question file → the sentence a stakeholder said.
3. Say where your chain broke, if it did.

---

## 9 · When you are stuck

| Symptom | Do this |
|---|---|
| No welcome message, no `aidlc-docs/` | The rules are in the wrong folder. Check §1.1, then start a **new** session |
| Kiro says it's starting a **workflow**, or a Workflows panel opens | Kiro Workflows is still on. Turn it off (§1.0), reload the window, start a **new** session |
| Kiro suggests switching to Spec mode | Decline. Stay in Vibe mode: AI-DLC replaces the spec workflow |
| Kiro keeps asking the same thing | Your answer was vague. The follow-up file is the system working. Be more specific |
| Kiro proposes a database, Docker, login or a new endpoint | Reject it at the gate and point to `technical-environment.md` |
| You can't find the answer in the documents | Record an assumption, say it's an assumption, move on. Timebox it to 2 minutes |
| `check_ideas.py` says "Cannot reach" | Start the service: `uvicorn app.main:app --port 8000` |
| `check_ideas.py` fails a step | Read the step's `what_happens` column, then find the stakeholder sentence it depends on |
| Feature 2: Reverse Engineering is skipped | Kiro didn't see your code. Check that you opened this `ai-dlc` folder, the one with `app/` in it, then start a **new** session |
| `check_ideas.py --feature 2` says "Setup failed" | Feature 1 is broken. Make `check_ideas.py` pass first |
| Feature 2 broke a Feature 1 step | Tell Kiro which step of `check_ideas.py` fails and let it fix it inside the workflow |
| Rankings look crowded after many checker runs | Restart the service. Every run adds ideas |
| You're running out of Kiro credits | Stop asking for explanations in chat. Read the files instead |
