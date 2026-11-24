# 5.1 Create the spec

**About 10 minutes.**

## Open the workspace

```bash
git clone https://github.com/gdex-waiken/kiro-workshop.git
```

Open the **`kiro-workshop/spec-driven`** folder, not the repo root, so Kiro only sees this part's files and rules.

<div class="shot-pair">
  <img class="panel" src="/images/kiro-ide-panel.png" alt="The Kiro panel: Specs, Agent Hooks, Steering and MCP servers" />
  <img src="/images/kiro-ide-chat.png" alt="The Kiro chat with the Spec, Plan, Bug Fix and Quick Spec agents" />
</div>

*The Kiro panel, with the workspace `tech` rules already loaded, and the chat with its built-in agents.*

## Start a spec

::: code-group

```text [Kiro IDE]
1. Open the Kiro panel (the ghost icon in the activity bar).
2. Specs → Create New Spec. Or choose "Spec" in the chat.
3. When Kiro asks: Build a Feature → start with Requirements.
4. Paste the prompt below.
```

```bash [Kiro CLI]
cd kiro-workshop/spec-driven
kiro-cli
# inside Kiro CLI:
/spec new pelita-ideas
# then choose: Build a Feature → Requirements, and paste the prompt below
```

:::

## Your prompt

::: tip Copy this
```text
Build the Pelita Ideas service described in ticket.md and api-contract.md. Feature 1 only: submit an idea, list every idea newest first, and open one idea. Submitter names and departments come from sample-data/staff.csv, and categories from sample-data/categories.csv. The service must pass check_ideas.py. Keep it an MVP: at most 5 tasks, no optional tasks.
```
:::

## What you should see

- A new folder: `.kiro/specs/pelita-ideas/` (the name may differ).
- `requirements.md` opens in the editor, and Kiro stops to ask you to review it.

::: warning Kiro is not asking about stakeholders
Notice what Kiro does **not** ask: how long a title may be, what happens when it's too long, or whether two ideas can share a title. Spec mode drafts first and lets you correct. Keep that in mind for Chapter 6.
:::

**Next:** [5.2 Review the requirements](./2-requirements)
