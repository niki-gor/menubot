from pydantic import BaseModel, AnyHttpUrl


class UrlButton(BaseModel):
    text: str
    url: AnyHttpUrl


class Page(BaseModel):
    name: str
    keyboard: list[UrlButton]
