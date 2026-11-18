# 6. Build the KedaiKu cart

**1:35 – 4:20.** KedaiKu is a fictional online store in Malaysia. Its mobile app team has already built a cart screen against a fixed API contract. You build the service behind it.

## Read first, in this order

| # | File | Why |
|---|---|---|
| 1 | [`ticket.md`](https://github.com/gdex-waiken/kiro-workshop/blob/main/ai-dlc/ticket.md) | What Product asked for |
| 2 | [`vision-document.md`](https://github.com/gdex-waiken/kiro-workshop/blob/main/ai-dlc/vision-document.md) | Why, for whom, what's in and out of scope |
| 3 | [`stakeholder-notes.md`](https://github.com/gdex-waiken/kiro-workshop/blob/main/ai-dlc/stakeholder-notes.md) | **The real requirements.** People disagree here on purpose |
| 4 | [`api-contract.md`](https://github.com/gdex-waiken/kiro-workshop/blob/main/ai-dlc/api-contract.md) | The fixed contract the app already uses |
| 5 | [`technical-environment.md`](https://github.com/gdex-waiken/kiro-workshop/blob/main/ai-dlc/technical-environment.md) | Stack, architecture and what is prohibited |
| 6 | [`sample-data/`](https://github.com/gdex-waiken/kiro-workshop/tree/main/ai-dlc/sample-data) | The product catalog and **the answer key** |

Read 1–3 as a team **before** Kiro asks its first question.

## The stakeholders don't agree

Four topics have people pulling in different directions:

- **The cart badge:** what number should it show?
- **How many is too many:** is there a limit per product?
- **When it's too many:** what happens to the customer's request?
- **A launch promotion:** does it belong in this release?

Don't settle these by vote. Look for who has the authority and what else they said. The Product Owner decides; the Scribe records the decision, the reason and the source in `team-log.md`. Some requests should be refused, and refusing on record counts.

## Five rules

1. **Answer in files, not in chat.**
2. **Read before you approve.** Open the files at every gate.
3. **Trim the plan.** Delete every stage, story or task the ticket didn't ask for, and say why at the gate.
4. **Record the why.** "We chose B" is worth nothing. "We chose B because Siti said customers must never have their quantity changed without being told" is worth everything.
5. **No vibe coding.** Don't edit files outside the workflow. If you do, tell Kiro what you changed.

## Timeline and checkpoints

| Time | You should be… | Checkpoint |
|---|---|---|
| 1:35 – 2:30 | **Requirements Analysis:** question files answered, extension decision recorded, conflicts settled | **CP1:** every conflict has a recorded decision |
| 2:40 – 3:25 | **Workflow Planning** trimmed, **Application Design** approved | **CP2:** you deleted or questioned something in the plan |
| 3:25 – 4:20 | **Construction:** code and tests, then `check_cart.py` | **CP3:** checker result on screen, one traceability chain written |

Behind schedule at 3:25? Ask the facilitator for a ready-made `aidlc-docs/` and jump to Construction.

## When you're stuck

| Symptom | Do this |
|---|---|
| No welcome message, no `aidlc-docs/` | The rules are in the wrong folder. Check chapter 5, then start a **new** session |
| Kiro suggests switching to Spec mode | Decline. Stay in Vibe mode |
| Kiro keeps asking the same thing | Your answer was vague. Be more specific in the follow-up file |
| Kiro plans login, checkout, a database or a new endpoint | Delete it at the gate and point to `technical-environment.md` |
| You can't find the answer in the documents | Record an assumption, say it's an assumption, move on. Two minutes, no more |
| `check_cart.py` says "Cannot reach" | Start the service: `uvicorn app.main:app --port 8000` |
| `check_cart.py` fails a step | Read that step's `what_happens` column, then find the stakeholder sentence behind it |
| You're running low on Kiro credits | Stop asking for explanations in chat. Read the files instead |
