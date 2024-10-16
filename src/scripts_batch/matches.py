import requests
import urllib.parse
from src import settings
from datetime import datetime


def player_uuid(tag=None, name=None):
    core_url = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id'
    headers = {
        "X-Riot-Token": settings.RIOT_API,
    }

    puuid_response = requests.get(f'{core_url}/{urllib.parse.quote(name)}/{urllib.parse.quote(tag)}',
                                  headers=headers).json()
    puuid = puuid_response['puuid']

    summoner_response = requests.get(f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}',
                                     headers=headers).json()

    return {
        'summoner_id': summoner_response['id'],
        'acount_id': summoner_response['accountId'],
        'puuid': summoner_response['puuid'],
        'profile_icon_id': summoner_response['profileIconId'],
        'revision_date': summoner_response['revisionDate'],
        'summoner_level': summoner_response['summonerLevel']
    }


def matches(puuid, start=datetime.now().strftime('%Y-%m-%d'), end=datetime.now().strftime('%Y-%m-%d')):
    start = datetime.strptime(start, '%Y-%m-%d')
    start = int(start.timestamp())

    end = datetime.strptime(end, '%Y-%m-%d')
    end = int(end.timestamp())

    headers = {
        "X-Riot-Token": settings.RIOT_API,
    }
    core_url = 'https://americas.api.riotgames.com'
    params = {
        'startTime': start,
        'endTime': end,
        'start': '0',
        'count': '3'
    }

    matches_ids = requests.get(f'{core_url}/lol/match/v5/matches/by-puuid/{puuid}/ids', headers=headers, params=params).json()

    lst_matches_data = []
    for match_id in matches_ids:
        match_url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}'
        match_data = requests.get(match_url, headers=headers).json()
        lst_matches_data.append(match_data)

    return lst_matches_data


if __name__ == '__main__':
    dd = player_uuid('WBRL', 'WBRL Robshowsz')
    tt = matches(dd['puuid'], start='2024-10-01')
    breakpoint()