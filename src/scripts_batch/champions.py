import polars as pl
import requests

from src import settings


def champions_info():
    core_url = 'https://ddragon.leagueoflegends.com/cdn/14.11.1/data/pt_BR'

    champions_data = requests.get(f'{core_url}/champion.json').json()['data']

    lst_champs = []
    for champion in champions_data:
        _champ = {
            'key': champions_data[champion]['key'],
            'id': champions_data[champion]['id'],
            'name': champions_data[champion]['name'],
            'attack': champions_data[champion]['info']['attack'],
            'defense': champions_data[champion]['info']['defense'],
            'magic': champions_data[champion]['info']['magic'],
            'difficulty': champions_data[champion]['info']['difficulty'],
            'tags': ', '.join(champions_data[champion]['tags']),
                    'hp': champions_data[champion]['stats']['hp'],
                    'hpperlevel': champions_data[champion]['stats']['hpperlevel'],
                    'mp': champions_data[champion]['stats']['mp'],
                    'mpperlevel': champions_data[champion]['stats']['mpperlevel'],
                    'movespeed': champions_data[champion]['stats']['movespeed'],
                    'armor': champions_data[champion]['stats']['armor'],
                    'armorperlevel': champions_data[champion]['stats']['armorperlevel'],
                    'spellblock': champions_data[champion]['stats']['spellblock'],
                    'spellblockperlevel': champions_data[champion]['stats']['spellblockperlevel'],
                    'attackrange': champions_data[champion]['stats']['attackrange'],
                    'hpregen': champions_data[champion]['stats']['hpregen'],
                    'hpregenperlevel': champions_data[champion]['stats']['hpregenperlevel'],
                    'mpregen': champions_data[champion]['stats']['mpregen'],
                    'mpregenperlevel': champions_data[champion]['stats']['mpregenperlevel'],
                    'crit': champions_data[champion]['stats']['crit'],
                    'critperlevel': champions_data[champion]['stats']['critperlevel'],
                    'attackdamage': champions_data[champion]['stats']['attackdamage'],
                    'attackdamageperlevel': champions_data[champion]['stats']['attackdamageperlevel'],
                    'attackspeed': champions_data[champion]['stats']['attackspeed'],
                    'attackspeedperlevel': champions_data[champion]['stats']['attackspeedperlevel'],
                    'png_path': f'https://ddragon.leagueoflegends.com/cdn/14.20.1/img/champion/{champions_data[champion]['image']['full']}',
        }
        lst_champs.append(_champ)

    pl.DataFrame(lst_champs).write_database(
        table_name='champions',
        connection=settings.DB_URI, if_table_exists='replace',
    )


if __name__ == '__main__':
    champions_info()
