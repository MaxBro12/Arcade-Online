from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True, slots=True)
class ServerStatus:
    status: Literal['OK']
    server_time: int
    ping: int