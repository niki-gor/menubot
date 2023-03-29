from pydantic import BaseSettings, SecretStr
import yaml

from menubot.models import HandlerConfig


class Settings(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()

with open("pages_config.yml") as f:
    data = yaml.safe_load(f)

handler_config = HandlerConfig(**data)
