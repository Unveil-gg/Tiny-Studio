# Tiny Studio — agent bootstrap

This file stays **short** on purpose. Tools that read **`AGENTS.md`** (for
example OpenAI **Codex CLI**) pick up pointers here without duplicating the
full studio guide.

## Read next

- **`CLAUDE.md`** — operating guide, principles, slash workflows, agents.
- **`.claude/skills/<name>/SKILL.md`** — workflows: `start`, `brainstorm`,
  `design-feature`, `implement-feature`, `art-direction`, `playtest-review`,
  `qa`, `ship-check`. Open the file that matches the task.
- **`.claude/agents/*.md`** — role cards for subagent or task flows.

## Cursor only

**`.cursor/skills`** is a **symlink** to **`.claude/skills`** for Cursor. Codex
and other CLIs do not use that path for discovery; use **`.claude/skills`**
directly.
