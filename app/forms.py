from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField
from wtforms.validators import DataRequired
from datetime import datetime


class SymbolForm(FlaskForm):
    symbol = StringField('symbol', validators=[DataRequired()])
    frequency = StringField('frequency')
    submit = SubmitField('Submit')


class RecordForm(FlaskForm):
    symbol = StringField('Symbol', validators=[DataRequired()])
    date = DateField(
        'Date', default=datetime.today, validators=[DataRequired()])
    quantity = DecimalField('Quantity', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
