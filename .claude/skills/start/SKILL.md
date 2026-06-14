---
name: start
description: >-
  Onboards a game project and produces design/gdd.md — the single source of
  truth for design, art direction, and asset generation. Sets studio mode
  (jam or studio). Use at project start or when resetting direction.
---

# /start — Project onboarding

## Goal

Orient the human + three agents so every later command shares the same
assumptions. Produce `design/gdd.md` as the single source of truth.
Keep it a **conversation**, not a form.

## Steps

1. **Scan the repo** (Read, Glob, Grep): engine files (`project.godot`,
   `ProjectSettings`, `.uproject`, `package.json`, `Cargo.toml`, etc.),
   existing `design/gdd.md` or `design/pillars.md`.

2. **Classify state**: empty / idea-only / prototype / active / unknown.

3. **If `design/gdd.md` exists**: read it, summarize what's already there,
   ask what has changed — do not start over.

4. **Interview** (one compact block; infer what the repo already shows):
   - Working title or codename?
   - Engine, language, primary platform?
   - Core fantasy — one sentence: what does the player feel they are?
   - **Studio mode** (required — record the answer):
     > **jam** — ship fast, one pillar, ugly ok
     > **studio** — quality gates, refactor ok, perf matters

5. **Write** `design/gdd.md` using the template below.
   - **jam**: fill only Quick context + gameplay sections; mark art
     direction `TBD` unless the user volunteers specifics.
   - **studio / build mode**: fill all sections; ask up to 2 follow-up
     questions if critical fields (camera, controls, win/lose) are unclear.

6. **Confirm**: "Anything wrong? You have final edit rights."

## Template: `design/gdd.md`

```markdown
# Game Design Document — <title>

_Mode: jam | studio. Last updated: <date>._

## Quick context
- Engine / language / platform:
- Studio mode: jam | studio
- Pillars (3 max):
- Target feel:
- Scope: jam | small | ambitious

## Core fantasy
One sentence.

## Genre
Primary + secondary influences.

## Player actions
Verbs the player performs.

## Camera
Perspective, angle, zoom rules.

## Controls
Input mapping. TBD if not decided.

## Win / lose conditions
What ends a session in success or failure.

## Progression
Skill, unlocks, difficulty curve.

## Core gameplay loop
Moment-to-moment → session → long-term (three levels).

## Enemy and obstacle design
Types, behaviors, challenge to player actions.

## Vertical slice scope
What is playable now. One paragraph, tight scope.

## Not in this slice
What is explicitly deferred. At least two items.

---

## Art direction

_Filled lightly at /start; refine with /art-direction._

### Visual style
### Inspiration references
### Color palette
### Lighting direction
### Character proportions
### Environment style
### UI style
### Iconography
### Texture / material guidelines
### Animation tone
### Audio direction
### Explicitly avoid
```

## Mode affects all skills

- **jam**: skip optional gates, accept placeholder quality, TBD art ok
- **studio**: run `/proof-of-fun` before implementation, enforce `/qa`
  regression table, `/retrospective` after each ship

## Tone

Friendly stand-up, not a form factory. Infer as much as possible from the
user's words. Ask only what cannot be inferred. If the repo is empty,
celebrate the blank page.

## Do not

- Rewrite an existing `design/gdd.md` without diffing first
- Write more than ~150 lines in the GDD unless asked
- Skip the studio mode question — it calibrates every other skill
- Spawn extra agents or sub-workflows
