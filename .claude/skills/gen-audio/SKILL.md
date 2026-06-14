---
name: gen-audio
description: >-
  Generates audio assets using ElevenLabs. Normalizes output and verifies
  duration, loudness, looping suitability, and purpose before accepting.
  Falls back to placeholder if provider is missing or output fails.
  Only runs after /asset-plan is confirmed.
---

# /gen-audio — Audio generation

## Lead

**game-developer** runs generation. **game-artist** reviews output against
the GDD audio direction.

## Preconditions

1. `design/asset-plan.md` must exist with `Confirmed by developer: yes`.
2. The asset must be listed in the plan as requiring generation (not
   already marked `placeholder`).

## Steps

1. **Read** `design/gdd.md` → `## Art direction` → `### Audio direction`
   (SFX palette, music genre anchor, dry/wet balance).
2. **Read** `design/asset-plan.md` → confirm this asset is approved and
   ElevenLabs is listed as its provider.
3. **Check provider**: if `ELEVENLABS_API_KEY` is not set, skip generation,
   create a placeholder (labeled silent file or tone stub), and log the
   fallback. Never attempt to call the API when the key is absent.
4. **Generate** via ElevenLabs API. The `ELEVENLABS_API_KEY` is read from
   the environment by the API client. Never print or log its value.
5. **Verify** output before accepting:
   - Duration within expected range for its intended use
   - Loudness normalized (target −14 LUFS or project standard)
   - Loop point clean if flagged as looping
   - No clipping, pops, DC offset, or excessive silence
   - Consistent with GDD audio direction
6. **Reject** if any check fails — retry once with a refined prompt. If the
   second attempt also fails, fall back to placeholder and log the reason.
7. **Place** in `assets/audio/<category>/` and write a metadata sidecar:

   ```json
   {
     "name": "",
     "provider": "elevenlabs | placeholder",
     "duration_s": 0,
     "lufs": 0,
     "loops": false,
     "purpose": "",
     "generated_at": ""
   }
   ```

8. **Update** `design/asset-plan.md` — mark the asset row as `generated`
   or `placeholder`.

## Do not

- Call ElevenLabs without a confirmed asset plan
- Accept clipped or obviously broken output
- Generate variants unless explicitly listed in the asset plan
- Print or log the API key value at any point
- Block the pipeline if this one asset fails — log and continue
