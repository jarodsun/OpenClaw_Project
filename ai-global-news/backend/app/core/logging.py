from __future__ import annotations

import json
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from app.core.config import Settings


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            'ts': self.formatTime(record, datefmt='%Y-%m-%dT%H:%M:%S%z'),
            'level': record.levelname,
            'service': getattr(record, 'service', 'app'),
            'trace_id': getattr(record, 'trace_id', '-'),
            'event': getattr(record, 'event', record.name),
            'message': record.getMessage(),
        }

        extra = getattr(record, 'extra_data', None)
        if isinstance(extra, dict) and extra:
            payload['extra'] = extra

        if record.exc_info:
            payload['exception'] = self.formatException(record.exc_info)

        return json.dumps(payload, ensure_ascii=False)


def _build_formatter(json_enabled: bool) -> logging.Formatter:
    if json_enabled:
        return JsonFormatter()
    return logging.Formatter('%(asctime)s %(levelname)s [%(name)s] %(message)s')


def _build_rotating_handler(path: Path, level: int, formatter: logging.Formatter, max_bytes: int, backup_count: int) -> RotatingFileHandler:
    handler = RotatingFileHandler(
        filename=path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8',
    )
    handler.setLevel(level)
    handler.setFormatter(formatter)
    return handler


def setup_logging(settings: Settings) -> None:
    level_name = (settings.log_level or 'INFO').upper()
    level = getattr(logging, level_name, logging.INFO)

    log_dir = Path(settings.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    formatter = _build_formatter(settings.log_json)

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)

    app_file = _build_rotating_handler(
        log_dir / 'app.log',
        level,
        formatter,
        settings.log_max_bytes,
        settings.log_backup_count,
    )
    ingest_file = _build_rotating_handler(
        log_dir / 'ingest.log',
        level,
        formatter,
        settings.log_max_bytes,
        settings.log_backup_count,
    )
    scheduler_file = _build_rotating_handler(
        log_dir / 'scheduler.log',
        level,
        formatter,
        settings.log_max_bytes,
        settings.log_backup_count,
    )

    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.setLevel(level)
    root_logger.addHandler(console)

    api_logger = logging.getLogger('aign.api')
    api_logger.handlers.clear()
    api_logger.setLevel(level)
    api_logger.propagate = False
    api_logger.addHandler(console)
    api_logger.addHandler(app_file)

    ingest_logger = logging.getLogger('aign.ingest')
    ingest_logger.handlers.clear()
    ingest_logger.setLevel(level)
    ingest_logger.propagate = False
    ingest_logger.addHandler(console)
    ingest_logger.addHandler(ingest_file)

    scheduler_logger = logging.getLogger('aign.scheduler')
    scheduler_logger.handlers.clear()
    scheduler_logger.setLevel(level)
    scheduler_logger.propagate = False
    scheduler_logger.addHandler(console)
    scheduler_logger.addHandler(scheduler_file)
