# Tiny Studio

*An indie game studio in your Claude Code terminal.*

## Claude / Cursor operating guide

Three AI collaborators (developer, designer, artist) and you -- not a large
multi-agent pipeline.

## What this is

- **Agents:** `.claude/agents/` -- three role cards for subagent flows.
- **Skills:** `.claude/skills/` -- slash workflows (see **How to work here**).
- **Optional depth:** `.claude/docs/` -- short summaries in **Opt-in docs**;
  open files when you want the full read.

## Principles (read before coding)

1. **Small team, big taste** -- fewer roles, sharper intent.
2. **Fun first** -- mechanics and feel beat feature lists.
3. **Clarity over complexity** -- players and future-you must understand the game.
4. **Finishability** -- scope that can ship beats a backlog that cannot.
5. **Soul over volume** -- one memorable beat beats ten forgettable ones.
6. **You decide** -- AI proposes, critiques, and collaborates; **you** approve.

## Opt-in docs (human-first; `@` when useful)

| Path | In brief |
|------|----------|
| `.claude/docs/philosophy.md` | Template rationale; what we kept vs refused; decisions; taste. |
| `.claude/docs/collaboration.md` | Peer roles; who leads when; disagreement -> options for you. |
| `.claude/docs/qa-evidence.md` | `/qa` ladder: run -> logs -> captures; label guesses honestly. |
| `.claude/docs/vision-setup.md` | Optional vision MCP: screen snapshots (`take_game_snapshot`) for vibe/UI checks. |
| `.claude/docs/assets-setup.md` | Asset MCP (`tiny-assets`): `gen_audio`, `gen_2d`, `gen_3d_draft`, `gen_3d_refine`. |

## How to work here

1. **`/start`** -- onboard; set studio mode (`jam` or `studio`).
2. **`/brainstorm`** → **`/proof-of-fun`** → **`/design-feature`** → **`/implement-feature`**
3. **`/art-direction`** -- look, UI, mood.
4. **`/playtest-review`** -- all three voices on a slice.
5. **`/qa`** -- evidence-first quality pass.
6. **`/ship-check`** -- release readiness.
7. **`/retrospective`** -- post-ship loop.
8. **`/cut`** -- descope with memory.
9. **`/session-handoff`** -- end-of-session continuity.

### Asset generation (vertical slice)

`/start` creates `design/gdd.md` — the single source of truth for design,
art direction, and generation. Run it first.

10. **`/gen-gdd`** -- deepen or restructure `design/gdd.md` after `/start`.
    Use when specific sections are thin or the design has shifted.
11. **`/asset-plan`** -- minimal asset budget. Presents estimated API calls
    and waits for your confirmation before any paid provider is used.
12. **`/gen-audio`** -- generate audio via ElevenLabs (`gen_audio` MCP); verify before accepting.
13. **`/gen-3d`** -- generate 3D via Tripo (`gen_3d_draft` / `gen_3d_refine` MCP).
14. **`/gen-2d`** -- generate 2D via Nano Banana (`gen_2d` MCP); verify against GDD.
15. **`/vertical-slice`** -- master orchestration: provider check → asset plan
    confirmation → generation → integration → `/qa`. Runs
    `tools/orchestration/pipeline.py` for a status summary when Python is
    available.

## Invoking agents

Use the **Task tool** or your client's subagent flow with:

| Agent | File | Lead when... |
|-------|------|-------------|
| game-developer | `.claude/agents/game-developer.md` | Code, engine, tools, performance |
| game-designer | `.claude/agents/game-designer.md` | Loops, scope, motivation, feel |
| game-artist | `.claude/agents/game-artist.md` | Look, UI tone, readability, motion |

## Project artifacts (optional)

| Path | Purpose |
|------|---------|
| `design/gdd.md` | Single source of truth — design + art direction (from `/start`) |
| `design/features/` | Feature specs from `/design-feature` |
| `design/art-notes.md` | Art scratchpad from `/art-direction` (pre-GDD or supplemental) |
| `design/asset-plan.md` | Asset budget and approval record from `/asset-plan` (optional) |
| `design/pillars.md` | Legacy — superseded by `gdd.md`; kept for backward compat |
| `design/session-log.md` | Session handoffs from `/session-handoff` |
| `design/retros.md` | Retrospectives from `/retrospective` |
| `assets/audio/` | Generated audio assets |
| `assets/3d/` | Generated 3D model assets |
| `assets/2d/` | Generated 2D assets |
| `tools/orchestration/` | Pipeline checker (pure Python, no framework) |
| `core/assets/` | Asset generation MCP (`tiny-assets`) |

## Tooling notes

- **Cursor:** `.cursor/skills` -> `.claude/skills` (symlink). Wrong link after
  clone -> **`TROUBLESHOOTING.md`**.
- **Asset MCP:** `tiny-assets` — see **`.claude/docs/assets-setup.md`**.
- **Codex CLI** (and similar): default read is **`AGENTS.md`**; it points here.

---

*Tiny Studio: friends making a game, not a department org chart.*
