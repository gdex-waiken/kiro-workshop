# Pre-workshop checklist

> Do this **2–3 days before** the workshop, on the laptop your team will actually use. The biggest risk on the day is a Kiro that cannot sign in.

## Each team (one shared laptop)

- [ ] **Kiro IDE installed and signed in.** Kiro CLI also works if you prefer the terminal.
- [ ] **Kiro answers a test prompt.** Ask it to "write a haiku about shopping carts". That proves sign-in, plan and network in one go. A spinner is not a pass.
- [ ] **You have Kiro credits left.** Check your usage in Kiro. The hands-on uses a fair number of requests; a fresh free account should be fine, but don't arrive with an almost empty allowance.
- [ ] **Python 3.12** installed: `python --version` prints `Python 3.12.x`. Avoid 3.13+ for this workshop.
- [ ] **Git** installed: `git --version` prints a version.
- [ ] **Windows only:** Git Bash, or use the PowerShell commands in the guide.

## Get the material

```bash
git clone https://github.com/gdex-waiken/kiro-workshop.git
cd kiro-workshop/ai-dlc
python check_cart.py
```

The last command should say it **cannot reach** `http://localhost:8000`. That is correct: you build the service in the workshop. It proves Python and the checker work.

## Nice to have

- [ ] Install the libraries at home, so the venue Wi-Fi isn't a problem: `pip install fastapi uvicorn pytest httpx`
- [ ] A second screen or laptop, so one person can read documents while the Driver types

## Do NOT

- Do not download the AI-DLC rules yet. The facilitator names the exact version on the day (v1.0.1) and has a USB copy.
- Do not use a different AI-DLC package. Take the rules only from **`awslabs/aidlc-workflows`**.
- Do not start the exercise early: the stakeholder conflicts work best when the team reads them together.
