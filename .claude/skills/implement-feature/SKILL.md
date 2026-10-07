---
name: implement-feature
description: Developer-led build in slices; verifies design/visual intent before coding. Use after feature is specified.
---

# /implement-feature -- Build the thing

## Lead

**game-developer** only. If behavior is ambiguous, write the question under
`## Developer notes` and stop. Do not roleplay the designer or the artist.
Read `design/specs/art_style.md` for readability and UI constraints.

## Target

The code slice, plus `design/specs/schema.json` when the data shape changes.
The feature file's `## Developer notes` records what you built.

## Preconditions

- Prefer an existing `design/features/<slug>.md`. If missing, draft a
  micro-spec in that file (5 bullets max) and get user confirmation
  before large edits.
- Read `studio.config.json` `studioMode` (`jam` vs `studio`) and
  `design/specs/mechanics.md`. Calibrate quality gates from those.

## Steps

1. **Restate** the feature in one paragraph -- dev voice.
2. **Check intent** -- any contradictions with mechanics or the index?
   Flag them in `## Developer notes` and stop if they block the slice.
3. **Plan** the smallest shippable slice (tasks in order).
4. **Implement** one slice at a time:
   - After each slice, **stop and check**:

     > Stop. Does this slice run? What is broken? Do not begin the next slice
     > until the current slice is confirmed playable or the breakage is logged.

   - Note how to **run / try** it before moving on.
5. **Self-review** against acceptance criteria. List missing feedback.
   If a slot is needed, append metadata to `design/specs/asset_hooks.json`
   (`id`, `kind`, `purpose`, `status: "unassigned"`). Do not generate files.

## Engineering habits

- Prefer **data/config** for tuning when the designer will iterate numbers.
- Avoid drive-by refactors outside the feature unless necessary for safety.
- Log or expose **debug views** temporarily if it speeds validation (remove or
  gate later).

## Stop

Done when this slice runs (or the breakage is logged in `## Developer notes`)
and schema changes still pass `npm run validate`. If `maxTurns` hits first,
add `## Blocked` to the feature file and stop.

Suggest `/playtest-review` or `/qa` when something is runnable. Do not
start those skills in this turn.

## Do not

- Gold-plate or expand scope without user approval
- Skip mentioning breaking changes
- Begin the next slice while the current one is broken and unlogged
- Roleplay the other roles or generate binaries
