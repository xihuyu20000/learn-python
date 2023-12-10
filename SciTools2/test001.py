import pandas as pd

from helper import PandasUtil

df = pd.read_excel(r'D:\workspace\github\learn-python\SciTools2\datafiles\1.xlsx')

df2 = PandasUtil.cocon_matrix(df, 'A1', threhold=0)
df3 = PandasUtil.trunc_matrix(df2)
