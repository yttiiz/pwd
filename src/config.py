from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(env_file=".env")

    pwd_database_path: str = ""
    api_key: str = ""
    app_path: str = ""
    origins_path: str = ""
    port: int = 8000


settings = Settings()
