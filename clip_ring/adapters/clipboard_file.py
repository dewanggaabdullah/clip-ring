from __future__ import annotations

from pathlib import Path

from clip_ring.core.record import ClipboardRecord


def make_file_record(path: str | Path) -> ClipboardRecord:
    p = Path(path)
    stat = p.stat()
    return ClipboardRecord(kind="file", payload={
        "path": str(p),
        "name": p.name,
        "size": stat.st_size,
        "mtime": stat.st_mtime,
        "policy": "metadata_only",
    })
