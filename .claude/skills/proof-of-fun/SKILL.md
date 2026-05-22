---
name: proof-of-fun
description: >-
  Mandatory gate between brainstorm and implementation. Answers "is this
  actually fun to play for 30 seconds?" Designer defines the smallest runnable
  slice; developer estimates effort; human approves or kills. No code before
  go/no-go.
---

# /proof-of-fun -- Fun gate

## Purpose

Stop wasted implementation by forcing a concrete, human-approved answer to:
**"Is this worth 30 seconds of a player's attention right now?"**

## Trigger

Run this before any `/implement-feature` that came from `/brainstorm`. Skip
only when an explicit feature spec already has a confirmed slice.

## Roles

- **game-designer** -- defines the smallest runnable slice (5 bullets max)
- **game-developer** -- estimates effort: S (< 2h), M (half-day), L (1+ day)
- **Human** -- approves (go) or kills (no-go) before any code is written

## Steps

1. **Designer** describes the 30-second experience in plain language:
   what does the player do, what do they feel, what makes them want to do it
   again?
2. **Designer** lists the smallest runnable slice -- 5 bullets max. Every
   bullet must be playable, not infrastructure.
3. **Developer** estimates effort (S / M / L) and flags any hidden complexity.
4. **Present to human** -- one compact block (see output format below).
5. **Wait for human decision.** Do not begin implementation until you have an
   explicit go.

## Output format (fixed)

```markdown
## Proof-of-fun: <feature name>

**30-second experience:** <one sentence>

**Smallest runnable slice:**
- <bullet 1>
- <bullet 2>
- ...

**Effort estimate:** S / M / L -- <one-line rationale>

**Decision:** [ ] go  [ ] no-go  [ ] revise slice
```

## Do not

- Begin any code before the human marks "go"
- Expand the slice during estimation
- Skip this step because the idea "seems obviously fun"
