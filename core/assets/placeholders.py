"""Placeholder assets when a provider is missing or generation fails."""

from __future__ import annotations

import struct
import wave
from pathlib import Path

from core.assets.paths import asset_dir, slugify, write_metadata


def _minimal_glb_bytes() -> bytes:
    """Return a tiny valid GLB with a single unit cube."""
    gltf = (
        b'{"asset":{"version":"2.0"},'
        b'"scenes":[{"nodes":[0]}],'
        b'"nodes":[{"mesh":0}],'
        b'"meshes":[{"primitives":[{"attributes":{"POSITION":0},'
        b'"indices":1}]}],'
        b'"accessors":[{"bufferView":0,"componentType":5126,'
        b'"count":8,"type":"VEC3"},'
        b'{"bufferView":1,"componentType":5123,"count":36,'
        b'"type":"SCALAR"}],'
        b'"bufferViews":[{"buffer":0,"byteOffset":0,"byteLength":96},'
        b'{"buffer":0,"byteOffset":96,"byteLength":72}],'
        b'"buffers":[{"byteLength":168}]}'
    )
    verts = struct.pack(
        "<24f",
        -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5, 0.5,
        -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, -0.5,
    )
    indices = struct.pack(
        "<36H",
        0, 1, 2, 2, 3, 0, 1, 5, 6, 6, 2, 1, 7, 6, 5, 5, 4, 7,
        4, 0, 3, 3, 7, 4, 4, 5, 1, 1, 0, 4, 3, 2, 6, 6, 7, 3,
    )
    bin_chunk = verts + indices
    json_chunk = gltf
    while len(json_chunk) % 4:
        json_chunk += b" "
    while len(bin_chunk) % 4:
        bin_chunk += b"\x00"
    total = 12 + 8 + len(json_chunk) + 8 + len(bin_chunk)
    header = struct.pack("<4sII", b"glTF", 2, total)
    json_hdr = struct.pack("<I4s", len(json_chunk), b"JSON") + json_chunk
    bin_hdr = struct.pack("<I4s", len(bin_chunk), b"BIN\x00") + bin_chunk
    return header + json_hdr + bin_hdr


def placeholder_audio(
    purpose: str,
    category: str,
    reason: str,
    *,
    loops: bool = False,
) -> dict:
    """Write a short silent WAV placeholder."""
    folder = asset_dir("audio", category)
    path = folder / f"{slugify(purpose)}.wav"
    with wave.open(str(path), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(22050)
        wf.writeframes(b"\x00\x00" * int(22050 * 0.1))
    meta = write_metadata(
        path,
        {
            "name": purpose,
            "provider": "placeholder",
            "duration_s": 0.1,
            "lufs": None,
            "loops": loops,
            "purpose": purpose,
            "reason": reason,
        },
    )
    return {
        "path": str(path),
        "metadata_path": str(meta),
        "provider": "placeholder",
        "duration_s": 0.1,
        "lufs": None,
        "loops": loops,
        "error": reason,
    }


def placeholder_2d(
    purpose: str,
    category: str,
    reason: str,
    *,
    width: int = 256,
    height: int = 256,
) -> dict:
    """Write a labeled solid-color PNG placeholder."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        folder = asset_dir("2d", category)
        path = folder / f"{slugify(purpose)}.placeholder.txt"
        path.write_text(f"placeholder: {purpose}\n{reason}", encoding="utf-8")
        meta = write_metadata(
            path,
            {
                "name": purpose,
                "provider": "placeholder",
                "dimensions": [0, 0],
                "has_alpha": False,
                "purpose": purpose,
                "reason": reason,
            },
        )
        return {
            "path": str(path),
            "metadata_path": str(meta),
            "provider": "placeholder",
            "dimensions": [0, 0],
            "has_alpha": False,
            "error": reason,
        }

    folder = asset_dir("2d", category)
    path = folder / f"{slugify(purpose)}.png"
    img = Image.new("RGBA", (width, height), (64, 64, 96, 255))
    draw = ImageDraw.Draw(img)
    label = purpose[:40] or "placeholder"
    draw.rectangle([8, 8, width - 8, height - 8], outline=(200, 200, 220, 255))
    draw.text((16, height // 2 - 8), label, fill=(230, 230, 240, 255))
    img.save(path, format="PNG")
    meta = write_metadata(
        path,
        {
            "name": purpose,
            "provider": "placeholder",
            "dimensions": [width, height],
            "has_alpha": True,
            "purpose": purpose,
            "reason": reason,
        },
    )
    return {
        "path": str(path),
        "metadata_path": str(meta),
        "provider": "placeholder",
        "dimensions": [width, height],
        "has_alpha": True,
        "error": reason,
    }


def placeholder_3d(
    purpose: str,
    category: str,
    reason: str,
) -> dict:
    """Write a minimal unit-cube GLB placeholder."""
    folder = asset_dir("3d", category)
    path = folder / f"{slugify(purpose)}.glb"
    path.write_bytes(_minimal_glb_bytes())
    meta = write_metadata(
        path,
        {
            "name": purpose,
            "provider": "placeholder",
            "poly_count": 12,
            "format": "glb",
            "blender_processed": False,
            "purpose": purpose,
            "reason": reason,
        },
    )
    return {
        "path": str(path),
        "metadata_path": str(meta),
        "provider": "placeholder",
        "poly_count": 12,
        "format": "glb",
        "task_id": "",
        "stage": "placeholder",
        "error": reason,
    }
