from pydantic import AnyHttpUrl, BaseModel
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class UrlButton(BaseModel):
    text: str
    url: AnyHttpUrl


class Page(BaseModel):
    name: str
    keyboard: list[UrlButton]


class HandlerConfig(BaseModel):
    home_button_text: str
    main_menu_text: str
    page_name_format: str = '{}'
    pages: list[Page]
