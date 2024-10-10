import socket
import json
from .client_dataclass import ServerStatus
from core.dot_env import get_env
from time import time
from threading import Thread

class ClientSocket:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("127.0.0.1", 8228)) # подключаемся к айпи адресу сервера

        self.status = ServerStatus(status='OFFLINE',server_time=0,ping=0)

        self.players = [] # Создаем массив для хранения данных об игроках
        Thread(target=self.get_server_status).start() # Делаем новый поток с циклом, в которым берем данные об игроках

    def get_server_status(self):
        while True:
            st = time()
            self.sock.sendall(bytes(json.dumps({
                "request": "server_status"
            }), 'UTF-8')) # Отправляем серверу запрос для получения игроков

            received = json.loads(self.sock.recv(1024).decode('UTF-8'))
            print(received)

            self.status = ServerStatus(status=received['response']['status'],server_time=0,ping=int((time() - st) * 1000)) # сохраняем результат запроса в переменную
