import logging
import time
from datetime import UTC, datetime

from fastapi import FastAPI, Request

from app.core.config import get_settings
from app.core.logging import setup_logging


settings = get_settings()
setup_logging(settings.log_level)
logger = logging.getLogger(__name__)
start_time = time.time()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)


@app.middleware('http')
async def request_log_middleware(request: Request, call_next):
    started = time.perf_counter()
    response = await call_next(request)
    cost_ms = (time.perf_counter() - started) * 1000
    logger.info(
        '%s %s -> %s %.2fms',
        request.method,
        request.url.path,
        response.status_code,
        cost_ms,
    )
    return response


@app.get('/health')
def health() -> dict[str, str | float]:
    return {
        'status': 'ok',
        'env': settings.app_env,
        'version': settings.app_version,
        'timestamp': datetime.now(UTC).isoformat(),
        'uptime_seconds': round(time.time() - start_time, 2),
    }
