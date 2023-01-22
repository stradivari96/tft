from typing import List

from pydantic import BaseModel, HttpUrl


class Queues(BaseModel):
    queueType: str
    ratedTier: str
    ratedRating: str
    ratedRating: str
    wins: int
    losses: int


class ProfileResponseSchema(BaseModel):
    name: str
    profile_icon_url: HttpUrl
    summonerLevel: int
    leaguePoints: int = None
    other_queues: List[Queues]

    # TODO: Literals?
    tier: str = None
    rank: str = None

    wins: int = None
    losses: int = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Stradivari96",
                "profile_icon_url": "https://raw.communitydragon.org/latest/plugins/"
                "rcp-be-lol-game-data/global/default/v1/profile-icons/4627.jpg",
                "summonerLevel": 165,
                "leaguePoints": 20,
                "tier": "PLATINUM",
                "rank": "IV",
                "wins": 9,
                "losses": 49,
            }
        }
