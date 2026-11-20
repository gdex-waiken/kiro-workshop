# 1. Meet Kiro

**1:00 – 1:20 · Talk and demo.** By the end of this chapter you know which Kiro to open for which job.

<img src="/images/kiro-ghost.png" alt="The Kiro ghost" class="mascot-float" />

## One agent, every surface

Kiro is an AI teammate from AWS that plans, writes, tests and fixes software. One agent runs behind every surface, and your `.kiro/` folder (steering, specs, skills, hooks, MCP servers) works in all of them.

> "Start a spec in the IDE, continue it from the CLI, hand off implementation to the Web agent." — kiro.dev/docs

<div class="surface-row">
  <figure><img src="/images/icon-ide.png" alt="Kiro IDE" /><figcaption>IDE</figcaption></figure>
  <figure><img src="/images/icon-cli.png" alt="Kiro CLI" /><figcaption>CLI</figcaption></figure>
  <figure><img src="/images/icon-web.png" alt="Kiro Web" /><figcaption>Web</figcaption></figure>
  <figure><img src="/images/icon-mobile.png" alt="Kiro Mobile" /><figcaption>Mobile</figcaption></figure>
  <figure><img src="/images/icon-crew.png" alt="Kiro Crew" /><figcaption>Crew</figcaption></figure>
</div>

## Kiro IDE: build and review at your desk

A desktop editor built on a VS Code foundation. It's where you'll work today.

![Kiro IDE](/images/kiro-ide.png){.shot}

- **Specs:** requirements, design and tasks, reviewed in the editor.
- **Chat** with full project context, plus built-in agents: Spec, Plan, Bug Fix and Quick Spec.
- **Hooks, steering, skills and MCP servers** in the Kiro panel.

## Kiro CLI: the agent in your terminal

The same agent, in your terminal. Use it over SSH, in scripts, or as a headless step in a CI/CD pipeline.

![Kiro CLI V3 asking to trust a workspace](/images/kiro-cli-v3.png){.shot}

```bash
curl -fsSL https://cli.kiro.dev/install | bash
kiro-cli
```

The first time you start it in a folder, Kiro asks whether to trust the workspace. Trust only folders you mean Kiro to work in.

## Kiro Web: hand over a task, get a pull request back

A browser agent at **app.kiro.dev**. Every task runs in its own isolated sandbox, and Kiro never merges on its own: you review the pull request.

![Kiro Web](/images/kiro-web.png){.shot}

| Mode | Use it for |
|---|---|
| **Default** | Chat and build together |
| **Spec** | Plan before it builds |
| **Autonomous** | A clear feature, a reproducible bug, tests for existing code: Kiro plans, builds with sub-agents and opens the PR |

You can also start work from GitHub: add the `kiro` label to an issue, or comment `/kiro`. Kiro Web needs a Pro plan or higher.

## Kiro Mobile

Check on tasks, review pull requests and chat with your agent on the go.

![Kiro Mobile](/images/kiro-mobile.png){.shot .narrow}

## Kiro Crew: a workspace that keeps working

IDE, CLI and Web handle one session while you drive. **Crew carries the work across sessions**: it remembers, runs on a schedule, and keeps working when no chat is open. It's open source (Apache 2.0), runs on the Kiro CLI and reads your `.kiro/` setup.

![Kiro Crew](/images/kiro-crew.png){.shot}

| Crew can | How |
|---|---|
| Work in parallel | Sessions and subagents that report back |
| Run on a schedule | Cron jobs and heartbeats that watch PRs and pipelines |
| Remember | Teach a rule once; every future session applies it |
| Be reached | Dashboard, Slack, Telegram, Discord, Teams |

### Many agents, one workspace

| Level | What it is |
|---|---|
| **Subagents** | Parallel helpers inside one chat. Each has its own session and context, then reports back |
| **Crew agents** | Specialists with their own prompt, model and tools. No memory of their own |
| **Bots** | Persistent, named agents with their own thread, memory, workspace and goals |
| **Apps** | Packages that add agents, skills, MCP servers and schedules in one install |

A **bot** is a conductor: it does short tasks itself, briefs **workers** for long ones, and asks you before it changes its model, permissions or goals. It works towards a goal, with milestones you approve and regular check-ins.

![A Kiro Crew bot driving three specialist sessions](/images/kiro-crew-bot.png){.shot}

*The "CEO Boss" bot drives AWS Cloud Architect, Data Engineer and DevOps/IaC sessions.*

## Which one, when?

| You want to… | Open |
|---|---|
| Code and review at your desk | **Kiro IDE** |
| Work in the terminal, over SSH, or in a CI pipeline | **Kiro CLI** |
| Say "come back with a pull request" | **Kiro Web**, autonomous mode |
| Keep something watched and reported on for days | **Kiro Crew** |

::: tip Try it
Open Kiro IDE and ask the chat:

```text
In two sentences, what can you do in this workspace, and which steering files have you loaded?
```
:::

::: info Sources
kiro.dev/docs · kiro.dev/docs/ide · kiro.dev/docs/cli · kiro.dev/docs/web · kiro.dev/docs/web/autonomous-mode · kiro.dev/crew · kiro.dev/docs/crew/bots. Product images: kiro.dev.
:::
