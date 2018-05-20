from datetime import datetime
from app import db

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(9))
    date = db.Column(db.Date, default=datetime.today)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Numeric(5,2))

    def __repr__(self):
        return f'<Record {self.id}>'


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
