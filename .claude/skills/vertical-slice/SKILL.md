---
name: vertical-slice
description: >-
  Playable slice from confirmed specs: implement, then /qa. Does not
  generate audio, images, or meshes.
---

# /vertical-slice — Playable slice

## Goal

The smallest playable slice that matches the specs. Feel and pacing
before more content.

## Target

`design/reviews/<YYYY-MM-DD>-slice.md` — what was confirmed, what
shipped, and that `/qa` ran.

## Precondition

`design/gdd.md` is filled (title is not `Untitled`).
`design/specs/mechanics.md` has real **Verbs** and **Loop** text, not
`TBD`. If not, stop and run `/start`.

## Pipeline

1. **Read** the index, mechanics, schema, and art style. Do not
   interview the other roles. The files are the brief.

2. **Implement** the slice in `/implement-feature` terms: one playable
   path, then stop and check that it runs. Update
   `design/specs/schema.json` if the data shape changes.

3. **Slots, not files.** If the slice needs an asset, append a slot to
   `design/specs/asset_hooks.json` (`id`, `kind`, `purpose`,
   `status: "unassigned"`). Use a code placeholder. Do not generate
   binaries. Mason stays external; see `.claude/docs/external-assets.md`.

4. **`/qa`** on the running slice. Check controls, readability against
   `art_style.md`, and missing hook slots.

5. **Write** the review note: specs used, files touched, how to run,
   open `TBD`s.

## Platform

Default to a **web prototype** unless the index names something else.
If the request implies native, desktop, console, or Steam-first, ask
which platform is first. Default native stack, if they pick native:
**SDL3 + bgfx**.

## Stop

Done when the slice note is written and `/qa` has a review file.
If `maxTurns` hits first, write `## Blocked` in the slice note and stop.

## Do not

- Call image, audio, or mesh providers
- Invent generation prompts
- Block the build because Mason is disabled
- Roleplay designer and artist inside this turn
