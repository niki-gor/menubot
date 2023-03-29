from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from menubot.config_reader import config, handler_config
from menubot.handler import setup_dispatcher

if __name__ == "__main__":
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher(bot)
    setup_dispatcher(dp, handler_config)

    executor.start_polling(dp, skip_updates=True)
