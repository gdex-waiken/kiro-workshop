# 5. Set up

**1:20 – 1:35.** Teams of 3–4, one laptop per team.

## Get the material

```bash
git clone https://github.com/gdex-waiken/kiro-workshop.git
cd kiro-workshop/ai-dlc
```

## Install the AI-DLC rules (v1.0.1)

Run these **inside the `ai-dlc` folder**.

::: code-group

```bash [Git Bash / macOS / Linux]
curl -fsSL -o ai-dlc-rules-v1.0.1.zip https://github.com/awslabs/aidlc-workflows/releases/download/v1.0.1/ai-dlc-rules-v1.0.1.zip
unzip ai-dlc-rules-v1.0.1.zip
mkdir -p .kiro/steering
cp -R aidlc-rules/aws-aidlc-rules .kiro/steering/
cp -R aidlc-rules/aws-aidlc-rule-details .kiro/
rm -rf ai-dlc-rules-v1.0.1.zip aidlc-rules
```

```powershell [Windows PowerShell]
Invoke-WebRequest -Uri https://github.com/awslabs/aidlc-workflows/releases/download/v1.0.1/ai-dlc-rules-v1.0.1.zip -OutFile ai-dlc-rules-v1.0.1.zip
Expand-Archive ai-dlc-rules-v1.0.1.zip -DestinationPath .
New-Item -ItemType Directory -Force .kiro\steering | Out-Null
Copy-Item -Recurse aidlc-rules\aws-aidlc-rules .kiro\steering\
Copy-Item -Recurse aidlc-rules\aws-aidlc-rule-details .kiro\
Remove-Item -Recurse -Force ai-dlc-rules-v1.0.1.zip, aidlc-rules
```

:::

You should now have `.kiro/steering/aws-aidlc-rules/` and `.kiro/aws-aidlc-rule-details/`.

## Check your toolchain

```bash
python --version          # Python 3.12.x
python check_cart.py      # "Cannot reach http://localhost:8000 ... Is the service running?"
```

The "cannot reach" message is correct for now: there's no service yet. It proves the checker runs.

## Assign roles

| Role | Job |
|---|---|
| **Driver** | Types into Kiro. Never answers a question alone |
| **Product Owner** | Owns the documents, settles conflicts, has the final say at gates |
| **Reviewer** | Opens and reads every file before a gate |
| **Scribe** | Keeps `team-log.md` up to date: decisions **and why** |

Write the roles at the top of `team-log.md`. Swap the Driver at the break. With three people, the Reviewer is also the Scribe.

## Paste the trigger phrase

Open the `ai-dlc` folder in **Kiro IDE** (or run `kiro-cli chat` there). Start a **new Vibe session** and paste exactly:

```text
Using AI-DLC, build the KedaiKu cart service described in ticket.md: Feature 1 (add items to cart and view the cart) only. Follow vision-document.md, stakeholder-notes.md, technical-environment.md and api-contract.md. The service must pass check_cart.py. This is a greenfield project.
```

You should get the AI-DLC welcome message, and a new `aidlc-docs/` folder with `aidlc-state.md` and `audit.md`. No welcome message? The rules are in the wrong folder: check the paths above and start a new session.
