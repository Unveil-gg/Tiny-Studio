---
name: gen-gdd
description: >-
  Deepens or restructures design/gdd.md. Use when /start produced a lean GDD
  and specific sections need filling, or when the design has shifted
  significantly. Requires design/gdd.md to exist — run /start first.
---

# /gen-gdd — Deepen the Game Design Document

## Lead

**game-designer** drives. Pull in:
- **game-developer** — feasibility, controls, platform constraints
- **game-artist** — camera feel, art direction section

## Precondition

`design/gdd.md` must exist. This skill refines; `/start` creates.
If `gdd.md` is missing, stop and run `/start` first.

## Steps

1. **Read** `design/gdd.md`. List sections that are `TBD` or thin.
2. **Surface the three most impactful gaps** to the user, or ask which
   sections they want to deepen.
3. **Update only the sections that changed.** Do not rewrite confirmed
   sections unless the user explicitly asks.
4. **Confirm** before writing: "Here is what will change — ok?"

## Do not

- Rewrite the whole GDD when only one section needs work
- Contradict confirmed sections without flagging the change explicitly
- Exceed ~150 lines total in the GDD
- Create the file — that is `/start`'s job
