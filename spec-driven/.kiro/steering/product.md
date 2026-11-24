---
inclusion: always
---

# Product: Pelita Ideas

## Purpose
The backend for Pelita Ideas, the staff idea portal at Pelita Group (a fictional logistics company). A workshop MVP: small, correct and easy to extend.

## Users
- **Staff**, through the portal: submit ideas and browse them. Later: vote.
- **Developer** (workshop participant): runs and extends the service locally.

## Features
| Feature | Status |
|---|---|
| Submit an idea (title, description, category) | MVP, build first |
| List ideas, newest first; open one idea | MVP |
| Vote for an idea and see a ranked list | Next, added later to the existing code |
| Comments, editing, attachments, login, database, AI features | Out of scope |

## Rules we already know
- The API is fixed: follow `api-contract.md` exactly.
- Submitter names and departments come from `sample-data/staff.csv`, never from the client.
- Categories come from `sample-data/categories.csv`.
- A failed request changes nothing.

## Do not
- Add features that are not in the current spec.
- Add optional tasks unless asked.
