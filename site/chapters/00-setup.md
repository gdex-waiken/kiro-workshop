# Session 0 · Setup

**Mon 7 Dec · 30 minutes · online.** Get to green before the workshop day, so the morning is spent building, not installing. Can't join? Do it on your own and post your green screenshot in the workshop channel by **Tue 8 Dec, 5 PM**. A setup desk is open from **9:00** on the day for anyone still red.

You need: the laptop you'll bring on the day, with rights to install software, and your phone with an authenticator app for MFA.

::: tip Stuck for more than 2 minutes?
Type **STUCK** and the step number in the meeting chat. A helper will take you to a breakout room. Every fix is also on the [Debugging](./troubleshooting) page.
:::

## Step 1 · Install Kiro IDE

1. Go to **[kiro.dev/ide](https://kiro.dev/ide/)** and download Kiro IDE for your system.
2. Run the installer and open Kiro.

**Green when** Kiro shows its welcome screen with a **Sign in** button.

## Step 2 · Sign in with your organization

We've already added you with your **work email**. Follow the red boxes, in number order.

**In Kiro**, click **Sign in** (1). Your browser opens.

![Kiro welcome screen: the Sign in button](/images/setup-01-kiro-sign-in.png){.shot .narrow}

Choose **Your organization** → **Sign in** (2). Not Google, GitHub or Builder ID.

![Choose a way to sign in: Your organization](/images/setup-02-your-organization.png){.shot .narrow}

Fill in the start URL (3), click **Show region** (4), type the region (5), then **Continue** (6):

| Field | Type exactly |
|---|---|
| Work email or start URL | `https://sweetmag-kiro.awsapps.com/start` |
| Region | `us-east-1` |

![Sign in with your organization: start URL, region, Continue](/images/setup-03-start-url-region.png){.shot .narrow}

The AWS sign-in page opens. Type your **work email** (7), then **Next** (8):

![AWS sign in: username and Next](/images/setup-04-username.png){.shot .narrow}

Type your **password** (9), then **Sign in** (10). No password yet, or forgot it? Click **Forgot password?**.

![AWS sign in: password and Sign in](/images/setup-05-password.png){.shot .narrow}

Type the **six-digit code** from your authenticator app (11), then **Sign in** (12). If AWS asks you to register an MFA device first, follow its steps with the app on your phone. If the browser then asks you to allow access for Kiro, choose **Allow**.

![AWS additional verification: MFA code and Sign in](/images/setup-06-mfa.png){.shot .narrow}

Go back to Kiro. You're good to go: the account icon at the bottom left has a tick, and the chat says **Let's build**.

![Kiro signed in: the account icon with a tick, and the chat box](/images/setup-07-signed-in.png){.shot}

Send this in the chat:

```text
Write a haiku about good ideas.
```

**Green when** Kiro answers. A spinner that never stops is not green.

## Step 3 · Accept the invitation

You'll also get an email inviting you to AWS IAM Identity Center. Open it and **accept the invitation**. It asks you to sign in first: use the same work email, password and MFA code as in Step 2.

## Step 4 · Install Python, Git and aidlc

Type these in a **PowerShell** window (Windows) or **Terminal** (macOS; there, type `python3` wherever this page says `python`). Check what you already have:

```bash
python --version
git --version
```

You need **Python 3.12.x** (avoid 3.13+) from [python.org](https://www.python.org/downloads/) and any recent Git from [git-scm.com](https://git-scm.com/downloads).

Install the Python packages the service will use, so the venue Wi-Fi isn't a problem on the day:

```bash
python -m pip install fastapi uvicorn httpx pytest
```

Then install **aidlc**, the AI-DLC command from AWS. You'll use it at 11:00 on the day.

::: code-group

```powershell [Windows PowerShell]
irm https://github.com/awslabs/aidlc-workflows/releases/latest/download/install.ps1 | iex
```

```bash [macOS / Linux]
curl -fsSL https://github.com/awslabs/aidlc-workflows/releases/latest/download/install.sh | sh
```

:::

::: warning Quit Kiro and open it again
Kiro keeps the PATH it started with. Close **every** Kiro window (on macOS, Cmd + Q), then open it again. Reload Window is not enough.
:::

```bash
aidlc version
```

**Green when** it prints `aidlc 2.11.x` (2.11.4 or later).

## Step 5 · Get the material

In Kiro, open a terminal (**Terminal → New Terminal**) and run:

::: code-group

```powershell [Windows PowerShell]
cd $HOME
git clone https://github.com/gdex-waiken/kiro-workshop.git
cd kiro-workshop\spec-driven
python check_ideas.py
```

```bash [macOS / Linux]
cd ~
git clone https://github.com/gdex-waiken/kiro-workshop.git
cd kiro-workshop/spec-driven
python3 check_ideas.py
```

:::

**Green when** the last command says **Cannot reach http://127.0.0.1:8000 … Is the service running?** That's right: you build the service on the day. It proves Python and the checker work.

## Step 6 · Smoke test

1. In Kiro: **File → Open Folder** → `kiro-workshop/spec-driven`. If a **Restricted Mode** banner shows, click **Manage → Trust**.
2. In the chat, send:

```text
In two sentences, what is this workspace about, and which steering files have you loaded?
```

**Green when** Kiro mentions Lumen Ideas and the `product`, `tech` and `structure` steering files. Take a screenshot and post it in the workshop channel. You're done: see you on Wednesday.

::: danger Don't change anything else yet
Leave Kiro's settings as they are. You'll change one setting together at 11:00, just before AI-DLC. Don't run any `/aidlc` command, and don't open `ai-dlc/stakeholder-notes.md`: the conflicts work best when your team reads them together on the day.
:::

## When something goes wrong

| What you see | Fix |
|---|---|
| "There was an error signing you in" | Your seat isn't active yet. Tell the trainer |
| The browser signs you in but Kiro stays on the sign-in screen | Check the start URL and that the region is exactly `us-east-1`. On a company network, try a phone hotspot once to see if the network blocks it |
| "No profiles available" | Your network inspects HTTPS traffic. IT needs an exception for `*.kiro.dev` |
| `aidlc` is not recognised | Kiro or the terminal was open while you installed. Quit it fully and open it again |
| `python` opens the Microsoft Store | Install Python 3.12 from python.org and tick **Add python.exe to PATH** |

More fixes: [Debugging](./troubleshooting).
