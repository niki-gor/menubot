from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from menubot.config import secrets, menu_config
from menubot.handlers import setup_handlers


if __name__ == "__main__":
    bot = Bot(token=secrets.bot_token.get_secret_value())
    dp = Dispatcher(bot)
    setup_handlers(dp, menu_config)

    executor.start_polling(dp, skip_updates=True)
