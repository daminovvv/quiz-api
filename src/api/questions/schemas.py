import datetime

from pydantic import BaseModel, Field


class Item(BaseModel):
    questions_num: int = Field(ge=0)


class QuestionSchema(BaseModel):
    class Config:
        orm_mode = True

    id: int
    text: str
    answer: str
    created_at: datetime.datetime
