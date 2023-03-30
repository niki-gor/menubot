from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from menubot.models import HandlerConfig, Page


class PageDecorator:
    def __init__(self, page: Page):
        self.inline_keyboard = InlineKeyboardMarkup(row_width=1)
        for button in page.keyboard:
            self.inline_keyboard.add(InlineKeyboardButton(button.text, url=button.url))

        self.name = page.name
        self.page_id = hash(page.name)


class Router:
    HOME_PREFIX = "/home/"
    PAGE_PREFIX = "/page/"

    def __init__(self, config: HandlerConfig):
        self.main_menu_text = config.main_menu_text
        self.home_button_text = config.home_button_text
        self.page_name_prefix = config.page_name_prefix
        self.pages = [PageDecorator(page) for page in config.pages]
        self.main_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        for page in self.pages:
            self.main_menu_keyboard.add(
                InlineKeyboardButton(
                    page.name,
                    callback_data=f"{self.PAGE_PREFIX}{page.page_id}",
                )
            )

    def _page_handler(self, page: PageDecorator):
        async def handler(call: types.CallbackQuery):
            await call.message.answer(
                text=f"{self.page_name_prefix}{page.name}",
                reply_markup=page.inline_keyboard,
            )

        return handler

    async def _main_menu_message_handler(self, message: types.Message):
        await message.answer(
            self.config.main_menu_text, reply_markup=self.main_menu_keyboard
        )

    async def _main_menu_callback_query_handler(self, call: types.CallbackQuery):
        await self._main_menu_message_handler(call.message)

    def setup_routes(self, dp: Dispatcher):
        self.dp.register_message_handler(
            self._main_menu_message_handler, commands=["start"]
        )

        for page in self.pages:
            dp.register_callback_query_handler(
                self._page_handler(page), text=f"{self.PAGE_PREFIX}{page.page_id}"
            )

        dp.register_callback_query_handler(
            self._main_menu_callback_query_handler, text=self.HOME_PREFIX
        )


def setup_routes(dp: Dispatcher, config: HandlerConfig):
    router = Router(config)
    router.setup_routes(dp)
