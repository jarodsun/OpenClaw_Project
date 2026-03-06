from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


AppEnv = Literal['dev', 'prod']


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='AIGN_',
        case_sensitive=False,
        extra='ignore',
    )

    app_env: AppEnv = Field(default='dev')
    app_name: str = Field(default='AI Global News API')
    app_version: str = Field(default='0.1.0')
    debug: bool = Field(default=False)
    log_level: str = Field(default='INFO')
    log_dir: str = Field(default='logs')
    log_json: bool = Field(default=True)
    log_max_bytes: int = Field(default=10_485_760)
    log_backup_count: int = Field(default=7)

    database_url: str = Field(default='sqlite:///./ai_global_news_dev.db')
    ingest_collect_max_attempts: int = Field(default=3)
    ingest_collect_backoff_seconds: float = Field(default=1.0)
    ingest_db_max_attempts: int = Field(default=2)
    ingest_db_backoff_seconds: float = Field(default=0.5)
    admin_api_token: str | None = Field(default=None)


class DevSettings(Settings):
    app_env: AppEnv = 'dev'
    debug: bool = True
    log_level: str = 'DEBUG'


class ProdSettings(Settings):
    app_env: AppEnv = 'prod'
    debug: bool = False
    log_level: str = 'INFO'
    database_url: str = Field(default='sqlite:///./ai_global_news_prod.db')


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    base = Settings()
    if base.app_env == 'prod':
        return ProdSettings()
    return DevSettings()
