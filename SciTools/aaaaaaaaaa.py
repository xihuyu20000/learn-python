import pandas as pd

from core.util import PandasUtil

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

from core import Parser

raw_df = Parser.parse_cnki(r'C:\Users\Administrator\Desktop\论文\cnki-科学计量\CNKI-科学计量-合并.txt')
print(raw_df.shape)
print(raw_df.columns)
print(raw_df.head())

PandasUtil.write_excel(raw_df, 'aaa.xlsx', 'aa', False)