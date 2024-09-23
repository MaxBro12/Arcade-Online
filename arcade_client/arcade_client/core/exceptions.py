from .debug import create_log


class LoadTokenException(Exception):
    def __init__(self, msg: str):
        super().__init__(
            f'Cant load token {msg}'
        )


class FileMaxTriesException(Exception):
    def __init__(self, file_name):
        self.txt = f'Cant delete file {file_name} max runs out!'
        super().__init__(self.txt)


class TelegramNoneException(Exception):
    def __init__(self, error: str) -> None:
        create_log(error, 'error')
        super().__init__(error)


class SQLInjectionException(Exception):
    def __init__(self, injection: str) -> None:
        msg = f'SQL Ingection founded: {injection}'
        create_log(
            msg,
            'error'
        )
        super().__init__(msg)