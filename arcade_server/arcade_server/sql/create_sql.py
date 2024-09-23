import sqlite3
from core.debug import create_log
from core.filemanage import delete_file
from settings import SQL_DATABASE_NAME, SQL_CREATE_BANS_DATABASE


def create_bd():
    try:
        with sqlite3.connect(SQL_DATABASE_NAME) as db:
            cursor = db.cursor()
            
            # ! Все таблицы которые нужно создать
            cursor.execute(SQL_CREATE_BANS_DATABASE)
            
            db.commit()
            cursor.close()
    except sqlite3.Error as error:
        create_log(error, 'error')
        create_log(f'Delete sql database {SQL_DATABASE_NAME}', 'info')
        delete_file(SQL_DATABASE_NAME)
        exit(1)
