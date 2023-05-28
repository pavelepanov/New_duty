from fastapi import APIRouter
from student.repository import RepositoryStudent

router = APIRouter(
    prefix="/student",
    tags=["student"],
)

@router.get("/all/student")
async def get_all_student():
    result = await RepositoryStudent.get_all_student()
    return result