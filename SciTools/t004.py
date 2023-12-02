import numpy as np
import pandas as pd

from cleaner.clean import Utils

df=pd.DataFrame(np.arange(16).reshape(4,4),columns=["one","two","three","four"])

print(df)
print(df.loc[0, ['one','two']].tolist())