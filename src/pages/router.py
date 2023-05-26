from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from defection.router import post_defection

router = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/base")
def get_base_template(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/search")
def get_search(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@router.post("/search")
async def post_defection_form(request: Request, name: str = Form(...), surname: str = Form(...), grade: int = Form(...),
                        letter: str = Form(...), defection_type: str = Form(...), reason: str = Form(...)):
    result = await post_defection(name, surname, grade, letter, defection_type, reason)
    print(result)
    return templates.TemplateResponse("search.html", {"request": request, "result": result})

