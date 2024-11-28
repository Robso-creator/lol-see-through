from datetime import datetime

import requests

from src import settings


def matches(puuid, start=datetime.now().strftime('%Y-%m-%d'), end=datetime.now().strftime('%Y-%m-%d')):
    start = datetime.strptime(start, '%Y-%m-%d')
    start = int(start.timestamp())

    end = datetime.strptime(end, '%Y-%m-%d')
    end = int(end.timestamp())

    headers = {
        'X-Riot-Token': settings.RIOT_API,
    }
    core_url = 'https://americas.api.riotgames.com'
    params = {
        'startTime': start,
        'endTime': end,
        'start': '0',
        'count': '100',
    }

    matches_ids = requests.get(
        f'{core_url}/lol/match/v5/matches/by-puuid/{puuid}/ids', headers=headers, params=params,
    ).json()

    lst_matches_data = []
    for match_id in matches_ids:
        match_url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}'
        match_data = requests.get(match_url, headers=headers).json()
        lst_matches_data.append(match_data)

    return lst_matches_data


if __name__ == '__main__':
    player_info = player_info('WBRL', 'WBRL Robshowsz')
    summoner_data = summoner_info(puuid=player_info['puuid'])
    matches_data = matches(puuid=player_info['puuid'], start='2024-10-01')
