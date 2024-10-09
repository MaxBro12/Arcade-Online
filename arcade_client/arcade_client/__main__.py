from sys import argv
from core.debug import create_log
from start import main_checks
from game_package.game_main import Game


def main(args: list):
    main_checks()
    game_cl = Game()
    game_cl.setup()
    game_cl.run()


if __name__ == "__main__":
    try:
        create_log(f'Run main: {argv}')
        main(argv[1:])
    except Exception as err:
        create_log(err, "crit")
