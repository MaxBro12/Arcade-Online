from sys import argv
from core.debug import create_log
from game_package.game_main import Game


def main(args: list):
    game_cl = Game()


if __name__ == "__main__":
    try:
        create_log(f'Run main: {argv}')
        main(argv[1:])
    except Exception as err:
        create_log(err, "crit")
