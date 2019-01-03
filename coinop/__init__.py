import os
from flask import Flask

from coinop import views
from coinop.models import db
from coinop.serializers import ma
from coinop.settings import common
from coinop.views import auth, coins


def create_app(db, config_name):
    _app = Flask(__name__)
    _app.config.from_object(config_name)
    db.app = _app
    db.init_app(_app)
    ma.init_app(_app)
    db.create_all()

    return _app


app = create_app(db, common)

# Configure routes
app.register_blueprint(auth.auth_bp)
app.register_blueprint(coins.coin_bp)
