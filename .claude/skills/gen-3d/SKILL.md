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
**game-artist** reviews style, proportion, and usability against the GDD.

## Preconditions

1. `design/asset-plan.md` must exist with `Confirmed by developer: yes`.
2. The asset must be listed in the plan as requiring Tripo AI generation.

## Steps

1. **Read** `design/gdd.md`:
   - `## Art direction` → character proportions, environment style,
     texture/material guidelines, shape language
   - `## Enemy and obstacle design` → how this model is used in gameplay

2. **Check provider**: if `TRIPO_API_KEY` is not set, create a labeled
   placeholder mesh (primitive geometry with named material) and log the
   fallback.

3. **Generate** via Tripo AI. The `TRIPO_API_KEY` is read from the
   environment. Never print or log its value. The prompt must reference
   GDD art direction anchors (shape language, proportions, explicit avoids).

4. **Optional Blender post-process** (if `blender` is in PATH):
   - Normalize scale to project units
   - Fix orientation (Z-up, forward −Y)
   - Remove loose geometry
   - Export to `.glb` (default project format)

5. **Verify** output before accepting:
   - Scale within expected bounds for the asset's role
   - Orientation correct (no accidental rotations or flips)
   - Polygon count within GDD art direction budget
   - Materials present and named per GDD conventions
   - Export format opens without errors
   - Style consistent with GDD shape language and proportions

6. **Reject** if verification fails — retry once with a tighter prompt.
   If the second attempt also fails, fall back to placeholder and log reason.

7. **Place** in `assets/3d/<category>/` and write a metadata sidecar:

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

8. **Update** `design/asset-plan.md` — mark the asset row as `generated`
   or `placeholder`.

## Do not

- Generate LOD variants unless the GDD explicitly requires them
- Accept assets with broken normals, missing materials, or inverted faces
- Skip Blender normalization when scale is obviously wrong
- Print or log the API key value at any point
- Block the pipeline if this one asset fails — log and continue
