from time import time, sleep
import uvicorn
from fastapi import FastAPI, APIRouter
from multiprocessing import Process, Queue

queue = Queue()
router = APIRouter()


class Game:
    def __init__(self) -> None:
        self.tick = 0

    def run(self):
        while True:
            self.tick += 1
            sleep(1)
            print(f'Game tick: {self.tick}')


game = Game()
queue.put(game)

@router.get('/test')
async def server_get_status():
    game = queue.get()
    return {'msg': game.tick}


app = FastAPI(title='Game Server')
app.include_router(router)

class Server:
    def __init__(self) -> None:
        #self.server_proc = Process(name='game server', target=self.server, args=(queue,))
        #self.server_proc.start()
        #print('>>>>', self.server_proc.pid)
        #game.run()
        self.server()

    def server(self):
        uvicorn.run(app)

"""
class GameServer:
    def __init__(self) -> None:
        self.router = APIRouter()
        self.router.add_api_route('/test', self.server_get_status, methods=['GET'])

        self.app = FastAPI(title='Game Server')
        self.app.include_router(self.router)

        self.game = Game()

        self.queue = Queue()
        self.queue.put(self.game)

        self.server_proc = Process(name='game server', target=self.server, args=(self.queue,))
        self.server_proc.start()
        self.game.run()
        #self.server_proc.join()

    def server(self, queue):
        game = queue.get()
        uvicorn.run(self.app)

    async def server_get_status(self):
        return {'msg': game.tick}
"""