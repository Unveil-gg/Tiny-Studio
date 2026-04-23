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
**Cursor** loads them through **`.cursor/skills`** (a symlink; see below).

## What this is

- **`CLAUDE.md`** — master operating guide for the repo.
- **`AGENTS.md`** — thin bootstrap for **Codex CLI** (and other tools that read
  `AGENTS.md`); full detail stays in **`CLAUDE.md`**.
- **`.claude/agents/`** — exactly **three** agents: `game-developer`,
  `game-designer`, `game-artist`.
- **`.claude/skills/`** — **eight** workflows (`/start`, `/brainstorm`, …).
- **`.cursor/skills`** — symlink to **`.claude/skills/`** so Cursor stays in sync
  (**Cursor only** — see [Cursor symlink](#cursor-symlink-cursor-only)).
- **`.claude/docs/`** — philosophy, collaboration, QA-evidence, and optional
  **vision MCP** setup (`.claude/docs/vision-setup.md`).
- **`.claude/settings.json`** — starter permission hints you can extend.

There is **no** mandatory `src/`, engine, or engine-specific stack — add your game
where you like; the template stays lightweight.

## Quick start

1. Copy this folder or use it as a **GitHub template** (when published).
2. Open the project in **Claude Code**, **Cursor**, or **Codex CLI**.
   - **Cursor:** project skills come from **`.cursor/skills`** → **`.claude/skills`**
     ([verify the symlink](#cursor-symlink-cursor-only), especially on **Windows**).
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

## Cursor symlink (Cursor only)

This section matters **only if you use Cursor** and want `/start`, `/qa`, etc. as
project skills. **Codex CLI** does not read `.cursor/skills`; use **`.agents/skills`**
for Codex ([skills doc](https://developers.openai.com/codex/skills)).

**`.cursor/skills`** must be a **directory symlink** to **`../.claude/skills`**
(Git mode `120000`). Edit skills only under **`.claude/skills/`**.

### Windows (Git) — set once, ideally before clone

Without this, Git on Windows may check out the link as a **plain text file**
instead of a symlink:

```powershell
git config --global core.symlinks true
```

Repo-only: `git config core.symlinks true`, then re-clone or re-checkout
`.cursor/skills`.

### Verify after clone

**Windows (PowerShell), from repo root:**

```powershell
Get-Item .cursor/skills | Select-Object LinkType, Target
```

Expect **`SymbolicLink`** and **`..\.claude\skills`** (or `../.claude/skills`).

**macOS / Linux:**

```bash
ls -la .cursor/skills
```

Expect a line starting with **`l`** pointing at **`../.claude/skills`**.

### Fix a broken or missing link

From **repo root**, remove the bad `.cursor/skills`, then either restore from Git
(after `core.symlinks true`) or recreate the symlink.

**Restore from Git (Windows):**

```powershell
Remove-Item -Recurse -Force .cursor/skills
git checkout HEAD -- .cursor/skills
```

**Create manually (Windows — Developer Mode or elevated terminal):**

```powershell
New-Item -ItemType Directory -Path .cursor -Force | Out-Null
Set-Location .cursor
cmd /c "mklink /D skills ..\.claude\skills"
Set-Location ..
```

**Create manually (macOS / Linux):**

```bash
mkdir -p .cursor
ln -sfn ../.claude/skills .cursor/skills
```

If **`mklink`** / **`ln`** fails, enable **Settings → System → For developers →
Developer Mode** on Windows (or run the shell as Administrator), then retry.

### OneDrive / cloud sync

Repos under OneDrive can break or confuse symlinks. If `.cursor/skills` keeps
misbehaving, move the repo to a normal disk or recreate the symlink after sync.

### Codex CLI — instructions file

Root **`AGENTS.md`** is the thin entry Codex loads by default. For layering and
limits, see OpenAI’s [Codex `AGENTS.md` guide](https://developers.openai.com/codex/guides/agents-md).

## How this differs from huge “game studio” repos

[Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
(and similar) offer **dozens** of agents, **many** skills, hierarchy tiers,
hooks, and broad process. That can be powerful — it can also be **noise** for a
solo dev or jam team.

**Tiny Studio** keeps:

- **Three roles** you can hold in your head.
- **Eight commands** that cover the real loop: **orient → ideate → specify →
  build → look → review → QA → ship check**.
- **Peer critique**, not escalation charts — **you** stay the creative director.

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
