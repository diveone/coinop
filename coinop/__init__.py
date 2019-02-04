from flask import Flask

from coinop import views
from coinop.models import db
from coinop.serializers import ma
from coinop.settings import common
from coinop.tasks import rq, daily_coins
from coinop.views import auth, coins


def create_app(db, config_name):
    _app = Flask(__name__)
    _app.config.from_object(config_name)
    db.app = _app
    rq.app = _app
    db.init_app(_app)
    ma.init_app(_app)
    rq.init_app(_app)
    _app.config.broker_url = 'redis://localhost:6379/0'
    db.create_all()

    return _app


app = create_app(db, common)

# Configure routes
app.register_blueprint(auth.auth_bp)
app.register_blueprint(coins.coin_bp)
