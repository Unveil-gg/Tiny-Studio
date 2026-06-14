---
name: gen-2d
description: >-
  Generates 2D assets using Nano Banana (Google AI Studio). Verifies
  dimensions, transparency, readability, composition, and ADD consistency
  before accepting. Falls back to placeholder if provider is missing or
  output fails checks. Only runs after /asset-plan is confirmed.
---

# /gen-2d — 2D asset generation

## Lead

**game-artist** drives and reviews every output against the ADD before
accepting. **game-developer** handles API calls and asset integration.

## Preconditions

1. `design/asset-plan.md` must exist with `Confirmed by developer: yes`.
2. The asset must be listed in the plan as requiring Nano Banana generation.
3. Run `/check-providers` if `GOOGLE_API_KEY` status is unknown.

## Steps

1. **Read** `design/add.md` — visual style, color palette, iconography style,
   texture guidelines, and critically the "Explicitly avoid" list.
2. **Read** `design/gdd.md` — how this asset is used in gameplay (affects
   required dimensions, alpha needs, and composition priority).
3. **Check providers**: if `GOOGLE_API_KEY` is `missing`, create a labeled
   placeholder (solid rectangle in palette color with asset name overlaid)
   and log the fallback.
4. **Generate** via Nano Banana (Google AI Studio). The `GOOGLE_API_KEY` is
   read from the environment. Never print or log its value. The prompt must
   reference ADD anchors: palette (use hex values), shape language, style
   inspirations, and the full "Explicitly avoid" list.
5. **Verify** output before accepting:
   - Dimensions match project spec (power-of-2 if texture, exact px if UI)
   - Transparency correct: no white fringe on sprites, alpha channel present
     where the asset requires it
   - Readable at intended display size (scale down and inspect)
   - Composition serves the asset's in-game purpose
   - Style consistent with ADD palette and shape language
   - Nothing from the ADD "Explicitly avoid" list visible in the output
6. **Reject** if any check fails — retry once with a tighter prompt that
   explicitly names what was wrong. If the second attempt also fails, fall
   back to placeholder and log the reason.
7. **Place** verified asset in `assets/2d/<category>/` and write a metadata
   sidecar:

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

8. **Update** `design/asset-plan.md` — mark the asset row as `generated`
   or `placeholder`.

## Do not

- Accept output that contradicts the ADD "Explicitly avoid" list
- Generate multiple variants by default — one clean asset per slot
- Skip the at-scale readability check before accepting
- Print or log the API key value at any point
- Block the pipeline if this one asset fails — log and continue
