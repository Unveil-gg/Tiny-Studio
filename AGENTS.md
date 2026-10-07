# Tiny Studio — agent bootstrap

Thin entry for tools that read **`AGENTS.md`** by default (e.g. **Codex CLI**).
Full guide: **`CLAUDE.md`**.

## Pointers

- **`.claude/skills/<name>/SKILL.md`** — workflows (names match `/` commands in
  `CLAUDE.md`).
- **`.claude/agents/*.md`** — subagent role cards. Turn budgets live in
  `studio.config.json` and must match each card's `maxTurns`.

Clone / symlink help: **`TROUBLESHOOTING.md`**.

Specs: **`design/gdd.md`** (index) and **`design/specs/`**. Check them
with **`npm run validate`**.

Optional **screen snapshot MCP** (Codex / Cursor / Claude Code): see
**`.claude/docs/vision-setup.md`** (`take_game_snapshot`, `prune_snapshots`).

Asset binaries are out of repo. Slot metadata:
**`.claude/docs/external-assets.md`**.
