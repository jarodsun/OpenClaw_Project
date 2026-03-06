from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path

from sqlalchemy import func, select
from sqlalchemy.exc import OperationalError

from app.db.session import SessionLocal
from app.models.article import Article


THRESHOLDS = {
    'ingest_success_rate': 95.0,
    'summary_success_rate': 90.0,
    'duplicate_ratio': 15.0,
    'search_p95_ms': 800.0,
}


def _to_percent(numerator: int, denominator: int) -> float:
    if denominator == 0:
        return 0.0
    return round((numerator / denominator) * 100, 2)


def collect_metrics() -> dict[str, float | int | str | None]:
    try:
        with SessionLocal() as session:
            total_articles = session.scalar(select(func.count()).select_from(Article)) or 0

            summary_count = session.scalar(
                select(func.count())
                .select_from(Article)
                .where(Article.summary.is_not(None), func.length(func.trim(Article.summary)) > 0)
            ) or 0

            titles = session.scalars(select(Article.title)).all()
            normalized = [title.strip().lower() for title in titles if title and title.strip()]
            title_counter = Counter(normalized)
            duplicate_title_rows = sum(count - 1 for count in title_counter.values() if count > 1)

            latest_ingested_at = session.scalar(select(func.max(Article.ingested_at)))

        summary_success_rate = _to_percent(summary_count, total_articles)
        duplicate_ratio = _to_percent(duplicate_title_rows, total_articles)
        data_warning = None
    except OperationalError as exc:
        total_articles = 0
        summary_count = 0
        duplicate_title_rows = 0
        summary_success_rate = 0.0
        duplicate_ratio = 0.0
        latest_ingested_at = None
        data_warning = f'数据库未初始化或缺少 articles 表：{exc.__class__.__name__}'

    return {
        'total_articles': total_articles,
        'summary_count': summary_count,
        'summary_success_rate': summary_success_rate,
        'duplicate_title_rows': duplicate_title_rows,
        'duplicate_ratio': duplicate_ratio,
        'latest_ingested_at': latest_ingested_at.isoformat() if latest_ingested_at else None,
        'ingest_success_rate': None,
        'search_p95_ms': None,
        'stable_72h': None,
        'data_warning': data_warning,
        'generated_at': datetime.now().isoformat(timespec='seconds'),
    }


def _gate_status(name: str, value: float | None) -> str:
    if value is None:
        return 'N/A'
    threshold = THRESHOLDS[name]
    if name == 'duplicate_ratio':
        return 'PASS' if value <= threshold else 'FAIL'
    return 'PASS' if value >= threshold else 'FAIL'


def build_report(metrics: dict[str, float | int | str | None]) -> str:
    summary_status = _gate_status('summary_success_rate', metrics['summary_success_rate'])
    duplicate_status = _gate_status('duplicate_ratio', metrics['duplicate_ratio'])

    lines = [
        '# 04 Acceptance Report（自动生成）',
        '',
        f"- 生成时间：{metrics['generated_at']}",
        f"- 样本总量：{metrics['total_articles']}",
        f"- 最新入库时间：{metrics['latest_ingested_at'] or '无数据'}",
    ]

    if metrics['data_warning']:
        lines.extend([
            '',
            f"- 数据告警：{metrics['data_warning']}",
        ])

    lines.extend([
        '',
        '## 指标快照（当前数据库）',
        '',
        '| 指标 | 当前值 | 门禁阈值 | 状态 | 说明 |',
        '|---|---:|---:|---|---|',
        f"| 抓取成功率 | N/A | >= {THRESHOLDS['ingest_success_rate']}% | N/A | 需接入调度运行统计后再判定 |",
        f"| 摘要成功率 | {metrics['summary_success_rate']}% | >= {THRESHOLDS['summary_success_rate']}% | {summary_status} | 非空摘要占比 |",
        f"| 重复占比 | {metrics['duplicate_ratio']}% | <= {THRESHOLDS['duplicate_ratio']}% | {duplicate_status} | 基于标题归一化的近似重复占比 |",
        f"| 检索 P95 | N/A | <= {THRESHOLDS['search_p95_ms']}ms | N/A | 需压测脚本输出 |",
        '| 72h 稳定运行 | N/A | 通过 | N/A | 需连续观测结果 |',
        '',
        '## 结论',
        '',
        '- 当前只能完成摘要率与重复占比的静态核验。',
        '- 抓取成功率、检索 P95、72h 稳定性缺少自动化证据，门禁未满足。',
        '- 上线判定：不可上线。',
    ])
    return '\n'.join(lines) + '\n'


def main() -> None:
    metrics = collect_metrics()
    report = build_report(metrics)
    output_path = Path(__file__).resolve().parents[2] / 'docs' / '04-acceptance-report.md'
    output_path.write_text(report, encoding='utf-8')
    print(f'Acceptance report generated: {output_path}')


if __name__ == '__main__':
    main()
