
def income_formula(x, y, z):
    """
    收益计算公式
    :param x:
    :param y:
    :param z:
    :return:
    """
    if 0 == int(z):
        return 0
    return int((float(x) - float(y)) * int(z))


def percent_formula(x, y):
    """
    收益率计算公式
    :param x: 市价
    :param y: 昨收价
    :return:
    """
    if y == 0:
        return 0
    return round((float(x) - float(y)) / float(y) * 100, 3)


def value_formula(x, y):
    """
    市值计算公式
    :param x: 市价
    :param y: 持仓股数
    :return:
    """
    if 0 == int(y):
        return 0
    return float(x) * int(y)

