# Traceability worksheet

Pick a result that `check_ideas.py` checks and walk it back to the sentence that caused it. One complete chain is the goal; two is great.

```
a result you can point at
  └─ the test that would fail if the decision flipped
      └─ the design decision
          └─ the requirement
              └─ the answer you typed in a question file
                  └─ the sentence a stakeholder said
```

## Chain 1

| Link | Where it is (file, line or section) | What it says |
|---|---|---|
| The result | `ideas-scenario.csv` or `votes-scenario.csv`, step | |
| The test | | |
| The design decision | `aidlc-docs/...` | |
| The requirement | `aidlc-docs/...` | |
| Your answer | `aidlc-docs/...` question file | |
| The stakeholder sentence | `stakeholder-notes.md` | |

Where did the chain break, if anywhere?

## Chain 2 (optional)

| Link | Where it is (file, line or section) | What it says |
|---|---|---|
| The result | `ideas-scenario.csv` or `votes-scenario.csv`, step | |
| The test | | |
| The design decision | `aidlc-docs/...` | |
| The requirement | `aidlc-docs/...` | |
| Your answer | `aidlc-docs/...` question file | |
| The stakeholder sentence | `stakeholder-notes.md` | |

Where did the chain break, if anywhere?

## Good results to try

| Result | Step | Hint |
|---|---|---|
| `409` | 3 | Why is "  REUSABLE PARCEL BAGS  " the same idea? |
| `422` | 5 | Why not just cut the title to 80 characters? |
| `422` | 8 | Why can't a shy junior submit without a name? |
| `422` | 7 | Why is there no "Other" category? |
| `409` | votes step 3 | Why not just ignore a second tap and say OK? |
| `A` before `B` | votes step 10 | Two ideas with 2 votes each: who decided the order? |
