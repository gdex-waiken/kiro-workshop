# Debugging

Find what you see in the left column. If nothing matches, type **STUCK** in the chat (Session 0) or put your hand up (on the day).

## Signing in

| What you see | Fix |
|---|---|
| "There was an error signing you in" | Your seat isn't active yet. Tell the trainer |
| The browser signs you in but Kiro stays on the sign-in screen | Check the start URL `https://sweetmag-kiro.awsapps.com/start` and the region `us-east-1`. On a company network, try a phone hotspot once to see if the network blocks it, then tell IT |
| "No profiles available" | Your network inspects HTTPS traffic. IT needs an exception for `*.kiro.dev` |
| Forgot your password | **Forgot password?** on the AWS sign-in page |
| Lost your MFA device | **Troubleshoot MFA** on the MFA page, or ask the trainer to reset it |
| Kiro says your session expired | Click **Reconnect** and sign in again |

## Where to see your credits

The status bar at the bottom right of Kiro shows **Kiro Credit Pooling** with what's used and the total (3 in the picture below). If it's close to the total, stop asking Kiro to explain things in chat and read the files instead.

## `/goal` is missing

Kiro's **goal** runs as a workflow recipe: open the **Workflows** view in the activity bar (1) and look under **Recipes** for **goal** (2).

![Kiro Workflows view: the activity-bar icon, the goal recipe, and the credits in the status bar](/images/debug-goal-recipe.png){.shot}

| What you see | Fix |
|---|---|
| Typing `/goal` in the chat offers nothing | Check that the Kiro CLI is installed: run `kiro-cli --version` in a terminal. If it isn't found, install it (below), then quit Kiro fully and open it again |
| The recipes are there but goal won't start | Workflows is off. That's expected from 11:00 today: AI-DLC needs it off. Turn it back on after the workshop (Settings → `@id:kiroAgent.workflows.enabled` → tick) |

::: code-group

```powershell [Windows PowerShell]
irm 'https://cli.kiro.dev/install.ps1' | iex
kiro-cli --version
```

```bash [macOS / Linux]
curl -fsSL https://cli.kiro.dev/install | bash
kiro-cli --version
```

:::

## Installing the tools

| What you see | Fix |
|---|---|
| `python` opens the Microsoft Store | Install Python 3.12 from python.org and tick **Add python.exe to PATH** |
| `aidlc` is not recognised | Kiro or the terminal was open while you installed. Quit it fully and open it again. Reload Window is not enough |
| `aidlc-shim.ps1 cannot be loaded` | Windows blocks scripts. Run `Get-ExecutionPolicy -List`; if **CurrentUser** is `Restricted`, run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`. If **MachinePolicy** is set, ask IT |
| `Filename too long` | Clone to a short folder, for example `C:\kw`, and run `git config --global core.longpaths true` |

## AI-DLC in Kiro

| What you see | Fix |
|---|---|
| No **aidlc** in the chat's agent picker | In the `ai-dlc` folder: `aidlc config --harness kiro --yes`, `aidlc doctor`, then **Developer: Reload Window** |
| A normal chat answer, no record folder | You weren't on the **aidlc** agent. New chat, pick **aidlc**, send the message again |
| "Approval needed in agent-aidlc-…" panels, or AI-DLC's reviews don't run | Kiro Workflows is still on. Turn it off ([6.1 Step 1](./06-ai-dlc/1-set-up#step-1-turn-off-kiro-workflows)), **Developer: Reload Window**, new chat, pick **aidlc**, `/aidlc --resume` |
| Kiro's terminal shows `Exit Code: -1` | Kiro is waiting for you to allow the command: choose **Allow** or **Trust**. Still -1 on Windows? `aidlc config trust --kiro-terminal powershell --yes`, then restart Kiro |
| An offer of a 20-stage plan | The word `express` is missing from your first message. Send it again from the [Prompts](./prompts) page |
| Kiro offers to switch to Spec mode | Decline. Stay in AI-DLC |
| The chat is nearly full | `/aidlc park`, new chat, pick **aidlc**, `/aidlc --resume` |
| Restricted Mode banner | **Manage → Trust** for the workshop folder only |

## Running the service

| What you see | Fix |
|---|---|
| "Cannot reach … Is the service running?" | Start it in another terminal: `python -m uvicorn app.main:app --port 8000` |
| `uvicorn` is not recognised | Use `python -m uvicorn app.main:app --port 8000` |
| `No module named fastapi` | `python -m pip install fastapi uvicorn httpx pytest` |
| "Address already in use" on port 8000 | Another service is still running: close that terminal, or wait for Kiro to finish Build and Test |
