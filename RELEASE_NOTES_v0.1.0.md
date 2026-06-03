# clip-ring v0.1.0 Release Notes

## Overview

This first clean-room release introduces a local-first clipboard history manager core with a tested CLI, privacy documentation, metadata-only file records, sensitive-text filtering, and one-command clearing.

## Included

- Rolling ring buffer with default 8-record retention.
- Text records with defensive sensitive-text filtering.
- File records that store metadata only: path, name, size, mtime, and policy.
- Demo image record stored as a local cache placeholder.
- JSON local storage with `CLIP_RING_HOME` override for tests and demos.
- CLI commands: `add-text`, `add-file`, `demo-image`, `list`, and `clear`.
- README, privacy, storage, security, file-policy docs, issue templates, pull-request template, and GitHub Actions test workflow.

## Not Included

- No telemetry.
- No cloud sync.
- No upload.
- No real clipboard history.
- No packaged executable.
- No GUI/tray/hotkey dependency in the core.

## Tests

Expected local verification:

```bash
python -m pytest
python -m clip_ring.cli add-text "hello"
python -m clip_ring.cli list
python -m clip_ring.cli clear
```

## Known Limitations

- Image handling is a demo placeholder, not a full native clipboard adapter.
- Secret filtering is heuristic and cannot guarantee full protection.
- GUI, tray, and hotkey support are intentionally deferred to optional modules.

## Recommended Next Steps

- Create the initial issues listed in `docs/initial_issues.md`.
- Add screenshots or GIFs using synthetic clipboard content.
- Decide optional GUI toolkit and license boundary before v0.2.0.
