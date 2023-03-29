from pydantic import AnyHttpUrl, BaseModel


class UrlButton(BaseModel):
    text: str
    url: AnyHttpUrl


class Page(BaseModel):
    name: str
    keyboard: list[UrlButton]


class HandlerConfig(BaseModel):
    home_button_text: str
    main_menu_text: str
    pages: list[Page]
