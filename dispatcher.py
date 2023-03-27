from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from models import Page


def greet(pages: list[Page]):
    kb = InlineKeyboardMarkup(row_width=1).add(
        *[InlineKeyboardButton(page.name, callback_data=page.name) for page in pages]
    )

    async def f(message: types.Message):
        await message.answer("Выберите, что вас интересует:", reply_markup=kb)

    return f


def menu(page: Page):
    kb = InlineKeyboardMarkup(row_width=1).add(
        *[InlineKeyboardButton(button.text, url=button.url) for button in page.keyboard]
    )

    async def f(call: types.CallbackQuery):
        await call.message.edit_text(text=page.name, reply_markup=kb)

    return f


def setup_dispatcher(dp: Dispatcher, pages: list[Page]):
    dp.register_message_handler(callback=greet(pages), commands=["start"])
    for page in pages:
        dp.register_callback_query_handler(callback=menu(page), text=page.name)
