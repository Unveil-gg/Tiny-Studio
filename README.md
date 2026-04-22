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
Cursor loads the same tree via a **symlink** at **`.cursor/skills`**.

## What this is

- **`CLAUDE.md`** — master operating guide for the repo.
- **`.claude/agents/`** — exactly **three** agents: `game-developer`,
  `game-designer`, `game-artist`.
- **`.claude/skills/`** — **eight** slash workflows (`/start`, `/brainstorm`, …).
- **`.cursor/skills`** — symlink to **`.claude/skills/`** so Cursor project
  skills stay in sync (see below).
- **`.claude/docs/`** — short philosophy, collaboration, and QA-evidence notes.
- **`.claude/settings.json`** — starter permission hints you can extend.

There is **no** mandatory `src/`, engine, or engine-specific stack — add your game
where you like; the template stays lightweight.

## Cursor skills symlink

`.cursor/skills` is a **directory symlink** to `../.claude/skills` (Git mode
`120000`). Edit skills only under **`.claude/skills/`**; Cursor reads them via
`/start`, `/qa`, etc.

### 1. Verify after clone

**Windows (PowerShell):**

```powershell
Get-Item .cursor/skills | Select-Object LinkType, Target
```

You should see `SymbolicLink` and `..\.claude\skills` (or `../.claude/skills`).

**macOS / Linux:**

```bash
ls -la .cursor/skills
```

The line should start with `l` (symlink) and point at `../.claude/skills`.

### 2. Enable symlinks in Git (Windows)

Without this, Git may check out the link as a **plain text file** instead of a
directory link.

```powershell
git config core.symlinks true
```

Then re-checkout the path (step 3) or clone again.

### 3. Fix a broken or missing link

From the **repository root**, remove the bad entry, then restore or recreate.

**Windows — restore from Git (after `core.symlinks true`):**

```powershell
Remove-Item -Recurse -Force .cursor/skills
git checkout HEAD -- .cursor/skills
```

**Windows — create manually (Developer Mode *or* elevated shell):**

```powershell
New-Item -ItemType Directory -Path .cursor -Force | Out-Null
Set-Location .cursor
cmd /c "mklink /D skills ..\.claude\skills"
Set-Location ..
```

**macOS / Linux — create manually:**

```bash
mkdir -p .cursor
ln -sfn ../.claude/skills .cursor/skills
```

### 4. If `mklink` / `ln` fails (privileges)

On Windows, turn on **Settings → System → For developers → Developer Mode** (or
run the terminal **as Administrator**), then repeat step 3.

### 5. OneDrive / cloud sync

Repos under OneDrive can be fussy with symlinks. If the link keeps breaking,
keep the repo on a normal disk or recreate the link after sync (step 3).

### Other CLI tools (e.g. Codex CLI)

There is no separate skills folder. Point your tool at **`CLAUDE.md`** and the
files under **`.claude/skills/<name>/SKILL.md`**, or add a short root
**`AGENTS.md`** that references those paths (see OpenAI’s
[Codex `AGENTS.md` guide](https://developers.openai.com/codex/guides/agents-md)).

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

## Quick start

1. Copy this folder or use it as a **GitHub template** (when published).
2. Open **Claude Code** or **Cursor** in the project (skills load from
   **`.cursor/skills`** → **`.claude/skills`**).
3. Run **`/start`** to detect state and write **`design/pillars.md`**.
4. Use **`/brainstorm`**, **`/design-feature`**, **`/implement-feature`** in
   that order when building something new.
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

Names may appear with or without the slash depending on your client; skills live
under `.claude/skills/<name>/SKILL.md`.

### Invoking agents

Use your client’s **subagent** or **Task** flow with the markdown files in
`.claude/agents/`. Each file describes voice, ownership, and collaboration.

## Hooks

No hooks are required. Add **minimal** scripts under `.claude/hooks/` only if
they solve a **real** problem (e.g. your team wants a pre-commit lint). The
default template stays quiet.

## Customization

- Edit **`CLAUDE.md`** with your non-negotiables (platform, engine, tone).
- Tighten or loosen agent prompts in **`.claude/agents/`**.
- Add **one** skill at a time under **`.claude/skills/`** — keep the set small.

## License

MIT — see `LICENSE`.
