from database import async_session_maker

from repository.base import BaseRepo

from sqlalchemy import (
    select,
    insert,
    and_,
)

from student.models import Student, Grade


class RepositoryGrade(BaseRepo):
    @classmethod
    async def get_group_id(cls, grade: int, letter: str):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Grade.id).where(
                    and_(Grade.grade == grade, Grade.letter == letter)
                )
            )

            return result.scalars().one()

    @classmethod
    async def get_info_by_group_id(cls, group_id: int):
        async with async_session_maker() as session:
            result = await session.execute(select(Grade).where(
                Grade.id == group_id
            ))
            return result.scalars().all()


class RepositoryStudent(BaseRepo):
    @classmethod
    async def get_studentttt(cls, name: str, surname: str, grade: int, letter: str):

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

    @classmethod
    async def get_all_student(cls):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Student.id))

            return result.scalars().all()

    @classmethod
    async def get_student_info_by_id(cls, student_id: int):
        async with async_session_maker() as session:
            result = await session.execute(select(Student).where(
                Student.id == student_id
            ))
            return result.scalars().first()
