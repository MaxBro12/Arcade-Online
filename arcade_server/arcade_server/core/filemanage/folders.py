from os import mkdir
from shutil import rmtree
from .path import wayfinder
from ..debug import create_log


def create_folder(name: str) -> bool:
    try:
        if not wayfinder(name):
            mkdir(name)
            return True
        return False
    except FileNotFoundError as err:
        create_log(f'Cant create folder {name}', 'error')
        return False


def delete_folder(name: str) -> bool:
    try:
        if wayfinder(name):
            rmtree(name)
            return True
        return False
    except FileNotFoundError as err:
        create_log(f'Cant delete folder {name}', 'error')
        return False
