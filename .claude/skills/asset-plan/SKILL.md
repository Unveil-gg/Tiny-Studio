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

2. **Check providers** via MCP `check_asset_providers` or:
   `python -m core.assets.providers`
   Report each provider's status. Missing or unavailable providers use
   placeholders for their asset types — **do not block** the plan or
   generation for providers that are configured.

3. **Draft** the asset budget using the template below. Apply the
   stinginess rule for every asset:
   > "Does custom generation materially improve this playable slice,
   > or can a placeholder serve the same purpose?"
   When in doubt, mark it `placeholder`.

4. **Present** to the developer:
   - Total estimated external API calls (configured providers only)
   - Which providers would be called
   - Asset count vs placeholder count
   - Which providers are missing and will fall back to placeholders

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
- Block the plan because one provider is missing
- Add environment filler not in the GDD slice scope
- Generate variants by default — one canonical asset per slot
