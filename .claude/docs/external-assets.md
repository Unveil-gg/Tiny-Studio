# External assets

Tiny Studio does not generate audio, images, or meshes. An external tool
such as Mason may attach later. This repo only publishes slot metadata.

## Hook file

`design/specs/asset_hooks.json`

Each slot has exactly four fields:

| Field | Meaning |
|-------|---------|
| `id` | Stable name, unique in the file |
| `kind` | `model`, `sprite`, `audio`, or `ui` |
| `purpose` | Design label, such as "player character" |
| `status` | Always `unassigned` in this repo |

Do not add prompt text, provider names, file paths, or generated binaries.

## Attaching a tool

`studio.config.json` names the external server and whether it is enabled:

```json
"externalTools": {
  "mason": { "enabled": false, "mcpServer": "mason" }
}
```

Leave `enabled` false until a human attaches that MCP server in their
client. Agents must not call generation tools, invent provider prompts,
or flip `enabled` on their own.

`npm run validate` rejects extra slot fields, so a prompt cannot hide
in the manifest.
