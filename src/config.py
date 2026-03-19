from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pwd_database_path: str = ""
    api_key: str = ""
    app_path: str = ""
    origins_path: str = ""
    port: int = 8000

    class Config:
        env_file: str = ".env"


settings = Settings()
