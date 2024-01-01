import pandas as pd

from core import Parser
from core.const import DistanceStyle
from core.metrics.metrics_stat import MetricsStat
from core.util import PandasUtil

#设置value的显示长度为200，默认为50
pd.set_option('max_colwidth',20000)
#显示所有列，把行显示设置成最大
pd.set_option('display.max_columns', None)
#显示所有行，把列显示设置成最大
pd.set_option('display.max_rows', None)

# df = Parser.parse_weipu(r'D:\workspace\github\learn-python\SciTools\datafiles\refworks维普.txt')
df = Parser.parse_csv(r'C:\Users\Administrator\Desktop\1.csv', ',')
print(df.columns)
# tmp = MetricsStat.yearly_count(df, 'YR')
# tmp = MetricsStat.freq_count(df, 'A1')
# tmp = MetricsStat.freq_grouped(df, 'YR', 'A1', first_n=10)
tmp = MetricsStat.matrix1(df, 'AD')
# tmp = MetricsStat.matrix2(df, 'AD', 'A1')
tmp = MetricsStat.distance(tmp, DistanceStyle.euclidean)
print(tmp)
