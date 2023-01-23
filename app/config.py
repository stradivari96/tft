from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    api_key: str
    environment: str = "dev"


@lru_cache
def get_settings() -> Settings:
    settings = Settings(_env_file="./.env")
    return settings
