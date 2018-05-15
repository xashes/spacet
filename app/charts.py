from pyecharts import Kline, Bar, Line
from pyecharts import Grid, Overlap, Page
from app.zen import hist_sum


def grids(data):
    kline = Kline(data.symbol[0])
    kline.add(
        '',
        data.index,
        data.loc[:, ['open', 'close', 'low', 'high']].values,
        mark_line=['max', 'min'],
        mark_line_valuedim=['highest', 'lowest'],
        is_datazoom_show=True,
        datazoom_xaxis_index=[0, 1],
    )

    turnover = Bar()
    turnover.add(
        '',
        data.index,
        data['turnover'].values / pow(10, 9),
        mark_line=['max', 'min'],
        is_datazoom_show=True,
    )

    grid = Grid(page_title=data['symbol'][0], width='100%', height=900)
    grid.add(kline, grid_bottom='40%')
    grid.add(turnover, grid_top='65%')
    return grid


def brush(data):
    data = hist_sum(data)
    kline = Kline()
    kline.add(
        'Kline',
        data.index,
        data.loc[:, ['open', 'close', 'low', 'high']].values,
        mark_line=['max', 'min'],
        mark_line_valuedim=['highest', 'lowest'],
        is_datazoom_show=True,
        datazoom_xaxis_index=[0, 1, 2],
    )
    brush = Line()
    brush.add(
        'Brush',
        data.index,
        data.endpoint.values,
    )
    overlap = Overlap()
    overlap.add(kline)
    overlap.add(brush)

    turnover = Bar()
    turnover.add(
        '',
        data.index,
        data.brush_amount.values / pow(10, 6),
        mark_line=['max', 'min']
    )

    macd = Bar()
    macd.add(
        '',
        data.index,
        data.hist_sum.values,
        mark_line=['max', 'min'],
    )

    grid = Grid('', width='100%', height=900)
    grid.add(overlap, grid_bottom='40%')
    grid.add(turnover, grid_top='65%', grid_bottom='20%')
    grid.add(macd, grid_top='85%')

    return grid
