import difflib

import pandas as pd

from core.util import PandasCache, PandasUtil

PandasCache.init_cache()
cache = PandasCache()
df1 = pd.DataFrame({"id": [1, 2], "name": ["a", "b"]})
cache.push('aa', df1)

df2 = pd.DataFrame({"id": [3, 4], "name": ["aa", "bb"]})
cache.push('bb', df2)

df1 = cache.get(1)
df2 = cache.get(2)


# print(htmlContent)
with open('diff.html','w') as f:
    f.write(PandasUtil.diff_pandas(df1, df2))
