"""ElevenLabs sound-effect generation."""

from __future__ import annotations

import os
from pathlib import Path

from core.assets.paths import asset_dir, slugify, write_metadata
from core.assets.placeholders import placeholder_audio
from core.assets.retry import is_retryable_http, with_retries


def _audio_duration_s(path: Path) -> float | None:
    """Return MP3 duration in seconds when mutagen is available."""
    try:
        from mutagen.mp3 import MP3

        return float(MP3(path).info.length)
    except Exception:  # noqa: BLE001
        return None


def generate_audio(
    prompt: str,
    purpose: str,
    *,
    category: str = "sfx",
    loops: bool = False,
    duration_target_s: float | None = None,
    output_name: str = "",
) -> dict:
    """Generate an MP3 via ElevenLabs or return a placeholder."""
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        return placeholder_audio(
            purpose, category, "ELEVENLABS_API_KEY not set", loops=loops
        )

    try:
        from elevenlabs import ElevenLabs
    except ImportError:
        return placeholder_audio(
            purpose, category, "elevenlabs package not installed", loops=loops
        )

    stem = slugify(output_name or purpose)
    folder = asset_dir("audio", category)
    out_path = folder / f"{stem}.mp3"

    def _call() -> None:
        client = ElevenLabs(api_key=api_key)
        kwargs: dict = {
            "text": prompt,
            "loop": loops,
            "model_id": "eleven_text_to_sound_v2",
        }
        if duration_target_s is not None:
            kwargs["duration_seconds"] = max(0.5, min(30.0, duration_target_s))
        audio = client.text_to_sound_effects.convert(**kwargs)
        with out_path.open("wb") as handle:
            for chunk in audio:
                handle.write(chunk)

    try:
        with_retries(
            _call,
            retry_if=lambda exc: is_retryable_http(getattr(exc, "status_code", None)),
        )
    except Exception as exc:  # noqa: BLE001
        return placeholder_audio(purpose, category, str(exc), loops=loops)

    if not out_path.exists() or out_path.stat().st_size == 0:
        return placeholder_audio(
            purpose, category, "ElevenLabs returned empty audio", loops=loops
        )

    duration = _audio_duration_s(out_path)
    meta = write_metadata(
        out_path,
        {
            "name": purpose,
            "provider": "elevenlabs",
            "duration_s": duration,
            "lufs": None,
            "loops": loops,
            "purpose": purpose,
            "prompt": prompt,
        },
    )
    return {
        "path": str(out_path),
        "metadata_path": str(meta),
        "provider": "elevenlabs",
        "duration_s": duration,
        "lufs": None,
        "loops": loops,
        "error": "",
    }
