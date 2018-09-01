from app import app
from flask import render_template, redirect, url_for, session
from app.forms import SymbolForm, RecordForm
from tdata import local, feature
from tdata import chart as tchart
from arctic import Arctic

arctic = Arctic('pi3')
DAILY_LIB = arctic['daily']
instruments = arctic['basedata'].read('instruments').data
symbols = (instruments.symbol + ' ' + instruments.name)
frequencies = ['D', 'W', 'M', 1, 3, 5, 15, 30, 60, 120]

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SymbolForm()
    if form.validate_on_submit():
        return redirect(f'/chart/{form.symbol.data.split()[0]}')
    return render_template('index.html', form=form, symbols=symbols)


@app.route('/chart/<symbol>/<freq>', methods=['GET', 'POST'])
def chart(symbol='000001.SH', freq='D'):
    # render a standalone html file and open a new tab for it?
    # downside: can't input information in it
    form = SymbolForm()
    data = local.bar(symbol, freq=freq)
    data = feature.add_columns(data)
    chart = tchart.brush(data)
    context = dict(
        myechart=chart.render_embed(),
        host=REMOTE_HOST,
        script_list=chart.get_js_dependencies(),
    )
    if form.validate_on_submit():
        session['symbol'] = form.symbol.data.split()[0]
        session['freq'] = form.frequency.data
        return redirect(url_for('chart', symbol=session.get('symbol'), freq=session.get('freq')))
    return render_template(
        'chart.html',
        form=form,
        symbol=session.get('symbol'),
        freq=session.get('freq'),
        symbols=symbols,
        frequencies=frequencies,
        **context)


@app.route('/record', methods=['GET', 'POST'])
def record():
    form = RecordForm()
    if form.validate_on_submit():
        return render_template('record.html', form=form)
    return render_template('record.html', form=form)
