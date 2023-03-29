from pathlib import Path

import yaml
from pydantic import BaseSettings, SecretStr

from menubot.models import HandlerConfig

CONFIG_DIRECTORY = Path("config")


class Secrets(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = CONFIG_DIRECTORY / ".env"
        env_file_encoding = "utf-8"


with open(CONFIG_DIRECTORY / "menu.yml") as f:
    data = yaml.safe_load(f)

secrets = Secrets()
menu_config = HandlerConfig(**data)
