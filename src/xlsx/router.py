from fastapi import APIRouter

from xlsx.utils import get_table_no_card, get_table_appearance, get_table_being_late

router = APIRouter(
    prefix="/xlsx",
    tags=["xlsx"],
)


@router.get("/xlsx")
async def get_xlsx():
    no_card = await get_table_no_card()
    being_late = await get_table_being_late()
    appearance = await get_table_appearance()
    return no_card, being_late, appearance
