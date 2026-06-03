# clip-ring

`clip-ring` is a local-first clipboard history manager core. It keeps a configurable rolling history of recent clipboard records, supports text/image/file record types, and is designed around privacy: no network calls, metadata-only file records, sensitive-text filtering, and one-command clearing.

The current public package is a minimal CLI-first core. GUI, tray, and hotkey integrations are optional future layers so the core stays testable and lightweight.

## Quick start

```bash
python -m clip_ring.cli add-text "hello"
python -m clip_ring.cli list
python -m clip_ring.cli add-file ./examples/example.txt
python -m clip_ring.cli demo-image
python -m clip_ring.cli clear
```

By default, history is stored locally under the user's application data directory. For tests or demos, set `CLIP_RING_HOME`.

## Privacy boundary

- No cloud sync, telemetry, or upload.
- File records store path, name, size, and mtime metadata only.
- Text that looks like an API key, token, password, or long secret is blocked by default.
- Image records are local cache files and can be cleared.

## Development

```bash
python -m pytest
```

## License

MIT is recommended for the core. Apache-2.0 is a reasonable alternative if future security/privacy patent language is desired.
