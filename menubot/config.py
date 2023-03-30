from pathlib import Path

import yaml
from pydantic import BaseSettings, SecretStr

from menubot.models import HandlerConfig

CONFIG_DIRECTORY = Path("config")
SECRETS_FILE = ".env"
MENU_CONFIG_FILE = "menu.yml"


class Secrets(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = CONFIG_DIRECTORY / SECRETS_FILE
        env_file_encoding = "utf-8"


with open(CONFIG_DIRECTORY / MENU_CONFIG_FILE) as f:
    data = yaml.safe_load(f)

secrets = Secrets()
menu_config = HandlerConfig(**data)
