import numpy as np
import pandas as pd
from loguru import logger

"""
问题二：什么是Series？

Series是一维数组，但是带有索引！
多个Series组成Dataframe
"""
s1 = pd.Series(data=(10, 20, 30, 40, 50), index=['a', 'b', 'c', 'd', 'e'], name='age', dtype=object)
logger.debug('\n{}'.format(s1))

"""
问题三：Series如何索引？
"""
# 位置索引 [整数] 或者 iloc[整数]
logger.debug('\n{}'.format(s1[2]))
logger.debug('\n{}'.format(s1.iloc[2]))
# 标签索引   [标签名]  或者  loc[标签名]
logger.debug('\n{}'.format(s1['c']))
logger.debug('\n{}'.format(s1.loc['c']))

"""
问题四：Seires如何切片？
"""
# mylist = [('John', 22), ('Tom', 23), ('Lisa', 24), ('Jack', 25)]
# df1 = pd.DataFrame(mylist, columns=['姓名', '年龄'])
# print(df1)
