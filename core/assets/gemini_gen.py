"""Google Gemini (Nano Banana) image generation."""

from __future__ import annotations

import os

from core.assets.paths import asset_dir, slugify, write_metadata
from core.assets.placeholders import placeholder_2d
from core.assets.retry import with_retries

NANO_BANANA_MODELS = {
    "nano-banana-2": "gemini-3.1-flash-image",
    "nano-banana": "gemini-2.5-flash-image",
    "nano-banana-pro": "gemini-3-pro-image",
}


def _gemini_api_key() -> str:
    """Read Gemini key from env without logging it."""
    return (
        os.environ.get("GEMINI_API_KEY", "").strip()
        or os.environ.get("GOOGLE_API_KEY", "").strip()
    )


def _retryable_gemini(exc: Exception) -> bool:
    """Return True for Gemini rate-limit / overload errors."""
    code = getattr(exc, "code", None)
    if code in (429, 500, 503):
        return True
    message = str(exc).lower()
    return "429" in message or "503" in message or "unavailable" in message


def generate_2d(
    prompt: str,
    purpose: str,
    *,
    category: str = "sprites",
    model: str = "nano-banana-2",
    width: int = 0,
    height: int = 0,
    has_alpha: bool = True,
    output_name: str = "",
) -> dict:
    """Generate a PNG via Nano Banana or return a placeholder."""
    api_key = _gemini_api_key()
    if not api_key:
        return placeholder_2d(
            purpose,
            category,
            "GEMINI_API_KEY or GOOGLE_API_KEY not set",
            width=width or 256,
            height=height or 256,
        )

    try:
        from google import genai
    except ImportError:
        return placeholder_2d(
            purpose,
            category,
            "google-genai package not installed",
            width=width or 256,
            height=height or 256,
        )

    model_id = NANO_BANANA_MODELS.get(model, NANO_BANANA_MODELS["nano-banana-2"])
    stem = slugify(output_name or purpose)
    folder = asset_dir("2d", category)
    out_path = folder / f"{stem}.png"

    def _call():
        client = genai.Client(api_key=api_key)
        return client.models.generate_content(
            model=model_id,
            contents=[prompt],
        )

    try:
        response = with_retries(_call, retry_if=_retryable_gemini)
    except Exception as exc:  # noqa: BLE001
        return placeholder_2d(
            purpose,
            category,
            str(exc),
            width=width or 256,
            height=height or 256,
        )

    image = None
    candidates = getattr(response, "candidates", None) or []
    if candidates:
        parts = getattr(candidates[0].content, "parts", None) or []
        for part in parts:
            if getattr(part, "inline_data", None) is not None:
                image = part.as_image()
                break

    if image is None:
        return placeholder_2d(
            purpose,
            category,
            "Gemini returned no image part",
            width=width or 256,
            height=height or 256,
        )

    if width > 0 and height > 0:
        image = image.resize((width, height))

    if has_alpha and image.mode != "RGBA":
        image = image.convert("RGBA")
    elif not has_alpha:
        image = image.convert("RGB")

    image.save(out_path, format="PNG")
    if not out_path.exists() or out_path.stat().st_size == 0:
        return placeholder_2d(
            purpose,
            category,
            "Saved image is empty",
            width=width or image.width,
            height=height or image.height,
        )

    dims = [image.width, image.height]
    meta = write_metadata(
        out_path,
        {
            "name": purpose,
            "provider": "nano-banana",
            "model": model_id,
            "dimensions": dims,
            "has_alpha": has_alpha,
            "purpose": purpose,
            "prompt": prompt,
        },
    )
    return {
        "path": str(out_path),
        "metadata_path": str(meta),
        "provider": "nano-banana",
        "model": model_id,
        "dimensions": dims,
        "has_alpha": has_alpha,
        "error": "",
    }
