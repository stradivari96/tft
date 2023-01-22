from http import HTTPStatus

from httpx import AsyncClient

from ..config import get_settings
from ..constants import PLATFORMS, REGIONS
from ..exceptions import InvalidAPIKeyException, SummonerNotFoundException

BASE_URL = "https://{}.api.riotgames.com/tft"


async def get_summoner_by_name(name: str, platform: PLATFORMS):
    async with AsyncClient() as client:
        r = await client.get(
            f"{BASE_URL.format(platform)}/summoner/v1/summoners/by-name/{name}",
            headers={"X-Riot-Token": get_settings().api_key},
        )
    response = r.json()

    if "status" in response:
        if response["status"]["status_code"] == HTTPStatus.NOT_FOUND:
            raise SummonerNotFoundException
        if response["status"]["status_code"] == HTTPStatus.FORBIDDEN:
            raise InvalidAPIKeyException

    return response


async def get_entries_for_summoner(summoner_id: str, platform: PLATFORMS):
    async with AsyncClient() as client:
        r = await client.get(
            f"{BASE_URL.format(platform)}/league/v1/entries/by-summoner/{summoner_id}",
            headers={"X-Riot-Token": get_settings().api_key},
        )
    return r.json()


async def get_matches(puuid: str, region: REGIONS):
    async with AsyncClient() as client:
        matches_returned = 1000
        r = await client.get(
            f"{BASE_URL.format(region)}/match/v1/matches/by-puuid/"
            f"{puuid}/ids?count={matches_returned}",
            headers={"X-Riot-Token": get_settings().api_key},
        )
    return r.json()


# TODO use domain model
async def get_user(summoner_name, platform="euw1") -> dict:
    summoner = await get_summoner_by_name(summoner_name, platform)
    summoner["other_queues"] = []
    summoner["profile_icon_url"] = (
        "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data"
        f"/global/default/v1/profile-icons/{summoner['profileIconId']}.jpg"
    )

    entries = await get_entries_for_summoner(summoner["id"], platform)
    for e in entries:
        if e["queueType"] == "RANKED_TFT":
            summoner.update(e)
        else:
            summoner["other_queues"].append(e)
    summoner["top_rate"] = round(
        summoner["wins"] * 100 / (summoner["wins"] + summoner["losses"]), 1
    )
    return summoner
