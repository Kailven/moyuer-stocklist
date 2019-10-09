import pandas as pd
from .service import *
from .formula import *
from project import output_console


def profit_realtime():
    share_df = pd.read_csv('project/share_list.csv')
    share_df['code'] = share_df.code.apply(lambda code: str(code[1:]))
    df = get_real_price(share_df['code'])
    df = df.merge(share_df, on='code')
    # 上证和深证行情
    sh = get_real_price(['sh', 'sz'])
    sh['hold'], sh['cost_price'] = 0, 0
    df = pd.concat([sh, df], ignore_index=True)
    df['income'] = df.apply(lambda row: income_formula(row['price'], row['pre_close'], row['hold']), axis=1)
    df['percent'] = df.apply(lambda row: percent_formula(row['price'], row['pre_close']), axis=1)
    df['holding_value'] = df.apply(lambda row: value_formula(row['pre_close'], row['hold']), axis=1)
    df['profit'] = df.apply(lambda row: income_formula(row['price'], row['cost_price'], row['hold']), axis=1)
    df['profit_percent'] = df.apply(lambda row: percent_formula(row['price'], row['cost_price']), axis=1)
    # 今日收益
    income_total = df['income'].sum()
    # 总市值
    holding_value_total = df['holding_value'].sum()
    # 总浮盈
    profit_total = df['profit'].sum()
    print(" %d|%.2f   %s" % (income_total, income_total*100/holding_value_total, '↑↑↑' if income_total > 0 else ''))
    print(" %d   %s" % (profit_total, '↑↑↑' if profit_total > 0 else ''))
    output_console(df)
