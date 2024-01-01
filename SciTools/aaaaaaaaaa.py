from core import Parser
from core.util import PandasUtil

df = Parser.parse_weipu(r'D:\workspace\github\learn-python\SciTools\datafiles\refworks维普.txt')
df['作者单位'] = df['作者单位'].apply(lambda x:x)
print(df['作者单位'])