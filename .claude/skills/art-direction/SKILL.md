---
name: art-direction
description: >-
  Leads visual direction with game-artist: style, tone, asset direction, UI/FX
  notes, and cohesion rules. Updates the Art direction section of design/gdd.md
  when it exists, otherwise writes design/art-notes.md. Use when establishing
  look, rescuing inconsistency, or before a polish pass.
---

# /art-direction — Make it coherent

## Lead

**game-artist** drives. Consult **game-designer** when clarity affects
mechanics; **game-developer** when tech limits shaders, UI, or performance.

## Steps

1. **Read** `design/gdd.md` if it exists — focus on `## Art direction` and
   `## Quick context` for mode, feel, and genre.
   If `gdd.md` is absent, read `design/art-notes.md` (or note it's missing).

2. **Audit quickly**: 3 strengths + 3 honest problems in current visuals
   (from files, screenshots the user provides, or described state).

3. **Refine or define**:
   - **Palette** — primary, secondary, accent, danger/success (hex values)
   - **Shape language** — curves vs hard edges, proportions
   - **Motion** — timing personality (snappy vs floaty), restraint level
   - **UI rules** — hierarchy, one example screen described in words
   - **FX restraint** — minimal / playful / chaotic

4. **Cohesion rules** — 5–10 bullet do / don't pairs. Be specific: name
   values, timings, or shapes — not adjectives.

5. **Write output**:
   - If `design/gdd.md` exists: update only the `## Art direction` section
     in-place. Do not modify other GDD sections.
   - If it does not exist: write or update `design/art-notes.md`. Note that
     running `/start` will absorb these notes into a full GDD.

## Tone

Encouraging but specific. Replace "make it pop" with contrast, scale, or
timing numbers.

## Do not

- Demand a specific engine or pipeline
- Touch any GDD section outside `## Art direction`
- Add reference images to the repo without user request
