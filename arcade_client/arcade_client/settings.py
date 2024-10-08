from typing import Final
from dataclasses import dataclass


# ! DEBUG
DEBUG: Final = True
LOGGER_LEVEL: Final = 'debug'
MAIN_LOGGER: Final = 'logger'
MAIN_LOGGER_MAX_BITES: Final = 1_000_000
ERROR_LOGGER: Final = 'error'

# ! Основа
ENV_FILE: Final = '.env'
FOLDER_FILES: Final = 'data'
MAX_FILE_DELETE_TRIES: Final = 100


# ! Классы настроек
@dataclass
class Window:
    width: int = 600
    height: int = 400
    max_fps: int | None = 30
    vsync: bool = True

# ! Toml-settings
@dataclass
class GameSettings:
    window = Window()
