import aiosqlite
from ..protected import sql_protected
from .data_classes import User


@sql_protected
async def sql_get_user_by_name(username: str, password: str) -> User:
    pass


@sql_protected
async def sql_create_user(user: User) -> bool:
    pass


@sql_protected
async def sql_delete_user(user: User) -> bool:
    pass