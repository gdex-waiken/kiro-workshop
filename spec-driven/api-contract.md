# API contract: Lumen Ideas v1

Agreed with the app team. **Do not change paths, field names or status codes.**

Base URL when running locally: `http://localhost:8000`

## Feature 1: submit and browse ideas

### Submit an idea

`POST /ideas`

Request body:

```json
{
  "title": "Reusable parcel bags",
  "description": "Collect bags back from customers and reuse them three times.",
  "category": "Sustainability",
  "submitted_by": "E1002"
}
```

| Result | Status | Body |
|---|---|---|
| Submitted | `201` | the idea (below) |
| An idea like this already exists | `409` | error |
| Request not allowed (for example a bad title or category) | `422` | error |

### List ideas

`GET /ideas`

| Result | Status | Body |
|---|---|---|
| Always | `200` | `{ "ideas": [ idea, ... ], "count": 2 }`, newest first |

### Get one idea

`GET /ideas/{idea_id}`

| Result | Status | Body |
|---|---|---|
| Found | `200` | the idea |
| No such idea | `404` | error |

## Feature 2: vote and rank (afternoon, brownfield)

### Vote for an idea

`POST /ideas/{idea_id}/votes`

Request body:

```json
{ "voter": "E1003" }
```

| Result | Status | Body |
|---|---|---|
| Vote counted | `201` | the idea, with its new `vote_count` |
| No such idea | `404` | error |
| This person has already voted for this idea | `409` | error |
| Vote not allowed | `422` | error |

### Ranked ideas

`GET /rankings?limit=10`

| Result | Status | Body |
|---|---|---|
| Always, for a valid limit | `200` | `{ "ideas": [ idea, ... ], "count": 10 }`, most votes first |
| Limit outside 1 to 50 | `422` | error |

`limit` is optional. Without it, the service returns the top 10.

## The idea

```json
{
  "idea_id": "IDEA-0002",
  "title": "Reusable parcel bags",
  "description": "Collect bags back from customers and reuse them three times.",
  "category": "Sustainability",
  "submitted_by": "E1002",
  "submitter_name": "Raj Kumar",
  "department": "IT",
  "submitted_at": "2026-12-09T03:31:07Z",
  "vote_count": 0
}
```

- `idea_id` is chosen by the service.
- `submitter_name` and `department` come from the staff list, never from the app.
- `submitted_at` is UTC, ISO 8601, ending in `Z`.
- `vote_count` is `0` until Feature 2 exists.

## Errors

```json
{ "detail": "A human-readable message that says what was wrong" }
```

When a request fails, nothing changes: no idea is created and no vote is counted.
