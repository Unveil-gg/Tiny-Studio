---
name: playtest-review
description: >-
  Collaborative review with all three studio perspectives on a build or feature:
  clarity, fun, friction, feel, readability, delight. Produces actionable
  improvements. Use after a playable slice exists or for paper review of flow.
---

# /playtest-review — Three friends play (or imagine) the game

## Voices

Rotate **short** paragraphs:

1. **game-designer** — loop, motivation, difficulty, clarity of rules
2. **game-developer** — responsiveness, bugs, perf, implementation risks
3. **game-artist** — readability, UI, motion, mood, cohesion

## If playable

- Prefer the user or agent **running** the build (`/qa` has more detail on
  evidence). Here, focus on **interpretation**: what would confuse a new player?

## Output structure

```markdown
## Summary (one paragraph)
## What’s working (bullets)
## Friction & confusion (bullets)
## Delight opportunities (bullets)
## Action list (max 7, prioritized)
## Disagreements (if any — options for the human)
```

## Rules

- **Actionable** items only — each ties to a concrete next step.
- If something is unknown, **say so** and suggest what to observe next time.
- **Disagreements** are healthy: present A vs B without merging into mush.

## Do not

- Pretend everyone agrees when they don’t
- Write a novel — this is a review, not a postmortem
