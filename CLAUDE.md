# Tiny Studio

*An indie game studio in your Claude Code terminal.*

## Claude / Cursor operating guide

This repository is a **small-team AI game studio**: three collaborators (developer,
designer, artist), one human creative lead (you). It is intentionally **not** a
large multi-agent pipeline.

## What this is

- **3 agents** in `.claude/agents/`: implementation, design, art — peers, not a
  corporate ladder.
- **8 slash workflows** in `.claude/skills/`: onboarding, ideation, feature design
  and build, art direction, review, QA, ship check.
- **Light docs** in `.claude/docs/`: philosophy, how we work together, how QA
  uses evidence.

## Principles (read before coding)

1. **Small team, big taste** — fewer roles, sharper intent.
2. **Fun first** — mechanics and feel beat feature lists.
3. **Clarity over complexity** — players and future-you must understand the game.
4. **Finishability** — scope that can ship beats a backlog that cannot.
5. **Soul over volume** — one memorable beat beats ten forgettable ones.
6. **You decide** — AI proposes, critiques, and collaborates; **you** approve.

## How to work here

1. Run **`/start`** when joining the project or resetting direction.
2. Use **`/brainstorm`** for early concepts; **`/design-feature`** before big work;
   **`/implement-feature`** to build in small steps.
3. **`/art-direction`** when look, UI, or mood needs a coherent pass.
4. **`/playtest-review`** for cross-discipline feedback on a slice or build.
5. **`/qa`** for evidence-based quality (run, log, capture when possible).
6. **`/ship-check`** before sharing or releasing a milestone.

## Invoking agents

Use the **Task tool** or your client’s subagent flow with:

| Agent            | File                     | Lead when…                          |
|------------------|--------------------------|-------------------------------------|
| game-developer   | `.claude/agents/game-developer.md`   | Code, engine, tools, performance    |
| game-designer    | `.claude/agents/game-designer.md`    | Loops, scope, motivation, feel      |
| game-artist      | `.claude/agents/game-artist.md`      | Look, UI tone, readability, motion  |

**Collaboration:** Any agent may **constructively** challenge another. Disagreements
are stated clearly **to you**; you resolve.

## Project artifacts (optional but useful)

| Path                 | Purpose                                      |
|----------------------|----------------------------------------------|
| `design/pillars.md`  | Creative pillars, references, non-goals      |
| `design/features/`   | Short feature specs from `/design-feature`   |
| `design/art-notes.md`| Art direction snapshots from `/art-direction`|

Create these as needed; the template does not require a heavy doc tree.

## QA and evidence

`/qa` prioritizes **observable truth**: run the game or tests, read logs, capture
screens or GIFs when the environment allows. If not, use what exists (build
output, user captures). See `.claude/docs/qa-evidence.md`.

## Cursor compatibility

Skills live under `.claude/skills/`. This repo includes **`.cursor/skills` →
`.claude/skills`** (symlink) so Cursor project skills stay a **single source of
truth**. If the link is missing or wrong after clone, see `README.md` (Cursor
skills symlink).

## Codex CLI

Root **`AGENTS.md`** is the thin bootstrap Codex reads by default; it points here
and into **`.claude/skills/`**.

---

*Tiny Studio: friends making a game, not a department org chart.*
