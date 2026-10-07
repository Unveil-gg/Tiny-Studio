---
name: ship-check
description: >-
  Final lightweight pass before sharing or releasing: coherence, presentability,
  worth shipping for the stated scope. Use for milestones, demos, jams, or early
  access drops.
---

# /ship-check — Is this worth showing?

## Intent

Answer: **For our stated scope, is this coherent and shareable?** Not “is it
AAA perfect.”

## Steps

1. **Re-read** `design/gdd.md` and the spec you own (mechanics, schema,
   or art style). Does the build express the pillars?
2. **Smoke** — if possible, launch once (same evidence rules as `/qa`).
3. **Your lens only** — one short paragraph. Do not write the other roles.
4. **Audience** — who is this for, and one sentence **why play**?
5. **Verdict**: `ship`, `ship with caveats`, or `not yet` — with **3**
   concrete next steps max.

## Target

Append your note to `design/reviews/<YYYY-MM-DD>-ship.md`.

## Output

Keep under one page. Include **known issues** the user should **disclose** in
release notes (transparency builds trust).

## Do not

- Block on imaginary standards
- Hide risks — **ship with caveats** is a valid outcome
- Write the other two roles' verdicts in this turn

## Stop

Done when your note is appended. If `maxTurns` hits first, append
`## Blocked` and stop.
