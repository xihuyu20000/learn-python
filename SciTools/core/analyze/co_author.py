import collections
import itertools

import matplotlib
import pandas as pd
from matplotlib import pyplot as plt

from core import Parser, CleanBiz
from core.const import FileFormat
from core.log import logger
from core.util.mutil import Config, PandasUtil
import networkx as nx

class CoworsHierarchyCluster:
    """
    作者共著聚类

    能够揭示研究团体的结构和变化

    参考文献：专题文献高频主题词的共词聚类分析，崔雷，情报理论与实践，1996-07-30	期刊
    """
    def __init__(self, dataset: pd.DataFrame, col_name: str, freq_threshold: int = 0, cocon_threshold: int = 0, norm_method: str = None,
                 cluster_method: str = None, dist_method: str = None):
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

        # >=频次的作者，会被保留，用于下一步合著
        self.reserved_count_pairs = collections.defaultdict(int)
        # 合著数据集矩阵  Nx3
        self.cocon_thin_matrix = None



    def run(self):
        self.stat_coauthor_freqco()
        self.stat_cocon_freq()
        self.show_graph_networkx()



    def stat_coauthor_freqco(self):
        """
        统计合著作者的词频，会得到一个 reserved_words集合
        """

        # 对col_name列，拆分，然后计数
        words_count = collections.Counter(
            word.strip() for row in self.dataset.loc[:, self.col_name].tolist() for word in row.split(Config.seperator) if
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
            lambda col: [word for word in col.split(Config.seperator) if word in self.reserved_count_pairs])
        assert isinstance(tmp, pd.Series)
        # 两两组合，如果只有1个作者，也会出现在里面
        logger.debug('两两组合')
        tmp = tmp.apply(lambda word_list: [sorted(w) for w in itertools.combinations_with_replacement(word_list, 2)])
        assert isinstance(tmp, pd.Series)
        # 共现词计数
        logger.debug('共现词计数')
        pair_counter = collections.Counter(Config.seperator.join(pair) for row in tmp for pair in row)
        assert isinstance(pair_counter, collections.Counter)
        # 保留高频共现词
        logger.debug('保留高频共现词')
        pair_counter = {pair: times for pair, times in pair_counter.items() if times >= self.cocon_threshold}
        assert isinstance(pair_counter, dict)
        logger.debug('共现词统计 {}', pair_counter)

        # 形成共现数据集：拆分成 list嵌套list，作为DataFrame的values
        logger.debug('形成共现数据集')
        self.data_list_list = [[pair.split(Config.seperator)[0], pair.split(Config.seperator)[1], times] for pair, times in
                               pair_counter.items()]
        self.cocon_thin_matrix = pd.DataFrame(data=self.data_list_list, columns=['field1', 'field2', 'times'])
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


    def show_graph_networkx(self):
        """

        """

        # 设置显示中文字体
        matplotlib.rcParams["font.sans-serif"] = ["SimHei"]


        G = nx.Graph()
        G.add_weighted_edges_from(self.data_list_list)
        nx.draw(G, with_labels=True)
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

    cc = CoworsHierarchyCluster(df, col_name='A1', freq_threshold=1, cocon_threshold=3)
    cc.run()
