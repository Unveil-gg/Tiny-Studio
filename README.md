<div align="center">
  <img
    src="assets/logo.png"
    alt="Tiny Studio"
    width="200"
  />
  <p>
    <em>An indie game studio in your terminal or editor.</em>
  </p>
</div>

A **Claude Code**-, **Cursor**-, and **CLI**-friendly template for solo and tiny
teams who want AI help that feels like **three talented friends in a small
studio** — not a AAA corporation. Workflows live in **`.claude/skills/`**;
**Cursor** loads them through **`.cursor/skills`**, a **symlink** to that folder.
If the link is wrong after clone, or skills never appear in Cursor, see
**[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** (common causes: **Windows** Git
checkout without symlinks, **OneDrive**, or missing **Developer Mode** /
elevated shell for `mklink`).

## Highlights

- **Three agents, eight skills** — developer, designer, and artist voices plus
  slash workflows from `/start` through `/ship-check`, scoped for small teams.
- **Client-flexible, engine-agnostic** — use **Claude Code**, **Cursor**, or
  **Codex CLI**; no required `src/` layout or engine stack in the template.
- **Single source for skills** — edit **`.claude/skills/`** only; Cursor stays in
  sync via **`.cursor/skills`** when the symlink is intact
  ([TROUBLESHOOTING.md](TROUBLESHOOTING.md) if not).

## What this is

- **`CLAUDE.md`** — master operating guide for the repo.
- **`AGENTS.md`** — thin bootstrap for **Codex CLI** (and other tools that read
  `AGENTS.md`); full detail stays in **`CLAUDE.md`**.
- **`.claude/agents/`** — exactly **three** agents: `game-developer`,
  `game-designer`, `game-artist`.
- **`.claude/skills/`** — **eight** workflows (`/start`, `/brainstorm`, …).
- **`.cursor/skills`** — symlink to **`.claude/skills/`** so Cursor stays in sync
  (**Cursor only** — see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)).
- **`.claude/docs/`** — philosophy, collaboration, QA-evidence, and optional
  **vision MCP** setup (`.claude/docs/vision-setup.md`).
- **`.claude/settings.json`** — starter permission hints you can extend.

There is **no** mandatory `src/`, engine, or engine-specific stack — add your game
where you like; the template stays lightweight.

## Quick start

1. Copy this folder or use it as a **GitHub template** (when published).
2. Open the project in **Claude Code**, **Cursor**, or **Codex CLI**.
   - **Cursor:** project skills come from **`.cursor/skills`** → **`.claude/skills`**
     (verify the symlink in [TROUBLESHOOTING.md](TROUBLESHOOTING.md), especially on
     **Windows**).
   - **Codex CLI:** reads **`AGENTS.md`** by default; follow into **`CLAUDE.md`**
     and skill files as needed. Codex **Agent Skills** are discovered under
     **`.agents/skills`** at the repo root ([OpenAI: Agent Skills](https://developers.openai.com/codex/skills)) — not `.claude/skills`. To reuse these
     workflows in Codex, copy or symlink skill folders there (same `SKILL.md`
     layout).
3. Run **`/start`** (or your client’s equivalent) to detect state and write
   **`design/pillars.md`**.
4. When building something new: **`/brainstorm`**, **`/design-feature`**,
   **`/implement-feature`** in that order.
5. Before you show a build: **`/qa`** and **`/ship-check`**.

### Slash commands (skills)

| Command              | Purpose                                      |
|----------------------|----------------------------------------------|
| `/start`             | Onboard: engine, pillars, feel, scope        |
| `/brainstorm`        | Shape concepts, verbs, emotional goals       |
| `/design-feature`    | Lean feature spec (designer-led)             |
| `/implement-feature` | Build in slices (developer-led)              |
| `/art-direction`     | Cohesion, palette, UI/motion rules           |
| `/playtest-review`   | All three perspectives on a slice or idea  |
| `/qa`                | Evidence-first quality pass                  |
| `/ship-check`        | Share/release readiness for the stated scope |

Names may appear with or without the slash depending on your client. Skill files:
**`.claude/skills/<name>/SKILL.md`**.

### Invoking agents

Use your client’s **subagent** or **Task** flow with the markdown files in
`.claude/agents/`. Each file describes voice, ownership, and collaboration.

## Who it is for

- Solo developers using AI for **design + code + art direction** conversations.
- Pairs or trios who want **shared vocabulary** without enterprise workflow.
- Anyone who liked the *idea* of a “game studio in a repo” but **not** the
  **scale** of the big templates.

## Hooks

No hooks are required. Add **minimal** scripts under `.claude/hooks/` only if
they solve a **real** problem (e.g. your team wants a pre-commit lint). The
default template stays quiet.

## Customization

- Keep **`AGENTS.md`** short; put durable studio rules in **`CLAUDE.md`**.
- Edit **`CLAUDE.md`** with your non-negotiables (platform, engine, tone).
- Tighten or loosen agent prompts in **`.claude/agents/`**.
- Add **one** skill at a time under **`.claude/skills/`** — keep the set small.

## License

MIT — see `LICENSE`.
