from time import time
import requests
from core.dot_env import get_env
from .server_dataclass import ServerStatus


class Server:
    def __init__(self):
        self.host = get_env('API_REQ')

    @staticmethod
    def status() -> ServerStatus:
        st = time()
        req =  requests.get(
            'http://127.0.0.1:8000/status'
        ).json()
        return ServerStatus(
            status=req['status'],
            server_time=req['server_time'],
            ping=int((time() - st) / 1000)
        )
