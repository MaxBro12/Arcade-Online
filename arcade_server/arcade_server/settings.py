from typing import Final


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

# ! SQL
SQL_DATABASE_NAME: Final = 'db.sqlite3'

SQL_EXCEPT_VALUES: Final = (
    '"',
    '\'',
    ':',
    ';'
)

SQL_TABLE_USERS: Final = 'users'
SQL_TABLE_CHARS: Final = 'chars'
SQL_TABLE_USER_CHARS: Final = 'user_chars'
SQL_TABLE_IP_BANS: Final = 'ip_bans'

SQL_CREATE_TABLE_USERS: Final = f'''CREATE TABLE IF NOT EXISTS {SQL_TABLE_USERS} (
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR(15) NOT NULL UNIQUE,
    user_password VARCHAR(15) NOT NULL,
    user_email VARCHAR(256) NOT NULL,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP);'''

SQL_CREATE_TABLE_CHARS: Final = f'''CREATE TABLE IF NOT EXISTS {SQL_TABLE_CHARS} (
    char_id INTEGER PRIMARY KEY,
    char_name INTEGER UNIQUE);'''

SQL_CREATE_TABLE_USER_CHARS: Final = f'''CREATE TABLE IF NOT EXISTS {SQL_TABLE_USER_CHARS} (
    user_id INTEGER NOT NULL,
    char_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES {SQL_TABLE_USERS}(user_id) ON DELETE CASCADE),
    FOREIGN KEY(char_id) REFERENCES {SQL_TABLE_CHARS}(char_id) ON DELETE CASCADE);'''

SQL_CREATE_TABLE_IP_BANS: Final = f'''CREATE TABLE IF NOT EXISTS {SQL_CREATE_TABLE_BANS} (
    );'''