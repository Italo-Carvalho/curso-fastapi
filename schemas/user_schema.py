from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from schemas.article_schema import ArticleSchema


class UserSchemaBase(BaseModel):
    id: Optional[int] = None
    name: str
    last_name: str
    email: EmailStr
    is_admin: bool = False

    class Config:
        from_attributes: True


class UserSchemaCreate(UserSchemaBase):
    passwd: str


class UserSchemaArticles(UserSchemaBase):
    articles: Optional[List[ArticleSchema]]


class UserSchemaUp(UserSchemaBase):
    name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    passwd: Optional[str] = None
    is_admin: Optional[bool] = None
