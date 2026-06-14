---
name: gen-audio
description: >-
  Generates audio assets via the tiny-assets MCP tool gen_audio (ElevenLabs).
  Verifies duration and purpose before accepting. Falls back to placeholder
  when the provider is missing or output fails. Only runs after /asset-plan
  is confirmed.
---

# /gen-audio — Audio generation

## Lead

**game-developer** runs generation. **game-artist** reviews output against
the GDD audio direction.

## Preconditions

1. `design/asset-plan.md` must exist with `Confirmed by developer: yes`.
2. The asset must be listed in the plan as requiring generation (not
   already marked `placeholder`).
3. **`tiny-assets` MCP** must be enabled (see `.claude/docs/assets-setup.md`).

## Steps

1. **Read** `design/gdd.md` → `## Art direction` → `### Audio direction`.
2. **Read** `design/asset-plan.md` → confirm this asset is approved.
3. **Call** MCP tool `gen_audio` with:
   - `prompt` — aligned with GDD audio direction
   - `purpose` — asset name from the plan
   - `category` — subfolder (e.g. `sfx`, `music`, `ui`)
   - `loops` — true when the plan marks a looping asset
   - `duration_target_s` — when the plan specifies length (0 = auto)
4. **Inspect** the tool result. If `error` is non-empty and
   `provider` is `placeholder`, log and continue — do not block.
5. **Verify** before accepting (agent judgment, not the tool):
   - Duration suitable for intended use
   - No obvious clipping or silence-only output
   - Matches GDD audio direction
6. **Reject** if checks fail — call `gen_audio` once more with a tighter
   prompt. If the second attempt fails, keep the placeholder and log why.
7. **Update** `design/asset-plan.md` — mark the row `generated` or
   `placeholder`.

## Do not

- Call `gen_audio` without a confirmed asset plan
- Print or log API key values
- Generate variants unless listed in the asset plan
- Block the pipeline if this one asset fails
