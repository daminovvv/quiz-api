import datetime

from sqlalchemy import func, insert

from src.api.questions.schemas import QuestionSchema
from src.models import Question
from src.settings.database import SessionLocal


def create_questions(session: SessionLocal, question_list: list[dict]) -> int:
    """Saves questions into the database
    and returns number of questions that already exist
    """
    id_list = [question["id"] for question in question_list]
    values = [
        {
            "id": question["id"],
            "text": question["question"],
            "answer": question["answer"],
            "created_at": datetime.datetime.utcnow(),
        }
        for question in question_list
    ]
    count = (
        session.query(func.count())
        .select_from(Question)
        .where(Question.id.in_(id_list))
        .scalar()
    )
    session.execute(insert(Question).values(values))
    session.commit()
    return count


def select_latest_question(session: SessionLocal) -> QuestionSchema | None:
    """Returns last saved question"""
    latest_question = (
        session.query(Question)
        .order_by(Question.created_at.desc())
        .first()
    )
    if latest_question:
        return latest_question
    else:
        return None


def select_all_question(session: SessionLocal) -> list[QuestionSchema]:
    """Returns list of all questions"""
    questions = (
        session.query(Question)
        .order_by(Question.created_at.desc())
        .all()
    )
    return questions
