import numpy as np
from texttable import Texttable

out_columns = ['name', 'profit', 'profit_percent', 'pre_close', 'price', 'income', 'percent']
out_columns_name = ['名称', '总浮盈', '总浮盈率', '上交易日收价', '市价', '今日收益', '今日收益率']


def output_console(data):
    data = data[out_columns]
    to_be_list = np.array(data)
    table = Texttable()
    table.set_deco(Texttable.BORDER)
    table.add_rows(to_be_list.tolist(), header=False)
    print(table.draw())
