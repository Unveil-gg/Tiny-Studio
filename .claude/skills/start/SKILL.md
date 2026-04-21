---
name: start
description: >-
  Onboards a game project: detects repo state, records engine/language/platform,
  creative pillars, target feel, visual direction, and scope level. Use when
  beginning work, resetting direction, or adopting an existing codebase.
---

# /start — Project onboarding

## Goal

Orient the **human + three agents** so every later command shares the same
assumptions. Keep outputs **short and actionable**.

## Steps

1. **Scan the repo** (Read, Glob, Grep): presence of engine files (e.g. Godot
   `project.godot`, Unity `ProjectSettings`, Unreal `.uproject`), `package.json`,
   `Cargo.toml`, custom engine, etc.
2. **Classify state**: empty / idea-only / prototype / active production /
   unknown.
3. **Interview the user** if anything critical is missing (engine, platform,
   solo vs team size). One compact question block at a time.
4. **Record** in `design/pillars.md` (create if absent) a **lean** snapshot:

   - Working title (or codename)
   - Engine, language, primary platform(s)
   - **Pillars** (3 bullets max) — what the game must always be
   - **Target feel** — one paragraph: pace, fantasy, emotional beat
   - **Visual direction** — a few words + optional reference games/media
   - **Scope level**: `jam` | `small` | `ambitious` (honest label)

5. **Confirm** with the user: “Anything wrong? You have final edit rights.”

## Tone

Friendly studio stand-up, not a form factory. If the repo is empty, **celebrate**
the blank page and still capture pillars from the user’s words.

## Do not

- Spawn extra agents or workflows
- Write more than ~1–2 screens of markdown in `design/pillars.md` unless asked
