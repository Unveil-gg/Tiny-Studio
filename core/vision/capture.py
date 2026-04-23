"""Screen capture for Tiny Studio: mss grab, 720p cap, snapshot retention."""

from __future__ import annotations

import base64
import io
import sys
import time
from pathlib import Path
from typing import Literal

try:
    import mss
    from mss.base import MSSBase
    from PIL import Image as PILImage
except ImportError:  # pragma: no cover - exercised when deps missing
    mss = None  # type: ignore[assignment]
    MSSBase = object  # type: ignore[misc, assignment]
    PILImage = None  # type: ignore[assignment]

# Long edge cap (720p class).
_MAX_W = 1280
_MAX_H = 720
_PRUNE_MAX_FILES = 50
_PRUNE_MAX_AGE_HOURS = 24


def repo_root() -> Path:
    """Return repository root (parent of ``core``)."""
    return Path(__file__).resolve().parents[2]


def snapshot_dir() -> Path:
    """Directory for PNG snapshots under ``.tiny_studio/snapshots``."""
    root = repo_root()
    out = root / ".tiny_studio" / "snapshots"
    return out


def _ensure_deps() -> None:
    """Raise ``RuntimeError`` with install hints if imports failed."""
    if mss is None or PILImage is None:
        raise RuntimeError(
            "Vision dependencies missing. Install with: "
            "pip install -r requirements-vision.txt"
        )


def _downscale_rgba(img: "PILImage.Image") -> "PILImage.Image":
    """Resize so the image fits within ``_MAX_W`` x ``_MAX_H`` (keep aspect)."""
    w, h = img.size
    scale = min(_MAX_W / float(w), _MAX_H / float(h), 1.0)
    nw = max(1, int(w * scale))
    nh = max(1, int(h * scale))
    return img.resize((nw, nh), PILImage.Resampling.LANCZOS)


def _grab_region(sct: MSSBase, region: dict) -> "PILImage.Image":
    """Grab a screen region and return a PIL RGB image."""
    raw = sct.grab(region)
    return PILImage.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")


def _primary_monitor_region(sct: MSSBase) -> dict:
    """Return mss region dict for the primary monitor (index 1)."""
    mon = sct.monitors[1]
    return {
        "left": mon["left"],
        "top": mon["top"],
        "width": mon["width"],
        "height": mon["height"],
    }


def _windows_find_window_rects(title_substring: str) -> list[tuple[str, dict]]:
    """Find visible windows whose title contains ``title_substring`` (Windows).

    Returns a list of ``(title, region_dict)`` for each match. Empty on
    non-Windows or if ctypes APIs fail.
    """
    if sys.platform != "win32":
        return []

    import ctypes
    from ctypes import wintypes

    user32 = ctypes.windll.user32
    needle = title_substring.lower()
    matches: list[tuple[str, dict]] = []

    def _enum(hwnd: int, _lparam: int) -> bool:
        if not user32.IsWindowVisible(hwnd):
            return True
        length = user32.GetWindowTextLengthW(hwnd) + 1
        buf = ctypes.create_unicode_buffer(length)
        user32.GetWindowTextW(hwnd, buf, length)
        title = buf.value or ""
        if needle not in title.lower():
            return True
        rect = wintypes.RECT()
        if not user32.GetWindowRect(hwnd, ctypes.byref(rect)):
            return True
        w = rect.right - rect.left
        h = rect.bottom - rect.top
        if w < 32 or h < 32:
            return True
        region = {
            "left": int(rect.left),
            "top": int(rect.top),
            "width": int(w),
            "height": int(h),
        }
        matches.append((title, region))
        return True

    EnumProc = ctypes.WINFUNCTYPE(
        wintypes.BOOL, wintypes.HWND, wintypes.LPARAM
    )
    enum_proc = EnumProc(_enum)
    user32.EnumWindows(enum_proc, 0)
    return matches


def _pick_best_window(
    matches: list[tuple[str, dict]],
    title_substring: str,
) -> tuple[str, dict] | None:
    """Prefer exact case-insensitive title match; else largest area."""
    if not matches:
        return None
    exact = [m for m in matches if m[0].lower() == title_substring.lower()]
    pool = exact if exact else matches

    def area(item: tuple[str, dict]) -> int:
        r = item[1]
        return int(r["width"]) * int(r["height"])

    return max(pool, key=area)


def prune_snapshots_dir(
    directory: Path | None = None,
    *,
    max_age_hours: int = _PRUNE_MAX_AGE_HOURS,
    keep_latest: int = _PRUNE_MAX_FILES,
) -> int:
    """Delete old or excess PNG snapshots. Returns how many files removed."""
    directory = directory or snapshot_dir()
    if not directory.is_dir():
        return 0

    cutoff = time.time() - max_age_hours * 3600
    paths = sorted(
        (p for p in directory.glob("*.png") if p.is_file()),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    deleted = 0
    for i, path in enumerate(paths):
        mtime = path.stat().st_mtime
        too_old = mtime < cutoff
        beyond_cap = i >= keep_latest
        if too_old or beyond_cap:
            try:
                path.unlink()
                deleted += 1
            except OSError:
                pass
    return deleted


def take_snapshot(
    window_title: str = "",
) -> tuple[
    Literal["ok", "error"],
    dict[str, str],
]:
    """Capture primary monitor, or a Windows window matching ``window_title``.

    Saves a downscaled PNG under ``.tiny_studio/snapshots/`` and prunes old
    files. Returns ``(status, payload)`` where payload includes ``path``,
    ``base64_png``, ``capture_mode``, and on failure ``error``.
    """
    try:
        _ensure_deps()
    except RuntimeError as exc:
        return "error", {"error": str(exc)}

    out_dir = snapshot_dir()
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        return "error", {"error": f"Cannot create snapshot dir: {exc}"}

    mode: str
    region: dict

    title = (window_title or "").strip()
    try:
        with mss.mss() as sct:
            if not title:
                region = _primary_monitor_region(sct)
                mode = "primary_monitor"
            elif sys.platform == "win32":
                rects = _windows_find_window_rects(title)
                picked = _pick_best_window(rects, title)
                if not picked:
                    return "error", {
                        "error": (
                            f"No visible window title containing {title!r}. "
                            "Try an empty title for the primary monitor, or "
                            "run the game windowed so the title is matchable."
                        ),
                    }
                mode = "window"
                region = picked[1]
            else:
                return "error", {
                    "error": (
                        "Window capture by title is only supported on Windows "
                        "in this version. Use an empty window_title for the "
                        "primary monitor (borderless fullscreen recommended)."
                    ),
                }

            image = _grab_region(sct, region)
    except Exception as exc:  # pragma: no cover - platform-specific
        return "error", {"error": f"Screen capture failed: {exc}"}

    try:
        image = _downscale_rgba(image)
        buf = io.BytesIO()
        image.save(buf, format="PNG", optimize=True)
        png_bytes = buf.getvalue()
    except Exception as exc:
        return "error", {"error": f"Image encode failed: {exc}"}

    name = time.strftime("snapshot-%Y%m%d-%H%M%S", time.localtime())
    name = f"{name}-{int(time.time() * 1000) % 100000}.png"
    path = out_dir / name
    try:
        path.write_bytes(png_bytes)
    except OSError as exc:
        return "error", {"error": f"Cannot write snapshot: {exc}"}

    try:
        prune_snapshots_dir(out_dir)
    except Exception:
        pass

    b64 = base64.standard_b64encode(png_bytes).decode("ascii")
    return "ok", {
        "path": str(path.resolve()),
        "base64_png": b64,
        "capture_mode": mode,
        "error": "",
    }
