from time import time, sleep
import uvicorn
from fastapi import FastAPI, APIRouter
from threading import Thread
from core.dot_env import get_env


class Game:
    def __init__(self) -> None:
        self.tick = 0

    def run(self):
        while True:
            self.tick += 1
            sleep(1)
            print(f'Game tick: {self.tick}')


class Server:
    def __init__(self) -> None:
        self.status = 'OK'

        self.router = APIRouter()
        self.router.add_api_route('/status', self.server_get_status, methods=['GET'])

        self.app = FastAPI(title='Game Server')
        self.app.include_router(self.router)

        self.game = Game()

        self.server_proc = Thread(name='game server', target=self.server, daemon=True)
        self.server_proc.start()

        self.game.run()
        #self.server_proc.join()

    def server(self):
        uvicorn.run(
            self.app,
            host = get_env('host'),
            port = int(get_env('port'))
        )

    async def server_get_status(self):
        return {
            'status': self.status,
            'server_time': time()
        }
