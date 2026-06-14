---
name: gen-gdd
description: >-
  Creates or updates design/gdd.md — the Game Design Document used by all
  generation skills. Designer-led with dev and artist input. Run before
  /asset-plan or /gen-add. Requires design/pillars.md to exist (/start first).
---

# /gen-gdd — Game Design Document

## Lead

**game-designer** drives. Pull in:
- **game-developer** — technical feasibility, controls, platform constraints
- **game-artist** — camera feel, visual style anchor

## Preconditions

Read `design/pillars.md` before writing anything. If it does not exist,
stop and run `/start` first — `gdd.md` extends pillars, it does not
replace them.

## Steps

1. **Read** `design/pillars.md` for engine, studio mode, target feel, scope.
2. **Check** whether `design/gdd.md` already exists. If it does, present a
   diff of proposed changes rather than overwriting silently.
3. **Ask up to 3 focused questions** if the request lacks detail needed to
   define the vertical slice scope. If the developer prefers speed, infer
   a small slice and confirm once before writing.
4. **Write** `design/gdd.md` using the template below. Mark genuinely unknown
   fields as `TBD` — never omit a section.
5. **Confirm** with the developer: "Anything wrong? You have final edit rights."

## Template: `design/gdd.md`

```markdown
# Game Design Document — <title>

_Last updated: <date>. References: design/pillars.md._

## Core fantasy
One sentence: what does the player feel they are?

## Genre
Primary genre + any secondary influences.

## Player actions
Bullet list of verbs the player performs (move, shoot, build, etc.).

## Camera
Perspective, angle, zoom rules.

## Controls
Platform-specific input mapping. Mark as TBD if not yet decided.

## Win / lose conditions
What ends a session in success? What ends it in failure?

## Progression
How does the player grow: skill, unlocks, difficulty curve?

## Core gameplay loop
Moment-to-moment → session → long-term arcs (three levels).

## Enemy and obstacle design
Types, behaviors, how they challenge the player actions listed above.

## Vertical slice scope
Exactly what is playable in this slice. One paragraph, tight scope.

## Not in this slice
Everything discussed but explicitly deferred. At least three items.
```

## Do not

- Write more than ~100 lines unless the developer asks for depth
- Invent pillars that contradict `design/pillars.md`
- Begin writing before the vertical slice scope is confirmed
- Move to `/gen-add` or `/asset-plan` until the developer approves this file
