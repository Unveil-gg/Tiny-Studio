---
name: gen-3d
description: >-
  Generates 3D model assets using Tripo AI with optional Blender
  post-processing. Verifies scale, orientation, poly count, materials, and
  export format before accepting. Falls back to placeholder if provider is
  missing or output is broken. Only runs after /asset-plan is confirmed.
---

# /gen-3d — 3D model generation

## Lead

**game-developer** runs generation and Blender post-processing.
**game-artist** reviews style, proportion, and usability against the ADD.

## Preconditions

1. `design/asset-plan.md` must exist with `Confirmed by developer: yes`.
2. The asset must be listed in the plan as requiring Tripo AI generation.
3. Run `/check-providers` if Tripo AI or Blender status is unknown.

## Steps

1. **Read** `design/add.md` → character proportions, environment style,
   texture/material guidelines, shape language.
2. **Read** `design/gdd.md` → how this model is used in gameplay (affects
   LOD needs, collision shape expectations, animation requirements).
3. **Check providers**: if Tripo AI is `missing`, create a labeled placeholder
   mesh (primitive geometry with named material) and log the fallback.
4. **Generate** via Tripo AI. The `TRIPO_API_KEY` is read from the environment
   by the API client. Never print or log its value. The generation prompt
   must reference ADD style anchors (shape language, proportions,
   material style, explicit avoids).
5. **Optional Blender post-process** (run if Blender is `installed` and the
   asset needs normalization):
   - Normalize scale to project units
   - Fix orientation (Z-up, forward −Y)
   - Remove loose geometry and duplicate verts
   - Export to project format (`.glb` by default)
6. **Verify** output before accepting:
   - Scale within expected bounds for the asset's role
   - Orientation correct (no accidental rotations or flips)
   - Polygon count within ADD texture/poly budget
   - Materials present and named per ADD conventions
   - Export format opens without errors
   - Style matches ADD shape language and proportions
7. **Reject** if verification fails — retry once with a tighter prompt. If
   the second attempt also fails, fall back to placeholder and log the reason.
8. **Place** verified asset in `assets/3d/<category>/` and write a metadata
   sidecar:

   ```json
   {
     "name": "",
     "provider": "tripo | placeholder",
     "poly_count": 0,
     "format": "glb",
     "blender_processed": false,
     "purpose": "",
     "generated_at": ""
   }
   ```

9. **Update** `design/asset-plan.md` — mark the asset row as `generated`
   or `placeholder`.

## Do not

- Generate LOD variants unless the GDD explicitly requires them
- Accept assets with broken normals, missing materials, or inverted faces
- Skip Blender normalization when scale is obviously wrong
- Print or log the API key value at any point
- Block the pipeline if this one asset fails — log and continue
