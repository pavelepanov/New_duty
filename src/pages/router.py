from typing import Tuple

from fastapi import APIRouter, Request, Form, Depends
from fastapi.security import OAuth2PasswordRequestForm

from fastapi.templating import Jinja2Templates
from fastapi_users import BaseUserManager, models
from fastapi_users.authentication import Strategy
from starlette.responses import Response

from auth.auth import auth_backend
from auth.manager import get_user_manager
from defection.router import post_defection

from auth.router import login, logout2
from auth.permissions import current_superuser

from xlsx.router import get_xlsx

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
    cookie = request.cookies.get("duty")
    if cookie:

        return templates.TemplateResponse("search.html", {"request": request})
    else:
        return templates.TemplateResponse("no_account.html", {"request": request})


@router.post("/search")
async def post_defection_form(request: Request, name: str = Form(...), surname: str = Form(...), grade: int = Form(...),
                              letter: str = Form(...), defection_type: str = Form(...), reason: str = Form(...)):
    result = await post_defection(name, surname, grade, letter, defection_type, reason)
    print(result)
    return templates.TemplateResponse("search.html", {"request": request, "result": result})


@router.get("/account")
def get_account(request: Request):
    cookie = request.cookies.get("duty")
    if cookie:
        print("cookie")
        return templates.TemplateResponse("account_good.html", {"request": request})
    else:
        return templates.TemplateResponse("account.html", {"request": request})
    # return templates.TemplateResponse("account.html", {"request": request})


@router.post("/account")
async def post_account(request: Request,
                       credentials: OAuth2PasswordRequestForm = Depends(),
                       user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager),
                       strategy: Strategy[models.UP, models.ID] = Depends(auth_backend.get_strategy), ):
    try:
        result = await login(request, credentials, user_manager, strategy)
        return result
    except:
        return templates.TemplateResponse("account_loser.html", {"request": request})


@router.get("/logout")
async def logout(request: Request, response: Response):
    response.delete_cookie(key="duty")


@router.get("/mail")
async def xlsx_form(request: Request):
    cookie = request.cookies.get("duty")
    if cookie:
        return templates.TemplateResponse("xlsx_get.html", {"request": request})
    else:
        return templates.TemplateResponse("no_account.html", {"request": request})


@router.post("/mail")
async def post_defection_form(request: Request, mail: str = Form(...)):
    result = await get_xlsx()
    print(mail)
    return templates.TemplateResponse("base.html", {"request": request, "result": result})





