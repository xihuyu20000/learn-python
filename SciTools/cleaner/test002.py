import pandas as pd
import numpy as np

value = {'用户ID':['001','002','003','004','005','006'],
         '用户类型':['大','小','中','大','小','中'],
         '区域':['A','B','A','C','B','A'],
         '7月销量':[50,60,75,100,120,130],
         '7月销售额':[500,1200,2250,1100,3600,5200]}
df = pd.DataFrame(value)
df2 = df[df['区域'].isin(['A','B'])]
print(df2)