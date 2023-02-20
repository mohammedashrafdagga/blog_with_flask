from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from database import Base
from sqlalchemy.orm import relationship, backref



class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    author = relationship('auth_app.models.User', backref=backref('articles', lazy=True))

    def __repr__(self):
        return self.title