from fastapi import APIRouter, Depends

from defection.repository import RepositoryDefection
from defection.schemas import Defection
from student.repository import RepositoryStudent
from auth.permissions import current_superuser
from auth.databasesq import User

from student.repository import RepositoryStudent

router = APIRouter(
    prefix="/defection",
    tags=["defection"],
)


@router.post("add/defection", response_model=Defection)
async def post_defection(name: str, surname: str, grade: int, letter: str, defection_type: str, reason: str,
                         user: User = Depends(current_superuser)):
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


@router.get("/get/defection/no_card")
async def get_defection_no_card_all():
    count_students_defection = {}
    students_id = await RepositoryStudent.get_all_student()
    for id in students_id:
        result = await RepositoryDefection.get_defection_with_id_student_and_defection_id(id, 1)
        count_students_defection[id] = len(result)
    return count_students_defection


@router.get("/get/defection/being_late")
async def get_defection_no_card_all():
    count_students_defection = {}
    students_id = await RepositoryStudent.get_all_student()
    for id in students_id:
        result = await RepositoryDefection.get_defection_with_id_student_and_defection_id(id, 2)
        count_students_defection[id] = len(result)
    return count_students_defection


@router.get("/get/defection/appearance")
async def get_defection_no_card_all():
    count_students_defection = {}
    students_id = await RepositoryStudent.get_all_student()
    for id in students_id:
        result = await RepositoryDefection.get_defection_with_id_student_and_defection_id(id, 3)
        count_students_defection[id] = len(result)
    return count_students_defection
