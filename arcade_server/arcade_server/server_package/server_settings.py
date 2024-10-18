from core.dot_env import get_env
from typing import Final


SERVER_MAIN_HOST: Final = get_env('main_host')
SERVER_MAIN_PORT: Final = int(get_env('main_port'))