"""Provider availability checks for Tiny Studio asset generation.

Returns sanitized status strings only.
Never reads, prints, logs, summarizes, or passes raw API key values.

Usage:
    python -m core.assets.providers
"""

from __future__ import annotations

import os
import shutil
import subprocess
from dataclasses import dataclass
from enum import Enum


class ProviderStatus(str, Enum):
    CONFIGURED = "configured"
    MISSING = "missing"
    UNAVAILABLE = "unavailable"
    INSTALLED = "installed"


# Maps display name → environment variable name (value never read)
_API_PROVIDERS: dict[str, str] = {
    "ElevenLabs": "ELEVENLABS_API_KEY",
    "Tripo AI": "TRIPO_API_KEY",
}

# Maps display name → CLI command to probe
_LOCAL_TOOLS: dict[str, str] = {
    "Blender": "blender",
}


@dataclass
class ProviderResult:
    """Sanitized availability report for a single provider."""

    name: str
    status: ProviderStatus
    note: str = ""
    used_by: str = ""


def _check_gemini_provider() -> ProviderResult:
    """Check Gemini / Nano Banana key presence (value never read)."""
    if os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"):
        return ProviderResult(name="Nano Banana", status=ProviderStatus.CONFIGURED)
    return ProviderResult(
        name="Nano Banana",
        status=ProviderStatus.MISSING,
        note="Set GEMINI_API_KEY or GOOGLE_API_KEY to enable.",
    )


def _check_api_provider(name: str, env_var: str) -> ProviderResult:
    """Check whether an API key env var is present. Value is never read."""
    if os.environ.get(env_var):
        return ProviderResult(name=name, status=ProviderStatus.CONFIGURED)
    return ProviderResult(
        name=name,
        status=ProviderStatus.MISSING,
        note=f"Set {env_var} to enable.",
    )


def _check_local_tool(name: str, command: str) -> ProviderResult:
    """Check whether a CLI tool is installed and responds."""
    if shutil.which(command) is None:
        return ProviderResult(
            name=name,
            status=ProviderStatus.UNAVAILABLE,
            note=f"'{command}' not found in PATH.",
        )
    try:
        result = subprocess.run(
            [command, "--version"],
            capture_output=True,
            timeout=5,
        )
        if result.returncode == 0:
            return ProviderResult(name=name, status=ProviderStatus.INSTALLED)
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return ProviderResult(
        name=name,
        status=ProviderStatus.UNAVAILABLE,
        note=f"'{command}' found but did not respond to --version.",
    )


def _check_snapshot_tool() -> ProviderResult:
    """Check whether the take_game_snapshot MCP tool is active."""
    available = os.environ.get("TINY_STUDIO_SNAPSHOT_AVAILABLE", "").lower()
    if available in ("1", "true", "yes"):
        return ProviderResult(
            name="Snapshot tools",
            status=ProviderStatus.CONFIGURED,
        )
    return ProviderResult(
        name="Snapshot tools",
        status=ProviderStatus.UNAVAILABLE,
        note="Enable tiny-vision MCP or set TINY_STUDIO_SNAPSHOT_AVAILABLE=1.",
    )


def check_all() -> list[ProviderResult]:
    """Return sanitized availability for all known providers."""
    used_by: dict[str, str] = {
        "ElevenLabs": "/gen-audio",
        "Tripo AI": "/gen-3d",
        "Nano Banana": "/gen-2d",
        "Blender": "/gen-3d (post)",
        "Snapshot tools": "/vertical-slice",
    }

    results: list[ProviderResult] = []

    for name, env_var in _API_PROVIDERS.items():
        r = _check_api_provider(name, env_var)
        r.used_by = used_by.get(name, "")
        results.append(r)

    r = _check_gemini_provider()
    r.used_by = used_by.get("Nano Banana", "")
    results.append(r)

    for name, command in _LOCAL_TOOLS.items():
        r = _check_local_tool(name, command)
        r.used_by = used_by.get(name, "")
        results.append(r)

    r = _check_snapshot_tool()
    r.used_by = used_by.get("Snapshot tools", "")
    results.append(r)

    return results


def print_status_table(results: list[ProviderResult]) -> None:
    """Print a plain-text status table. No key values are printed."""
    print(f"\n{'Provider':<20} {'Status':<14} {'Used by':<20} {'Note'}")
    print("-" * 72)
    for r in results:
        print(f"{r.name:<20} {r.status.value:<14} {r.used_by:<20} {r.note}")
    print()

    missing = [r for r in results if r.status == ProviderStatus.MISSING]
    unavailable = [r for r in results if r.status == ProviderStatus.UNAVAILABLE]

    if missing or unavailable:
        print("Affected assets will use placeholders; other providers continue:")
        for r in missing + unavailable:
            print(f"  · {r.name}: {r.note or 'placeholder will be used'}")
        print()


if __name__ == "__main__":
    print_status_table(check_all())
