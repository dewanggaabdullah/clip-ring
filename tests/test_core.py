import json
from pathlib import Path

import pytest

from clip_ring.adapters.clipboard_file import make_file_record
from clip_ring.adapters.clipboard_text import make_text_record
from clip_ring.cli.main import main
from clip_ring.core.ring_buffer import RingBuffer
from clip_ring.core.storage import JsonStorage


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


def test_json_storage_roundtrip(tmpdir):
    storage = JsonStorage(home=str(tmpdir), max_items=8)
    rb = RingBuffer(max_items=8)
    rb.add(make_text_record("hello"))
    storage.save(rb)
    loaded = storage.load()
    assert loaded.list()[0].payload["text"] == "hello"


def test_export_redacts_text(tmpdir, capsys, monkeypatch):
    monkeypatch.setenv("CLIP_RING_HOME", str(tmpdir))
    storage = JsonStorage(max_items=8)
    rb = RingBuffer(max_items=8)
    rb.add(make_text_record("this is private text"))
    storage.save(rb)

    main(["--max-items", "8", "export", "--redacted"])

    raw_output = capsys.readouterr().out
    output = json.loads(raw_output)

    assert output["records"][0]["kind"] == "text"
    assert output["records"][0]["payload"]["text"] == "[REDACTED]"
    assert "this is private text" not in raw_output


def test_export_keeps_file_metadata(tmpdir, capsys, monkeypatch):
    monkeypatch.setenv("CLIP_RING_HOME", str(tmpdir))
    file_path = Path(str(tmpdir.join("demo.txt")))
    file_path.write_text("secret file content", encoding="utf-8")

    storage = JsonStorage(max_items=8)
    rb = RingBuffer(max_items=8)
    rb.add(make_file_record(file_path))
    storage.save(rb)

    main(["--max-items", "8", "export", "--redacted"])

    raw_output = capsys.readouterr().out
    output = json.loads(raw_output)

    record = output["records"][0]

    assert record["kind"] == "file"
    assert record["payload"]["name"] == "demo.txt"
    assert record["payload"]["size"] == len("secret file content".encode("utf-8"))
    assert record["payload"]["policy"] == "metadata_only"
    assert "secret file content" not in raw_output


def test_export_redacts_text_and_keeps_file_metadata(tmpdir, capsys, monkeypatch):
    monkeypatch.setenv("CLIP_RING_HOME", str(tmpdir))
    file_path = Path(str(tmpdir.join("demo.txt")))
    file_path.write_text("secret file content", encoding="utf-8")

    storage = JsonStorage(max_items=8)
    rb = RingBuffer(max_items=8)

    rb.add(make_text_record("first private text"))
    rb.add(make_file_record(file_path))
    rb.add(make_text_record("second private text"))

    storage.save(rb)

    main(["--max-items", "8", "export", "--redacted"])

    raw_output = capsys.readouterr().out
    output = json.loads(raw_output)

    records = output["records"]

    assert records[0]["kind"] == "text"
    assert records[0]["payload"]["text"] == "[REDACTED]"

    assert records[1]["kind"] == "file"
    assert records[1]["payload"]["name"] == "demo.txt"
    assert records[1]["payload"]["policy"] == "metadata_only"

    assert records[2]["kind"] == "text"
    assert records[2]["payload"]["text"] == "[REDACTED]"

    assert "first private text" not in raw_output
    assert "second private text" not in raw_output
    assert "secret file content" not in raw_output
