from fastapi import APIRouter, Depends, HTTPException, Request
from auth.auth import auth_backend
from fastapi_users import BaseUserManager, models
from fastapi_users.authentication import backend, Strategy
from fastapi_users.router import ErrorCode
from starlette import status

from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.permissions import fastapi_users
from fastapi.security import OAuth2PasswordRequestForm

from auth.manager import get_user_manager

router = APIRouter(
    prefix="/login",
    tags=["pages"]
)


@router.post("/login_real")
async def login(
        request: Request,
        credentials: OAuth2PasswordRequestForm = Depends(),
        user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager),
        strategy: Strategy[models.UP, models.ID] = Depends(auth_backend.get_strategy),
        requires_verification=None):
    user = await user_manager.authenticate(credentials)

    if user is None or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorCode.LOGIN_BAD_CREDENTIALS,
        )
    if requires_verification and not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorCode.LOGIN_USER_NOT_VERIFIED,
        )
    response = await auth_backend.login(strategy, user)
    await user_manager.on_after_login(user, request, response)
    return response
