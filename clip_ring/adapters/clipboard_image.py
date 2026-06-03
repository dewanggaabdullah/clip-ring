from __future__ import annotations

from pathlib import Path

from clip_ring.core.record import ClipboardRecord


def make_demo_image_record(cache_dir: str | Path) -> ClipboardRecord:
    cache = Path(cache_dir)
    cache.mkdir(parents=True, exist_ok=True)
    path = cache / "demo-image.txt"
    path.write_text("demo image placeholder; replace with a local image adapter", encoding="utf-8")
    return ClipboardRecord(kind="image", payload={"cache_path": str(path), "policy": "local_cache"})
