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

## Who writes this turn

- **game-designer** (default): 30-second experience and the 5-bullet slice.
  Leave the effort line as `TBD`.
- **game-developer**, only when the slice is already in the file: fill
  **Effort estimate** only (S < 2h, M half-day, L 1+ day).
- **Human** marks go or no-go. Do not begin implementation until they do.

## Target

Append `## Proof-of-fun` to `design/features/<slug>.md` when that file
exists. Otherwise show the block and stop; do not invent a second spec.

## Steps

1. Read `design/specs/mechanics.md` and the feature file. Do not load
   another role's transcript.
2. Write only your section of the block below.
3. Stop and wait for the human. Do not start `/implement-feature`.

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

## Stop

Done when your section of the proof block is in the feature file (or
shown, if no feature file exists). If `maxTurns` hits first, add
`## Blocked` and stop.

## Do not

- Begin any code before the human marks "go"
- Expand the slice during estimation
- Write the other role's section
- Skip this step because the idea "seems obviously fun"
