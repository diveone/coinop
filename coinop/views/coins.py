from flask import Blueprint, current_app, jsonify, request
from coinop.models import Coin
from coinop.serializers import coin_schema

coin_bp = Blueprint('coins', __name__)


@coin_bp.route('/latest')
def latest_coins():
    current_app.logger.info("Fetching latest coin prices ...")
    coins = coin_schema.dump(Coin.all(), many=True)
    current_app.logger.info(f"--> Coin count: {len(coins[0])}")
    return jsonify(coins)
