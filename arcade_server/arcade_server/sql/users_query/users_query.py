import aiosqlite
from core.debug import create_log
from ..protected import sql_protected
from .classes import User

from settings import (
    SQL_DATABASE_NAME,
    SQL_TABLE_USERS
)


@sql_protected
async def sql_get_user_by_name(username: str, password: str) -> User | None:
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
        return None


@sql_protected
async def sql_create_user(user: User) -> bool:
    pass


@sql_protected
async def sql_delete_user(user: User) -> bool:
    pass


async def db_all_bans() -> list[UserBanned,]:
    create_log('db_all_bans > called', 'debug')
    try:
        bans = []
        async with aiosqlite.connect(SQL_DATABASE_NAME) as db:
            async with db.execute(f"SELECT * FROM {SQL_TABLE_BANS}") as cursor:
                async for row in cursor:
                    bans.append(
                        UserBanned(
                            row[0],
                            row[1]
                        )
                    )
        create_log(f'db_all_bans > found {len(bans)}', 'debug')
        return bans

    except aiosqlite.Error as err:
        create_log(err, 'error')
        return []


@sql_protected
async def db_user_banned(user_id: int) -> bool:
    create_log(f'db_user_banned > call with args {user_id}')
    try:
        async with aiosqlite.connect(SQL_DATABASE_NAME) as db:
            async with db.execute(f"""SELECT EXISTS (SELECT user_id FROM {SQL_TABLE_BANS} WHERE user_id={user_id});""") as cursor: 
                return True if list(await cursor.fetchall())[0][0] == 1 else False
    except aiosqlite.Error as err:
        create_log(err, 'error')
        return False


@sql_protected
async def db_ban(user: UserBanned) -> bool:
    create_log(f'db_ban > called with args {user}')
    try:
        async with aiosqlite.connect(SQL_DATABASE_NAME) as db:
            await db.execute(
                f"""
                INSERT INTO {SQL_TABLE_BANS} (user_id, reason)
                VALUES ({user.user_id}, '{user.reason}');"""   
            )
            await db.commit()
            create_log('db_ban > True')
            return True
    except aiosqlite.Error as err:
        create_log('db_ban > False')
        create_log(err, 'error')
        return False


@sql_protected
async def db_unban(user_id: int) -> bool:
    create_log(f'db_unban > called with args {user_id}')
    try:
        async with aiosqlite.connect(SQL_DATABASE_NAME) as db:
            await db.execute(
                f"""DELETE FROM {SQL_TABLE_BANS} WHERE user_id={user_id};"""
            )
            await db.commit()
            create_log('db_ban > True')
            return True
    except aiosqlite.Error as err:
        create_log(err, 'error')
        return False