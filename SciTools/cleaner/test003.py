import pandas as pd
import numpy as np

# 创建一个对称矩阵的示例 DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [2, 5, 6, 7],
        'C': [3, 6, 8, 9],
        'D': [4, 7, 9, 10]}
df = pd.DataFrame(data)
# columns_to_remove = df.columns[(df<5).all()]
# df = df.drop(columns=columns_to_remove)

# 使用 all(axis=1) 确保每一行的所有值都小于阈值
condition = (df < 5).all(axis=1)
df = df[~condition]

print(df)
# print(df[df>3].dropna(how='all', inplace=True))
# 删除小于阈值的行和列
# df = df.mask(mask).dropna(how='all').dropna(axis=1, how='all')
