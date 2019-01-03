from decimal import Decimal
from coinop.models import Coin


def coin_factory(coin_name, coin_data):
    """
    Create a coin and return it.

    :param coin_name: string, name of the cryptocurrency
    :param coin_data: dict
    :return:
    """

    coin = Coin(date=coin_data.get('Date'),
                name=coin_name,
                open=Decimal(coin_data.get('Open')),
                high=Decimal(coin_data.get('High')),
                low=Decimal(coin_data.get('Low')),
                close=Decimal(coin_data.get('Close')),
                volume=format_str_int(coin_data.get('Volume')),
                market_cap=format_str_int(coin_data.get('Market Cap')))
    coin.save()
    return coin


def format_str_int(s):
    if s == '-':
        return None
    else:
        update = s.replace(',', '')
        return int(update)
