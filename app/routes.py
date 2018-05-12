from app import app
from flask import render_template
from app.forms import ChartForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/chart')
def chart():
    form = ChartForm()
    return render_template('chart.html', title='Chart', form=form)
