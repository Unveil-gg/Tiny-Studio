"""Shared retry helpers for provider HTTP calls."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")

# HTTP status codes worth retrying with exponential backoff.
RETRYABLE_HTTP = frozenset({429, 500, 502, 503, 504})


def is_retryable_http(status_code: int | None) -> bool:
    """Return True when an HTTP status should be retried."""
    return status_code in RETRYABLE_HTTP if status_code is not None else False


def with_retries(
    fn: Callable[[], T],
    *,
    max_attempts: int = 3,
    base_delay_s: float = 2.0,
    retry_if: Callable[[Exception], bool] | None = None,
) -> T:
    """Run ``fn`` with exponential backoff on retryable failures."""
    last_exc: Exception | None = None
    for attempt in range(max_attempts):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 — provider-specific errors
            last_exc = exc
            if attempt >= max_attempts - 1:
                raise
            if retry_if is not None and not retry_if(exc):
                raise
            time.sleep(base_delay_s * (2**attempt))
    if last_exc is not None:
        raise last_exc
    raise RuntimeError("with_retries exhausted without result")
