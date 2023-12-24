import jieba
import pandas as pd
from jieba.analyse import extract_tags

from core import Parser, CleanBiz
from core.const import Config

if __name__ == '__main__':
    # df = Parser.parse_pickle([r'D:\workspace\github\learn-python\SciTools\datafiles\146万记录.pkl'])

    df = pd.DataFrame({
        'A1':['张三;李四;王五;赵六','张三;李四;王五', '张三;李四','张三'],
        'K1': ['词3;词4;词5;词6', '词4;词3;词5', '词4;词3;', '词3']
    })

    CleanBiz.extract_features(df, ['A1','K1'])

    s1 = '在网络上收集了到了2个资料，对比了它们对Pooling的翻译，其中来自机器之心翻译为汇聚，似乎更能体会在CNN中的物理含义，更好理解。'
    words = ' '.join([word for word, flag in jieba.posseg.cut(s1) if flag in ('Ng', 'n','nr','nt','ns','nz','v')])

    [word for word, weight in extract_tags(words, 5, withWeight=True)]
