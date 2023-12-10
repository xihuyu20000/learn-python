import collections
import functools
import itertools
import operator

import numpy as np
import pandas as pd
import pandas as pd
from itertools import combinations
from collections import Counter, UserList, defaultdict

from helper import Cfg


# 创建示例数据
df = pd.read_excel(r'D:\workspace\github\learn-python\SciTools2\datafiles\11.xlsx')

def cocon_matrix(df, col_name, threhold=0, diagonal_values=False):

    df2 = df[col_name].str.split(';')

    sfunc = itertools.combinations_with_replacement if diagonal_values else itertools.combinations
    #
    df2 = df2.apply(lambda x:[Cfg.seperator.join(sorted(item)) for item in sfunc(x, 2)])

    total_pairs = collections.defaultdict(int)

    for row in df2:
        for pair in row:
            total_pairs[pair] +=1


    total_pairs = {k:v for k,v in total_pairs.items() if v>threhold}

    total_words = set()
    for k,v in total_pairs.items():
        total_words.update(k.split(Cfg.seperator))

    result = pd.DataFrame(index=list(total_words), columns=list(total_words))

    for k,v in total_pairs.items():
        ss = k.split(Cfg.seperator)
        i, j = ss[0], ss[1]
        result.loc[i,j]=v
        result.loc[j,i] = v
    result.fillna(0, inplace=True)
    result.reset_index(inplace=False, drop=False)
    print(result.shape)
    print(result.columns)
    print(result.index)
    return result

def heter_matrix(df, col_name1, col_name2, threshold=0):
    df.fillna('', inplace=True)
    df1 = df[col_name1].str.split(Cfg.seperator)
    df2 = df[col_name2].str.split(Cfg.seperator)

    pair_dict = defaultdict(int)
    for i in range(len(df1)):
        for arr in itertools.product(df1[i], df2[i]):
            pair_dict[Cfg.seperator.join(arr)] += 1


    columns = set()
    index = set()
    for item, v in pair_dict.items():
        arr = str(item).split(Cfg.seperator)
        index.add(arr[0])
        columns.add(arr[1])

    result = pd.DataFrame(columns = list(columns), index = list(index), dtype=np.uint8)

    for item, v in pair_dict.items():
        arr = str(item).split(Cfg.seperator)
        result.loc[arr[0],arr[1]] = v
    result = result.fillna(0).astype(np.uint8)

    # 删除行
    condition = (result < threshold).all(axis=1)
    result = result[~condition]
    # 删除列
    columns_to_remove = result.columns[(result < threshold).all()]
    result = result.drop(columns=columns_to_remove)

    return result


heter_matrix(df, 'A1', 'JF', threshold=1)
# cocon_matrix(df, 'A1', threhold=0, diagonal_values=True)