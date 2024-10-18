import uvicorn
from time import time
from fastapi import FastAPI, APIRouter, Request
from threading import Thread
from .server_settings import SERVER_MAIN_PORT, SERVER_MAIN_HOST
from game_package.game_main import Game
from game_package.game_players import Player

class Server:
    def __init__(self) -> None:
        self.status = 'OK'

        self.router = APIRouter()
        self.router.add_api_route('/status', self.server_get_status, methods=['GET'])

        self.app = FastAPI(title='Game Server')
        self.app.include_router(self.router)

        self.game = Game()

        Thread(name='game server', target=self.server, daemon=True).start()

        self.game.run()

    def server(self):
        uvicorn.run(
            self.app,
            host = SERVER_MAIN_HOST,
            port = SERVER_MAIN_PORT
        )

    async def server_get_status(self):
        return {
            'status': self.status,
            'server_time': time()
        }

    async def authorize(self, request: Request):
        params = request.json()
        print(params)
        self.game.players.append(
            Player(
                request.session
            )
        )