import datetime

from database import async_session_maker

from sqlalchemy import (
    select,
    insert,
    and_,
)

from duty.models import Defection, Student, Grade, DefectionType


class RepositoryGrade:
    @classmethod
    async def get_group_id(cls, grade, letter):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Grade.id).where(
                    and_(Grade.grade == grade, Grade.letter == letter)
                )
            )

            return result.scalars().one()


class RepositoryStudent:
    @classmethod
    async def get_studentttt(cls, name, surname, grade, letter):

        async with async_session_maker() as session:
            result = await session.execute(
                select(Student).where(
                    and_(Student.name == name, Student.surname == surname)
                )
            )
            result = result.scalars().first()
        if result:
            return result
        else:
            async with async_session_maker() as session:
                group_id = await RepositoryGrade.get_group_id(grade, letter)
                result = await session.execute(
                    insert(Student).returning(Student),
                    [
                        {"name": name, "surname": surname, "group_id": group_id}
                    ]
                )

                await session.commit()
                return result.scalars().one()


class RepositoryDefection:

    @classmethod
    async def get_defection_type_id(cls, defection_type):
        async with async_session_maker() as session:
            result = await session.execute(select(DefectionType.id).where(
                DefectionType.defection_type == defection_type
            ))

            return result.scalars().first()

    @classmethod
    async def post_defection(cls, student_id, reason, defectiontype_id):
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
