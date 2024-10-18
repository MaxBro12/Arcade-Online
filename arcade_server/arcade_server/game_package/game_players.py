from dataclasses import dataclass


@dataclass(slots=True)
class Player:
    session: dict


class Players:
    players: list[Player,] = []

    def __getitem__(self, item: int) -> Player:
        return self.players[item]

    def __setitem__(self, key, player: Player):
        self.players[key] = player

    def __iter__(self) -> list[Player,]:
        return self.players

    def __len__(self) -> int:
        return len(self.players)

    def __delitem__(self, key: int):
        del self.players[key: int]

    def __contains__(self, item) -> bool:
        return True if item in self.players else False