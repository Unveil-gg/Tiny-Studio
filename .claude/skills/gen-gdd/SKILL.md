---
name: gen-gdd
description: >-
  Deepens one spec file per run: mechanics, schema, art style, or the
  index. Requires /start first. Stops after that file validates.
---

# /gen-gdd — Deepen one spec

## Lead

The owner of the file you were asked to deepen:

- `mechanics` → game-designer → `design/specs/mechanics.md`
- `schema` → game-developer → `design/specs/schema.json`
- `art` → game-artist → `design/specs/art_style.md`
- `index` → whoever was invoked → `design/gdd.md` (links and studio
  facts only; do not paste the other specs into the index)

If the user does not name one, list which files are still `TBD` and
ask. Do not deepen more than one.

## Precondition

`design/gdd.md` exists and its title is not `Untitled`. If it is
missing or still blank, stop and run `/start`.

## Steps

1. **Read** the named file and the index. Note sections that are `TBD`
   or thin.
2. **Name the gap** you will fill. Confirm with the user before writing
   if the change contradicts a filled section.
3. **Update that file only.** Bump `revision` and `updated`. Keep a
   markdown `## Changelog` to 5 bullets. Do not rewrite confirmed
   sections unless the user asks.
4. Run `npm run validate`. If it fails, fix once.

## Stop

Done when that one file validates. If `maxTurns` hits first, add
`## Blocked` on a markdown spec and stop. For `schema.json`, do not
add extra keys; tell the user what is missing and stop.

## Do not

- Deepen a second file in this turn
- Pull the other roles into this chat
- Contradict a confirmed section without saying so
- Add generation prompts or binary assets
