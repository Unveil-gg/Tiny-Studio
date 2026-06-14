---
name: gen-3d
description: >-
  Generates 3D models via tiny-assets MCP tools gen_3d_draft and
  gen_3d_refine (Tripo AI). Draft first; refine only after developer
  approval. Falls back to placeholder when missing or broken. Only runs
  after /asset-plan is confirmed.
---

# /gen-3d — 3D model generation

## Lead

**game-developer** runs MCP tools. **game-artist** reviews style and
usability against the GDD.

## Preconditions

1. `design/asset-plan.md` must exist with `Confirmed by developer: yes`.
2. The asset must be listed as Tripo AI generation (not `placeholder`).
3. **`tiny-assets` MCP** must be enabled (see `.claude/docs/assets-setup.md`).

## Workflow

### Step 1 — Draft (always)

1. **Read** `design/gdd.md` — art direction + enemy/obstacle usage.
2. **Call** `gen_3d_draft` with:
   - `prompt` — GDD shape language, proportions, explicit avoids
   - `purpose` — asset name from the plan
   - `category` — e.g. `characters`, `props`, `environment`
   - `smart_low_poly` — `true` by default for game assets
   - `style` — optional modifier (`stylized`, etc.)
3. **Save** the returned `task_id` — required for refine.
4. **Verify** draft GLB: non-empty file, readable silhouette intent.
5. If draft fails → log placeholder, update asset plan, continue.

### Step 2 — Refine (developer-gated)

Only when the asset plan explicitly lists **refine** for this asset
and the developer approved the draft:

1. **Confirm** with the developer before calling (refine costs ~40–50
   credits).
2. **Call** `gen_3d_refine` with the draft `task_id`.
3. **Verify** refined GLB same as draft checks plus poly/material sanity.
4. If refine fails → keep draft GLB or placeholder; log reason.

## Credit awareness

- Draft: ~10–20 credits, ~10–15s
- Refine: ~40–50 credits, longer wait (MCP timeout ≥ 180s)

## Do not

- Call `gen_3d_refine` without a succeeded draft `task_id`
- Refine without explicit plan approval
- Retry `banned` tasks — change the prompt instead
- Block the pipeline on a single asset failure
