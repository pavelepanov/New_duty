from fastapi import APIRouter

router = APIRouter(
    prefix="/duty",
    tags=["duty"],
)


@router.get("/")
async def get_home_page():
    return {"answer": "Hello world"}
