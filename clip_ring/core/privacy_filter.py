from __future__ import annotations

import re


PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*\S+"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"[A-Za-z0-9+/]{40,}={0,2}"),
]


def looks_sensitive(text: str) -> bool:
    return any(pattern.search(text) for pattern in PATTERNS)


def redact_text(text: str) -> str:
    return "[REDACTED]"
