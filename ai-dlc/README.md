# Part 2 – AI-DLC (AI-Driven Development Life Cycle)

**Time:** 2:50 – 3:50 PM (1 hour, hands-on)

This time Kiro leads. It asks you structured questions in a file, writes a plan, and waits for your approval at every stage before it builds. Everything it asks, plans and decides is saved in `aidlc-docs/`.

You build **the same shopping cart API** as in Part 1, so you can compare the two results.

## 1. Install the AI-DLC rules (v1.0.1)

Run these inside the `ai-dlc` folder.

**Git Bash, macOS or Linux:**

```bash
cd ai-dlc
curl -fsSL -o ai-dlc-rules-v1.0.1.zip https://github.com/awslabs/aidlc-workflows/releases/download/v1.0.1/ai-dlc-rules-v1.0.1.zip
unzip ai-dlc-rules-v1.0.1.zip
cp -R aidlc-rules/aws-aidlc-rules .kiro/steering/
cp -R aidlc-rules/aws-aidlc-rule-details .kiro/
rm -rf ai-dlc-rules-v1.0.1.zip aidlc-rules
```

**Windows PowerShell:**

```powershell
cd ai-dlc
Invoke-WebRequest -Uri https://github.com/awslabs/aidlc-workflows/releases/download/v1.0.1/ai-dlc-rules-v1.0.1.zip -OutFile ai-dlc-rules-v1.0.1.zip
Expand-Archive ai-dlc-rules-v1.0.1.zip -DestinationPath .
Copy-Item -Recurse aidlc-rules\aws-aidlc-rules .kiro\steering\
Copy-Item -Recurse aidlc-rules\aws-aidlc-rule-details .kiro\
Remove-Item -Recurse -Force ai-dlc-rules-v1.0.1.zip, aidlc-rules
```

You should now have `.kiro/steering/aws-aidlc-rules/` and `.kiro/aws-aidlc-rule-details/`.

## 2. Start Kiro and check the rules loaded

```bash
kiro-cli chat
```

```
/context show
```

Look for `.kiro/steering/aws-aidlc-rules/core-workflow.md` in the list, then press `Esc`.

## 3. State your intent

Every AI-DLC request starts with **"Using AI-DLC, ..."**. Paste:

```
Using AI-DLC, build a shopping cart API for an e-commerce system. Start with "add items to cart" only.
User story: As a customer, I want to add items to my shopping cart, so that I can collect items I intend to purchase.
Acceptance criteria:
- I can add an item with a specified quantity to my cart
- The cart should display the updated item count
- The cart should show the item details (product name, price, quantity)
- The cart should calculate and display the subtotal
Follow the technical rules in .kiro/steering/tech.md.
```

## 4. Answer the questions file

Kiro does not ask in the chat. It writes the questions to a file, usually:

`aidlc-docs/inception/requirements/requirement-verification-questions.md`

1. Open the file.
2. Type your chosen letter after each `[Answer]:` tag. Answer every question.
3. **Save the file.** Kiro reads your answers from disk.
4. Tell Kiro: `I've answered the questions, please proceed`

The last questions are opt-ins for Security, Resiliency and Property-Based Testing extensions. Each one you enable adds requirements and tasks, so the run takes longer.

## 5. Approve each gate

At every stage Kiro writes a file to `aidlc-docs/`, prints **REVIEW REQUIRED**, and waits.

- Read the file, then type `proceed`. Expect to do this about 3 to 6 times.
- Code generation is gated twice: first you approve the plan, then the code.
- You can also ask for changes, or ask Kiro to add back a stage it skipped.

## 6. Check the result

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Then read the record Kiro kept:

- `aidlc-docs/audit.md` – every question, answer and approval, with timestamps
- `aidlc-docs/aidlc-state.md` – which stages ran and which were skipped

---
Steps adapted from the AWS workshop *Kiro – Getting Started*, Lab 12 Part 2 (AI-DLC), and the Code Challenge. AI-DLC rules: github.com/awslabs/aidlc-workflows (release v1.0.1).
