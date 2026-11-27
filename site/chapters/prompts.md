# Every prompt, in order

Every message you type today, in the order you type it. Each one was run in a reference build of this exercise with `aidlc` 2.11.4: Feature 1 passed 13/13 and Feature 2 passed 14/14.

## Session 0 · Setup

| # | Where | Type |
|---|---|---|
| S1 | Kiro chat | `Write a haiku about good ideas.` |
| S2 | Kiro chat, folder `spec-driven` | `In two sentences, what is this workspace about, and which steering files have you loaded?` |

## Hands-on 1 · Spec (folder `spec-driven`)

Kiro panel → **Specs** → **Create New Spec**, then:

```text
Build the Lumen Ideas service described in ticket.md and api-contract.md. Feature 1 only: submit an idea, list every idea newest first, and open one idea. Submitter names and departments come from sample-data/staff.csv, and categories from sample-data/categories.csv. The service must pass check_ideas.py. Keep it an MVP: at most 5 tasks, no optional tasks.
```

Optional, to ask for a change:

```text
Update requirements.md: remove anything not in ticket.md or api-contract.md, and add acceptance criteria for a blank title (422), a category that is not in categories.csv (422), a staff ID that is not in staff.csv (422) and an unknown idea id (404). Keep the EARS format.
```

## Hands-on 2 · AI-DLC, Feature 1 (folder `ai-dlc`)

First: Workflows off, `aidlc config --harness kiro --yes`, `aidlc doctor`, **Developer: Reload Window** ([6.1](./06-ai-dlc/1-set-up)). Then new chat → agent picker → **aidlc**.

| # | When | Type |
|---|---|---|
| 1 | Start | *(the message below)* |
| 2 | Answers saved in the question file | `done` |
| 3 | Gate: requirements | `Approve` |
| – | Gate: code plan, if you want to trim it | `Request changes: <what to remove> because <the ticket or rule it breaks>. The rest of the plan is fine.` |
| 4 | Gate: code plan | `Approve Plan` |
| 5 | Gate: Code Generation | `Approve` |
| 6 | Gate: Build and Test, after you ran the checker | `Approve` |

Message 1:

```text
/aidlc express --plan-approval on --skip deployment-pipeline,deployment-execution,observability-setup Build the Lumen Ideas service described in ticket.md: Feature 1 (submit and browse ideas) only. Follow vision-document.md, stakeholder-notes.md, technical-environment.md and api-contract.md, and build test-first. The service must pass check_ideas.py. This is a greenfield project. We will answer your questions by editing the question files.
```

Checking it yourselves (two terminals):

```bash
python -m uvicorn app.main:app --port 8000
python check_ideas.py
```

## Hands-on 3 · AI-DLC, Feature 2 (same folder)

Stop your service. New chat → agent picker → **aidlc**.

| # | When | Type |
|---|---|---|
| 1 | Start | *(the message below)* |
| 2 | Gate: Reverse Engineering | `Approve` |
| 3 | Answers saved in the question file | `done` (if Kiro asks how you'll answer: `2. The answers are in the file, done.`) |
| 4 | Gate: requirements | `Approve` |
| 5 | Gate: code plan | `Approve Plan` |
| 6 | Gate: Code Generation | `Approve` |
| 7 | Gate: Build and Test, after you ran both checkers | `Approve` |

Message 1:

```text
/aidlc express --plan-approval on --project-type brownfield --skip deployment-pipeline,deployment-execution,observability-setup Add Feature 2 from ticket.md (vote for an idea and see a ranked list) to the existing Lumen Ideas service in this folder. Follow stakeholder-notes.md, technical-environment.md and api-contract.md, and build test-first. The service must pass check_ideas.py --feature 2 and still pass check_ideas.py. We will answer your questions by editing the question files.
```

```bash
python -m uvicorn app.main:app --port 8000
python check_ideas.py --feature 2
python check_ideas.py
```

## Any time

| You want to | Type |
|---|---|
| Ask for a change at any gate | `Request changes: <what> because <why>.` |
| Fix a failing checker step | `check_ideas.py fails step <n> (<what_happens>): <paste the problem lines>. Find the requirement and the stakeholder decision behind this step, then fix the code with a failing test first.` |
| Trace a result | `Trace step <n> of sample-data/ideas-scenario.csv back through the tests, the code and the requirements in this workflow's record to the stakeholder sentence it depends on. Quote each file and line.` |
| See where you are | `/aidlc --status` |
| Stop, then carry on in a new chat | `/aidlc park`, new chat, pick **aidlc**, `/aidlc --resume` |

::: warning Words to keep out of an `/aidlc` request
`workshop`, `lab`, `training`, `fix`, `bug`, `prototype` and `spike` make AI-DLC pick a different, longer or shorter workflow. The messages above avoid them on purpose.
:::
