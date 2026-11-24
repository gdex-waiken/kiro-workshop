# Spec demo (facilitator, 10 minutes, live on the projector)

**Time:** inside the 9:30 – 9:50 opening (Chapter 1, Meet Kiro). Participants watch; they do not type.

The point: show what Kiro's built-in **spec workflow** looks like before anyone uses it. Spec mode turns a prompt into three documents and a task list. Later this morning teams use it for real (Chapter 5), then see what AI-DLC adds on top: questions in files, stakeholder conflicts, an execution plan you can challenge, and a gate at every stage.

## Before the session

- Open this `spec-demo` folder in Kiro IDE and check that the **Steering** panel lists the six files in `.kiro/steering/`.
- Do one dry run the day before, so the requirements come back in about a minute.
- If the venue network is slow, skip the live generation and open `finished-spec/` instead.

> This demo uses a generic idea list, not Pelita Ideas. No staff list, no categories, no votes. Don't open the Pelita `stakeholder-notes.md` here: the conflicts in it are the hands-on exercise.

## The demo, step by step

### 1. Steering (2 minutes)

Open `.kiro/steering/` and show the three kinds of steering file:

| File | Loaded | Say this |
|---|---|---|
| `product.md`, `tech.md`, `structure.md` | always | "What we build, with what, and where things go. Sent with every request, so keep them short." |
| `testing.md`, `api-conventions.md` | only when a matching file is open | "Detail that only loads when it's relevant." |
| `code-review.md` | only when you type `#code-review` | "A checklist that costs nothing until you use it." |

### 2. Create a spec (4 minutes)

In the Kiro chat, choose **Spec**, then paste:

```
An idea list API for staff. Start with "submit an idea" only: submit an idea with a title and a description, and list all ideas, newest first. Keep it an MVP: at most 5 tasks, no optional tasks.
```

Walk through what comes back:

- `requirements.md`: requirements with acceptance criteria in **EARS** form (`WHEN … THE SYSTEM SHALL …`). Point out one decision Kiro made that nobody asked for (a title length limit, trimming spaces, the order of two ideas sent in the same second).
- `design.md`: the three Clean Architecture layers, taken from `tech.md` and `structure.md`.
- `tasks.md`: a short list, each task linked to the requirements it covers.

### 3. Run one task (2 minutes)

Click **Start task** on task 1 only. While it runs, say:

> "Every task is a separate run that reloads the steering and the spec. Five tasks cost about five times the context. That's why the plan has 5 tasks, not 18."

That's the link to the "more agents, more tokens" slide.

### 4. Point ahead (2 minutes)

| Spec mode | AI-DLC |
|---|---|
| Kiro decides, then you review the documents | Kiro **asks first**, in question files, then writes the documents |
| One requirements → design → tasks path | **Workflow Planning** chooses which stages run, and you can challenge it |
| Feedback in chat | Answers in files, with an audit trail in `aidlc-docs/audit.md` |
| Fast for a clear, small change | Better when the requirements are unclear or people disagree |

Then: "Later you'll build a real version of this, Pelita Ideas, twice: first in spec mode, then with AI-DLC, where the stakeholders don't agree."

## Fallback

`finished-spec/` holds a complete, lean `requirements.md`, `design.md` and `tasks.md` (4 tasks) for the same generic idea list. Open them if live generation is slow.
