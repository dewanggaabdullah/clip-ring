from __future__ import annotations

from dataclasses import asdict, dataclass, field
from time import time
from typing import Any


@dataclass
class ClipboardRecord:
    kind: str
    payload: dict[str, Any]
    created_at: float = field(default_factory=time)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ClipboardRecord":
        return cls(kind=data["kind"], payload=dict(data["payload"]), created_at=float(data["created_at"]))
