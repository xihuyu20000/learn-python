import collections
import itertools

import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

from core import Parser, CleanBiz
from core.const import HierachyClusterStyle, DistanceStyle, NormStyle, FileFormat
from core.log import logger
from core.util import PandasUtil
from core.util.mutil import Cfg


class CowordsHierarchyCluster:
    """
    共词（关键词/主题词/受控词）层次聚类

    能够揭示学科/主题的结构和变化

    参考文献：专题文献高频主题词的共词聚类分析，崔雷，情报理论与实践，1996-07-30	期刊
    """

    def __init__(self, dataset: pd.DataFrame, col_name: str, freq_threshold: int = 0, cocon_threshold: int = 0,
                 norm_method: str = NormStyle.ochiia,
                 cluster_method: str = HierachyClusterStyle.ward, dist_method: str = DistanceStyle.euclidean):
        """
        :param dataset:
        :param col_name:
        :param freq_threshold: 词频阈值
        :param cocon_threshold: 共现阈值
        :param norm_method: 标准化方法
        :param cluster_method: 衡量类间距离的方法
        :param dist_method: 距离方法
        """
        self.dataset = dataset
        self.col_name = col_name
        self.freq_threshold = freq_threshold
        self.cocon_threshold = cocon_threshold
        self.norm_method = norm_method
        self.cluster_method = cluster_method
        self.dist_method = dist_method

        assert isinstance(self.dataset, pd.DataFrame)
        assert self.col_name is not None and len(self.col_name) > 0

        # >=频次的主题词，会被保留，用于下一步共词分析
        self.reserved_count_pairs = collections.defaultdict(int)
        # 共词数据集矩阵  Nx3
        self.cocon_thin_matrix = None
        # 共词矩阵   NxN
        self.cocon_matrix = None
        # 相异度矩阵
        self.dissimilarity_matrix = None
        # 层次聚类后的矩阵
        self.linkage_matrix = None

    def run(self):
        self.stat_words_freq()
        self.stat_cocon_freq()
        self.calc_dissimilarity_matrix()
        self.hierarchical_clustering()
        self.show_graph_hierarchy()

    def stat_words_freq(self):
        """
        统计主题词的词频，会得到一个 reserved_words集合
        """

        # 对col_name列，拆分，然后计数
        words_count = collections.Counter(
            word.strip() for row in self.dataset.loc[:, self.col_name].tolist() for word in row.split(Cfg.seperator) if
            word.strip())
        logger.debug('词频统计 {}', words_count)
        # 保留高频词
        self.reserved_count_pairs = {word: times for word, times in words_count.items() if times >= self.freq_threshold}
        logger.debug('保留词数据集 {}', self.reserved_count_pairs)

    def stat_cocon_freq(self):
        """
        :param cocon_threshold: 共现阈值
        """
        # 保留高频词
        logger.debug('保留高频词')
        tmp = self.dataset[self.col_name].apply(
            lambda col: [word for word in col.split(Cfg.seperator) if word in self.reserved_count_pairs])
        assert isinstance(tmp, pd.Series)
        # 两两组合，如果只有1个作者，也会出现在里面
        logger.debug('两两组合')
        tmp = tmp.apply(lambda word_list: [sorted(w) for w in itertools.combinations_with_replacement(word_list, 2)])
        assert isinstance(tmp, pd.Series)
        # 共现词计数
        logger.debug('共现词计数')
        pair_counter = collections.Counter(Cfg.seperator.join(pair) for row in tmp for pair in row)
        assert isinstance(pair_counter, collections.Counter)
        # 保留高频共现词
        logger.debug('保留高频共现词')
        pair_counter = {pair: times for pair, times in pair_counter.items() if times >= self.cocon_threshold}
        assert isinstance(pair_counter, dict)
        logger.debug('共现词统计 {}', pair_counter)

        # 形成共现数据集：拆分成 list嵌套list，作为DataFrame的values
        logger.debug('形成共现数据集')
        data_list = [[pair.split(Cfg.seperator)[0], pair.split(Cfg.seperator)[1], times] for pair, times in
                     pair_counter.items()]
        self.cocon_thin_matrix = pd.DataFrame(data=data_list, columns=['field1', 'field2', 'times'])
        logger.debug('共词数据集 {}', self.cocon_thin_matrix.shape)
        logger.debug('\r\n{}', self.cocon_thin_matrix)

        # 列转行，形成共现矩阵
        logger.debug('形成共现矩阵')
        self.cocon_matrix = self.cocon_thin_matrix.pivot_table(index='field1', columns='field2', values='times')
        # 填充空值
        self.cocon_matrix.fillna(0, inplace=True)
        # 类型转换
        self.cocon_matrix = self.cocon_matrix.astype(int)
        logger.debug('共词矩阵 {}', self.cocon_matrix.shape)
        logger.debug('\r\n{}', self.cocon_matrix)
        PandasUtil.write_excel(self.cocon_matrix, '1.xlsx', 'aaa', True)

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
    filestyle = FileFormat.PICKLE
    filepath = r'D:\workspace\github\learn-python\SciTools\datafiles\146万记录.pkl'

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

    cc = CowordsHierarchyCluster(df, col_name='K1', freq_threshold=10, cocon_threshold=0)
    cc.run()
