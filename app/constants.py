from typing import Literal

# Translate to PLATFORMS later
SERVERS = Literal[
    "br",
    "eune",
    "euw",
    "jp",
    "kr",
    "las",
    "lan",
    "na",
    "oc",
    "tr",
    "ru",
]

server_to_platform = {
    "br": "br1",
    "eune": "eun1",
    "euw": "euw1",
    "jp": "jp1",
    "kr": "kr",
    "las": "la1",
    "lan": "la2",
    "na": "na1",
    "oc": "oc1",
    "tr": "tr1",
    "ru": "ru",
}

# Riot API
PLATFORMS = Literal[
    "br1",
    "eun1",
    "euw1",
    "jp1",
    "kr",
    "la1",
    "la2",
    "na1",
    "oc1",
    "tr1",
    "ru",
]

REGIONS = Literal["americas", "asia", "europe"]
