# Vision: Pelita Ideas

> Pelita Group is a fictional logistics company in Malaysia. Every company, person and quote in this workshop is invented.

## Why we are building this

Pelita Group asks staff for improvement ideas, but today they arrive by email, in WhatsApp groups and in corridor chats. The business wants three problems gone:

1. **Ideas get lost.** Nobody can see what has already been suggested, so good ideas disappear in inboxes.
2. **The same idea arrives again and again.** Last quarter "reusable parcel bags" was sent in five times by five people.
3. **Nobody knows why an idea was picked.** Managers choose favourites behind closed doors. Staff want to see which ideas their colleagues back.

The app team has already designed the portal screens against an agreed API contract (`api-contract.md`). They need a backend that honours that contract so they can start testing.

## Who uses it

| Who | How |
|---|---|
| Staff | Through the portal: submit ideas, browse them and, later, vote |
| Innovation committee | Reviews the top-ranked ideas once a month |
| App team | Calls the API exactly as described in `api-contract.md` |

## In scope

| Feature | When |
|---|---|
| Submit an idea, list ideas, open one idea | Release 1, this morning (greenfield) |
| Vote for an idea, see a ranked list | Release 1, this afternoon (brownfield: added to the existing code) |

## Out of scope for this release

- Comments, editing or deleting ideas, attachments
- Anonymous ideas
- AI summaries, auto-tagging or any other AI feature inside the portal
- Prizes, points or leaderboards of people
- Login and single sign-on. The staff ID in the request is trusted for now
- A real database and any cloud deployment

## What success looks like

- The app team can run its screens against this API without changing their code.
- Replaying the answer key with `check_ideas.py` passes every step, for each feature.
- Every disagreement in `stakeholder-notes.md` has a recorded decision.
