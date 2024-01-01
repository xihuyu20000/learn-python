import collections
import functools
import itertools
import math

import pandas as pd

from core.const import Cfg, DistanceStyle
from core.log import logger


class MetricsStat:
    @staticmethod
    def yearly_count(df: pd.DataFrame, by: str) -> pd.DataFrame:
        """
        按年统计，也可能分组统计
        :param df:
        :param by: 分组一句
        """
        # 分组计数
        tmp = df.groupby(by)[by].count()
        new = tmp.to_frame(name="times")

        # 分组累计计数
        tmp = tmp.cumsum()
        new['acctimes'] = tmp.tolist()
        # by作为列
        new = new.reset_index()

        return new

    @staticmethod
    def freq_count(df: pd.DataFrame, by: str, first_n: int = 100):
        """
        频次统计：关键词、作者、机构、期刊、国家、学科
        :param df:
        :param by: 统计字段
        :param first_n:
        """
        tmp = df[by].str.split(Cfg.seperator.value).tolist()
        tmp = [word.strip() for arr in tmp for word in arr if len(word.strip()) > 0]
        tmp = collections.Counter(tmp)
        tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
        tmp = tmp[:first_n]
        tmp = pd.DataFrame(tmp, columns=[by, 'times'])
        return tmp

    @staticmethod
    def freq_grouped(df: pd.DataFrame, by:str, item:str, first_n: int = 100):
        """
        分组统计
        :param df:
        :param by: 分组字段：年份
        :param item: 统计字段：关键词
        :param first_n:
        """
        df1 = df.copy(True)

        mapping = collections.defaultdict(list)
        for i, row in df1.iterrows():
            for k in [k.strip() for k in row[by].split(Cfg.seperator.value) if k.strip()]:
                for v in [v.strip() for v in row[item].split(Cfg.seperator.value) if v.strip]:
                    mapping[k].append(v.strip())

        mapping = {k:collections.Counter(v) for k,v in mapping.items()}
        mapping = {k:sorted(v.items(), key=lambda x: x[1], reverse=True)[:first_n] for k, v in mapping.items()}

        arr = [(k, v) for k, v in mapping.items()]

        result = pd.DataFrame(arr, columns=[by, item])
        return result
    @staticmethod
    def matrix1(df:pd.DataFrame, item:str, first_freq:int = 100, first_cocon:int=100):
        # 对col_name列，拆分，然后计数
        words_count = collections.Counter(
            word.strip() for row in df.loc[:, item].tolist() for word in row.split(Cfg.seperator.value) if
            word.strip())
        logger.debug('词频统计 {}', words_count)
        # 保留高频词
        reserved_count_pairs = {word: times for word, times in words_count.items()}
        logger.debug('保留词数据集 {}', reserved_count_pairs)


        tmp = df[item].apply(
            lambda col: [word for word in col.split(Cfg.seperator.value) if word in reserved_count_pairs])
        assert isinstance(tmp, pd.Series)
        # 两两组合，如果只有1个作者，也会出现在里面
        logger.debug('两两组合')
        tmp = tmp.apply(lambda word_list: [sorted(w) for w in itertools.combinations_with_replacement(word_list, 2)])
        assert isinstance(tmp, pd.Series)
        # 共现词计数
        logger.debug('共现词计数')
        pair_counter = collections.Counter(Cfg.seperator.value.join(pair) for row in tmp for pair in row)
        assert isinstance(pair_counter, collections.Counter)
        # 保留高频共现词
        logger.debug('保留高频共现词')
        pair_counter = {pair: times for pair, times in pair_counter.items()}
        assert isinstance(pair_counter, dict)
        logger.debug('共现词统计 {}', pair_counter)

        # 形成共现数据集：拆分成 list嵌套list，作为DataFrame的values
        logger.debug('形成共现数据集')
        data_list = [[pair.split(Cfg.seperator.value)[0], pair.split(Cfg.seperator.value)[1], times] for pair, times in
                     pair_counter.items()]
        cocon_thin_matrix = pd.DataFrame(data=data_list, columns=['field1', 'field2', 'times'])
        logger.debug('共词数据集 {}', cocon_thin_matrix.shape)
        logger.debug('\r\n{}', cocon_thin_matrix)

        return cocon_thin_matrix


    @staticmethod
    def matrix2(df: pd.DataFrame, item1:str, item2:str, first_n: int = 100):
        """
        分组统计
        :param df:
        :param item1: 分组字段：年份
        :param item2: 统计字段：关键词
        :param first_n:
        """
        df1 = df.copy(True)

        mapping = collections.defaultdict(int)
        for i, row in df1.iterrows():
            for k in [k.strip() for k in row[item1].split(Cfg.seperator.value) if k.strip()]:
                for v in [v.strip() for v in row[item2].split(Cfg.seperator.value) if v.strip]:
                    co_k = Cfg.seperator.value.join([k,v])
                    mapping[co_k] += 1

        arr = [ [k.split(Cfg.seperator.value)[0], k.split(Cfg.seperator.value)[1], v] for k, v in mapping.items()]

        cocon_thin_matrix = pd.DataFrame(arr, columns=['field1', 'field2', 'times'])
        return cocon_thin_matrix

    @staticmethod
    def coupled_matrix(df:pd.DataFrame, item1:str, kw:str, first_n: int = 100):
        """
        耦合分析
        """
        df1 = df.copy(True)

        mapping = collections.defaultdict(list)
        for i, row in df1.iterrows():
            for k in [k.strip() for k in row[item1].split(Cfg.seperator.value) if k.strip()]:
                for v in [v.strip() for v in row[kw].split(Cfg.seperator.value) if v.strip]:
                    mapping[k].append(v)
        items = list(mapping.items())

        result = []
        for i, pair1 in enumerate(items):
            for pair2 in items[i:]:
                a1 = pair1[0]
                a2 = pair2[0]
                v = len(set(pair1[1])&set(pair2[1]))
                if v:
                    result.append([a1, a2, v])

        return pd.DataFrame(result, columns=['field1', 'field2', 'times'])


    @staticmethod
    def distance(df: pd.DataFrame, style:DistanceStyle):
        """
        距离
        """
        A = df['field1'].tolist()
        B = df['field2'].tolist()
        # dist = math.sqrt(sum([(a - b) ** 2 for (a, b) in zip(A, B)]))
        # print(dist)