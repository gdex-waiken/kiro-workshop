# Design: Submit and list ideas

Follows `tech.md` (Clean Architecture, UTC times, TDD) and `structure.md` (file locations).

## API
| Method | Path | Body | Success | Errors |
|---|---|---|---|---|
| POST | `/ideas` | `{"title": "Water station at the loading bay", "description": "Put a cold-water dispenser next to bay 3."}` | 201 + idea | 422 bad title or description |
| GET | `/ideas` | none | 200 + list | none |

Idea response:
```json
{
  "idea_id": "IDEA-0001",
  "title": "Water station at the loading bay",
  "description": "Put a cold-water dispenser next to bay 3.",
  "created_at": "2026-12-09T03:31:07Z"
}
```

List response: `{"ideas": [idea, ...], "count": 1}`, newest first.

## Components
| Layer | Component | Responsibility | Requirements |
|---|---|---|---|
| Domain | `Idea` | Frozen: `idea_id`, `title`, `description`, `created_at`. `Idea.create(...)` checks the title and description rules | 1.1, 1.3, 3.1, 3.2 |
| Domain | errors | `InvalidIdeaError` | 3.1, 3.2 |
| Application | ports | `IdeaRepository.add/next_id/list_newest_first`, `Clock.now` | 1.2, 2.1 |
| Application | `SubmitIdea` | Get the next id and the time, create the idea, add it, return an `IdeaView` | 1.1–1.3, 3.1, 3.2 |
| Application | `ListIdeas` | Return an `IdeaListView` with the ideas newest first and the count | 2.1–2.4 |
| Adapters | in-memory repo, `SystemClock` | A list in submission order; ids `IDEA-0001`, `IDEA-0002`, …; UTC time to the second | 1.2, 2.1 |
| Adapters | `api.py`, `main.py` | Schemas (`title: str = Field(min_length=1, max_length=100)`), routes, error mapping, `create_app()` | all |

## Key decisions
- Newest first means reverse submission order, not a sort on `created_at`. Two ideas sent in the same second still list in the right order.
- The title is stored as typed. Spaces are not trimmed; a title of only spaces counts as empty.
- Validation happens twice: Pydantic at the boundary, and `Idea.create` in the domain.
- `add` is called only after every check passes, so errors never change state.
- The request schema has no `idea_id` or `created_at` field, so the client cannot set them.

## Testing
- Domain: title of 1 and 100 characters accepted; empty, only spaces and 101 characters rejected; description limits.
- Application: fakes for the ports with a fixed clock; a rejected idea adds nothing; list order and count.
- API: 201 with every field, `created_at` ending in `Z`, 422 for each bad input with the list unchanged, 200 on an empty list and on a list of two, newest first.
