import yaml
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from config_reader import config
from handler import setup_dispatcher
from models import HandlerConfig, Page

if __name__ == "__main__":
    with open("pages_config.yml") as f:
        data = yaml.safe_load(f)

    handler_config = HandlerConfig(**data)

    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher(bot)
    setup_dispatcher(dp, handler_config)

    executor.start_polling(dp, skip_updates=True)
