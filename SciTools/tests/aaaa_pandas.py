import pandas as pd

from mbiz import AnalyzeBiz

if __name__ == '__main__':
    df = pd.DataFrame(data={'A1': ['作者1;作者2;作者3;', '作者1;作者2;', '作者1;', '作者2;'], 'BR': ['ADFASD', 'ADGDSG;', 'QADFA', 'HRTW'], 'YR': [2000, 2001, 2002, 2002]})

    result = AnalyzeBiz.count(df, by='A1')
    print(result)





