

from pydantic import BaseModel

class AliasModel(BaseModel):
    username: str
    key: str

class ImageModel(BaseModel):
    img: list

class CrawlModel(BaseModel):
    url: str
    keywords: list[str]