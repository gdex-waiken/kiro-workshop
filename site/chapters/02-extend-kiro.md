# 2. Extend Kiro, safely

**9:50 – 10:00 · Demo.** Connect tools with MCP, add skills and powers, and spend tokens on purpose. Worth knowing before the hands-on starts: it's how you keep the next three hours cheap.

## Which one do I need?

| You want | Use | Where it lives |
|---|---|---|
| A one-off result | **Prompt** | The chat |
| Standing project rules | **Steering** | `.kiro/steering/` |
| A reusable capability for a kind of task | **Skill** | `.kiro/skills/<name>/` |
| Live access to a tool or data source | **MCP server** | `.kiro/settings/mcp.json` |
| Tools and know-how together, loaded on demand | **Power** | Installed from kiro.dev/powers |

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
Use environment variables for tokens, start with read-only calls, and approve write operations deliberately.
:::

## Skills: get them safely

| Step | How |
|---|---|
| **Find** | [github.com/anthropics/skills](https://github.com/anthropics/skills), the skills.sh registry, or Kiro IDE: Steering panel → **+** |
| **Install** | Copy the skill folder into `.kiro/skills/`, then start a new session |
| **Check first** | Read `SKILL.md` and every script. A third-party skill is code your agent will run |

::: tip Prompt: check what you have
```text
What Skills do I have installed, and what can each one do?
```
:::

## Powers: tools and know-how in one install

A power bundles MCP tools, skills and guidance in one folder (`plugin.json`, optional `skills/` and `mcp.json`). Kiro activates it when its keywords come up, and loads its MCP tools only when needed. Powers work in the IDE, CLI (V3), Web and Mobile.

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

The rule is the same in every tool: **every request re-sends its context**, so more agents, tasks and turns cost more. Kiro bills in credits per request, so watch the number of tasks and turns.

::: info Sources
AWS workshop *Kiro – Getting Started*: References (configuring MCP servers, installing skills) · kiro.dev/docs/powers · the "More agents, more tokens" run (session logs, 18 November 2026)
:::
