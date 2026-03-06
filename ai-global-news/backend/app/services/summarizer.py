from __future__ import annotations

from collections import OrderedDict

from app.services.text_normalizer import normalize_text


class SummaryService:
    def __init__(self, max_cache_size: int = 2000, max_chars: int = 180) -> None:
        self.max_cache_size = max_cache_size
        self.max_chars = max_chars
        self._cache: OrderedDict[str, str] = OrderedDict()

    def generate(self, title: str | None, summary: str | None, content: str | None) -> str:
        cache_key = f'{title or ""}|{summary or ""}|{content or ""}'
        cached = self._cache.get(cache_key)
        if cached is not None:
            self._cache.move_to_end(cache_key)
            return cached

        try:
            result = self._build_summary(title=title, summary=summary, content=content)
        except Exception:
            result = self._fallback_summary(title=title, summary=summary, content=content)

        self._cache[cache_key] = result
        self._cache.move_to_end(cache_key)
        if len(self._cache) > self.max_cache_size:
            self._cache.popitem(last=False)
        return result

    def _build_summary(self, title: str | None, summary: str | None, content: str | None) -> str:
        seed = normalize_text(summary) or normalize_text(content)
        if not seed:
            return self._fallback_summary(title=title, summary=summary, content=content)

        first_sentence = self._first_sentence(seed)
        if first_sentence:
            return self._truncate(first_sentence)
        return self._truncate(seed)

    def _fallback_summary(self, title: str | None, summary: str | None, content: str | None) -> str:
        if normalize_text(summary):
            return self._truncate(normalize_text(summary) or '')
        if normalize_text(content):
            return self._truncate(normalize_text(content) or '')
        return self._truncate(normalize_text(title) or '暂无摘要')

    def _first_sentence(self, text: str) -> str:
        for sep in ('。', '！', '？', '.', '!', '?'):
            idx = text.find(sep)
            if idx != -1:
                return text[: idx + 1].strip()
        return text

    def _truncate(self, text: str) -> str:
        compact = normalize_text(text) or ''
        if len(compact) <= self.max_chars:
            return compact
        return f"{compact[: self.max_chars - 1]}…"


summary_service = SummaryService()
