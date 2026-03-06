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

    mysql_host: str = Field(default='127.0.0.1')
    mysql_port: int = Field(default=3306)
    mysql_user: str = Field(default='ai_news')
    mysql_password: str = Field(default='ai_news')
    mysql_db: str = Field(default='ai_global_news')

    @property
    def database_url(self) -> str:
        return (
            f"mysql+pymysql://{self.mysql_user}:{self.mysql_password}"
            f"@{self.mysql_host}:{self.mysql_port}/{self.mysql_db}"
        )


class DevSettings(Settings):
    app_env: AppEnv = 'dev'
    debug: bool = True
    log_level: str = 'DEBUG'


class ProdSettings(Settings):
    app_env: AppEnv = 'prod'
    debug: bool = False
    log_level: str = 'INFO'


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    base = Settings()
    if base.app_env == 'prod':
        return ProdSettings()
    return DevSettings()
