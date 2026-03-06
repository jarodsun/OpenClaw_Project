from __future__ import annotations

from app.services.text_normalizer import normalize_text

_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ('llm', ('llm', 'gpt', 'claude', 'gemini', 'deepseek', 'qwen', 'mistral', 'model release', 'reasoning model')),
    ('agent', ('agent', 'agents', 'multi-agent', 'autonomous', 'copilot')),
    ('infra', ('gpu', 'cuda', 'inference', 'serving', 'throughput', 'latency', 'accelerator', 'chip')),
    ('research', ('arxiv', 'paper', 'benchmark', 'sota', 'dataset', 'preprint')),
    ('product', ('launch', 'released', 'rollout', 'update', 'feature', 'api', 'preview', '发布', '上线', '更新')),
    ('policy', ('policy', 'regulation', 'compliance', 'safety', 'governance', 'copyright', 'lawsuit')),
)


def classify_tags(*parts: str | None) -> list[str]:
    merged = ' '.join(part for part in parts if part)
    normalized = normalize_text(merged)
    if not normalized:
        return ['general']

    text = normalized.lower()
    tags: list[str] = []
    for tag, keywords in _RULES:
        if any(keyword in text for keyword in keywords):
            tags.append(tag)

    if not tags:
        tags.append('general')
    return tags
