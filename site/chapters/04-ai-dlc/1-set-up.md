# 4.1 Set up

**11:20 – 11:30.** Same teams, swap the Driver.

## Install the AI-DLC rules (v1.0.1)

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

## Open the workspace and check the rules loaded

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

## Check the toolchain

```bash
python --version          # Python 3.12.x
python check_cart.py      # "Cannot reach http://localhost:8000 ... Is the service running?"
```

"Cannot reach" is correct: there's no service yet. It proves the checker runs.

## Paste the trigger phrase

Start a **new chat session** (not Spec mode) and paste exactly:

::: tip Copy this
```text
Using AI-DLC, build the KedaiKu cart service described in ticket.md: Feature 1 (add items to cart and view the cart) only. Follow vision-document.md, stakeholder-notes.md, technical-environment.md and api-contract.md. The service must pass check_cart.py. This is a greenfield project.
```
:::

## What you should see

- The AI-DLC welcome message.
- A new `aidlc-docs/` folder with `aidlc-state.md` and `audit.md`.

No welcome message? The rules are in the wrong folder. Check the paths above and start a **new** session.

**Next:** [4.2 Questions and conflicts](./2-inception)
