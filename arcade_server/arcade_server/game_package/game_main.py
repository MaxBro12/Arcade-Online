from time import sleep


class Game:
    def __init__(self) -> None:
        self.tick = 0

    def run(self):
        # ! Сначала грузимся и выполняем запуски

        # ! Запускаем цикл игры
        self.update()

    def update(self):
        while True:
            self.tick += 1
            sleep(1)
            print(f'Game tick: {self.tick}')