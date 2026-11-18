# 3. What agents really cost

A real run, used here as a **bad-practice** example.

## The experiment

A multi-agent task runner, driving Claude Opus, built the same small cart API you'll build today. It broke the work into a task board, with an agent for each task and a reviewer agent after each one.

| | |
|---|---|
| Tasks on the board | 18, all passed |
| Time | 40 minutes 43 seconds |
| Separate agent sessions | **37** (19 workers + 18 reviewers) |
| Context tokens re-read | **about 11.2 million** |
| Tokens actually written (code, answers) | about 139 thousand, **about 1%** |
| Result | Most of a team plan's usage allowance, gone |

## Where the tokens went

| Role | Sessions | Context tokens | Written |
|---|---|---|---|
| Workers (do the task) | 19 | about 8.3 million | about 117 thousand |
| Reviewers (check the task) | 18 | **about 4.8 million** | about 22 thousand |

Every reviewer was a full session with about 40,000 tokens of setup. It ran a few commands and replied with one line: `{"ok": true}`. Reviewers used about 37% of all the context for 16% of the output.

## Why it cost so much

1. **Every task is a new session**, and each one reloads 35–80 thousand tokens of instructions, tools and specs before writing anything.
2. **Every step inside a session re-reads the whole context.**
3. **A reviewer agent after every task** doubled the number of sessions.
4. **The work was cut too fine.** The spec had 9 tasks; the board ran 18, because writing the spec and marking it done became agent tasks too.
5. **Personal settings rode along.** Every installed plugin and global rule was loaded in all 37 sessions.

## Spend tokens on purpose

| Bad practice | Better practice |
|---|---|
| 18 tiny tasks, each a new agent | 4 to 6 meaningful tasks |
| A reviewer agent after every task | One review at the end, by you |
| The top model for everything | Top model to plan, a cheaper one to execute |
| Every plugin and global rule loaded | Only what this project needs |
| Only `tech.md` as steering | `product.md`, `tech.md`, `structure.md`, kept short |
| Asking Kiro to explain in chat | Reading the files it wrote |
| One endless chat | Short, focused sessions |

## Does Kiro have the same problem?

Partly. The rule is the same everywhere: **every request re-sends its context, so more agents, tasks and turns cost more.** Kiro bills in credits per request, so the number of tasks and turns is what you watch. What helps in Kiro: you start tasks yourself, there's no hidden reviewer per task, and you can pick a smaller model for simple work.
