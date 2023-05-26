import datetime

from database import async_session_maker

from repository.base import BaseRepo

from sqlalchemy import (
    select,
    insert,
    and_,
)

from defection.models import Defection, DefectionType


class RepositoryDefection(BaseRepo):

    @classmethod
    async def get_defection_type_id(cls, defection_type: str):
        async with async_session_maker() as session:
            result = await session.execute(select(DefectionType.id).where(
                DefectionType.defection_type == defection_type
            ))

            return result.scalars().first()

    @classmethod
    async def post_defection(cls, student_id: int, reason: str, defectiontype_id: int):
        async with async_session_maker() as session:
            result = await session.execute(insert(Defection).returning(Defection),
                                           [
                                               {"timedefection": datetime.datetime.now(),
                                                "student_id": student_id,
                                                "reason": reason,
                                                "defection_type_id": defectiontype_id,
                                                }
                                           ])
            await session.commit()
            return result.scalars().one()
