from fastapi import FastAPI
from fastapi_users import fastapi_users, FastAPIUsers
from starlette.staticfiles import StaticFiles

from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from defection.router import router as router_duty
from pages.router import router as router_pages

from auth.permissions import fastapi_users

from auth.router import router as router_auth

app = FastAPI(
    title="New defection"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_duty)
app.include_router(router_pages)
app.include_router(router_auth)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


