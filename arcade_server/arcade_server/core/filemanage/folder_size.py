from os.path import getsize, isfile
from os import scandir


def get_folder_size(folder_path) -> int:
    """Кладем сюда директорию, получаем размер сколько байтов занимает"""
    size = 0
    for element in scandir(folder_path):
        if not isfile(element):
            size += get_folder_size(element)
        size += getsize(element)
    return size