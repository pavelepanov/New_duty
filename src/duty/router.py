from fastapi import APIRouter

from duty.repository import RepositoryDefection, RepositoryStudent, RepositoryGrade

router = APIRouter(
    prefix="/duty",
    tags=["duty"],
)


@router.get("/")
async def get_home_page():
    return {"answer": "Hello world"}


@router.post("/add/defection")
async def post_defection(name: str, surname: str, grade: int, letter: str, defection_type: str, reason: str):
    student_id = RepositoryStudent.get_studentttt(name, surname, grade, letter)
    defectiontype_id = RepositoryDefection.get_defection_type_id(defection_type)

    result = await RepositoryDefection.post_defection(student_id, reason, defectiontype_id)

    return result


@router.get("/grade_id")
async def get_grade_id(grade: int, letter: str):
    result = await RepositoryGrade.get_group_id(grade, letter)
    return result


@router.get("defectiontype_id")
async def get_defectiontype_id(defection_type: str):
    result = await RepositoryDefection.get_defection_type_id(defection_type)

    return result


@router.post("/student")
async def student_id(name: str, surname: str, grade: int, letter: str):
    result = await RepositoryStudent.get_studentttt(name, surname, grade, letter)

    return result


@router.post("defection_real")
async def defectionnn(name: str, surname: str, grade: int, letter: str, defection_type: str, reason: str):
    defectiontype_id = await RepositoryDefection.get_defection_type_id(defection_type)
    student = await RepositoryStudent.get_studentttt(name, surname, grade, letter)

    result = await RepositoryDefection.post_defection(student.id, reason, defectiontype_id)

    return result
