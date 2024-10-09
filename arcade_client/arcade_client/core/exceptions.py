from .debug import create_log


class LoadTokenException(Exception):
    def __init__(self, msg: str):
        create_log(f'Cant load token {msg}')
        super().__init__(
            f'Cant load token {msg}'
        )


class FileMaxTriesException(Exception):
    def __init__(self, file_name):
        self.txt = f'Cant delete file {file_name} max runs out!'
        super().__init__(self.txt)


class LoadSettingsExceprion(Exception):
    def __init__(self, error) -> None:
        create_log(error, 'error')
        super().__init__(error)