from .debug import create_log


class LoadTokenException(Exception):
    def __init__(self, msg: str):
        super().__init__(
            f'Cant load token {msg}'
        )
