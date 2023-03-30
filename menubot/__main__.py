from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from menubot.config import secrets, menu_config
from menubot.api import setup_routes


if __name__ == "__main__":
    bot = Bot(token=secrets.bot_token.get_secret_value())
    dp = Dispatcher(bot)
    setup_routes(dp, menu_config)

    executor.start_polling(dp, skip_updates=True)
