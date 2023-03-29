from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from menubot.models import HandlerConfig, Page


class Setupper:
    def __init__(self, dp: Dispatcher, config: HandlerConfig):
        self.dp = dp
        self.config = config
        self.main_menu_keyboard = InlineKeyboardMarkup(row_width=1).add(
            *[
                InlineKeyboardButton(page.name, callback_data=page.name)
                for page in config.pages
            ]
        )

    def setup_greet(self):
        async def handler(message: types.Message):
            await message.answer(
                self.config.main_menu_text, reply_markup=self.main_menu_keyboard
            )

        self.dp.register_message_handler(callback=handler, commands=["start"])

    def page_handler(self, page: Page):
        kb = InlineKeyboardMarkup(row_width=1).add(
            *[
                InlineKeyboardButton(button.text, url=button.url)
                for button in page.keyboard
            ],
            InlineKeyboardButton(self.config.home_button_text, callback_data="HOOOME")
        )

        async def handler(call: types.CallbackQuery):
            await call.message.answer(text=f'📝 {page.name}', reply_markup=kb)

        return handler

    def setup_pages(self):
        for page in self.config.pages:
            self.dp.register_callback_query_handler(
                callback=self.page_handler(page), text=page.name
            )

    def setup_home_button(self):
        async def handler(call: types.CallbackQuery):
            await call.message.answer(
                self.config.main_menu_text, reply_markup=self.main_menu_keyboard
            )

        self.dp.register_callback_query_handler(callback=handler, text="HOOOME")


def setup_dispatcher(dp: Dispatcher, config: HandlerConfig):
    s = Setupper(dp, config)
    s.setup_greet()
    s.setup_pages()
    s.setup_home_button()
