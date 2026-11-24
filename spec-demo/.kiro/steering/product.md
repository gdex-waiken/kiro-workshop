---
inclusion: always
---

# Product: Idea List API

## Purpose
A backend API where staff send improvement ideas and see what others have sent. It is a workshop MVP: small, correct and easy to extend.

## Users
- **Staff** (through a web or mobile front end): submit ideas and browse the list.
- **Developer** (workshop participant): runs and extends the API locally.

## Features
| Feature | Status |
|---|---|
| Submit an idea with a title and a description | MVP, build first |
| List all ideas, newest first | MVP |
| Open one idea by its id | Next |
| Voting, comments, editing, deleting | Out of scope |
| Categories, authors, user accounts, login, persistent database | Out of scope |

## Business rules
- The title is required: 1 to 100 characters, and not only spaces.
- The description is required: 1 to 1000 characters.
- The service chooses the `idea_id` and the `created_at` time, never the client.
- What someone typed is stored exactly as typed.
- The list shows every idea, newest first.
- A request that fails stores nothing.

## Definition of done
- Every acceptance criterion has a passing test.
- `pytest` passes with no skipped tests.
- The README says how to install, test and run the API.

## Do not
- Add features that are not in the current spec.
- Add "nice to have" or optional tasks unless asked.
