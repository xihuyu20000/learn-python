import pandas as pd

df = pd.read_excel(r'D:\工作空间\datafiles\1.xlsx', sheet_name=[0,1])
values = [i  for i in df.values()]
print(values)