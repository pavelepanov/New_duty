from fastapi import APIRouter, Depends

from defection.repository import RepositoryDefection
from defection.schemas import Defection
from student.repository import RepositoryStudent
from auth.permissions import current_superuser
from auth.databasesq import User

router = APIRouter(
    prefix="/defection",
    tags=["defection"],
)


@router.post("add/defection", response_model=Defection)
async def post_defection(name: str, surname: str, grade: int, letter: str, defection_type: str, reason: str, user: User = Depends(current_superuser)):
    """
    :param name: name of student
    :param surname: surname of student
    :param grade: grade of student for get group_id
    :param letter: grade's letter of student for get group_id
    :param defection_type: defection type for get defection_type_id
    :param reason: why did the student do it
    :return:
    """
    defectiontype_id = await RepositoryDefection.get_defection_type_id(defection_type)
    student = await RepositoryStudent.get_studentttt(name, surname, grade, letter)

    result = await RepositoryDefection.post_defection(student.id, reason, defectiontype_id)

    return result
