from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from menubot.config import secrets, menu_config
from menubot.api import Router


if __name__ == "__main__":
    bot = Bot(token=secrets.bot_token.get_secret_value())
    dp = Dispatcher(bot)
    router = Router(menu_config)
    router.setup_routes(dp)
\
    executor.start_polling(dp, skip_updates=True)
