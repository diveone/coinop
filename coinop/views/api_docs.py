from flask import Blueprint, current_app, url_for, render_template, make_response

from coinop.serializers import coin_schema, Coin

docs = Blueprint('docs', __name__, template_folder='api_docs')


@docs.route('/api/docs')
def docs_index():
    urls = {
        'coins': '/api/docs/coins',
    }
    return render_template('index.html', urls=urls)


@docs.route('/api/docs/coins')
def docs_coins():
    coins = coin_schema.dump(Coin.all(), many=True)
    return render_template('coins.html', coins=coins)
