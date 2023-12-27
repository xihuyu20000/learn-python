import collections
from typing import Dict

import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

from core import Parser, CleanBiz
from core.const import NormStyle, FileFormat
from core.log import logger
from core.util.mutil import Cfg


class AuthorWordsCouplingAnalysis:
    """
    作者-关键词耦合分析，比作者共被引分析，能更加及时的反应作者之间的合作关系

    分析潜在合作关系

    参考文献：基于作者关键词耦合的潜在合作关系挖掘，陈卫静 郑颖，情报杂志，2013-05-18	期刊
    """

    def __init__(self, dataset: pd.DataFrame, author_col_name: str, words_col_name: str, author_freq_threshold: int = 0,
                 words_freq_threshold: int = 0):
        self.dataset = dataset
        self.author_col_name = author_col_name
        self.words_col_name = words_col_name
        self.author_freq_threshold = author_freq_threshold
        self.words_freq_threshold = words_freq_threshold

        assert isinstance(self.dataset, pd.DataFrame)
        assert self.author_col_name is not None and len(self.author_col_name) > 0
        assert self.words_col_name is not None and len(self.words_col_name) > 0

    def run(self):
        self.stat_authors_freq()
        self.stat_words_freq()
        self.stat_each_author_each_word_freq()
        # self.hierarchical_clustering()
        # self.show_graph_hierarchy()

    def stat_authors_freq(self):
        """
        统计作者的发文频次，会得到一个 reserved_words集合
        """
        # 对col_name列，拆分，然后计数
        author_count = collections.Counter(
            author.strip() for row in self.dataset.loc[:, self.author_col_name].tolist() for author in
            row.split(Cfg.seperator) if
            author.strip())
        logger.debug('作者发文统计 {}', author_count)
        # 保留高产作者
        self.reserved_author_count_pairs: Dict[str, int] = {author: times for author, times in author_count.items() if
                                                            times >= self.author_freq_threshold}
        logger.debug('高产作者发文数据集 {}', self.reserved_author_count_pairs)

    def stat_words_freq(self):
        """
        统计主题词的词频，会得到一个 reserved_words集合
        """
        # 对col_name列，拆分，然后计数
        words_count = collections.Counter(
            word.strip() for row in self.dataset.loc[:, self.words_col_name].tolist() for word in
            row.split(Cfg.seperator) if
            word.strip())
        logger.debug('词频统计 {}', words_count)
        # 保留高频词
        self.reserved_words_count_pairs: Dict[str, int] = {word: times for word, times in words_count.items() if
                                                           times >= self.words_freq_threshold}
        logger.debug('保留词数据集 {}', self.reserved_words_count_pairs)

    def stat_each_author_each_word_freq(self):
        """
        统计每个作者每个主题词的频次
        """
        tmp = self.dataset.copy()
        logger.debug('\r\n{}', tmp)
        # 形成author:word组合
        tmp['pairs'] = tmp.apply(
            lambda df: [author + Cfg.seperator + word for author in df[self.author_col_name].split(Cfg.seperator) if
                        author in self.reserved_author_count_pairs for word in
                        df[self.words_col_name].split(Cfg.seperator) if word in self.reserved_words_count_pairs],
            axis=1)
        logger.debug('\r\n{}', tmp)
        # 转成np.Series
        tmp = tmp['pairs']
        logger.debug('\r\n{}', tmp)
        # 转成多列
        tmp = tmp.apply(pd.Series)
        logger.debug('\r\n{}', tmp)
        # 列转行
        tmp = tmp.stack()
        logger.debug('\r\n{}', tmp)
        author_word_freq = collections.Counter(tmp)
        logger.debug('\r\n{}', author_word_freq)
        # 转数组：拆分成 list嵌套list，作为DataFrame的values
        logger.debug('形成共现数据集')
        data_list = [[pair.split(Cfg.seperator)[0], pair.split(Cfg.seperator)[1], times] for pair, times in
                     author_word_freq.items()]
        self.author_word_thin_matrix = pd.DataFrame(data=data_list, columns=['author', 'word', 'times'])
        logger.debug('作者-主题词频次数据集 {}', self.author_word_thin_matrix.shape)
        logger.debug('\r\n{}', self.author_word_thin_matrix)
        self.author_word_freq_matrix = self.author_word_thin_matrix.pivot_table(index='author', columns='word',
                                                                                values='times')
        logger.debug('作者-主题词频次矩阵 {}', self.author_word_freq_matrix.shape)
        logger.debug('\r\n{}', self.author_word_freq_matrix)

        matrix = self.author_word_freq_matrix
        consin_matrix = pd.DataFrame(index=matrix.index, columns=matrix.columns)

        for i in range(len(consin_matrix.index.tolist())):
            for j in range(len(consin_matrix.columns.tolist())):
                cell = matrix.iloc[i, j]
                tf = cell / (matrix.iloc[i].sum(axis=0))
                idf = np.log10(cell / (matrix.iloc[:, j].sum() + 1))
                consin_matrix.iloc[i, j] = round(tf * idf, 4)

        logger.debug('作者-主题词权重矩阵 {}', consin_matrix.shape)
        logger.debug('\r\n{}', consin_matrix)

    def calc_dissimilarity_matrix(self):
        """
        相异度矩阵，是nxn矩阵
        :param norm_method: 归一化方法
        """

        # 计算相似度矩阵
        matrix = self.cocon_matrix
        similarity_matrix = pd.DataFrame(index=matrix.index, columns=matrix.columns)

        if self.norm_method == NormStyle.ochiia:
            for i in range(len(similarity_matrix.index.tolist())):
                for j in range(len(similarity_matrix.columns.tolist())):
                    v = np.sqrt(matrix.iloc[i, i] * matrix.iloc[j, j], dtype=np.float64)
                    similarity_matrix.iloc[i, j] = matrix.iloc[i, j] / v if v else 0
        else:
            raise ValueError('不识别的归一化方法' + self.norm_method)

        logger.debug('相似度矩阵 {}', similarity_matrix)
        logger.debug('\r\n{}', similarity_matrix)

        # 计算相异度矩阵
        self.dissimilarity_matrix = 1 - similarity_matrix

        logger.debug('相异度矩阵 {}', self.dissimilarity_matrix)
        logger.debug('\r\n{}', self.dissimilarity_matrix)

    def hierarchical_clustering(self):
        """
        """
        # 层次聚类
        self.linkage_matrix = linkage(self.dissimilarity_matrix, method=self.cluster_method, metric=self.dist_method)
        logger.debug('层次聚类矩阵 {}', self.linkage_matrix.shape)
        logger.debug('\r\n{}', self.linkage_matrix)

    def show_graph_hierarchy(self):
        """
        :param graph_style: 图表类型
        :param graph_args: 图表参数
        """
        # 绘制树状图
        matplotlib.rc("font", family='FangSong')
        dendrogram(self.linkage_matrix,
                   labels=self.dissimilarity_matrix.index,
                   orientation='right',
                   count_sort=True,
                   distance_sort=True,
                   show_leaf_counts=True)
        plt.title('')
        plt.xlabel('')
        plt.ylabel('')
        plt.show()


if __name__ == '__main__':
    # filestyle = FileFormat.PICKLE
    # filepath = r'D:\workspace\github\learn-python\SciTools\datafiles\146万记录.pkl'

    filestyle = FileFormat.CNKI
    filepath = r'D:\workspace\github\learn-python\SciTools\datafiles\2023年图清1.txt'

    df = Parser.parse(filestyle, filepath)
    df = CleanBiz.repalce_values1(df, 'K1', ',', ';', False)
    df = CleanBiz.combine_synonym(df, {'Citespace': 'CiteSpace'}, 'K1', False)
    logger.debug('\r\n{}', df)

    # df = pd.DataFrame({
    #     'A1':['张三;李四;王五;赵六','张三;李四;王五', '张三;李四','张三'],
    #     'K1': ['词3;词4;词5;词6', '词4;词3;词5', '词4;词3;', '词3']
    # })

    cc = AuthorWordsCouplingAnalysis(df, author_col_name='A1', words_col_name='K1', author_freq_threshold=0,
                                     words_freq_threshold=0)
    cc.run()
