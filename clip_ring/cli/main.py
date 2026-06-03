from __future__ import annotations

import argparse

from clip_ring.adapters.clipboard_file import make_file_record
from clip_ring.adapters.clipboard_image import make_demo_image_record
from clip_ring.adapters.clipboard_text import make_text_record
from clip_ring.core.storage import JsonStorage


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="clip-ring")
    parser.add_argument("--max-items", type=int, default=8)
    sub = parser.add_subparsers(dest="command", required=True)
    p_text = sub.add_parser("add-text")
    p_text.add_argument("text")
    p_file = sub.add_parser("add-file")
    p_file.add_argument("path")
    sub.add_parser("demo-image")
    sub.add_parser("list")
    sub.add_parser("clear")
    args = parser.parse_args(argv)

    storage = JsonStorage(max_items=args.max_items)
    rb = storage.load()
    if args.command == "add-text":
        rb.add(make_text_record(args.text))
        storage.save(rb)
        print("added text")
    elif args.command == "add-file":
        rb.add(make_file_record(args.path))
        storage.save(rb)
        print("added file metadata")
    elif args.command == "demo-image":
        rb.add(make_demo_image_record(storage.cache))
        storage.save(rb)
        print("added demo image cache record")
    elif args.command == "list":
        for idx, record in enumerate(rb.list(), 1):
            print(f"{idx}. {record.kind}: {record.payload}")
    elif args.command == "clear":
        rb.clear()
        storage.clear()
        print("cleared")


if __name__ == "__main__":
    main()
