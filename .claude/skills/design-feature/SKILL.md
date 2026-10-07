---
name: design-feature
description: >-
  Designer-led feature spec. Writes design/features/<slug>.md and stops.
  Developer and artist fill their own sections in a later turn.
---

# /design-feature -- Lean feature spec

## Who writes this turn

- **game-designer** (default): intent, rules, scope, risk, acceptance.
  Leave developer and artist sections as `TBD`.
- **game-developer**, only when the file already exists: fill
  `## Developer notes` only.
- **game-artist**, only when the file already exists: fill
  `## Visual / UI notes` only.

Do not write another role's sections.

## Target

`design/features/<slug>.md` (`<slug>` is kebab-case).

## Steps (designer)

1. **Name the feature** in the user's language; confirm **why now**.
2. **Player story**: "As a player, I can..." + **success moment**.
3. **Rules** -- inputs, outputs, failure, edge cases.
4. **Not in this slice** and **Risk** (both required; see below).
5. **Acceptance** -- 3-5 testable bullets.
6. Write the file. Stop.

## Template

```markdown
# Feature: <Title>
## Why
## Player experience
## Rules & edge cases
## Not in this slice
## Risk
## Acceptance criteria
## Open questions
## Developer notes
TBD — game-developer fills this in a later turn.
## Visual / UI notes
TBD — game-artist fills this in a later turn.
```

### Not in this slice (required)

List what will **not** ship in v1. If nothing was deferred, write one
thing you considered and rejected.

### Risk (required)

Exactly three bullets, one sentence each:

- **What makes this unfun?**
- **What makes this unreadable?**
- **What makes this unmaintainable?**

Keep the file **under ~120 lines** unless the user asks for depth.

## Stop

Done when your section of the feature file is written. If `maxTurns`
hits first, add `## Blocked` with what is missing, then stop.

Ask the human, once: "Ready to `/proof-of-fun` this, then
`/implement-feature`?" Then stop. Do not start those skills yourself.

## Do not

- Roleplay the other two voices in this turn
- Hide a disagreement -- write option A vs option B and let the user choose
- Skip "Not in this slice" or "Risk"
- Generate assets or write provider prompts
