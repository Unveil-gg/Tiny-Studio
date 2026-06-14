"""Tiny Studio asset generation MCP server (stdio)."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:  # pragma: no cover
    sys.stderr.write(
        "Missing MCP SDK. Install with: pip install -r requirements-assets.txt\n"
    )
    raise SystemExit(1) from exc

from core.assets.elevenlabs_gen import generate_audio
from core.assets.gemini_gen import NANO_BANANA_MODELS, generate_2d
from core.assets.tripo_gen import generate_3d_draft, generate_3d_refine
from core.assets.providers import ProviderStatus, check_all

mcp = FastMCP(
    "tiny-assets",
    instructions=(
        "Tiny Studio asset generation. Keys are read from the environment "
        "inside the server process only — never returned to the client. "
        "Paid providers: ElevenLabs (audio), Tripo AI (3D), Nano Banana "
        "(2D via Gemini). Missing keys fall back to labeled placeholders."
    ),
)


@mcp.tool()
def check_asset_providers() -> dict[str, Any]:
    """Return sanitized provider status. No API key values are exposed."""
    results = check_all()
    providers = {r.name: r.status.value for r in results}
    notes = {
        r.name: r.note
        for r in results
        if r.note and r.status != ProviderStatus.CONFIGURED
    }
    return {"providers": providers, "notes": notes, "error": ""}


@mcp.tool()
def gen_audio(
    prompt: str,
    purpose: str,
    category: str = "sfx",
    loops: bool = False,
    duration_target_s: float = 0,
    output_name: str = "",
) -> dict[str, Any]:
    """Generate an audio asset via ElevenLabs.

    Args:
        prompt: Sound-effect description sent to ElevenLabs.
        purpose: Human-readable asset label for metadata.
        category: Subfolder under ``assets/audio/``.
        loops: Request a seamlessly looping clip (v2 model).
        duration_target_s: Target length in seconds (0 = auto, max 30).
        output_name: Optional filename stem override.

    Returns:
        Dict with ``path``, ``metadata_path``, ``provider``, ``duration_s``,
        ``lufs``, ``loops``, and ``error`` (empty on success).
    """
    duration = duration_target_s if duration_target_s > 0 else None
    return generate_audio(
        prompt,
        purpose,
        category=category,
        loops=loops,
        duration_target_s=duration,
        output_name=output_name,
    )


@mcp.tool()
def gen_2d(
    prompt: str,
    purpose: str,
    category: str = "sprites",
    model: str = "nano-banana-2",
    width: int = 0,
    height: int = 0,
    has_alpha: bool = True,
    output_name: str = "",
) -> dict[str, Any]:
    """Generate a 2D PNG via Nano Banana (Google Gemini).

    Args:
        prompt: Image prompt referencing GDD art direction.
        purpose: Human-readable asset label for metadata.
        category: Subfolder under ``assets/2d/``.
        model: ``nano-banana-2`` (default), ``nano-banana``, or
            ``nano-banana-pro``.
        width: Optional resize width in pixels (0 = model default).
        height: Optional resize height in pixels (0 = model default).
        has_alpha: Keep RGBA when true; RGB when false.
        output_name: Optional filename stem override.

    Returns:
        Dict with ``path``, ``metadata_path``, ``provider``, ``model``,
        ``dimensions``, ``has_alpha``, and ``error``.
    """
    if model not in NANO_BANANA_MODELS:
        model = "nano-banana-2"
    return generate_2d(
        prompt,
        purpose,
        category=category,
        model=model,
        width=width,
        height=height,
        has_alpha=has_alpha,
        output_name=output_name,
    )


@mcp.tool()
def gen_3d_draft(
    prompt: str,
    purpose: str,
    category: str = "props",
    smart_low_poly: bool = True,
    style: str = "",
    output_name: str = "",
) -> dict[str, Any]:
    """Generate a Tripo AI draft GLB (10–20 credits, ~10–15s).

    Args:
        prompt: Text-to-3D prompt aligned with GDD art direction.
        purpose: Human-readable asset label for metadata.
        category: Subfolder under ``assets/3d/``.
        smart_low_poly: Enable Tripo smart low-poly (recommended for games).
        style: Optional Tripo style modifier (e.g. ``stylized``).
        output_name: Optional filename stem override.

    Returns:
        Dict with ``path``, ``metadata_path``, ``provider``, ``task_id``,
        ``stage`` (``draft``), ``format``, and ``error``.
    """
    return generate_3d_draft(
        prompt,
        purpose,
        category=category,
        smart_low_poly=smart_low_poly,
        style=style,
        output_name=output_name,
    )


@mcp.tool()
def gen_3d_refine(
    draft_task_id: str,
    purpose: str,
    category: str = "props",
    output_name: str = "",
) -> dict[str, Any]:
    """Refine a succeeded Tripo draft (40–50 credits, longer wait).

    Args:
        draft_task_id: ``task_id`` from a successful ``gen_3d_draft`` call.
        purpose: Human-readable asset label for metadata.
        category: Subfolder under ``assets/3d/``.
        output_name: Optional filename stem override.

    Returns:
        Dict with ``path``, ``metadata_path``, ``provider``, ``task_id``,
        ``draft_task_id``, ``stage`` (``refined``), ``format``, and ``error``.
    """
    return generate_3d_refine(
        draft_task_id,
        purpose,
        category=category,
        output_name=output_name,
    )


def main() -> None:
    """Run the MCP server over stdio."""
    mcp.run()


if __name__ == "__main__":
    main()
