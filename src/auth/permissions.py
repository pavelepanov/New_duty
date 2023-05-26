from auth.manager import get_user_manager
from fastapi_users import FastAPIUsers
from auth.databasesq import User
from auth.auth import auth_backend

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

current_superuser = fastapi_users.current_user(active=True, superuser=True)
