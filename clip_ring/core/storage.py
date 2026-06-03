from __future__ import annotations

import json
import os
from pathlib import Path

from .record import ClipboardRecord
from .ring_buffer import RingBuffer


def default_home() -> Path:
    override = os.environ.get("CLIP_RING_HOME")
    if override:
        return Path(override)
    base = os.environ.get("LOCALAPPDATA") or str(Path.home() / ".local" / "share")
    return Path(base) / "clip-ring"


class JsonStorage:
    def __init__(self, home: str | Path | None = None, max_items: int = 8):
        self.home = Path(home) if home else default_home()
        self.max_items = max_items
        self.path = self.home / "history.json"
        self.cache = self.home / "cache"

    def load(self) -> RingBuffer:
        rb = RingBuffer(max_items=self.max_items)
        if self.path.exists():
            data = json.loads(self.path.read_text(encoding="utf-8"))
            for item in data.get("records", []):
                rb.records.append(ClipboardRecord.from_dict(item))
        return rb

    def save(self, rb: RingBuffer) -> None:
        self.home.mkdir(parents=True, exist_ok=True)
        data = {"records": [record.to_dict() for record in rb.list()]}
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def clear(self) -> None:
        if self.path.exists():
            self.path.unlink()
        if self.cache.exists():
            for child in self.cache.glob("*"):
                if child.is_file():
                    child.unlink()
