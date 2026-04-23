"""Tiny Studio vision MCP server (stdio). Exposes screen snapshot tools."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Allow `python path/to/mcp_server.py` without installing the repo as a package.
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:  # pragma: no cover
    sys.stderr.write(
        "Missing MCP SDK. Install with: pip install -r requirements-vision.txt\n"
    )
    raise SystemExit(1) from exc

from core.vision.capture import prune_snapshots_dir, take_snapshot

mcp = FastMCP(
    "tiny-vision",
    instructions=(
        "Tiny Studio screen capture: primary monitor or Windows window by "
        "title substring. Snapshots are saved under .tiny_studio/snapshots/."
    ),
)


@mcp.tool()
def take_game_snapshot(window_title: str = "") -> dict[str, Any]:
    """Capture the game or desktop for visual review.

    Args:
        window_title: Optional substring to match a **Windows** window title.
            Leave empty to capture the **primary monitor** (best with borderless
            fullscreen on that display).

    Returns:
        A JSON-serializable dict with ``path``, ``base64_png``, ``capture_mode``,
        and ``error`` (empty string on success).
    """
    status, payload = take_snapshot(window_title=window_title)
    if status != "ok":
        err = payload.get("error", "Unknown error")
        return {
            "path": "",
            "base64_png": "",
            "capture_mode": "",
            "error": err,
        }
    return {
        "path": payload.get("path", ""),
        "base64_png": payload.get("base64_png", ""),
        "capture_mode": payload.get("capture_mode", ""),
        "error": "",
    }


@mcp.tool()
def prune_snapshots(
    max_age_hours: int = 24,
    keep_latest: int = 50,
) -> dict[str, Any]:
    """Remove old PNG files from ``.tiny_studio/snapshots``.

    Deletes files older than ``max_age_hours`` or beyond the ``keep_latest``
    newest files.

    Returns:
        ``{"deleted": <int>, "error": ""}`` or ``{"deleted": 0, "error": "..."}``.
    """
    try:
        n = prune_snapshots_dir(
            max_age_hours=max_age_hours,
            keep_latest=keep_latest,
        )
        return {"deleted": n, "error": ""}
    except Exception as exc:  # pragma: no cover
        return {"deleted": 0, "error": str(exc)}


def main() -> None:
    """Run the MCP server over stdio (default for FastMCP)."""
    mcp.run()


if __name__ == "__main__":
    main()
