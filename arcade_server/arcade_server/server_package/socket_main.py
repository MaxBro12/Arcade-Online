import json
import socket
from time import time
from threading import Thread

from core.debug import create_log
from core.dot_env import get_env
from game_package.game_main import Game


class ServerSocket:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((get_env('host'), int(get_env('port'))))
        self.sock.listen(10)

        print('test')
        self.status = 'OK'

        self.users = []

        self.game = Game()

        self.server_proc = Thread(name='game server', target=self.server, daemon=True)
        self.server_proc.start()

        self.game.run()
        #self.server_proc.join()

    def server(self):
        while True:
            conn, addr = self.sock.accept()
            print("New connection", addr)
            Thread(target=self.handle_client, args=(conn,)).start()

    def handle_client(self, conn: socket.socket):
        user = {
            'name': conn.getsockname()
        }
        self.users.append(user)

        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    print(f'Disconect: {user['name']}')
                    break
                data = json.loads(data.decode('utf-8'))
                if data['request'] == 'server_status':
                    conn.sendall(bytes(json.dumps({
                        'response': self.server_get_status()
                    }), 'UTF-8'))
            except Exception as err:
                create_log(err, 'error')

        self.users.remove(user)

    def server_get_status(self):
        return {
            'status': self.status,
            'server_time': time()
        }