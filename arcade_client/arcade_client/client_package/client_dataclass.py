from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True, slots=True)
class ResponseData:
    status: int
    json: dict


@dataclass(frozen=True, slots=True)
class ServerStatus:
    status: Literal['OK', 'OFFLINE']
    server_time: int
    ping: int