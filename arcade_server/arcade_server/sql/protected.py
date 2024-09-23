from dataclasses import is_dataclass, fields
from core.debug import create_log
from .exceptions import SQLInjectionException
from settings import SQL_EXCEPT_VALUES


def parse_arg(element: str):
    "Берем букву и проверяем что его нет в списке опасных"
    if element in SQL_EXCEPT_VALUES:
        create_log(f'Unsecured sql request: {element}')
        raise SQLInjectionException(element)


def sql_protected_old(func):
    async def wrapped(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str):
                for elem in arg:
                    parse_arg(elem)
            elif is_dataclass(arg):
                for field in fields(arg):
                    if field.type == str:
                        for elem in getattr(arg, field.name):
                            parse_arg(elem)
        await func(*args, **kwargs)
    return wrapped


def parse_arg_new(args: list[str]):
    "Берем букву и проверяем что его нет в списке опасных"
    for element in args:
        if element in SQL_EXCEPT_VALUES:
            create_log(f'Unsecured sql request: {element}')
            raise SQLInjectionException(element)


def get_dataclass_str_values(data_class) -> list[str]:
    ans = []
    for field in fields(data_class):
        if field.type == str:
            ans += getattr(data_class, field.name)
    return ans


def sql_protected(func):
    async def wrapped(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str):
                for elem in arg:
                    parse_arg(elem)
            elif is_dataclass(arg):
                for field in fields(arg):
                    if field.type == str:
                        for elem in getattr(arg, field.name):
                            parse_arg(elem)


        await func(*args, **kwargs)
    return wrapped
