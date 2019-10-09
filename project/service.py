import tushare as ts


hq_columns = ['code', 'name', 'price', 'high', 'low', 'pre_close', 'bid', 'ask', 'volume', 'amount', 'date', 'time']
hq_columns_name = ['股票代码', '股票代码', '市价', '最高价', '最低价', '上交易日收盘价', '买一报价', '卖一报价', '成交量',
                   '成交金额', '日期', '时间']


def get_real_price(codes, hq_column=hq_columns):
    """
    实时行情查询
    :param codes: 股票代码集合
    :param hq_column: 指定行情数据列
    :return:
    """
    real_hq = ts.get_realtime_quotes(codes)
    # print(real_hq.to_json(orient='records', force_ascii=False))
    real_hq = real_hq[hq_column]
    return real_hq
