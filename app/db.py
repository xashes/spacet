from arctic import Arctic
from tdata import local

store = Arctic('localhost')

def init_libraries():
    store.initialize_library('basedata')
    store.initialize_library('daily')


def update_stock_table():
    lib = store['basedata']
    stocks = local.query_stock_table()
    stocks = stocks[stocks.symbol.str.contains(r'(SH|SZ)')]
    lib.write('stock', stocks)
