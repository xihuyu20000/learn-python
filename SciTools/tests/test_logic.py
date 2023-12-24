from mbiz import Parser, AnalyzeBiz
import pandas as pd
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

def test_count():
    # 读取文件
    df = Parser.parse_pickle(r'D:\workspace\github\learn-python\SciTools\datafiles\153万记录.pkl')

    # 按年计数
    df = AnalyzeBiz.count(df, by='YR')

    print(df)

def test_count_by():
    # 读取文件
    df = Parser.parse_pickle(r'D:\workspace\github\learn-python\SciTools\datafiles\153万记录.pkl')

    # print('\r {}'.format(df.columns))



    # # 重命名列
    # df = CleanBiz.rename_columns(df, {'YR':'出版年', 'A1':'作者','AD':'机构', 'JF':'期刊', 'K1':'关键词', 'T1':'标题'})
    # assert '出版年' in df.columns and '机构' in df.columns and '期刊' in df.columns and '关键词' in df.columns
    # print('\r {}'.format(df.columns))
    #
    #
    # # 替换值
    # df = CleanBiz.repalce_values(df,
    #                         ['作者','关键词'],
    #                         0,
    #                         ',',
    #                         ';',
    #                         '',
    #                         True,
    #                         False)
    # assert any(df['作者'].tolist())
    # assert any(df['关键词'].tolist())

    # df = AnalyzeBiz.count_by(df, stat_column='A1', by='YR')
    #
    # print(df)

