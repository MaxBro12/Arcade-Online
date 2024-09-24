from sys import argv
from os import mkdir
from os.path import exists

from core.debug import create_log
from sql.create_sql import create_bd
from sql.users_query import sql_get_user_by_name

from settings import FOLDER_FILES, SQL_DATABASE_NAME

import falcon
import falcon.asgi
import gunicorn
import uvicorn


class QuoteResource:
    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        quote = {
            'user': await sql_get_user_by_name(req.params.get('username'), req.params.get('passwod'))
        }

        resp.data = quote
        resp.status = falcon.HTTP_200


def check_files():
    if not exists(FOLDER_FILES):
        create_log('Making folder', 'info')
        mkdir(FOLDER_FILES)
    if not exists(SQL_DATABASE_NAME):
        create_log('Making SQL', 'info')
        create_bd()

    app = falcon.asgi.App()
    app.add_route('/test', QuoteResource())

    uvicorn.run(app)


def main(args: list):
    check_files()


if __name__ == "__main__":
    try:
        create_log(f'Run main: {argv}')
        main(argv[1:])
    except Exception as err:
        create_log(err, "crit")
