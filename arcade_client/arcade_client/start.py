from os.path import exists
from os import mkdir

from settings import (
    FOLDER_FILES,
    SETTINGS_FILE,
)
from core.debug import create_log
from core.settings_toml import (
    load_settings,
    save_settings
)


def main_checks():
    if not exists(FOLDER_FILES):
        mkdir(FOLDER_FILES)
        create_log(f'Create {FOLDER_FILES}', 'info')

    if not exists(SETTINGS_FILE):
        save_settings()
        create_log(f'Create {SETTINGS_FILE}', 'info')