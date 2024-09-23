from dataclasses import dataclass
from datetime import date, datetime


@dataclass(frozen=True, slots=True)
class User:
    username: str
    password: str
    email: str
    last_login: datetime = datetime.now()