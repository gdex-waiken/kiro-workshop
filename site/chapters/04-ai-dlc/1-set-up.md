# 4.1 Set up

**11:20 – 11:30.** Same teams, swap the Driver.

## Step 1: Turn off Kiro Workflows first

Do this **before** you install the AI-DLC rules. If you already did it at home (see [Before you start](../00-before-you-start)), check it and move on.

::: warning Why it must be off
Kiro's **Workflows** feature runs work as background agent plans. While it's on, Kiro can take an AI-DLC request and run it as its own background workflow. AI-DLC's question files, gates and reviewers are then skipped or run out of sight, and commands ask for approval in a separate panel. AI-DLC needs to lead the chat itself, so Workflows must be off.
:::

The switch is **one setting for your whole computer** (a user setting). Turning it off in a project's `.vscode/settings.json` does nothing.

### Option A: from Settings

1. Open Settings: **Ctrl + ,** (Windows) or **Cmd + ,** (macOS). Or click the **gear** at the bottom left, then **Settings**.
2. Stay on the **User** tab and type `workflows` in the search box.
3. Find **Kiro Agent › Workflows: Enabled** and **untick** the box.

![Kiro Settings, searched for "workflows": the Kiro Agent › Workflows: Enabled box is unticked](/images/kiro-workflows-setting.png){.ui}

*Off looks like this: an empty box. A tick means Workflows is still on.*

### Option B: from the Command Palette

1. Open the Command Palette: **Ctrl + Shift + P** (Windows) or **Cmd + Shift + P** (macOS).
2. Type `kiro: workflows`.
3. Choose **Kiro: Disable Workflows**.

![The Command Palette with Kiro: Disable Workflows and Kiro: Enable Workflows](/images/kiro-workflows-command.png){.ui}

### Then reload Kiro

1. Command Palette → **Developer: Reload Window**.
2. Close any chat that was open before, and start a **new** one. The change only applies to new sessions.

::: details Using Kiro CLI instead?
Run `/settings` → **Features** → turn **Workflows** off, then quit and start `kiro-cli` again. The setting is `chat.enableWorkflows` in `~/.kiro/settings/cli.json`.
:::

::::: details Check it from a terminal (optional)
Your Kiro user settings file should contain `"kiroAgent.workflows.enabled": false`. No line at all also means off: Workflows is off unless someone turned it on.

::: code-group

```powershell [Windows PowerShell]
Select-String -Path "$env:APPDATA\Kiro\User\settings.json" -Pattern "workflows"
```

```bash [macOS]
grep workflows "$HOME/Library/Application Support/Kiro/User/settings.json"
```

:::

:::::

## Step 2: Trust the folder

Open **`kiro-workshop/ai-dlc`** with **File → Open Folder**. If a **Restricted Mode** banner shows at the top, click **Manage → Trust**, then **Developer: Reload Window**. Trust only folders you know: trusting lets the folder's `.kiro` files run on your machine.

## Step 3: Install the AI-DLC rules (v1.0.1)

Run these **inside the `ai-dlc` folder**, in the Kiro IDE terminal or any terminal.

::: code-group

```bash [Git Bash / macOS / Linux]
cd kiro-workshop/ai-dlc
curl -fsSL -o ai-dlc-rules-v1.0.1.zip https://github.com/awslabs/aidlc-workflows/releases/download/v1.0.1/ai-dlc-rules-v1.0.1.zip
unzip ai-dlc-rules-v1.0.1.zip
mkdir -p .kiro/steering
cp -R aidlc-rules/aws-aidlc-rules .kiro/steering/
cp -R aidlc-rules/aws-aidlc-rule-details .kiro/
rm -rf ai-dlc-rules-v1.0.1.zip aidlc-rules
```

```powershell [Windows PowerShell]
cd kiro-workshop\ai-dlc
Invoke-WebRequest -Uri https://github.com/awslabs/aidlc-workflows/releases/download/v1.0.1/ai-dlc-rules-v1.0.1.zip -OutFile ai-dlc-rules-v1.0.1.zip
Expand-Archive ai-dlc-rules-v1.0.1.zip -DestinationPath .
New-Item -ItemType Directory -Force .kiro\steering | Out-Null
Copy-Item -Recurse aidlc-rules\aws-aidlc-rules .kiro\steering\
Copy-Item -Recurse aidlc-rules\aws-aidlc-rule-details .kiro\
Remove-Item -Recurse -Force ai-dlc-rules-v1.0.1.zip, aidlc-rules
```

:::

You should now have `.kiro/steering/aws-aidlc-rules/` and `.kiro/aws-aidlc-rule-details/`.

## Step 4: Check the rules loaded

::: code-group

```text [Kiro IDE]
File → Open Folder → kiro-workshop/ai-dlc
Kiro panel → Agent Steering & Skills → Workspace:
you should see aws-aidlc-rules listed.
```

```bash [Kiro CLI]
cd kiro-workshop/ai-dlc
kiro-cli
# inside Kiro CLI:
/context show
# look for .kiro/steering/aws-aidlc-rules/core-workflow.md
```

:::

## Step 5: Check the toolchain

```bash
python --version          # Python 3.12.x
python check_cart.py      # "Cannot reach http://localhost:8000 ... Is the service running?"
```

"Cannot reach" is correct: there's no service yet. It proves the checker runs.

## Step 6: Paste the trigger phrase

Start a **new chat session** (not Spec mode) and paste exactly:

::: tip Copy this
```text
Using AI-DLC, build the KedaiKu cart service described in ticket.md: Feature 1 (add items to cart and view the cart) only. Follow vision-document.md, stakeholder-notes.md, technical-environment.md and api-contract.md. The service must pass check_cart.py. This is a greenfield project.
```
:::

## What you should see

- The AI-DLC welcome message.
- A new `aidlc-docs/` folder with `aidlc-state.md` and `audit.md`.

No welcome message? Check two things, then start a **new** session:

1. The rules are in the right folder (Step 3).
2. Workflows is off (Step 1). If Kiro says it's starting a **workflow**, or a **Workflows** panel opens, it's still on.

**Next:** [4.2 Questions and conflicts](./2-inception)
