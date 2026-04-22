# Tiny Studio

*An indie game studio in your Claude Code terminal.*

## Claude / Cursor operating guide

Three AI collaborators (developer, designer, artist) and you — not a large
multi-agent pipeline.

## What this is

- **Agents:** `.claude/agents/` — three role cards for subagent flows.
- **Skills:** `.claude/skills/` — slash workflows (see **How to work here**).
- **Optional depth:** `.claude/docs/` — short summaries in **Opt-in docs**;
  open files when you want the full read.

## Principles (read before coding)

1. **Small team, big taste** — fewer roles, sharper intent.
2. **Fun first** — mechanics and feel beat feature lists.
3. **Clarity over complexity** — players and future-you must understand the game.
4. **Finishability** — scope that can ship beats a backlog that cannot.
5. **Soul over volume** — one memorable beat beats ten forgettable ones.
6. **You decide** — AI proposes, critiques, and collaborates; **you** approve.

## Opt-in docs (human-first; `@` when useful)

| Path | In brief |
|------|----------|
| `.claude/docs/philosophy.md` | Template rationale; what we kept vs refused; decisions; taste. |
| `.claude/docs/collaboration.md` | Peer roles; who leads when; disagreement → options for you. |
| `.claude/docs/qa-evidence.md` | `/qa` ladder: run → logs → captures; label guesses honestly. |

## How to work here

1. **`/start`** — join or reset direction.
2. **`/brainstorm`** — early concepts; **`/design-feature`** before big work;
   **`/implement-feature`** to build in small steps.
3. **`/art-direction`** — coherent look, UI, mood.
4. **`/playtest-review`** — cross-discipline feedback on a slice or build.
5. **`/qa`** — evidence-based quality; prefer running and logs (see table
   above → `.claude/docs/qa-evidence.md`).
6. **`/ship-check`** — before sharing or shipping a milestone.

## Invoking agents

Use the **Task tool** or your client’s subagent flow with:

| Agent | File | Lead when… |
|-------|------|-------------|
| game-developer | `.claude/agents/game-developer.md` | Code, engine, tools, performance |
| game-designer | `.claude/agents/game-designer.md` | Loops, scope, motivation, feel |
| game-artist | `.claude/agents/game-artist.md` | Look, UI tone, readability, motion |

`/qa` prioritizes **observable truth**: run the game or tests, read logs, capture
screens or GIFs when the environment allows. If not, use what exists (build
output, user captures). See `.claude/docs/qa-evidence.md`.

## Project artifacts (optional)

| Path | Purpose |
|------|---------|
| `design/pillars.md` | Pillars, references, non-goals |
| `design/features/` | Feature specs from `/design-feature` |
| `design/art-notes.md` | Art snapshots from `/art-direction` |

## Tooling notes

- **Cursor:** `.cursor/skills` → `.claude/skills` (symlink). Wrong link after
  clone → **`README.md`**.
- **Codex CLI** (and similar): default read is **`AGENTS.md`**; it points here.

---

*Tiny Studio: friends making a game, not a department org chart.*
