from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.article_model import ArticleModel
from models.user_model import UserModel
from schemas.article_schema import ArticleSchema
from core.deps import get_session, get_current_user

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED,
             response_model=ArticleSchema)
async def post_article(article: ArticleSchema,
                       logged_user: UserModel = Depends(get_current_user),
                       db: AsyncSession = Depends(get_session)):

    new_article: ArticleModel = ArticleModel(title=article.title,
                                             description=article.description,
                                             font_url=article.font_url,
                                             user_id=logged_user.id)

    db.add(new_article)
    await db.commit()

    return new_article


@router.get('/', response_model=List[ArticleSchema])
async def get_articles(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArticleModel)
        result = await session.execute(query)
        articles: List[ArticleModel] = result.scalars().unique.all()

        return articles
