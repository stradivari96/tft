from typing import List, Optional

from pydantic import BaseModel, HttpUrl, validator


class Queues(BaseModel):
    name: str
    tier: Optional[str]
    rank: Optional[str]
    lp: Optional[int]
    wins: int
    losses: int

    top_rate: float = None

    @validator("top_rate", always=True)
    def calculate_rate(cls, v, values, **kwargs):
        wins, losses = values["wins"], values["losses"]
        total_games = wins + losses
        return round(100 * wins / total_games, 1)


class ProfileResponseSchema(BaseModel):
    name: str
    profile_icon_url: HttpUrl
    level: int
    queues: List[Queues]

    class Config:
        schema_extra = {
            "example": {
                "name": "Stradivari96",
                "profile_icon_url": (
                    "https://raw.communitydragon.org/latest/plugins/"
                    "rcp-be-lol-game-data/global/default/v1/profile-icons/4627.jpg"
                ),
                "summonerLevel": 165,
            }
        }
