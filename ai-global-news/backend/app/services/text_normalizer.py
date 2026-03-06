from __future__ import annotations

import re

_WHITESPACE_RE = re.compile(r'\s+')


def normalize_text(value: str | None) -> str | None:
    if value is None:
        return None

    text = value.replace('\x00', ' ')
    text = _WHITESPACE_RE.sub(' ', text).strip()
    return text or None
