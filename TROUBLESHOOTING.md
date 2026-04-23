# Troubleshooting

## Cursor: `.cursor/skills` symlink (Cursor only)

This page matters **only if you use Cursor** and want `/start`, `/qa`, and other
project skills. **Codex CLI** does not read `.cursor/skills`; use **`.agents/skills`**
for Codex ([OpenAI: Agent Skills](https://developers.openai.com/codex/skills)).

**`.cursor/skills`** must be a **directory symlink** to **`../.claude/skills`**
(Git mode `120000`). Edit skills only under **`.claude/skills/`**.

### Windows (Git) — set once, ideally before clone

Without this, Git on Windows may check out the link as a **plain text file**
instead of a symlink:

```powershell
git config --global core.symlinks true
```

Repo-only: `git config core.symlinks true`, then re-clone or re-checkout
`.cursor/skills`.

### Verify after clone

**Windows (PowerShell), from repo root:**

```powershell
Get-Item .cursor/skills | Select-Object LinkType, Target
```

Expect **`SymbolicLink`** and **`..\.claude\skills`** (or `../.claude/skills`).

**macOS / Linux:**

```bash
ls -la .cursor/skills
```

Expect a line starting with **`l`** pointing at **`../.claude/skills`**.

### Fix a broken or missing link

From **repo root**, remove the bad `.cursor/skills`, then either restore from Git
(after `core.symlinks true`) or recreate the symlink.

**Restore from Git (Windows):**

```powershell
Remove-Item -Recurse -Force .cursor/skills
git checkout HEAD -- .cursor/skills
```

**Create manually (Windows — Developer Mode or elevated terminal):**

```powershell
New-Item -ItemType Directory -Path .cursor -Force | Out-Null
Set-Location .cursor
cmd /c "mklink /D skills ..\.claude\skills"
Set-Location ..
```

**Create manually (macOS / Linux):**

```bash
mkdir -p .cursor
ln -sfn ../.claude/skills .cursor/skills
```

If **`mklink`** / **`ln`** fails, enable **Settings → System → For developers →
Developer Mode** on Windows (or run the shell as Administrator), then retry.

### OneDrive / cloud sync

Repos under OneDrive can break or confuse symlinks. If `.cursor/skills` keeps
misbehaving, move the repo to a normal disk or recreate the symlink after sync.

## Codex CLI: `AGENTS.md`

Root **`AGENTS.md`** is the thin entry Codex loads by default. For layering and
limits, see OpenAI’s [Codex `AGENTS.md` guide](https://developers.openai.com/codex/guides/agents-md).
