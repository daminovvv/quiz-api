from sqlalchemy import Column, DateTime, Integer, String

from src.settings.database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)
