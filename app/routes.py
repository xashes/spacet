from app import app
from flask import render_template, redirect, url_for
from app.forms import SymbolForm, RecordForm
from app.charts import brush, kline
from tdata import local
from arctic import Arctic

arctic = Arctic('pi3')
ZEN_LIB = arctic['zen']
DAILY_LIB = arctic['daily']
instruments = arctic['basedata'].read('instruments').data
symbols = (instruments.symbol + ' ' + instruments.name)

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SymbolForm()
    if form.validate_on_submit():
        return redirect(f'/chart/{form.symbol.data.split()[0]}')
    return render_template('index.html', form=form, symbols=symbols)


@app.route('/chart/<symbol>', methods=['GET', 'POST'])
def chart(symbol='000001.SH'):
    form = SymbolForm()
    data = ZEN_LIB.read(symbol).data
    data = data[data['open'] != 0]
    chart = brush(data)
    context = dict(
        myechart=chart.render_embed(),
        host=REMOTE_HOST,
        script_list=chart.get_js_dependencies(),
    )
    if form.validate_on_submit():
        return redirect(f'/chart/{form.symbol.data.split()[0]}')
    return render_template('chart.html', form=form, symbols=symbols, **context)


@app.route('/record', methods=['GET', 'POST'])
def record():
    form = RecordForm()
    if form.validate_on_submit():
        return render_template('record.html', form=form)
    return render_template('record.html', form=form)
