# 6.1 Start the workflow

**11:00 – 11:06 · We do it together.** The trainer does each step on the big screen. Do it at the same time.

## Step 1 · Turn off Kiro Workflows

AI-DLC must lead the chat itself. While Kiro's **Workflows** is on, Kiro can run your request as its own background workflow and skip AI-DLC's questions and gates. You left it alone for the spec hands-on; turn it off now. Pick **one** of the two ways.

**From Settings:** press **Ctrl + ,** (macOS: **Cmd + ,**), type `@id:kiroAgent.workflows.enabled` in the search box (1), stay on the **User** tab (2), and **untick** the box (3).

![Kiro Settings: search, User tab, Workflows: Enabled unticked](/images/aidlc-workflows-setting.png){.shot}

**Or from the Command Palette:** press **Ctrl + Shift + P** (macOS: **Cmd + Shift + P**), type `disable` (1), choose **Kiro: Disable Workflows** (2). The Workflows panel then says **Workflows is disabled** (3).

![Command Palette: Kiro: Disable Workflows, and the panel saying Workflows is disabled](/images/aidlc-workflows-command.png){.shot}

It's one setting for your whole computer. Turn it back on after the workshop if you want Kiro's own workflows, such as `/goal`.

## Step 2 · Set up AI-DLC in the folder

1. **File → Open Folder** → `kiro-workshop/ai-dlc`. If a **Restricted Mode** banner shows, click **Manage → Trust**.
2. Open a terminal (**Terminal → New Terminal**) and run:

```bash
aidlc config --harness kiro --yes
aidlc doctor
```

**Green when** `aidlc doctor` says **0 problems**. Warnings are fine.

3. Command Palette → **Developer: Reload Window**, so Kiro picks up the new agent.

## Step 3 · Pick the aidlc agent

1. In the chat panel, start a **new chat**.
2. Open the agent picker (it says **Default** next to the chat box) and choose **aidlc**.

::: warning Pick aidlc in every new chat
Kiro starts each new chat on its default agent. If you forget, Kiro answers as a normal assistant and nothing is recorded.
:::

## Step 4 · Send the first message

Copy it exactly. The words at the start choose a short workflow: four stages, four gates.

::: tip Prompt 1 · Start Feature 1
```text
/aidlc express --plan-approval on --skip deployment-pipeline,deployment-execution,observability-setup Build the Lumen Ideas service described in ticket.md: Feature 1 (submit and browse ideas) only. Follow vision-document.md, stakeholder-notes.md, technical-environment.md and api-contract.md, and build test-first. The service must pass check_ideas.py. This is a greenfield project. We will answer your questions by editing the question files.
```
:::

| Part of the message | Why it's there |
|---|---|
| `express` | The short AI-DLC plan. Without a scope word, AI-DLC offers a 20-stage plan |
| `--plan-approval on` | Kiro shows its code plan and waits, so you can trim it |
| `--skip deployment-…` | No cloud today: `technical-environment.md` says it runs on the laptop |
| "Follow … stakeholder-notes.md …" | Hand Kiro the documents, not your summary of them |
| "and build test-first" | AI-DLC's default is tests after the code; `technical-environment.md` says tests first |
| "This is a greenfield project" | There's no service code yet |
| "We will answer … by editing the question files" | Your answers go into the record, not just the chat |

## What you should see

In about 3 minutes Kiro:

- creates a record folder `aidlc/spaces/default/intents/<date>-<name>/`
- reads every document in the folder
- writes a question file and stops, asking you to edit it and send **done**

While it reads: everyone opens `stakeholder-notes.md` and reads it, out loud if you like.

::: details If Kiro asks you to allow a command
Kiro asks before it runs `aidlc`, `python`, `pip`, `pytest` or `uvicorn` in this folder. Choose **Trust** or **Allow**. `Exit Code: -1` in the chat means Kiro is waiting for that click.
:::

::: details If something else happens
| You see | Do this |
|---|---|
| A normal chat answer, no record folder | You weren't on the **aidlc** agent. New chat, pick **aidlc**, send Prompt 1 again |
| An offer of a 20-stage plan | The scope word is missing. Send Prompt 1 again, exactly as written |
| "How do you want to answer: Guide me / I'll edit the file / Chat" | Type `2` |
| "Approval needed in agent-aidlc-…" panels | Kiro Workflows is still on. Do Step 1 again, **Developer: Reload Window**, new chat, pick **aidlc**, then `/aidlc --resume` |
| No **aidlc** in the agent picker | Step 2 didn't finish, or Kiro wasn't reloaded. Run `aidlc doctor`, then **Developer: Reload Window** |
:::

**Next:** [6.2 Questions and conflicts](./2-inception)
