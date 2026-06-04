from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi import Depends
from functools import lru_cache
from typing import Annotated

class Settings(BaseSettings):
    DATABASE_URL : str
    CLIENT_ID : str
    CLIENT_SECRET : str
    SERVER_METADATA_URL : str
    JWT_SECRET : str
    JWT_ALGORITHM : str 
    DUMMY_HASH : str = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    ACCESS_TOKEN_EXPIRE_MIN : int = 15
    REFRESH_TOKEN_EXPIRE_DAYS : int = 7

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()

SettingsDep = Annotated[Settings, Depends(get_settings)]