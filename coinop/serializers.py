from flask_marshmallow import Marshmallow
from marshmallow import fields

from coinop.models import Coin

ma = Marshmallow()


class CoinSerializer(ma.ModelSchema):
    date = fields.DateTime('%Y-%m-%d')
    high = fields.Float()
    low = fields.Float()
    open = fields.Float()
    close = fields.Float()

    class Meta:
        model = Coin


coin_schema = CoinSerializer()
