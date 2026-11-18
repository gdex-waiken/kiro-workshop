# 4. The AI-DLC method

AI-DLC is a set of rules, from [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows), that turns Kiro into a disciplined teammate: it asks before it assumes, plans before it builds, and stops at a gate after every stage. This workshop uses release **v1.0.1**.

## Three phases

| Phase | Question | Today |
|---|---|---|
| **Inception** | What are we building, and why? | Yes |
| **Construction** | How do we build it, one unit at a time? | Yes |
| **Operation** | How do we deploy and run it? | After this workshop |

The stages are **adaptive**: Workflow Planning decides which stages run and which are skipped, based on what you asked for. Each stage builds richer context for the next.

## The stages

| Phase | Stage | Produces | Today |
|---|---|---|---|
| Inception | Workspace Detection | Spots existing code | runs |
| | Reverse Engineering | Docs for existing code | skipped: no code yet |
| | **Requirements Analysis** | Requirements and the extension question | the big one |
| | User Stories | Stories with acceptance criteria | keep it short |
| | **Workflow Planning** | The execution plan: which stages run or skip | **trim it** |
| | Application Design | Components and boundaries | keep it small |
| | Units Generation | Splits work into units | one unit is enough |
| Construction | Functional and NFR design | Detailed design per unit | lean |
| | **Code Generation** | Code and tests | runs |
| | **Build and Test** | Full test run | then `check_cart.py` |

Everything lands in `aidlc-docs/`: `aidlc-state.md` says where you are, and `audit.md` records every question, answer and approval.

## Gates

Every stage ends with two choices: **Request Changes** or **Continue**. Open the files Kiro points to before you choose. A gate you click without reading is a gate you didn't use.

## Question files, not chat

1. Kiro writes questions to a `.md` file, with lettered options and an `[Answer]:` tag.
2. Type your answer after each tag, and say where it came from.
3. Save the file.
4. Tell Kiro: `I've answered the questions, please proceed`.

```markdown
## Question 4
How are cart ids created?

A) The app chooses the id
B) The server generates the id
C) Other (please describe)

[Answer]: A, api-contract.md says so
```

Answers in chat don't reach the audit trail. A vague answer earns a follow-up question file: that's the system working.

## Trim the plan

**AI over-builds.** Ask for a cart and it may plan a whole shop.

| What Kiro might plan | Your call |
|---|---|
| Add items to the cart | Keep: in the ticket |
| View the cart and subtotal | Keep: in the ticket |
| Remove items from the cart | Later: stretch goal |
| User login and accounts | Delete: out of scope |
| Checkout and payment | Delete: out of scope |
| PostgreSQL database | Delete: prohibited |

Before you approve a plan, **delete everything the ticket didn't ask for**, and say why at the gate. Every task you delete is code you don't have to review, and credits you don't spend.

## Extensions

During Requirements Analysis, Kiro asks whether to enable **Security baseline**, **Resiliency** and **Property-Based Testing**. Each adds work. Whatever you choose, write down why: a "no" only counts if it's on record.
