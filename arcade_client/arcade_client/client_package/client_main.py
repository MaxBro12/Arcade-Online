from time import time, sleep
from threading import Thread
from core.dot_env import get_env
from .client_dataclass import ServerStatus
from .requests_maker import ServerSession


class Client:
    def __init__(self):
        self.server_requester = ServerSession()
        self.host = get_env('API_REQ')
        self.status = ServerStatus(status='OFFLINE', server_time=0, ping=0)

        Thread(name='Server_status', target=self.get_status, daemon=True).start()

    def get_status(self):
        while True:
            st = time()
            req =  self.server_requester.get(f'{self.host}/status')
            if req is not None:
                self.status = ServerStatus(
                    status=req.json['status'],
                    server_time=req.json['server_time'],
                    ping=int((time() - st) * 1000)
                )
                print(f'Status: {self.status.status}\nPing: {self.status.ping}\nCallback: {time() - self.status.server_time}')
            else:
                self.status = ServerStatus(status='OFFLINE',server_time=0,ping=0)
            sleep(1)

    def authorize(self):
        self.server_requester.post(
            f'{self.host}/authorize',
            params={
                'username': get_env('username'),
                'password': get_env('password')
            }
        )