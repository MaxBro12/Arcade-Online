import aiosqlite
from core.debug import create_log
from ..protected import sql_protected
from .classes import User

from settings import (
    SQL_DATABASE_NAME,
    SQL_TABLE_USERS
)


@sql_protected
async def sql_get_user_by_name(username: str, password: str) -> User | dict | None:
    create_log(f'sql_get_user_by_name > {username}', 'debug')
    try:
        async with aiosqlite.connect(SQL_DATABASE_NAME) as db:
            async with db.execute(f"SELECT * FROM {SQL_TABLE_USERS} WHERE username={username} AND password={password};") as cursor:
                async for row in cursor:
                    user = User(
                        username=row[0],
                        password=row[1],
                        email=row[2],
                        last_login=row[3]
                    )
                    return user
    except aiosqlite.Error as err:
        create_log(f'sql_get_user_by_name > {err}', 'error')
        return {'test': 'not'}


@sql_protected
async def sql_create_user(user: User) -> bool:
    pass


@sql_protected
async def sql_delete_user(user: User) -> bool:
    pass