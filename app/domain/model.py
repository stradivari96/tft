from dataclasses import asdict, dataclass
from typing import Dict, Optional


@dataclass
class Queue:
    name: str
    tier: Optional[str]
    rank: Optional[str]
    lp: Optional[int]
    wins: int
    losses: int

    @property
    def top_rate(self):
        total_games = self.wins + self.losses
        return round(100 * self.wins / total_games, 1)


@dataclass
class Profile:
    name: str
    level: int
    profile_icon_url: str
    queues: Dict[str, Queue]

    def dict(self) -> dict:
        return asdict(self)
