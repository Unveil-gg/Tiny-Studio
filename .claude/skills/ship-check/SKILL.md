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

1. **Re-read** `design/pillars.md` — does the build **express** them?
2. **Smoke** — if possible, launch once (same evidence rules as `/qa`).
3. **Cross-voice summary** (short):
   - **Designer** — is the core loop understandable in minutes?
   - **Developer** — crashes, saves, platforms, known blockers?
   - **Artist** — first-screen read, UI honesty, embarrassing placeholders?
4. **Audience** — who is this for, and one sentence **why play**?
5. **Verdict**: `ship`, `ship with caveats`, or `not yet` — with **3** concrete
   next steps max.

## Output

Keep under one page. Include **known issues** the user should **disclose** in
release notes (transparency builds trust).

## Do not

- Block on imaginary standards
- Hide risks — **ship with caveats** is a valid outcome
