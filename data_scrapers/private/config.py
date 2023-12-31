from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file="pred.env", env_file_encoding="utf-8")
