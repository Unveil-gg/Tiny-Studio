---
name: art-direction
description: >-
  Artist-led visual spec. Writes design/specs/art_style.md (palette, type,
  layout, motion). Specs only — no binary generation. Use when establishing
  look, rescuing inconsistency, or before a polish pass.
---

# /art-direction — Make it coherent

## Lead

**game-artist** only. Read mechanics for context. Do not roleplay the
designer or the developer in this turn.

## Target

`design/specs/art_style.md`

You may append slots to `design/specs/asset_hooks.json`. Each slot is
only `id`, `kind` (`model` | `sprite` | `audio` | `ui`), `purpose`
(a design label), and `status` (`unassigned`).

## Steps

1. **Read** `design/gdd.md`, `design/specs/art_style.md`, and
   `design/specs/mechanics.md`.

2. **Audit quickly**: 3 strengths + 3 honest problems (from files,
   screenshots the user provides, or described state).

3. **Fill the four sections** with concrete values:
   - **Palette** — `#RRGGBB` for background, foreground, accent, danger
   - **Type** — heading, body, label, caption sizes
   - **Layout** — spacing, corner radius, z-order bands
   - **Motion** — action feedback, transition, and idle timing in ms
   - Use `TBD` for an unknown value. Do not drop a section.

4. **Cohesion** — 5–10 do / don't pairs inside those sections. Name
   values, timings, or shapes.

5. Bump `revision` and `updated`. Keep `## Changelog` to 5 bullets.

6. Run `npm run validate`. If it fails, fix once.

## Tone

Encouraging but specific. Replace "make it pop" with contrast, scale,
or timing numbers.

## Stop

Done when `art_style.md` validates. If `maxTurns` hits first, add
`## Blocked` with what is missing, then stop.

## Do not

- Demand a specific engine or pipeline
- Edit mechanics, schema, or the index pillars
- Generate images, audio, or meshes
- Write a provider prompt into the hook file
- Add reference images to the repo without user request
