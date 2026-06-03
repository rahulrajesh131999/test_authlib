from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi import Depends
from functools import lru_cache
from typing import Annotated

class Settings(BaseSettings):
    DATABASE_URL : str
    CLIENT_ID : str
    CLIENT_SECRET : str
    SERVER_METADATA_URL : str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()

SettingsDep = Annotated[Settings, Depends(get_settings)]