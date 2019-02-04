from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ModelMixin:
    @classmethod
    def all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get(cls, instance_id):
        return cls.query.get(instance_id)


class Coin(ModelMixin, db.Model):
    __tablename__ = 'coins'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    name = db.Column(db.String)
    high = db.Column(db.Numeric)
    low = db.Column(db.Numeric)
    open = db.Column(db.Numeric)
    close = db.Column(db.Numeric)
    volume = db.Column(db.BigInteger)
    market_cap = db.Column(db.BigInteger, nullable=True)

    def __repr(self):
        return f"<Coin {self.name} | {self.low} - {self.high}>"


class Exchange(ModelMixin, db.Model):
    __tablename__ = 'exchanges'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    website = db.Column(db.String)


def init_db(app):
    app.config['SQL_ALCHEMY_URI'] = 'postgresql://coinop'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from coinop import app
    # from flask import Flask
    # app = Flask(__name__)
    init_db(app)

    db.create_all()
    print("Connected to database.")
