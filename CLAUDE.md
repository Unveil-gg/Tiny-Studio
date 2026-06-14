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

10. **`/check-providers`** -- sanitized status of ElevenLabs, Tripo AI,
    Nano Banana, Blender, and snapshot tools. No key values ever printed.
11. **`/gen-gdd`** -- create / update `design/gdd.md` (Game Design Document).
    Run before any generation. Requires `/start` first.
12. **`/gen-add`** -- create / update `design/add.md` (Art Direction Document).
    Formal spec used by all generation skills. Run after `/gen-gdd`.
13. **`/asset-plan`** -- minimal asset budget. Presents estimated API calls and
    waits for your confirmation before any paid provider is used.
14. **`/gen-audio`** -- generate audio via ElevenLabs; verify before accepting.
15. **`/gen-3d`** -- generate 3D models via Tripo AI; optional Blender
    post-process; verify before accepting.
16. **`/gen-2d`** -- generate 2D assets via Nano Banana (Google AI Studio);
    verify against ADD before accepting.
17. **`/vertical-slice`** -- master orchestration: runs steps 11–16 in order,
    gates paid calls at the asset-plan confirmation, then runs `/qa`.
    Uses `tools/orchestration/workflow.py` (LangGraph) when Python is
    available; falls back to manual skill sequence otherwise.

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
| `design/pillars.md` | Pillars, mode, references, non-goals |
| `design/features/` | Feature specs from `/design-feature` |
| `design/art-notes.md` | Art snapshots from `/art-direction` |
| `design/gdd.md` | Game Design Document from `/gen-gdd` |
| `design/add.md` | Art Direction Document from `/gen-add` |
| `design/asset-plan.md` | Asset budget and approval record from `/asset-plan` |
| `design/session-log.md` | Session handoffs from `/session-handoff` |
| `design/retros.md` | Retrospectives from `/retrospective` |
| `assets/audio/` | Generated audio assets |
| `assets/3d/` | Generated 3D model assets |
| `assets/2d/` | Generated 2D assets |
| `tools/orchestration/` | LangGraph pipeline (optional Python layer) |

## Tooling notes

- **Cursor:** `.cursor/skills` -> `.claude/skills` (symlink). Wrong link after
  clone -> **`TROUBLESHOOTING.md`**.
- **Codex CLI** (and similar): default read is **`AGENTS.md`**; it points here.

---

*Tiny Studio: friends making a game, not a department org chart.*
