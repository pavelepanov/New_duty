from fastapi import APIRouter, Request, Form, Depends
from fastapi.security import OAuth2PasswordRequestForm

from fastapi.templating import Jinja2Templates
from fastapi_users import BaseUserManager, models
from fastapi_users.authentication import Strategy

from auth.auth import get_jwt_strategy, auth_backend
from auth.manager import get_user_manager
from defection.router import post_defection
from auth.permissions import fastapi_users
from auth.databasesq import async_session_maker, get_user_db
from auth.manager import UserManager

from auth.router import login


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


@router.get("/account")
def get_account(request: Request):
    return templates.TemplateResponse("account.html", {"request": request})


# @router.post("/account")
# async def post_account(request: Request, credentials: OAuth2PasswordRequestForm = Depends()):
#     #user_manager = get_user_manager()
#     user_db = get_user_db()
#     user_manager = UserManager(user_db)
#     strategy = get_jwt_strategy()
#     result = login(request, credentials, user_manager, strategy)
#     return result

@router.post("/account")
async def post_account(request: Request,
        credentials: OAuth2PasswordRequestForm = Depends(),
        user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager),
        strategy: Strategy[models.UP, models.ID] = Depends(auth_backend.get_strategy),):
    result = await login(request, credentials, user_manager, strategy)
    return result

