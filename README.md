# kiro-workshop

Hands-on material for the **Kiro developer workshop** (1:00 – 5:00 PM).

You build the same small **shopping cart API** twice, on your own laptop:

1. **`spec-driven/`** – with Kiro's spec workflow (requirements → design → tasks).
2. **`ai-dlc/`** – with the AI-DLC methodology (Kiro asks, plans, waits for your approval, then builds).

Then you compare the two results side by side.

Everything runs **locally**. There is no cloud deployment in this version of the workshop.

## Before the workshop

| You need | Check it with |
|---|---|
| Kiro CLI (signed in) | `kiro-cli --version` |
| Python 3.12 or newer | `python --version` |
| Git | `git --version` |
| Git Bash (Windows only) for the AI-DLC install commands | open "Git Bash" |

## Get the workshop

```bash
git clone https://github.com/gdex-waiken/kiro-workshop.git
cd kiro-workshop
```

## What's in this repo

```
kiro-workshop/
├── docs/
│   ├── user-story.md              # the ticket you build
│   └── technical-requirements.md  # the rules Kiro must follow
├── spec-driven/                   # Part 1: start Kiro here
│   ├── README.md                  # step-by-step guide
│   └── .kiro/steering/tech.md     # standing rules Kiro reads every session
└── ai-dlc/                        # Part 2: start Kiro here
    ├── README.md                  # step-by-step guide
    └── .kiro/steering/tech.md     # the same standing rules
```

Both project folders start empty on purpose. Kiro writes the specs, plans and code during the workshop.

The two parts are independent: always start `kiro-cli` **inside** the folder you are working on, so each part only sees its own `.kiro/` configuration.

## Agenda

| Time | Part |
|---|---|
| 1:00 | Meet Kiro: IDE, CLI, Web and Crew |
| 1:20 | The scenario: the shopping cart ticket |
| 1:35 | **Part 1: spec-driven development** → [`spec-driven/`](spec-driven/README.md) |
| 2:35 | Break |
| 2:50 | **Part 2: AI-DLC** → [`ai-dlc/`](ai-dlc/README.md) |
| 3:50 | Break |
| 4:05 | Compare the two results |
| 4:25 | Extend Kiro: MCP, skills, powers |
| 4:45 | Wrap-up and Q&A |

## Compare the two results (4:05)

From the repo root:

```bash
# What each process left on disk
ls -R spec-driven/.kiro/specs/ ai-dlc/aidlc-docs/

# What AI-DLC recorded about itself
head -40 ai-dlc/aidlc-docs/audit.md
```

Ask yourself: six months from now, which project could a new teammate (or a new AI session) pick up and extend with confidence?

## Sources

- AWS workshop *Kiro – Getting Started*: Code Challenge and Lab 12 (catalog.workshops.aws/q-zero2hero)
- Kiro documentation: kiro.dev/docs/specs
- AI-DLC workflows: github.com/awslabs/aidlc-workflows (release v1.0.1)
