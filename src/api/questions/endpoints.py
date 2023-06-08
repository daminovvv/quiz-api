import requests
from fastapi import APIRouter, Depends

from src.api.questions.crud import (create_questions, select_all_question,
                                    select_latest_question)
from src.api.questions.schemas import Item, QuestionSchema
from src.settings.database import SessionLocal, get_session

router = APIRouter()


@router.post(
    "/question/",
    name="Request new questions",
    response_model=QuestionSchema,
    status_code=201,
)
async def post_question(
        body: Item,
        session: SessionLocal = Depends(get_session)
):
    """Request new questions and write it to db"""
    count = body.questions_num
    while count > 0:
        resp = requests.get(
            url=f"https://jservice.io/api/random?count={body.questions_num}"
        )
        count = create_questions(session, resp.json())
    response = select_latest_question(session)
    return response


@router.get(
    "/question/",
    name="Получить последний вопрос",
    response_model=QuestionSchema,
    status_code=200,
)
async def get_latest_question(session: SessionLocal = Depends(get_session)):
    """Gets last question from db"""
    question = select_latest_question(session)

    return question


@router.get(
    "/question/all/",
    name="Получить все вопросы",
    response_model=list[QuestionSchema],
    status_code=200,
)
async def get_all_question(session: SessionLocal = Depends(get_session)):
    """Gets all questions from db"""
    response = select_all_question(session)

    return response
