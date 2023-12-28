import collections
import itertools
import time
from typing import Dict, List, Set, Tuple

import numpy as np
import pandas as pd
import pendulum
from scipy import stats
from sklearn import metrics

from core.const import Cfg
from core.log import logger
from core.util import Utils


class PandasUtil:
    @staticmethod
    def delete_rows_by_indexes(df: pd.DataFrame, indexes: List[int])->None:
        """
        删除行
        """
        df.drop(df.index[indexes], inplace=True)


    @staticmethod
    def delete_columns_by_indexes(df: pd.DataFrame, col_indexes: List[int])->None:
        """
        删除列
        """
        df.drop(df.columns[col_indexes], axis=1, inplace=True)


    @staticmethod
    def delete_columns_by_names(df: pd.DataFrame, col_names: List[str])->None:
        """
        删除列
        """
        df.drop(columns=col_names, inplace=True)

    @staticmethod
    def cocon_matrix(df, col_name, threhold, diagonal_values=False):
        """
        共现矩阵
        :param df:
        :param col_name:
        :param threhold:
        :return:
        """
        df2 = df[col_name].str.split(Cfg.seperator.value)
        # 根据对角线是否有值，决定使用哪个函数
        sfunc = (
            itertools.combinations_with_replacement
            if diagonal_values
            else itertools.combinations
        )
        logger.debug("{} {}".format(1, pendulum.now()))
        df2 = df2.apply(
            lambda x: [Cfg.seperator.value.join(sorted(item)) for item in sfunc(x, 2)]
        )
        logger.debug("{} {}".format(2, pendulum.now()))
        total_pairs = collections.defaultdict(int)
        logger.debug("{} {}".format(3, pendulum.now()))
        for row in df2:
            for pair in row:
                total_pairs[pair] += 1
        logger.debug("{} {}".format(4, pendulum.now()))
        total_pairs = {k: v for k, v in total_pairs.items() if v > threhold}
        logger.debug("{} {}".format(5, pendulum.now()))
        total_words = set()
        for k, v in total_pairs.items():
            total_words.update(k.split(Cfg.seperator.value))
        logger.debug("{} {}".format(6, pendulum.now()))
        result = pd.DataFrame(
            index=list(total_words), columns=list(total_words), dtype=np.uint8
        )
        for k, v in total_pairs.items():
            ss = k.split(Cfg.seperator.value)
            i, j = ss[0], ss[1]
            result.loc[i, j] = v
            result.loc[j, i] = v
        logger.debug("{} {}".format(7, pendulum.now()))
        result.fillna(0, inplace=True)
        result.reset_index(inplace=False, drop=False)
        result = result.astype(np.uint8)
        return result

    @staticmethod
    def heter_matrix(df, col_name1, col_name2, threshold):
        df.fillna("", inplace=True)
        df1 = df[col_name1].str.split(Cfg.seperator.value)
        df2 = df[col_name2].str.split(Cfg.seperator.value)

        pair_dict = collections.defaultdict(int)
        for i in range(len(df1)):
            for arr in itertools.product(df1[i], df2[i]):
                pair_dict[Cfg.seperator.value.join(arr)] += 1

        columns = set()
        index = set()
        for item, v in pair_dict.items():
            arr = str(item).split(Cfg.seperator.value)
            index.add(arr[0])
            columns.add(arr[1])

        result = pd.DataFrame(columns=list(columns), index=list(index), dtype=np.uint8)

        for item, v in pair_dict.items():
            arr = str(item).split(Cfg.seperator.value)
            result.loc[arr[0], arr[1]] = v
        result = result.fillna(0).astype(np.uint8)

        # 删除行
        condition = (result < threshold).all(axis=1)
        result = result[~condition]
        # 删除列
        columns_to_remove = result.columns[(result < threshold).all()]
        result = result.drop(columns=columns_to_remove)

        return result

    @staticmethod
    def dissimilarity_matrix(cooccurrence_matrix):
        """
        相异矩阵
        :param df:
        :return:
        """
        num_rows, num_cols = cooccurrence_matrix.shape

        # 计算每个词的出现次数
        word_counts = cooccurrence_matrix.sum(axis=1)

        # 计算相异矩阵
        dissimilarity_matrix = pd.DataFrame(index=cooccurrence_matrix.index, columns=cooccurrence_matrix.columns)

        for i in range(num_rows):
            for j in range(num_cols):
                a = cooccurrence_matrix.iloc[i, j]
                b = word_counts.iloc[i]
                c = word_counts.iloc[j]

                ochiai_similarity = a / ((b * c) ** 0.5)

                # 计算相异度
                dissimilarity_matrix.iloc[i, j] = 1 - ochiai_similarity

        dissimilarity_matrix.fillna(0, inplace=True)
        return dissimilarity_matrix

    @staticmethod
    def cosine_similarity_matrix(df):
        """
        余弦相似度
        :param df:
        :return:
        """
        # 计算余弦相似度矩阵
        cosine_sim_matrix = metrics.pairwise.cosine_similarity(df)
        logger.debug(cosine_sim_matrix)
        # 转换成 Pandas DataFrame
        cosine_sim_df = pd.DataFrame(cosine_sim_matrix, index=df.index,
                                     columns=df.index)
        # 请注意，余弦相似度的取值范围在 [-1, 1] 之间，而相异度为 [0, 2]，因此标准化的方式可以选择使用 1 - cosine_similarity。如果你希望得到一个相似度矩阵而不是相异矩阵，可以直接使用 cosine_similarity_df。
        logger.debug(cosine_sim_matrix)
        # 使用余弦相似度进行标准化
        # normalized_df = 1 - cosine_sim_df
        assert isinstance(cosine_sim_df, pd.DataFrame)
        return cosine_sim_df

    @staticmethod
    def correlation_matrix(df):
        """
        相关系数计算矩阵
        :param df:
        :return:
        """
        # 计算相关系数
        correlation_matrix = df.corr()
        correlation_matrix.fillna('', inplace=True)
        return correlation_matrix

    @staticmethod
    def euclidean_distances_matrix(df):
        """
        欧式距离
        :param df:
        :return:
        """
        # 计算欧式距离矩阵
        euclidean_dist_matrix = metrics.euclidean_distances(df.T)

        # 转换成 Pandas DataFrame
        euclidean_dist_df = pd.DataFrame(euclidean_dist_matrix, index=df.columns,
                                         columns=df.columns)
        return euclidean_dist_df

    @staticmethod
    def z_score_matrix(df):
        # 使用 Z-Score 进行标准化
        zscore_matrix = df.apply(stats.zscore)
        return zscore_matrix

    @staticmethod
    def calc_similarity(
            df: pd.DataFrame, words_list: List[Set[str]], limited: int
    ) -> List[Tuple[int, int, str]]:
        """

        :param df:
        :param words_list: list中的每每个元素是一个set，set中存放的单词，这个set表示该行的用于相似度判断的所有单词
        :return: list中嵌套一个tuple，里面的结构是[原df的index， 组号，相似度]
        """
        assert df.shape[0] == len(words_list)
        assert limited >= 0

        t1 = time.time()
        pairs_dict = []
        group_no = 0
        for source_i, source_words in enumerate(words_list):
            logger.info("第{}轮  {}".format(source_i, time.time()))
            # 第1个不取，形成三角矩阵，不包括对角线
            used_indexes = [p[0] for p in pairs_dict]
            # 注意下面的判断逻辑：
            # 1、index>i表示只处理后面的句子
            # 2、index not in used_indexes表示不在 前面相似选择出来的范围内
            # 符合以上一个条件，返回本身；否则，返回空串。这样的目的，是为了保持句子的原始顺序号不变化
            targets: List[Set[str]] = []
            # 以下的代码不能合并到一起，必须保持这样
            for index, words in enumerate(words_list):
                if index > source_i:
                    if index not in used_indexes:
                        targets.append(words)
                    else:
                        targets.append(set())
                else:
                    targets.append(set())
            # print('比较完成的index',used_indexes)
            # print('待比较的句子', sentences)

            # 缩小到[0,1]之间
            threshold = limited / 100
            assert threshold > 0 and threshold <= 1
            # 计算出相似度
            result: Dict[int, float] = Utils.calculate_jaccard_similarity(
                threshold, source_words, targets
            )
            # print(threshold, result, source_words, targets)
            # print('比较结果', result)
            if result:
                # 组号+1
                group_no += 1
                # 把当前的句子放进去，第3个表示当前句子，使用None表示不跟自己比较相似度
                pairs_dict.append([source_i, group_no, "100"])
                for target_index, simil in result.items():
                    pairs_dict.append(
                        (target_index, group_no, "{:.1f}".format(simil * 100))
                    )
        # logger.info(pairs_dict)
        t2 = time.time()
        logger.info("计算相似度，耗时{0}".format(round(t2 - t1, 2)))
        return pairs_dict

    @staticmethod
    def read_csv(fpath: str, sep: str) -> pd.DataFrame:
        return pd.read_csv(fpath, sep=sep, encoding="UTF-8", dtype=str)

    @staticmethod
    def write_csv(df: pd.DataFrame, fpath: str, index: bool) -> None:
        df.to_csv(fpath, index=index)

    @staticmethod
    def read_excel(fpath: str) -> pd.DataFrame:
        return pd.read_excel(fpath, sheet_name=0, engine="openpyxl", dtype=str)

    @staticmethod
    def write_excel(df: pd.DataFrame, fpath: str, name: str, save_index: bool):
        """

        :param df: 数据集
        :param fpath: 保存路径
        :param name: sheet名称
        :param save_index: 是否写入索引
        :return:
        """
        with pd.ExcelWriter(fpath) as writer:
            df.to_excel(writer, sheet_name=name, index=save_index)

    @staticmethod
    def write_excel_many_sheet(fpath: str, sheet_name_and_df: Dict[str, pd.DataFrame], index=False):
        """
        写入多个sheet
        :param fpath:
        :param sheet_name_and_df:
        :return:
        """
        with pd.ExcelWriter(fpath) as writer:
            for sheet_name, df in sheet_name_and_df.items():
                df.to_excel(writer, sheet_name=sheet_name, index=index)

    @staticmethod
    def read_pickle(fpath: str) -> pd.DataFrame:
        return pd.read_pickle(fpath, compression="gzip")

    @staticmethod
    def write_pickle(df: pd.DataFrame, fpath: str, compression):
        return df.to_pickle(fpath, compression=compression)

    @staticmethod
    def read_parquet(fpath: str):
        return pd.read_parquet(fpath)

    @staticmethod
    def write_parquet(df: pd.DataFrame, fpath: str):
        df.to_parquet(fpath)


if __name__ == '__main__':
    df = pd.DataFrame({'A1':[1,2,3], 'B1':[4,5,6]})
    print(df)
    PandasUtil.delete_columns_by_indexes(df, [0])
    print(df)