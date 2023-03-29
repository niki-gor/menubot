from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from menubot.models import HandlerConfig, Page


class HandlerSetupper:
    HOME_CALLBACK_DATA = "/home"
    PAGE_CALLBACK_DATA_PREFIX = "/page/"

    def __init__(self, dp: Dispatcher, config: HandlerConfig):
        self.dp = dp
        self.config = config
        self.main_menu_keyboard = InlineKeyboardMarkup(row_width=1).add(
            *[
                InlineKeyboardButton(
                    page.name, callback_data=self.get_page_callback_data(page)
                )
                for page in config.pages
            ]
        )

    def get_page_callback_data(self, page: Page) -> str:
        return self.PAGE_CALLBACK_DATA_PREFIX + str(hash(page.name))

    def setup_greet(self):
        async def handler(message: types.Message):
            await message.answer(
                self.config.main_menu_text, reply_markup=self.main_menu_keyboard
            )

        self.dp.register_message_handler(callback=handler, commands=["start"])

    def get_page_handler(self, page: Page):
        kb = InlineKeyboardMarkup(row_width=1).add(
            *[
                InlineKeyboardButton(button.text, url=button.url)
                for button in page.keyboard
            ],
            InlineKeyboardButton(
                self.config.home_button_text, callback_data=self.HOME_CALLBACK_DATA
            ),
        )

        async def handler(call: types.CallbackQuery):
            await call.message.answer(text=f"📝 {page.name}", reply_markup=kb)

        return handler

    def setup_pages(self):
        for page in self.config.pages:
            self.dp.register_callback_query_handler(
                callback=self.get_page_handler(page),
                text=self.get_page_callback_data(page),
            )

    def setup_home_button(self):
        async def handler(call: types.CallbackQuery):
            await call.message.answer(
                self.config.main_menu_text, reply_markup=self.main_menu_keyboard
            )

        self.dp.register_callback_query_handler(
            callback=handler, text=self.HOME_CALLBACK_DATA
        )


def setup_handlers(dp: Dispatcher, config: HandlerConfig):
    hs = HandlerSetupper(dp, config)
    hs.setup_greet()
    hs.setup_pages()
    hs.setup_home_button()
