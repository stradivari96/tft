from httpx import AsyncClient, codes

from ..config import get_settings
from ..constants import PLATFORMS, REGIONS
from ..domain.model import Profile, Queue
from ..exceptions import InvalidAPIKeyException, SummonerNotFoundException

BASE_URL = "https://{}.api.riotgames.com/tft"


# TODO use domain model
async def get_profile(summoner_name: str, platform: PLATFORMS = "euw1") -> Profile:
    profile = await _get_summoner_by_name(summoner_name, platform)
    profile_icon_url = (
        "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data"
        f"/global/default/v1/profile-icons/{profile['profileIconId']}.jpg"
    )
    rank_icon_url_template = (
        "https://raw.communitydragon.org/latest/plugins/rcp-fe-lol-static-assets/"
        "global/default/images/ranked-emblem/emblem-{tier}.png"
    )
    queues = await _get_entries_for_summoner(profile["id"], platform)
    return Profile(
        name=profile["name"],
        profile_icon_url=profile_icon_url,
        level=profile["summonerLevel"],
        queues={
            q["queueType"]: Queue(
                name=q["queueType"],
                tier=q["tier"],
                rank=q["rank"],
                wins=q["wins"],
                losses=q["losses"],
                lp=q["leaguePoints"],
                rank_icon_url=rank_icon_url_template.format(tier=q["tier"].lower()),
            )
            for q in queues
        },
    )


async def _get_summoner_by_name(name: str, platform: PLATFORMS):
    async with AsyncClient() as client:
        r = await client.get(
            f"{BASE_URL.format(platform)}/summoner/v1/summoners/by-name/{name}",
            headers={"X-Riot-Token": get_settings().api_key},
        )
    response = r.json()

    if "status" in response:
        if response["status"]["status_code"] == codes.NOT_FOUND:
            raise SummonerNotFoundException
        if response["status"]["status_code"] == codes.FORBIDDEN:
            raise InvalidAPIKeyException

    return response


async def _get_entries_for_summoner(summoner_id: str, platform: PLATFORMS):
    async with AsyncClient() as client:
        r = await client.get(
            f"{BASE_URL.format(platform)}/league/v1/entries/by-summoner/{summoner_id}",
            headers={"X-Riot-Token": get_settings().api_key},
        )
    return r.json()


async def _get_matches(puuid: str, region: REGIONS):
    async with AsyncClient() as client:
        matches_returned = 1000
        r = await client.get(
            f"{BASE_URL.format(region)}/match/v1/matches/by-puuid/"
            f"{puuid}/ids?count={matches_returned}",
            headers={"X-Riot-Token": get_settings().api_key},
        )
    return r.json()
