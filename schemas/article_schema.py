from typing import Optional
from pydantic import BaseModel, HttpUrl, Field


class ArticleSchema(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    font_url: HttpUrl
    user_id: Optional[int] = None

    class Config:
        from_attributes = True
