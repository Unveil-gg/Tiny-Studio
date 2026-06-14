"""Project-relative asset paths and metadata sidecars."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


def project_root() -> Path:
    """Return the Tiny Studio project root (cwd or env override)."""
    import os

    override = os.environ.get("TINY_STUDIO_PROJECT_ROOT", "").strip()
    return Path(override) if override else Path.cwd()


def slugify(name: str) -> str:
    """Convert a label into a safe filename stem."""
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", name.strip().lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "asset"


def asset_dir(asset_type: str, category: str) -> Path:
    """Return (and create) ``assets/<type>/<category>/`` under project root."""
    folder = project_root() / "assets" / asset_type / slugify(category)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def write_metadata(path: Path, data: dict) -> Path:
    """Write a JSON sidecar next to an asset file."""
    meta_path = path.with_suffix(path.suffix + ".meta.json")
    payload = {
        **data,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    meta_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return meta_path


def ok_result(**fields: object) -> dict:
    """Build a success-shaped MCP tool response."""
    base = {
        "path": "",
        "metadata_path": "",
        "provider": "",
        "error": "",
    }
    base.update(fields)
    return base


def err_result(message: str, **fields: object) -> dict:
    """Build an error-shaped MCP tool response."""
    base = ok_result(error=message, provider=fields.pop("provider", ""))
    base.update(fields)
    return base
