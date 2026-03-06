from __future__ import annotations

from sqlalchemy import select

from app.collectors.sources import list_high_priority_sources
from app.db.session import SessionLocal
from app.models.source import Source


def main() -> None:
    created = 0
    updated = 0

    with SessionLocal() as session:
        for item in list_high_priority_sources():
            existing = session.execute(
                select(Source).where(Source.name == item.name)
            ).scalar_one_or_none()

            feed_url = item.endpoint if item.kind.value == 'rss' else None
            note = f'collector_kind={item.kind.value}; endpoint={item.endpoint}'

            if existing is None:
                session.add(
                    Source(
                        name=item.name,
                        category=item.category,
                        homepage_url=item.homepage_url,
                        feed_url=feed_url,
                        note=note,
                        enabled=True,
                    )
                )
                created += 1
                continue

            existing.category = item.category
            existing.homepage_url = item.homepage_url
            existing.feed_url = feed_url
            existing.note = note
            existing.enabled = True
            updated += 1

        session.commit()

    print(f'seed completed: created={created}, updated={updated}')


if __name__ == '__main__':
    main()
