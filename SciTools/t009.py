import pandas as pd

# 创建两个简单的DataFrame
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'key': ['K0', 'K1', 'K2', 'K3']})

df2 = pd.DataFrame({'A': ['C0', 'C1', 'C2', 'C3'],
                    'B': ['D0', 'D1', 'D2', 'D3'],
                    'key': ['K0', 'K1', 'K2', 'K3']})

# 沿着列（axis=1）连接两个DataFrame，根据'key'列进行连接
result = pd.concat([df1, df2], axis=0, ignore_index=True, sort=True)

pd.read_csv
#
# print("DataFrame 1:")
# print(df1)
#
# print("\nDataFrame 2:")
# print(df2)

print("\nResult after concat:")
print(result)
