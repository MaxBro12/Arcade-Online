from time import time
import requests
from core.dot_env import get_env
from .server_dataclass import ServerStatus
from .requests_maker import make_get_request


class Server:
    def __init__(self):
        self.host = get_env('API_REQ')

    def status(self) -> ServerStatus:
        st = time()
        req =  make_get_request(f'{self.host}/status')
        if req is not None:
            return ServerStatus(
                status=req.json['status'],
                server_time=req.json['server_time'],
                ping=int((time() - st) / 1000)
            )
        return ServerStatus(status='OFFLINE',server_time=0,ping=0)
