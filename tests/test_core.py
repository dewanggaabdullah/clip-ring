from pathlib import Path

import pytest

from clip_ring.adapters.clipboard_file import make_file_record
from clip_ring.adapters.clipboard_text import make_text_record
from clip_ring.core.ring_buffer import RingBuffer


def test_ring_limit():
    rb = RingBuffer(max_items=2)
    rb.add(make_text_record("one"))
    rb.add(make_text_record("two"))
    rb.add(make_text_record("three"))
    assert [r.payload["text"] for r in rb.list()] == ["three", "two"]


def test_sensitive_text_blocked():
    with pytest.raises(ValueError):
        make_text_record("api_key=sk-abcdefghijklmnopqrstuvwxyz123456")


def test_file_metadata_only(tmpdir):
    p = Path(str(tmpdir.join("demo.txt")))
    p.write_text("content", encoding="utf-8")
    record = make_file_record(p)
    assert record.payload["policy"] == "metadata_only"
    assert "content" not in record.payload
