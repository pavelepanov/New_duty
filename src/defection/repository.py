import datetime
from typing import List

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

    @classmethod
    async def get_defection_no_card(cls):
        async with async_session_maker() as session:
            result = await session.execute(select(Defection).where(
                DefectionType.defection_type == "no card"
            ))

            return result.scalars().all()

    # @classmethod
    # async def get_defection_with_id_student_no_card(cls, student_ids: List[int]):
    #     mydict = {}
    #     async with async_session_maker() as session:
    #         for id in student_ids:
    #             result = await session.execute(select(Defection.defection_type_id).where(and_(
    #                 Defection.student_id == id,
    #                 Defection.defection_type_id == 1
    #             )))
    #             if id in mydict:
    #                 mydict[id] += 1
    #             else:
    #                 mydict[id] = 1
    #
    #     return mydict

    @classmethod
    async def get_defection_with_id_student_and_defection_id(cls, student_id, defection_id):
        async with async_session_maker() as session:
            result = await session.execute(select(Defection).where(and_(
                Defection.defection_type_id == defection_id,
                Defection.student_id == student_id)))
            return result.scalars().all()

