from fastapi import APIRouter

from ..constants import SERVERS, server_to_platform
from ..service import riot
from .schemas import ProfileResponseSchema

router = APIRouter()


@router.get("/{server}/{summoner_name}", status_code=200)
async def get_profile(server: SERVERS, summoner_name: str) -> ProfileResponseSchema:
    profile = await riot.get_profile(summoner_name, server_to_platform[server])
    return ProfileResponseSchema(**profile.dict())
