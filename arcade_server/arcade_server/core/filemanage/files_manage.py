from time import sleep
from os import remove
from ..debug import create_log
from .path import wayfinder
from .exceptions import FileMaxTriesException

from settings import MAX_FILE_DELETE_TRIES


def load_file(path_to_file: str) -> bytes | None:
    try:
        if wayfinder(path_to_file):
            with open(path_to_file, 'rb') as f:
                return f.read()
    except Exception as err:
        create_log(f'Unexpected exception:\n{err}', 'error')


def delete_file(path_to_file: str) -> bool:
    tries = 0
    while wayfinder(path_to_file):
        try:
            remove(path_to_file)
            return True
        except Exception as err:
            create_log(f'Still waiting closing {path_to_file}', 'debug')
            tries += 1

            if tries >= MAX_FILE_DELETE_TRIES:
                raise FileMaxTriesException(path_to_file)
            sleep(5)
    return False
