import signal
import argparse
import json
from project.service import get_real_price
from project.profit_realtime import profit_realtime


class InputTimeoutError(Exception):
    pass


def interrupted(a, b):
    raise InputTimeoutError


signal.signal(signal.SIGALRM, interrupted)
time_out_seconds = 30


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='基于tushare开发的摸鱼小应用，'
                                                 '目前支持查看交易日实时持仓盈亏功能和股票实时行情功能。')
    parser.add_argument('--version', '-v', action='version', version='moyuer version: v0.01',
                        help='show the version')
    # 个股实时行情
    parser.add_argument('--codes', '-c', dest='codes', nargs='+', help='input: stock codes separated by blank, '
                                                                       'output: realtime data')
    args = parser.parse_args()
    if args.codes:
        result = get_real_price(args.codes)
        result = result.to_json(orient='records', force_ascii=False)
        result = json.loads(result)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        profit_realtime()

    # 任意键终止程序
    signal.alarm(time_out_seconds)
    try:
        name = input('press any key to clear screen')
        if name:
            signal.alarm(0)
    except InputTimeoutError:
        pass
