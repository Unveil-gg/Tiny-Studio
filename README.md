<div align="center">

<img src="assets/logo.png" alt="Tiny Studio" width="200" />

*An indie game studio in your terminal or editor.*

[![Join us on Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/gaZ5XuPhz)

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

- **Three agents, many skills** — developer, designer, and artist voices plus
  slash workflows from `/start` through `/vertical-slice`, scoped for small teams.
- **Client-flexible, engine-agnostic** — use **Claude Code**, **Cursor**, or
  **Codex CLI**; no required `src/` layout or engine stack in the template.
- **Optional MCP servers** — screen snapshots (`tiny-vision`) and asset
  generation (`tiny-assets`) when you want evidence and real audio/2D/3D output.
- **Single source for skills** — edit **`.claude/skills/`** only; Cursor stays in
  sync via **`.cursor/skills`** when the symlink is intact
  ([TROUBLESHOOTING.md](TROUBLESHOOTING.md) if not).

## What this is

- **`CLAUDE.md`** — master operating guide for the repo.
- **`AGENTS.md`** — thin bootstrap for **Codex CLI** (and other tools that read
  `AGENTS.md`); full detail stays in **`CLAUDE.md`**.
- **`.claude/agents/`** — exactly **three** agents: `game-developer`,
  `game-designer`, `game-artist`.
- **`.claude/skills/`** — slash workflows (`/start`, `/brainstorm`, …).
- **`.cursor/skills`** — symlink to **`.claude/skills/`** so Cursor stays in sync
  (**Cursor only** — see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)).
- **`.claude/docs/`** — philosophy, collaboration, QA-evidence, and optional
  MCP setup:
  - [vision-setup.md](.claude/docs/vision-setup.md) — `tiny-vision`
  - [assets-setup.md](.claude/docs/assets-setup.md) — `tiny-assets`
- **`.claude/settings.json`** — starter permission hints you can extend.

There is **no** mandatory `src/`, engine, or engine-specific stack — add your game
where you like; the template stays lightweight.

## Quick start

1. Copy this folder or use it as a **GitHub template** (when published).
2. Open the project in **Claude Code**, **Cursor**, or **Codex CLI**.
   - **Cursor:** project skills come from **`.cursor/skills`** → **`.claude/skills`**
     (verify the symlink in [TROUBLESHOOTING.md](TROUBLESHOOTING.md), especially on
     **Windows**).
   - **Codex CLI:** reads **`AGENTS.md`** → **`CLAUDE.md`** → skill files.
     Agent Skills live under `.agents/skills` ([docs](https://developers.openai.com/codex/skills)); copy or symlink `.claude/skills/<name>` there to reuse.
3. Run **`/start`** to onboard and write **`design/gdd.md`** (design + art direction).
4. When building gameplay: **`/brainstorm`**, **`/design-feature`**,
   **`/implement-feature`** in that order.
5. Before you show a build: **`/qa`** and **`/ship-check`**.

### Slash commands (skills)

| Command              | Purpose                                      |
|----------------------|----------------------------------------------|
| `/start`             | Onboard; write `design/gdd.md`               |
| `/brainstorm`        | Shape concepts, verbs, emotional goals       |
| `/design-feature`    | Lean feature spec (designer-led)             |
| `/implement-feature` | Build in slices (developer-led)              |
| `/art-direction`     | Refine GDD art direction section             |
| `/playtest-review`   | All three perspectives on a slice or idea    |
| `/qa`                | Evidence-first quality pass                  |
| `/ship-check`        | Share/release readiness for the stated scope |
| `/asset-plan`        | Asset budget; gate paid API calls            |
| `/gen-audio`         | Audio via ElevenLabs MCP                     |
| `/gen-2d`            | 2D via Nano Banana MCP                       |
| `/gen-3d`            | 3D via Tripo MCP (draft → optional refine)   |
| `/vertical-slice`    | Full slice: plan → generate → playtest       |

Names may appear with or without the slash depending on your client. Skill files:
**`.claude/skills/<name>/SKILL.md`**.

### Optional MCP servers

Both are **optional**. Skills work without them; placeholders are used when
providers are missing.

#### Vision — `tiny-vision`

Screen snapshots for playtest evidence. See
**[.claude/docs/vision-setup.md](.claude/docs/vision-setup.md)**.

```powershell
pip install -r requirements-vision.txt
# Cursor MCP: python -m core.vision.mcp_server  (cwd = repo root)
```

#### Assets — `tiny-assets`

Real audio, 2D, and 3D generation. API keys stay in the server process — never
returned to the LLM. Missing keys are **non-blocking**; those asset types use
placeholders while configured providers continue.

See **[.claude/docs/assets-setup.md](.claude/docs/assets-setup.md)** for full setup.

**Install:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-assets.txt
```

**Environment variables** (set only what you need):

| Provider    | Variable                          |
|-------------|-----------------------------------|
| ElevenLabs  | `ELEVENLABS_API_KEY`              |
| Tripo AI    | `TRIPO_API_KEY`                   |
| Nano Banana | `GEMINI_API_KEY` or `GOOGLE_API_KEY` |

**Cursor MCP config:**

- **Command:** venv `python`
- **Args:** `-m`, `core.assets.mcp_server`
- **Working directory:** this repo root
- **`tool_timeout_sec`:** `200` (Tripo refine can take up to ~180s)

**Check providers (CLI):**

```powershell
python -m core.assets.providers
```

**Tools exposed:** `check_asset_providers`, `gen_audio`, `gen_2d`,
`gen_3d_draft`, `gen_3d_refine`

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
