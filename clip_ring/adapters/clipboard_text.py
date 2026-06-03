from __future__ import annotations

from clip_ring.core.privacy_filter import looks_sensitive
from clip_ring.core.record import ClipboardRecord


def make_text_record(text: str, block_sensitive: bool = True) -> ClipboardRecord:
    if block_sensitive and looks_sensitive(text):
        raise ValueError("Sensitive-looking text was blocked by the privacy filter.")
    return ClipboardRecord(kind="text", payload={"text": text})
