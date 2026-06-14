---
name: gen-2d
description: >-
  Generates 2D assets using Nano Banana (Google AI Studio). Verifies
  dimensions, transparency, readability, composition, and GDD art direction
  consistency before accepting. Falls back to placeholder if provider is
  missing or output fails. Only runs after /asset-plan is confirmed.
---

# /gen-2d — 2D asset generation

## Lead

**game-artist** drives and reviews every output against the GDD art
direction before accepting. **game-developer** handles API calls and
integration.

## Preconditions

1. `design/asset-plan.md` must exist with `Confirmed by developer: yes`.
2. The asset must be listed in the plan as requiring Nano Banana generation.

## Steps

1. **Read** `design/gdd.md`:
   - `## Art direction` → visual style, color palette, iconography,
     texture guidelines, and critically `### Explicitly avoid`
   - `## Vertical slice scope` → how this asset is used in gameplay

2. **Check provider**: if `GOOGLE_API_KEY` is not set, create a labeled
   placeholder (solid rectangle in palette color with asset name overlaid)
   and log the fallback.

3. **Generate** via Nano Banana (Google AI Studio). The `GOOGLE_API_KEY`
   is read from the environment. Never print or log its value. The prompt
   must reference GDD art direction: palette (use hex values), shape
   language, style inspirations, and the full `### Explicitly avoid` list.

4. **Verify** output before accepting:
   - Dimensions match project spec (power-of-2 if texture, exact px if UI)
   - Transparency correct: no white fringe on sprites, alpha present if
     required
   - Readable at intended display size — scale down and inspect
   - Composition serves the asset's in-game purpose
   - Style consistent with GDD palette and shape language
   - Nothing from `### Explicitly avoid` visible in the output

5. **Reject** if any check fails — retry once with a tighter prompt naming
   exactly what failed. If the second attempt also fails, fall back to
   placeholder and log the reason.

6. **Place** in `assets/2d/<category>/` and write a metadata sidecar:

   ```json
   {
     "name": "",
     "provider": "nano-banana | placeholder",
     "dimensions": [0, 0],
     "has_alpha": false,
     "purpose": "",
     "generated_at": ""
   }
   ```

7. **Update** `design/asset-plan.md` — mark the asset row as `generated`
   or `placeholder`.

## Do not

- Accept output that contradicts `### Explicitly avoid` in the GDD
- Generate multiple variants by default — one clean asset per slot
- Skip the at-scale readability check before accepting
- Print or log the API key value at any point
- Block the pipeline if this one asset fails — log and continue
