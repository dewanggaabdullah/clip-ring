from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field

from .record import ClipboardRecord


@dataclass
class RingBuffer:
    max_items: int = 8
    records: deque[ClipboardRecord] = field(default_factory=deque)

    def add(self, record: ClipboardRecord) -> None:
        self.records.appendleft(record)
        while len(self.records) > self.max_items:
            self.records.pop()

    def clear(self) -> None:
        self.records.clear()

    def list(self) -> list[ClipboardRecord]:
        return list(self.records)
