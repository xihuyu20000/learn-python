"""
对数据做各种处理和分析，输出数据的组合模型

todo 同义词、数据去重、空值补全
"""
from collections import Counter, defaultdict
from typing import List, Any

import pandas as pd

from core import Logger
from core.models import BiblioModel
from core.parse_data import cnki_refworks

"""
处理数据
"""
class FreqStat:
    def __init__(self, modelList: List[BiblioModel]):
        self.models = modelList
        self.dictList = [m.to_dict() for m in modelList]
        self.df = pd.DataFrame(self.dictList)

    def freq_yearly(self):
        """
        历年发文量
        :return:
        """
        dd = self.df.groupby('pubyear').size().to_dict()
        dd = { int(kv[0]):kv[1] for kv in dd.items()}
        keys = dd.keys()
        for i in range(min(keys), max(keys)+1):
            if i not in keys:
                dd[i] = 0
        dd = sorted(dd.items(), key=lambda x: x[0], reverse=False)
        return dd


    def freq_kws(self):
        """
        关键词的频次
        :return:
        """
        df2 = self.df['kws'].tolist()
        df2 = [item for sub in df2 for item in sub.split(',') if item.strip()]
        df2 = Counter(df2)
        print(df2)

    def freq_doctype(self):
        """
        文献类型的频次
        :return:
        """
        df2 = self.df['doctype'].tolist()
        df2 = Counter(df2)
        print(df2)

    def freq_source(self):
        """
        来源的频次
        :return:
        """
        df2 = self.df['source'].tolist()
        df2 = Counter(df2)
        print(df2)

    def freq_authors(self):
        """
        作者文献数量
        :return:
        """
        df2 = self.df['authors'].tolist()
        df2 = [item for sub in df2 for item in sub.split(',') if item.strip()]
        df2 = Counter(df2)
        return df2

    def freq_orgs(self):
        """
        机构文献数量
        :return:
        """
        df2 = self.df['orgs'].tolist()
        df2 = [item for sub in df2 for item in sub.split(',') if item.strip()]
        df2 = Counter(df2)
        print(df2)

class YearlyStat:
    def __init__(self, modelList):
        """
        逐年统计，比如关键词
        """
        self.modelList = modelList
        self.dictList = [m.to_dict() for m in self.modelList]
        self.df = pd.DataFrame(self.dictList)

    def yearly_kws(self):
        """
        统计每年的关键词词频
        """
        df2 = self.df[['pubyear','kws']].to_dict('records')

        result = defaultdict() # 统计每年的关键词词频
        for line in df2:
            Logger.trace(line)
            pubyear = line['pubyear']
            kws = line['kws'].split(',')
            if pubyear in result.keys():
                result[pubyear].extend(kws)
            else:
                result[pubyear] = kws

        result = { kv[0]:Counter(kv[1]) for kv in result.items() if len(kv[1])}

        for k,v in result.items():
            Logger.trace(k+' '+str(v.most_common()))

class CoStat:

    def __init__(self, modelList):
        """
        共现统计，比如共现词、共现作者、共现机构、共现期刊
        """
        self.modelList = modelList
        self.dictList = [m.to_dict() for m in self.modelList]
        self.df = pd.DataFrame(self.dictList)

    def _line2set(self, line):
        """
        拆分一行，形成共线词组
        """
        kws = line.split(',')
        ll = len(kws)

        result = []
        for i in range(ll):
            for j in range(i + 1, ll):
                key = kws[i] + ',' + kws[j] if kws[i] > kws[j] else kws[j] + ',' + kws[i]
                result.append(key)
        return result

    def _co_word2str(self, df2: List[str], min_co=0):
        weights: defaultdict[Any, int] = defaultdict(int)
        co_dict: defaultdict[Any, int] = defaultdict(int)
        for line in df2:
            # 统计各个关键词的权重
            for kw in line.split(','):
                if kw in weights:
                    weights[kw] += 1
                else:
                    weights[kw] = 1
            # 统计共词
            for key in self._line2set(line):
                if key in co_dict.keys():
                    co_dict[key] += 1
                else:
                    co_dict[key] = 1
        # 排序，按照共现次数，降序排列
        co_list = sorted(co_dict.items(), key=lambda x: x[1], reverse=True)
        # 过滤掉最小共现次数
        if min_co:
            co_list = [kv for kv in co_list if kv[1] > min_co]
        co_list = [(kv[0].split(',')[0], kv[0].split(',')[1], kv[1]) for kv in co_list]
        return co_list, weights

    def co_kws(self, min_co=0):
        """
        关键词共现矩阵
        @param min_co 最小共现次数。会过滤掉<=min_co的数据
        """
        df2 = self.df['kws'].tolist()
        return self._co_word2str(df2, min_co)

    def co_orgs(self, min_co=0):
        """
        机构共现矩阵
        @param min_co 最小共现次数。会过滤掉<=min_co的数据
        """
        df2 = self.df['orgs'].tolist()
        return self._co_word2str(df2, min_co)

    def co_authors(self, min_co=0):
        """
        作者共现矩阵
        @param min_co 最小共现次数。会过滤掉<=min_co的数据
        """
        df2 = self.df['authors'].tolist()
        return self._co_word2str(df2, min_co)

class Mode2Matrix:
    def __init__(self, modelList):
        """
        二模矩阵
        TODO 算法是否正确，需要验证
        TODO 词篇矩阵，就是TF-IDF？
        TODO 接近中心度、中间中心度
        """
        self.modelList = modelList
        self.dictList = [m.to_dict() for m in self.modelList]
        self.df = pd.DataFrame(self.dictList)

    def _parse(self, df2, k1, k2):
        result = defaultdict()
        for line in df2:
            v1s = line[k1].split(',')
            v2s = line[k2].split(',')
            for v1 in v1s:
                for v2 in v2s:
                    if (v1, v2) in result:
                        result[(v1, v2)] += 1
                    else:
                        result[(v1, v2)] = 1
        return Counter(result)
    def author_kws(self):
        """
        作者——关键词
        """
        df2 = self.df[['authors','kws']].to_dict('records')
        result = self._parse(df2, 'authors', 'kws')
        print(result)

    def org_kws(self):
        """
        机构——关键词
        """
        df2 = self.df[['orgs','kws']].to_dict('records')
        result = self._parse(df2, 'orgs', 'kws')
        print(result)


    def org_authors(self):
        """
        机构——作者
        """
        df2 = self.df[['orgs','authors']].to_dict('records')
        result = self._parse(df2, 'orgs', 'authors')
        print(result)

    def source_kws(self):
        """
        来源——关键词
        """
        df2 = self.df[['source', 'kws']].to_dict('records')
        result = self._parse(df2, 'source', 'kws')
        print(result)

if __name__ == '__main__':
    filename = '../files/CNKI-refworks3.txt'
    ds = cnki_refworks.parse_file(filename)

    # yearlyStat = YearlyStat(ds)
    # yearlyStat.yearly_kws()

    # freqStat = FreqStat(ds)
    # freqStat.count_yearly()
    
    # coStat = CoStat(ds)
    # coStat.co_kws()
    # coStat.co_orgs()
    # coStat.co_authors()

    mode2 = Mode2Matrix(ds)
    # mode2.author_kws()
    # mode2.org_kws()
    # mode2.source_kws()
    mode2.org_authors()

