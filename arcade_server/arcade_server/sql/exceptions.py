from core.debug import create_log


class SQLInjectionException(Exception):
    def __init__(self, injection: str) -> None:
        msg = f'SQL Ingection founded: {injection}'
        create_log(
            msg,
            'error'
        )
        super().__init__(msg)
