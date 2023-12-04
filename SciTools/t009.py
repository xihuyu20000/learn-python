import pandas as pd

df = pd.read_excel('files/1.xlsx')

row_nos = [2,3]

# 求出组号
group_nos = df.loc[row_nos,'GROUP'].tolist()
uuids = df[df['GROUP'].isin(group_nos)].loc[:,'--UUID--']
print(uuids)

print(df.drop(uuids.index))