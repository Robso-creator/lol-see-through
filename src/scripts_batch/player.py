import urllib.parse

import requests

from src import settings


def player_info(tag=None, name=None):
    core_url = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id'
    headers = {
        'X-Riot-Token': settings.RIOT_API,
    }

    puuid_response = requests.get(
        f'{core_url}/{urllib.parse.quote(name)}/{urllib.parse.quote(tag)}',
        headers=headers,
    ).json()

    summoner_response = requests.get(
        f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid_response['puuid']}',
        headers=headers,
    ).json()

    return {
        'summoner_id': summoner_response['id'],
        'acount_id': summoner_response['accountId'],
        'puuid': summoner_response['puuid'],
        'profile_icon_id': summoner_response['profileIconId'],
        'revision_date': summoner_response['revisionDate'],
        'summoner_level': summoner_response['summonerLevel'],
        'game_name': puuid_response['gameName'],
        'tag_line': puuid_response['tagLine'],
    }
