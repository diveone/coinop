import csv
from decimal import Decimal
import dateutil.parser as dp

from coinop.models import Coin


def load_coins_from_csv(data):
    with open(data) as csv_file:
        coin_file = csv.DictReader(csv_file)
        for row in coin_file:
            if coin_file.line_num == 1:
                continue
            date = dp.parse(row.get('Date'))
            coin = Coin(date=date,
                        name='bitcoin',
                        open=Decimal(row.get('Open')),
                        high=Decimal(row.get('High')),
                        low=Decimal(row.get('Low')),
                        close=Decimal(row.get('Close')),
                        volume=int(row.get('Volume').replace(',', '')),
                        market_cap=fix_market_cap(row.get('Market Cap')))
            coin.save()


def clean_row_data(row):
    updated_row = {}
    for key, val in row.items():
        if val in '-':
            updated_row[key] = ''
        else:
            updated_row[key] = val
    return updated_row


def fix_market_cap(mc):
    if mc == '-':
        return None
    else:
        update = mc.replace(',', '')
        return int(update)
