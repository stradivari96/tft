from fastapi import APIRouter

from ..service import riot
from .schemas import ProfileResponseSchema

router = APIRouter()


@router.get("/{summoner_name}", status_code=200)
async def get_profile(summoner_name: str) -> ProfileResponseSchema:
    profile = await riot.get_profile(summoner_name)
    return ProfileResponseSchema(**profile.dict())
