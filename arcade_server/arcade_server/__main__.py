from sys import argv
from os import mkdir
from os.path import exists

from core.debug import create_log
from sql.create_sql import create_bd

from settings import FOLDER_FILES, SQL_DATABASE_NAME

import falcon
import falcon.asgi
import gunicorn


class QuoteResource:
    async def get(self, req, resp):
        quote = {
            'test': 'ыыыы'
        }

        resp.media = quote


def check_files():
    if not exists(FOLDER_FILES):
        create_log('Making folder', 'info')
        mkdir(FOLDER_FILES)
    if not exists(SQL_DATABASE_NAME):
        create_log('Making SQL', 'info')
        create_bd()


app = falcon.asgi.App()
app.add_route('/test', QuoteResource())


def main(args: list):
    check_files()


if __name__ == "__main__":
    try:
        create_log(f'Run main: {argv}')
        main(argv[1:])
    except Exception as err:
        create_log(err, "crit")
