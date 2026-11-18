# Traceability worksheet

Pick a number that `check_cart.py` checks and walk it back to the sentence that caused it. One complete chain is the goal; two is great.

```
a number you can point at
  └─ the test that would fail if the decision flipped
      └─ the design decision
          └─ the requirement
              └─ the answer you typed in a question file
                  └─ the sentence a stakeholder said
```

## Chain 1

| Link | Where it is (file, line or section) | What it says |
|---|---|---|
| The number | `cart-scenario.csv`, step | |
| The test | | |
| The design decision | `aidlc-docs/...` | |
| The requirement | `aidlc-docs/...` | |
| Your answer | `aidlc-docs/...` question file | |
| The stakeholder sentence | `stakeholder-notes.md` | |

Where did the chain break, if anywhere?

## Chain 2 (optional)

| Link | Where it is (file, line or section) | What it says |
|---|---|---|
| The number | `cart-scenario.csv`, step | |
| The test | | |
| The design decision | `aidlc-docs/...` | |
| The requirement | `aidlc-docs/...` | |
| Your answer | `aidlc-docs/...` question file | |
| The stakeholder sentence | `stakeholder-notes.md` | |

Where did the chain break, if anywhere?

## Good numbers to try

| Number | Step | Hint |
|---|---|---|
| `16` | 9 | Who decided what the badge counts? |
| `422` | 8 | Why not just cap the quantity at 10? |
| `54.00` | 9 | Why isn't there a discount on 3 notebooks? |
| `0.30` | 4 | What would floating point have shown? |
