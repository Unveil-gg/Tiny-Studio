"""Tripo AI 3D draft and refine generation."""

from __future__ import annotations

import asyncio
import os
from pathlib import Path

from core.assets.paths import asset_dir, slugify, write_metadata
from core.assets.placeholders import placeholder_3d
from core.assets.retry import is_retryable_http, with_retries

DRAFT_TIMEOUT_S = 90.0
REFINE_TIMEOUT_S = 180.0
POLL_INTERVAL_S = 2.0

FINAL_FAIL_NO_RETRY = frozenset({"banned", "cancelled"})


def _task_status(task: object) -> str:
    """Normalize Tripo task status to a lowercase string."""
    status = getattr(task, "status", "unknown")
    if hasattr(status, "value"):
        return str(status.value).lower()
    return str(status).lower()


def _tripo_retryable(exc: Exception) -> bool:
    """Return True when a Tripo error may succeed on retry."""
    status = getattr(exc, "status_code", None)
    return is_retryable_http(status)


async def _draft_async(
    prompt: str,
    *,
    smart_low_poly: bool,
    style: str,
) -> tuple[str, object]:
    """Submit and wait for a Tripo text-to-model draft."""
    from tripo3d import TaskStatus, TripoClient

    async with TripoClient() as client:
        kwargs: dict = {
            "prompt": prompt,
            "smart_low_poly": smart_low_poly,
            "texture_quality": "standard",
        }
        if style.strip():
            kwargs["style"] = style.strip()

        task_id = await client.text_to_model(**kwargs)
        task = await client.wait_for_task(
            task_id,
            polling_interval=POLL_INTERVAL_S,
            timeout=DRAFT_TIMEOUT_S,
        )
        return task_id, task


async def _refine_async(draft_task_id: str) -> tuple[str, object]:
    """Refine a succeeded Tripo draft task."""
    from tripo3d import TripoClient

    async with TripoClient() as client:
        refine_id = await client.refine_model(draft_model_task_id=draft_task_id)
        task = await client.wait_for_task(
            refine_id,
            polling_interval=POLL_INTERVAL_S,
            timeout=REFINE_TIMEOUT_S,
        )
        return refine_id, task


async def _download_async(task: object, folder: Path) -> str:
    """Download the primary GLB from a succeeded Tripo task."""
    from tripo3d import TripoClient

    async with TripoClient() as client:
        files = await client.download_task_models(task, str(folder))
    for key in ("model", "pbr_model", "base_model"):
        path = files.get(key)
        if path:
            return path
    raise ValueError("Tripo task succeeded but no model file was downloaded")


def _run_async(coro):
    """Run an async Tripo coroutine from sync MCP tool code."""
    return asyncio.run(coro)


def _task_failure(task: object) -> str:
    """Format a Tripo task failure message."""
    status = _task_status(task)
    error_code = getattr(task, "error_code", None)
    if error_code is not None:
        return f"Tripo task {status} (error_code={error_code})"
    return f"Tripo task {status}"


def generate_3d_draft(
    prompt: str,
    purpose: str,
    *,
    category: str = "props",
    smart_low_poly: bool = True,
    style: str = "",
    output_name: str = "",
) -> dict:
    """Generate a Tripo draft GLB or return a placeholder."""
    if not os.environ.get("TRIPO_API_KEY", "").strip():
        return placeholder_3d(
            purpose, category, "TRIPO_API_KEY not set"
        )

    try:
        from tripo3d import TaskStatus  # noqa: F401
    except ImportError:
        return placeholder_3d(
            purpose, category, "tripo3d package not installed"
        )

    stem = slugify(output_name or purpose)
    folder = asset_dir("3d", category)

    try:
        task_id, task = with_retries(
            lambda: _run_async(
                _draft_async(prompt, smart_low_poly=smart_low_poly, style=style)
            ),
            retry_if=_tripo_retryable,
        )
    except Exception as exc:  # noqa: BLE001
        return placeholder_3d(purpose, category, str(exc))

    status = _task_status(task)
    if status in FINAL_FAIL_NO_RETRY:
        return placeholder_3d(purpose, category, _task_failure(task))

    if status != "success":
        return placeholder_3d(purpose, category, _task_failure(task))

    try:
        downloaded = _run_async(_download_async(task, folder))
    except Exception as exc:  # noqa: BLE001
        return placeholder_3d(purpose, category, str(exc))

    src = Path(downloaded)
    dest = folder / f"{stem}_draft.glb"
    dest.write_bytes(src.read_bytes())
    if dest.stat().st_size == 0:
        return placeholder_3d(purpose, category, "Downloaded GLB is empty")

    meta = write_metadata(
        dest,
        {
            "name": purpose,
            "provider": "tripo",
            "stage": "draft",
            "task_id": task_id,
            "format": "glb",
            "smart_low_poly": smart_low_poly,
            "purpose": purpose,
            "prompt": prompt,
        },
    )
    return {
        "path": str(dest),
        "metadata_path": str(meta),
        "provider": "tripo",
        "task_id": task_id,
        "stage": "draft",
        "format": "glb",
        "error": "",
    }


def generate_3d_refine(
    draft_task_id: str,
    purpose: str,
    *,
    category: str = "props",
    output_name: str = "",
) -> dict:
    """Refine a succeeded Tripo draft or return a placeholder."""
    if not draft_task_id.strip():
        return placeholder_3d(purpose, category, "draft_task_id is required")

    if not os.environ.get("TRIPO_API_KEY", "").strip():
        return placeholder_3d(
            purpose, category, "TRIPO_API_KEY not set"
        )

    try:
        from tripo3d import TaskStatus  # noqa: F401
    except ImportError:
        return placeholder_3d(
            purpose, category, "tripo3d package not installed"
        )

    stem = slugify(output_name or purpose)
    folder = asset_dir("3d", category)

    try:
        refine_id, task = with_retries(
            lambda: _run_async(_refine_async(draft_task_id.strip())),
            retry_if=_tripo_retryable,
        )
    except Exception as exc:  # noqa: BLE001
        return placeholder_3d(purpose, category, str(exc))

    status = _task_status(task)
    if status in FINAL_FAIL_NO_RETRY:
        return placeholder_3d(purpose, category, _task_failure(task))

    if status != "success":
        return placeholder_3d(purpose, category, _task_failure(task))

    try:
        downloaded = _run_async(_download_async(task, folder))
    except Exception as exc:  # noqa: BLE001
        return placeholder_3d(purpose, category, str(exc))

    src = Path(downloaded)
    dest = folder / f"{stem}_refined.glb"
    dest.write_bytes(src.read_bytes())
    if dest.stat().st_size == 0:
        return placeholder_3d(purpose, category, "Downloaded GLB is empty")

    meta = write_metadata(
        dest,
        {
            "name": purpose,
            "provider": "tripo",
            "stage": "refined",
            "task_id": refine_id,
            "draft_task_id": draft_task_id.strip(),
            "format": "glb",
            "purpose": purpose,
        },
    )
    return {
        "path": str(dest),
        "metadata_path": str(meta),
        "provider": "tripo",
        "task_id": refine_id,
        "draft_task_id": draft_task_id.strip(),
        "stage": "refined",
        "format": "glb",
        "error": "",
    }
