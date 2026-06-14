---
name: asset-plan
description: >-
  Reads GDD and ADD, creates a minimal asset budget, and presents it for
  developer confirmation before any paid generation begins. Writes
  design/asset-plan.md. Run after /gen-gdd and /gen-add.
---

# /asset-plan — Asset budget and confirmation gate

## Lead

**game-developer** drives. All three agents review before presenting the
plan to the developer.

## Preconditions

Both `design/gdd.md` and `design/add.md` must exist and be confirmed.
If either is missing, stop and prompt — do not guess.

## Steps

1. **Read** `design/gdd.md` → vertical slice scope, enemy/obstacle types,
   player actions, platform.
2. **Read** `design/add.md` → style, materials, audio direction.
3. **Run** `/check-providers` to confirm which providers are available.
4. **Draft** the asset budget using the template below.
5. **Apply the stinginess rule**: for every asset, ask:

   > "Does custom generation materially improve this playable slice, or
   > can a placeholder serve the same role?"

   When in doubt, mark it `placeholder`.

6. **Present** the plan to the developer. Include:
   - Total estimated external API calls
   - Which providers would be called
   - Total asset count vs placeholder count

7. **Wait for explicit developer confirmation** before proceeding to any
   generation skill. A vague "ok" counts. Silence does not.

8. **Write** `design/asset-plan.md` after confirmation, setting
   `Confirmed by developer: yes`.

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

- Call any paid provider before the developer confirms this plan
- Add environment filler not explicitly required by the GDD slice
- Generate asset variants by default — one canonical asset per slot
- Block if a provider is missing — mark affected assets as `placeholder`
  and continue
