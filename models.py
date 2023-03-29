from pydantic import BaseModel, AnyHttpUrl, UUID4


class UrlButton(BaseModel):
    text: str
    url: AnyHttpUrl


class Page(BaseModel):
    name: str
    keyboard: list[UrlButton]


# class PageWithId(Page):
#     page_id: str


class HandlerConfig(BaseModel):
    home_button_text: str
    main_menu_text: str
    pages: list[Page]