

from pydantic import BaseModel
from typing import Literal, Union


class AliasModel(BaseModel):
    username: str
    key: str

class ImageModel(BaseModel):
    img: list

class ImageExifModel(BaseModel):
    img: str

class CrawlModel(BaseModel):
    url: str
    keywords: list[str]
    d: Union[int, Literal[1]]
    p: Union[int, Literal[1]]
