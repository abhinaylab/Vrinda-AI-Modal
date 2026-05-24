# backend/config/settings.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "VRINDA AI"
    VERSION: str = "1.0.0"

    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()