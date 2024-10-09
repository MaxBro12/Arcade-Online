from .debug import create_log
from .tomlfiles import (
    read_toml,
    write_toml,
)
from .exceptions import LoadSettingsExceprion
from settings import GameSettings, Window, SETTINGS_FILE, Window


def load_settings() -> GameSettings:
    try:
        data = read_toml(SETTINGS_FILE)
        return GameSettings(
            Window(
                width=data['window']['width'],
                height=data['window']['height'],
                max_fps=data['window']['max_fps'],
                vsync=data['window']['vsync']
            )
        )
    except KeyError as err:
        save_settings()
        raise LoadSettingsExceprion(err)


def save_settings(sets: GameSettings | None = None) -> bool:
    if sets is None:
        sets = GameSettings(window=Window())
    write_toml(
        {
            'window': {
                'width': sets.window.width,
                'height': sets.window.height,
                'max_fps': sets.window.max_fps,
                'vsync': sets.window.vsync
            }
        },
        SETTINGS_FILE
    )
    create_log('Settings saved!')
    return True
