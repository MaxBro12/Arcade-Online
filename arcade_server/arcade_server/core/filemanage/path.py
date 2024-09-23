from os import listdir, remove
from os.path import join, exists, splitext
from core import create_log
import time

from settings import MAX_FILE_DELETE_TRIES


def pjoin(*args: str) -> str:
    """Соединяет аргументы в путь до файла или папки"""
    return join(*args)


def wayfinder(way: str) -> bool:
    """Проверяет существование пути way"""
    return True if exists(way) else False


def listdir_path(where: str) -> list:
    """Возвращает список файлов по пути where с добавлением пути"""
    return list(map(lambda x: pjoin(where, x), listdir(where)))


def file_extention(path_to_file: str | None) -> str:
    if path_to_file is not None:
        return splitext(path_to_file)[1]
    else:
        return ''
