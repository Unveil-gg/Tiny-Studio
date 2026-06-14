---
name: asset-plan
description: >-
  Reads design/gdd.md and builds a minimal asset budget. Presents estimated
  API calls to the developer and waits for confirmation before any paid
  provider is used. Writes design/asset-plan.md. Run after /start.
---

# /asset-plan — Asset budget and confirmation gate

## Lead

**game-developer** drives. All three agents review before presenting to
the developer.

## Precondition

`design/gdd.md` must exist with a confirmed `## Vertical slice scope`
section. If missing, stop and run `/start` first.

## Steps

1. **Read** `design/gdd.md`:
   - `## Vertical slice scope` — what assets the slice explicitly needs
   - `## Art direction` — style, materials, audio direction
   - `## Enemy and obstacle design` — 3D/2D asset count hints

2. **Check providers** (inline — do not call the check-providers skill):
   - ElevenLabs: `ELEVENLABS_API_KEY` env var set? → configured / missing
   - Tripo AI: `TRIPO_API_KEY` env var set? → configured / missing
   - Nano Banana: `GOOGLE_API_KEY` env var set? → configured / missing
   - Blender: `blender --version` exits 0? → installed / unavailable

   Or run: `python tools/orchestration/providers.py`

3. **Draft** the asset budget using the template below. Apply the
   stinginess rule for every asset:
   > "Does custom generation materially improve this playable slice,
   > or can a placeholder serve the same purpose?"
   When in doubt, mark it `placeholder`.

4. **Present** to the developer:
   - Total estimated external API calls
   - Which providers would be called
   - Asset count vs placeholder count

5. **Wait for explicit confirmation** before writing. Silence is not approval.

6. **Write** `design/asset-plan.md` with `Confirmed by developer: yes`.

## Template: `design/asset-plan.md`

```markdown
# Asset Plan — <title> vertical slice

_Last updated: <date>_
_Confirmed by developer: no_

## 3D models

| Asset | Provider | Placeholder ok? | Est. calls |
|-------|----------|-----------------|------------|

## 2D assets

| Asset | Provider | Placeholder ok? | Est. calls |
|-------|----------|-----------------|------------|

## Audio assets

| Asset | Provider | Placeholder ok? | Est. calls |
|-------|----------|-----------------|------------|

## Summary

- Total external API calls: N
- Providers required: list
- Assets using placeholders: N / total
```

## Do not

- Call any paid provider before the developer confirms
- Add environment filler not in the GDD slice scope
- Generate variants by default — one canonical asset per slot
- Block if a provider is missing — mark affected assets as `placeholder`
