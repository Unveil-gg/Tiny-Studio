---
name: gen-2d
description: >-
  Generates 2D assets via the tiny-assets MCP tool gen_2d (Nano Banana /
  Gemini). Verifies dimensions, transparency, and GDD art direction before
  accepting. Falls back to placeholder when missing or output fails. Only
  runs after /asset-plan is confirmed.
---

# /gen-2d — 2D asset generation

## Lead

**game-artist** drives review. **game-developer** calls the MCP tool.

## Preconditions

1. `design/asset-plan.md` must exist with `Confirmed by developer: yes`.
2. The asset must be listed as Nano Banana generation.
3. **`tiny-assets` MCP** must be enabled (see `.claude/docs/assets-setup.md`).

## Steps

1. **Read** `design/gdd.md` — `## Art direction`, especially
   `### Explicitly avoid`.
2. **Read** `design/asset-plan.md` — confirm approval and dimensions.
3. **Call** `gen_2d` with:
   - `prompt` — palette hex values, shape language, avoids from GDD
   - `purpose` — asset name from the plan
   - `category` — e.g. `sprites`, `ui`, `icons`
   - `model` — `nano-banana-2` (default), `nano-banana-pro` when the
     plan needs legible baked text
   - `width` / `height` — from plan when specified (0 = model default)
   - `has_alpha` — true for sprites, false for opaque UI panels
4. **Inspect** tool result. Placeholder when `provider` is `placeholder`.
5. **Verify** before accepting:
   - Dimensions match plan
   - Transparency correct when `has_alpha` is true
   - Readable at intended display size
   - Nothing from `### Explicitly avoid` appears in output
6. **Reject** if checks fail — one retry with a tighter prompt naming
   what failed. Then keep placeholder and log.
7. **Update** `design/asset-plan.md` — mark `generated` or `placeholder`.

## Do not

- Accept output violating `### Explicitly avoid`
- Use `nano-banana-pro` by default — only when the plan requires it
- Print or log API key values
- Block the pipeline on a single asset failure
