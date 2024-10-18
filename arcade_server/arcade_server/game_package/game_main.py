from time import sleep
from .game_players import Player, Players


class Game:
    def __init__(self) -> None:
        self.tick = 0
        self.players = Players()

    def run(self):
        # ! Сначала грузимся и выполняем запуски

        # ! Запускаем цикл игры
        self.update()

    def update(self):
        while True:
            self.tick += 1
            sleep(1)
            print(f'Game tick: {self.tick}')