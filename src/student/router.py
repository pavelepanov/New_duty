from fastapi import APIRouter

from student.repository import RepositoryStudent, RepositoryGrade

router = APIRouter(
    prefix="/student",
    tags=["student"],
)


@router.get("/all/student")
async def get_all_student():
    result = await RepositoryStudent.get_all_student()
    return result


@router.get("/student_name_surname")
async def get_student_info_by_id(student_id: int):
    result = await RepositoryStudent.get_student_info_by_id(student_id)
    return result


@router.get("/group_info")
async def get_grade_info_by_id(group_id: int):
    result = await RepositoryGrade.get_info_by_group_id(group_id)
    return result
