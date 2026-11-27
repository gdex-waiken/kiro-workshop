# 2. Extend Kiro, safely

**Part of Meet Kiro, 9:40 – 10:00 · Demo.** Connect tools with MCP, add skills and powers, and spend credits on purpose. Read it again after the workshop when you set Kiro up for your own team.

## Which one do I need?

| You want | Use | Where it lives |
|---|---|---|
| A one-off result | **Prompt** | The chat |
| Standing project rules | **Steering** | `.kiro/steering/` |
| A reusable capability for a kind of task | **Skill** | `.kiro/skills/<name>/SKILL.md` |
| An action when something happens (file save, tool use, agent stop) | **Hook** | `.kiro/hooks/` |
| Live access to a tool or data source | **MCP server** | `.kiro/settings/mcp.json` |
| Tools and know-how together, loaded on demand | **Power** | Installed from kiro.dev/powers, from inside Kiro, or from a GitHub URL |

## MCP: connect a live source

MCP servers are defined in two places, and they merge:

- `.kiro/settings/mcp.json`: this workspace (it wins on a conflict)
- `~/.kiro/settings/mcp.json`: just you

```json
{
  "mcpServers": {
    "aws-docs": {
      "command": "uvx",
      "args": ["awslabs.aws-documentation-mcp-server@latest"]
    }
  }
}
```

::: tip Prompt: set one up and test it
```text
Set up the AWS documentation MCP server for this workspace, then test it with a simple read-only call: find the Amazon S3 documentation page about blocking public access.
```
:::

::: warning Keep secrets out of the repo
Reference tokens as environment variables (`${VAR_NAME}`), never commit credentials, start with read-only calls, and approve write operations deliberately. In the IDE, Kiro only expands variables listed in the **Mcp Approved Env Vars** setting.
:::

## Skills: get them safely

| Step | How |
|---|---|
| **Find** | [github.com/anthropics/skills](https://github.com/anthropics/skills), the skills.sh registry, or any public GitHub or GitLab repository |
| **Install** | Kiro IDE: **Agent Steering & Skills** in the Kiro panel → **+** → **Import a skill**. Or copy the folder into `.kiro/skills/` (this project) or `~/.kiro/skills/` (all projects). The CLI picks it up in a new session |
| **Check first** | Read `SKILL.md` and every script. A third-party skill is code your agent will run |

::: tip Prompt: check what you have
```text
What Skills do I have installed, and what can each one do?
```
:::

## Powers: tools and know-how in one install

A power bundles MCP tools, skills and guidance in one folder (`plugin.json`, optional `skills/` and `mcp.json`). Kiro activates it when its keywords come up, and loads its MCP tools only when needed. Powers work in the IDE, CLI (V3), Web and Mobile. Older powers with a `POWER.md` still work.

## Spend tokens on purpose

A real multi-agent run built a small API service, about the size of today's: **37 agent sessions, about 11 million tokens re-read, and only about 1% of them written as code.** Every reviewer agent was a full session that replied `{"ok": true}`.

| Bad practice | Better practice |
|---|---|
| 18 tiny tasks, each a new agent | 4 to 6 meaningful tasks |
| A reviewer agent after every task | One review at the end, by you |
| The top model for everything | Top model to plan, a cheaper one to execute |
| Every plugin and global rule loaded | Only what this project needs |
| Only `tech.md` as steering | `product.md`, `tech.md`, `structure.md`, kept short |
| One endless chat | Short, focused sessions |

The rule is the same in every tool: **every request re-sends its context**, so more agents, tasks and turns cost more. Kiro consumes credits for each request, scaled by the model's multiplier, so watch the number of tasks and turns.

Start with **Auto**, which picks a model for each request. When you pick one yourself, compare multipliers: Claude Opus 5.5 is 2.0×, Claude Sonnet 5.5 1.3×, GPT-5.6 Luna 0.6× (up to 272K tokens) and Claude Haiku 5.5 0.06× (up to 100K tokens).

::: info Sources
AWS workshop *Kiro – Getting Started*: References (configuring MCP servers, installing skills) · kiro.dev/docs/mcp/configuration · kiro.dev/docs/skills · kiro.dev/docs/hooks · kiro.dev/docs/powers · kiro.dev/docs/models/available-models · kiro.dev/docs/billing (as of 27 November 2026) · the "More agents, more tokens" run (session logs, 18 November 2026)
:::
