from time import time
from threading import Thread
from core.dot_env import get_env
from .client_dataclass import ServerStatus
from .requests_maker import make_get_request


class Client:
    def __init__(self):
        self.host = get_env('API_REQ')
        self.status = ServerStatus(status='OFFLINE', server_time=0, ping=0)

        Thread(name='Server_status', target=self.get_status, daemon=True).start()

    def get_status(self):
        while True:
            st = time()
            req =  make_get_request(f'{self.host}/status')
            if req is not None:
                self.status = ServerStatus(
                    status=req.json['status'],
                    server_time=req.json['server_time'],
                    ping=int((time() - st) / 1000)
                )
            else:
                self.status = ServerStatus(status='OFFLINE',server_time=0,ping=0)
