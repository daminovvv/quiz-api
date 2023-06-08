import datetime

from pydantic import BaseModel


class Item(BaseModel):
    questions_num: int


class QuestionSchema(BaseModel):
    class Config:
        orm_mode = True

    id: int
    text: str
    answer: str
    created_at: datetime.datetime
