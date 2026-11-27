# 4. Who asks the questions?

**10:30 – 10:40 · Talk.** In the spec hands-on, Kiro wrote good requirements fast, and your team still found decisions nobody had made. That's the gap AI-DLC closes.

## From AI-assisted to AI-DLC

![Human effort falls as AI takes the lead: AI-assisted, AI-DLC 1.0, AI-DLC 2.0, autonomous](/images/human-effort-curve.png){.figure}

| | Spec (AI-assisted) | AI-DLC |
|---|---|---|
| **Who asks the questions** | You notice the gaps, if you notice them | Kiro asks, in a question file, before it writes requirements |
| **Who decides** | You correct the draft afterwards | You decide at a gate after every stage |
| **Where decisions live** | `requirements.md`, `design.md` | Question files, requirements, design and an audit trail under `aidlc/` |
| **Speed** | Faster | Slower: it asks until the scope is right |
| **Best for** | A clear feature in a project you know | Fuzzy needs, people who disagree, several people on one repo, audit needs |

The roles flip. With a spec, **AI builds and you check**. With AI-DLC, **AI drives the process and you decide**.

## The words we'll use

| Word | Means |
|---|---|
| **Intent** | What you want built, in one sentence. One piece of work |
| **Phase** | Inception (what and why), Construction (how, then code), Operation (not today) |
| **Stage** | One step inside a phase, such as Requirements Analysis or Code Generation |
| **Question file** | A `.md` file where Kiro writes its questions and you write the answers |
| **Gate** | Kiro stops after a stage. You type **Approve** or say what to change |
| **Unit** | A piece of the work that can be built on its own |
| **Record** | Everything AI-DLC writes under `aidlc/`: state, questions, answers, approvals, the audit trail |

## When to use which

| Situation | Use |
|---|---|
| Prototypes, throwaway scripts, small fixes | **Vibe**: just chat |
| A clear feature in an ongoing project | **Spec** |
| Fuzzy needs, conflicting stakeholders, audit or compliance, a team sharing one repo | **AI-DLC** |
| You know the outcome but not the steps, and it can run for a while | **Goal** |

They mix: AI-DLC for the feature, a quick chat for a one-line fix inside it.

## Ask yourself

::: tip Before the break
1. In your spec, which decision would have caused a production bug if nobody had spotted it?
2. Six months from now, which project could a new teammate pick up without asking you?
:::

::: info Sources
*AI-Driven Development Lifecycle (AI-DLC) Method Definition*, Raja SP, AWS · AI-DLC user guide, awslabs.github.io/aidlc-workflows · kiro.dev/docs/specs
:::
