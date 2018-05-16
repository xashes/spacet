from datetime import datetime
from app import db

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(16))
    date = db.Column(db.Date, index=True, default=datetime.today)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Numeric(2))

    def __repr__(self):
        return f'<Record {self.id}>'