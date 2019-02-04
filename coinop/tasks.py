"""
Redis Queue

- Task functions must be separate from the job and queue execution!
- Workers must be active to execute the queue.
- If no workers are active, jobs are enqueued.
- When a worker becomes active, each job in the queue will run.

Example:
    >>> import redis, time
    >>> from rq import Queue
    >>> redis_conn = redis.Redis()
    >>> q = Queue('high', connection=redis_conn)
    >>> job = q.enqueue(daily_coins)
    >>> time.sleep(3)
    >>> print(job.result)

"""
import datetime as dt
import requests

from flask import current_app
from flask_rq2 import RQ

from coinop.factories import coin_factory
from coinop.serializers import coin_schema, Coin

import redis
from rq import Queue

rq = RQ()
redis_con = redis.Redis()

q = Queue('low', connection=redis_con)


@rq.job('high')
def daily_coins():
    """
    TODO: create supervisord config for coinop to send command to start workers in background
    :return:
    """
    with rq.app.app_context():
        url = current_app.config['COINAPI_URL']
        api_key = current_app.config['COINAPI_KEY']
        endpoint = f"{url}/v1/ohlcv/COINBASE_SPOT_BTC_USD/latest?period_id=1MTH&limit=50"
        headers = {'X-CoinAPI-Key': api_key}

        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        coins = response.json()
        for coin_data in coins:
            coin_factory('bitcoin', coin_data)

        current_app.logger.info('Coins stored in database.')
        print(f'Coins stored in database: {len(coins)}')

        return coin_schema.dump(Coin.query.filter(Coin.date >= dt.date.today()), many=True)
