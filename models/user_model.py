from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from core.configs import settings


class UserModel(settings.DBBaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    last_name = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    passwd = Column(String(256), nullable=False)
    is_admin = Column(Boolean, default=False)
    phone_number = Column(String(10), nullable=True)
    articles = relationship(
        'ArticleModel',
        cascade='all,delete-orphan',
        back_populates='creator',
        uselist=True,
        lazy='joined'
    )
