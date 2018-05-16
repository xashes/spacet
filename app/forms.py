from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField, IntegerField
from wtforms.validators import DataRequired
from datetime import datetime


class SymbolForm(FlaskForm):
    symbol = StringField(validators=[DataRequired()])
    submit = SubmitField('Submit')


class RecordForm(FlaskForm):
    symbol = StringField('Symbol', validators=[DataRequired()])
    date = DateField(
        'Date', default=datetime.today, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
