"""
对数据做各种处理和分析，输出数据的组合模型

todo 同义词、数据去重、空值补全
"""
from collections import Counter

import pandas as pd

"""
处理数据
"""


def count_yearly(df):
    """
    历年发文量
    todo 可能中间出现没有发文的年份
    :param df:
    :return:
    """
    print(df.groupby('pubyear').size())


def kw_freq(df):
    """
    关键词的频次
    :param df:
    :return:
    """
    df2 = df['kws'].tolist()
    df2 = [item for sub in df2 for item in sub.split(',') if item.strip()]
    df2 = Counter(df2)
    print(df2)


def doctype_freq(df):
    """
    文献类型的频次
    :param df:
    :return:
    """
    df2 = df['doctype'].tolist()
    df2 = Counter(df2)
    print(df2)


def source_freq(df):
    """
    来源的频次
    :param df:
    :return:
    """
    df2 = df['source'].tolist()
    df2 = Counter(df2)
    print(df2)


def author_freq(df):
    """
    作者文献数量
    :param df:
    :return:
    """
    df2 = df['authors'].tolist()
    df2 = [item for sub in df2 for item in sub.split(',') if item.strip()]
    df2 = Counter(df2)
    print(df2)


def org_freq(df):
    """
    机构文献数量
    :param df:
    :return:
    """
    df2 = df['orgs'].tolist()
    df2 = [item for sub in df2 for item in sub.split(',') if item.strip()]
    df2 = Counter(df2)
    print(df2)


if __name__ == '__main__':
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    pd.set_option('expand_frame_repr', False)
    from core.parse_data import cnki_refworks

    filename = '../files/CNKI-refworks3.txt'
    ds = cnki_refworks.parse_file(filename)
    ds = [m.to_dict() for m in ds]
    df = pd.DataFrame(ds)
    source_freq(df)
    author_freq(df)
    org_freq(df)
