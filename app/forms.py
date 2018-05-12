from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ChartForm(FlaskForm):
    symbol = StringField(validators=[DataRequired()])
    submit = SubmitField('Submit')
