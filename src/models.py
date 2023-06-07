from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime

from src.settings.database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)
