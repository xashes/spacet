from app import app
from flask import render_template, redirect, url_for
from app.forms import SymbolForm, RecordForm
from app.charts import brush
from tdata import local

REMOTE_HOST = "https://pyecharts.github.io/assets/js"

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
    data = local.daily(symbol)
    brush_chart = brush(data)
    context = dict(
        myechart=brush_chart.render_embed(),
        host=REMOTE_HOST,
        script_list=brush_chart.get_js_dependencies(),
    )
    if form.validate_on_submit():
        return redirect(f'/chart/{form.symbol.data}')
    return render_template('chart.html', form=form, **context)

@app.route('/record', methods=['GET', 'POST'])
def record():
    form = RecordForm()
    if form.validate_on_submit():
        return render_template('record.html', form=form)
    return render_template('record.html', form=form)
