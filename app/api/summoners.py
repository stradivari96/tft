from fastapi import APIRouter

from ..constants import PLATFORMS
from ..service import riot
from .schemas import ProfileResponseSchema

router = APIRouter()


@router.get(
    "/{platform}/{summoner_name}",
    status_code=200,
)
async def get_user(platform: PLATFORMS, summoner_name: str) -> ProfileResponseSchema:
    return await riot.get_user(summoner_name, platform)
