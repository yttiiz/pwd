from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pwd_database_path: str = ""
    api_key: str = ""
    origins_path: str = ""

    class Config:
        env_file: str = ".env"


settings = Settings()
