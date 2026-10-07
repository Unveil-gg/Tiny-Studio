---
name: start
description: >-
  Onboards a game project. Writes the design/gdd.md index, fills
  design/specs/mechanics.md, and sets studio mode in studio.config.json.
  Use at project start or when resetting direction.
---

# /start — Project onboarding

## Goal

Orient the human and the three roles around the same files. Keep it a
conversation, not a form. This turn writes files and stops.

## Target

- `design/gdd.md` (index)
- `design/specs/mechanics.md`
- `studio.config.json` → `studioMode` only

Art style, schema, and asset hooks stay stubs unless the human volunteers
those facts in this interview.

## Steps

1. **Scan the repo** (Read, Glob, Grep): engine files (`project.godot`,
   `ProjectSettings`, `.uproject`, `package.json`, `Cargo.toml`, etc.)
   and `design/gdd.md`.

2. **Classify state**: empty / idea-only / prototype / active / unknown.
   Title `Untitled` with pillars `TBD` counts as empty.

3. **If the index already has a real title**: read it and the specs,
   summarize, ask what changed. Do not start over.

4. **Interview** (one compact block; infer what the repo already shows):
   - Working title or codename?
   - Engine, language, primary platform?
   - Core fantasy — one sentence.
   - **Studio mode** (required):
     > **jam** — ship fast, one pillar, ugly ok
     > **studio** — quality gates, refactor ok, perf matters

5. **Write**:
   - Index: title, mode, engine, up to three pillars, links unchanged.
   - Mechanics: **jam** fills Verbs, Loop, and Win / lose; leave the
     rest `TBD`. **studio** fills every required heading. Ask up to
     two follow-ups if camera, controls, or win/lose are still unclear
     — put camera and controls under Loop or State machine, not new
     required headings.
   - Set `studioMode` in `studio.config.json` to `jam` or `studio`.
     Do not change turn budgets or paths.
   - Bump `revision` and `updated` on every file you change. Keep
     `## Changelog` to the latest 5 bullets.

6. Run `npm run validate`. If it fails, fix the files once.

7. **Confirm**: "Anything wrong? You have final edit rights."

## Index shape

```markdown
---
revision: 1
updated: YYYY-MM-DD
---

# <title>

_Index only. Owned specs live under design/specs/._

## Studio

- Mode: jam | studio
- Engine / language / platform:
- Pillars (3 max):

## Specs

- [Mechanics](specs/mechanics.md) — designer
- [Schema](specs/schema.json) — developer
- [Art style](specs/art_style.md) — artist
- [Asset hooks](specs/asset_hooks.json) — slot metadata
```

Required mechanic headings: `Verbs`, `Loop`, `Progression`,
`Win / lose`, `State machine`.

## Mode affects later skills

- **jam**: skip optional gates, `TBD` art is fine
- **studio**: `/proof-of-fun` before implementation, `/qa` regression
  table, `/retrospective` after each ship

## Stop

Done when the index and mechanics are written and `npm run validate`
passes. If `maxTurns` hits first, add `## Blocked` to mechanics with
what is missing, then stop.

## Do not

- Rewrite a filled index without reading it first
- Roleplay the developer or the artist
- Add generation prompts or binary assets
- Invent headings the validator does not require
- Spawn other agents
