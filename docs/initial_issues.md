# Initial Issues

These are suggested issues to create after the repository is public. They focus on local-first behavior, privacy boundaries, and small tested improvements.

## 1. Documentation: add screenshots or GIFs for the CLI workflow

**Label:** documentation

Add a visual walkthrough showing `add-text`, `add-file`, `demo-image`, `list`, and `clear`.

Acceptance criteria:

- Uses synthetic content only.
- Does not show real clipboard history or private paths.
- Mentions `CLIP_RING_HOME` for demos.

## 2. Feature: add configurable retention in a config file

**Label:** feature

Support a simple local config file for retention count, such as 8, 16, or 32 records.

Acceptance criteria:

- Defaults remain local-first and conservative.
- Tests cover default and custom limits.
- README documents the config location.

## 3. Bug: improve list output formatting for long paths

**Label:** bug

Long file paths can make `clip-ring list` hard to scan. Improve output formatting or truncation without losing metadata.

Acceptance criteria:

- File content is never copied or printed.
- Tests cover a long synthetic path.

## 4. Security/privacy: expand secret-pattern tests

**Label:** security/privacy

Add tests for additional token-like, password-like, and long random-string patterns.

Acceptance criteria:

- Test strings are fake.
- Documentation explains that filters are heuristics, not a guarantee.

## 5. Roadmap: decide optional GUI toolkit and license boundary

**Label:** roadmap

Decide how optional GUI, tray, and hotkey support should be structured without making the core depend on desktop packages.

Acceptance criteria:

- Core package remains CLI-testable.
- License implications are documented before adding GUI dependencies.

## 6. Good first issue: add `clip-ring export --redacted`

**Label:** good first issue

Add a CLI command that exports a redacted summary of records for debugging.

Acceptance criteria:

- Text payloads are redacted by default.
- File records remain metadata-only.
- Tests use synthetic records.

## 7. Feature: add local cache cleanup policy

**Label:** feature

Improve image-cache cleanup with an explicit retention or age-based policy.

Acceptance criteria:

- No cloud sync or upload.
- Tests verify local cache deletion behavior.
