import pandas as pd
import requests

from src.database import send_to_db


def items():
    core_url = 'https://ddragon.leagueoflegends.com/cdn/14.11.1/data/pt_BR'

    items_data = requests.get(f'{core_url}/item.json').json()['data']

    lst_items_data = []

    for item_id in items_data:
        _item = {
            'id': item_id,
            'name': items_data[item_id]['name'],
            'gold_value': items_data[item_id]['gold']['total'],
            'tags': ', '.join(items_data[item_id]['tags']),
            'purchasable': items_data[item_id]['gold']['purchasable'],
            'png_path': f'https://ddragon.leagueoflegends.com/cdn/14.21.1/img/item/{item_id}.png',
            'teste': 10,
        }
        lst_items_data.append(_item)

    send_to_db(pd.DataFrame(lst_items_data), 'items')


if __name__ == '__main__':
    items()
