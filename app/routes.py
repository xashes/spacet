from app import app
from flask import render_template, redirect, url_for
from app.forms import SymbolForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SymbolForm()
    if form.validate_on_submit():
        return redirect(f'/chart/{form.symbol.data}')
    return render_template('index.html', form=form)

@app.route('/chart/<symbol>', methods=['GET', 'POST'])
def chart(symbol):
    form = SymbolForm()
    if form.validate_on_submit():
        return redirect(f'/chart/{form.symbol.data}')
    return render_template('chart.html', form=form, symbol=symbol)
