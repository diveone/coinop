import datetime as dt
from flask import Blueprint, current_app, jsonify, render_template

from coinop.serializers import coin_schema, Coin
from coinop.tasks import daily_coins, rq

coin_bp = Blueprint('coins', __name__, template_folder='templates/coins')


@coin_bp.route('/')
def home():
    return render_template('coins/index.html')


@coin_bp.route('/api/latest')
def latest_coins():
    current_app.logger.info("Fetching latest coin prices ...")
    q = rq.get_queue('high')
    job = q.enqueue(daily_coins)

    coins = coin_schema.dump(Coin.query.filter(Coin.date >= dt.date.today()), many=True)
    current_app.logger.info(f"--> Coin count: {len(coins[0])}")
    return jsonify(coins)


@coin_bp.route('/api/subscribe')
def subscribe_to_coin_updates():
    pass
