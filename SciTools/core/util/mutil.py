"""
这是工具模块，这里的代码，一定不能依赖其他项目模块
"""
import collections
import itertools
import os
import re
import secrets
import sys
import time
import uuid
from typing import Dict, Union, Set
from typing import Tuple, List

import arrow
import jieba
import numpy as np
import pandas as pd
import requests
import wmi
from lxml import etree
from scipy.stats import zscore
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from zhon.hanzi import punctuation

from core.const import cfg
from core.log import logger


def is_running_as_exe():
    return getattr(sys, 'frozen', False)

class DictReader:
    @staticmethod
    def combine_words_file(abs_paths: Union[str, List[str]]) -> Dict[str, str]:
        """
        合并字典的返回值是dict，key是需要替换的词，value是保留的词
        abs_paths: 字典的绝对路径
        """
        if isinstance(abs_paths, str):
            abs_paths = [abs_paths]

        words_dict = collections.defaultdict(str)
        for abs_path in abs_paths:
            with open(abs_path, "r", encoding="utf-8") as f:
                # 去掉空行
                lines = [line.strip() for line in f.readlines() if line.strip()]
                # 去掉注释行
                lines = [line for line in lines if not line.startswith('#')]
                for line in lines:
                    words = line.split(';')
                    first = words[0]
                    for w in words[1:]:
                        words_dict[w] = first

        return words_dict


    @staticmethod
    def stop_words_file(abs_paths: Union[str, List[str]]) ->Set[str]:
        """
        停用词典
        """
        if isinstance(abs_paths, str):
            abs_paths = [abs_paths]

        words_set = set()
        for abs_path in abs_paths:
            with open(abs_path, "r", encoding="utf-8") as f:
                # 去掉空行
                lines = [line.strip() for line in f.readlines() if line.strip()]
                # 去掉注释行
                lines = [line for line in lines if not line.startswith('#')]
                for line in lines:
                    for w in line.split(';'):
                        words_set.add(w)
        return words_set

    @staticmethod
    def controlled_words_file(abs_paths: Union[str, List[str]]) ->Set[str]:
        """
        受控词典
        """
        if isinstance(abs_paths, str):
            abs_paths = [abs_paths]

        words_set = set()
        for abs_path in abs_paths:
            with open(abs_path, "r", encoding="utf-8") as f:
                # 去掉空行
                lines = [line.strip() for line in f.readlines() if line.strip()]
                # 去掉注释行
                lines = [line for line in lines if not line.startswith('#')]
                for line in lines:
                    for w in line.split(';'):
                        words_set.add(w)

        return words_set


class Utils:
    @staticmethod
    def resort_columns(old_names: List[str], new_names: List[str]):
        """
        新插入的列，位于原有列的后面。
        新的列名，是原列名后面加上了“-new”。其他格式不支持
        """
        for new1 in new_names:
            old_names.remove(new1)

        for new1 in new_names:
            i = old_names.index(new1[: new1.rfind("-")])
            old_names.insert(i + 1, new1)

        return old_names

    @staticmethod
    def calculate_jaccard_similarity(threshold, l1, sentences) -> Dict[int, float]:
        """
        threshold 在 [0.0, 1.0]
        """
        set1 = set(l1)
        result = {}
        for index, l2 in enumerate(sentences):
            set2 = set(l2)
            intersection = len(set1.intersection(set2))
            union = len(set1.union(set2))
            if union == 0:
                return 0
            if union:
                val = intersection / union
                if val >= threshold:
                    result[index] = val
        return result

    @staticmethod
    def jaccard_similarity(set1: Set[str], set2: Set[str]) -> float:
        """
        计算杰卡德相似度
        :param set1: set类型
        :param set2:
        :return: 在[0,1]之间的值
        """
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union

    @staticmethod
    def generate_random_color():
        """
        生成任意颜色
        """
        red = secrets.randbelow(256)
        green = secrets.randbelow(256)
        blue = secrets.randbelow(256)
        # return red, green, blue

        red = str(hex(red))[-2:].replace("x", "0").upper()
        green = str(hex(green))[-2:].replace("x", "0").upper()
        blue = str(hex(blue))[-2:].replace("x", "0").upper()
        return "#" + red + green + blue

    @staticmethod
    def replace(line, words_dict:Dict[str, str]):
        """
        假设line是'aa;bb;cc;dd'，words_dict是{'aa':1,'cc':2}，返回值是1;bb;2;dd
        :param line:
        :param words_dict:
        :return:
        """
        assert isinstance(line, str)
        assert isinstance(words_dict, dict)

        keys = words_dict.keys()
        words = [
            str(words_dict[w]) if w in keys else w for w in line.split(cfg.seperator.value)
        ]
        return cfg.seperator.value.join(words)

    @staticmethod
    def replace2(line, words_set: Union[List[str], Set[str]]):
        """
        如果 line是aa;bb;cc;dd, words_set是['aa','bb']，那么结果是cc;dd
        :param line:
        :param words_set:
        :return:
        """
        words = [w for w in line.split(cfg.seperator.value) if w not in words_set]
        return ";".join(words)

    @staticmethod
    def get_from_limit(i: int, arr: List[str], limit: int):
        if limit <= len(arr):
            return arr[i]
        else:
            if i < len(arr):
                return arr[i]
            else:
                return ""

    @staticmethod
    def split_string_by_length(string, length):
        """
        按照数量，拆分字符串
        """
        pattern = f".{{1,{length}}}"
        result = re.findall(pattern, string)
        return result

    @staticmethod
    def reserve_chars(other_char, line: str):
        rr = []
        for word in line.split(cfg.seperator.value):
            if other_char in word:
                rr.append(other_char)
            else:
                rr.append(word)
        return cfg.seperator.value.join(rr)

    @staticmethod
    def has_Chinese_or_punctuation(ws):
        return Utils.has_Chinese(ws) or Utils.has_punctuation(ws)

    @staticmethod
    def join_values(row, col_names: List[str]) -> Set[str]:
        """
        :param row:
        :param col_names:
        :return:
        """
        # 先合并
        joined = cfg.seperator.value.join([row[col] for col in col_names])
        # 再分割
        values = [item.strip() for item in re.split(r"\s+|;", joined) if item.strip()]
        return set(values)

    @staticmethod
    def has_Chinese(ws):
        return any(
            [True if "\u4e00" <= w <= "\u9fff" else False for w in jieba.lcut(ws)]
        )

    @staticmethod
    def has_punctuation(ws):
        # 中文符号
        return any([True if w in punctuation else False for w in jieba.lcut(ws)])

    array = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    @staticmethod
    def uuid8():
        id = str(uuid.uuid4()).replace("-", "")  # 注意这里需要用uuid4
        buffer = []
        for i in range(0, 8):
            start = i * 4
            end = i * 4 + 4
            val = int(id[start:end], 16)
            buffer.append(Utils.array[val % 62])
        return "".join(buffer)

    @staticmethod
    def get_html(url):
        headers = {
            'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '_tb_token_=berT80V49uJ9PFEJKGPI; cna=IhV+FpiDqRsCAXE54OSIgfFP; v=0; t=bb1c685b877ff64669f99c9dade7042c; cookie2=1e5103120f9886062722c86a5fad8c64; uc1=cookie14=UoTbm8P7LhIRQg%3D%3D; isg=BJWVw-e2ZCOuRUDfqsuI4YF0pJFFPHuu_ffxbBc6UYxbbrVg3-JZdKMoODL97mFc; l=dBMDiW9Rqv8wgDSFBOCiVZ9JHt_OSIRAguWfypeMi_5Zl681GgQOkUvZ8FJ6VjWftBTB4tm2-g29-etki6jgwbd6TCNQOxDc.',
            'referer': 'https://item-paimai.taobao.com/pmp_item/609160317276.htm?s=pmp_detail&spm=a213x.7340941.2001.61.1aec2cb6RKlKoy',
            'sec-fetch-mode': 'cors',
            "sec-fetch-site": 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        resp = requests.get(url, headers=headers)
        assert resp.status_code == 200
        return etree.HTML(resp.text)


class MachineCode:
    def __init__(self):
        """
        机器码，还有授权文件，还有验证
        """
        self.m_wmi = wmi.WMI()
        self.licence_path = os.path.join(os.path.expanduser("~"), ".licence.abc")

    def __cpu(self):
        cpu_info = self.m_wmi.Win32_Processor()
        if len(cpu_info) > 0:
            return cpu_info[0].ProcessorId
        return ""

    def __mac(self):
        for network in self.m_wmi.Win32_NetworkAdapterConfiguration():
            mac_address = network.MacAddress
            if mac_address != None:
                return mac_address
        return ""

    def __mainboard(self):
        board_info = self.m_wmi.Win32_BaseBoard()
        if len(board_info) > 0:
            return board_info[0].SerialNumber.strip().strip(".")
        return ""

    def get_code(self):
        """
        获得机器码
        """
        combine_str = self.__mac() + self.__cpu() + self.__mainboard()
        combine_byte = combine_str.encode("utf-8")
        return combine_byte.upper()

    def read_licence(self):
        """
        获取授权文件内容
        """

        if os.path.exists(self.licence_path):
            with open(self.licence_path, "r", encoding="utf-8") as f:
                return "".join(f.readlines())
        return ""

    def write_licence(self, text):
        """
        写入授权文件
        """
        with open(self.licence_path, "w", encoding="utf-8") as f:
            f.write(text)


class PandasUtil:
    @staticmethod
    def cocon_matrix(df, col_name, threhold, diagonal_values=False):
        """
        共现矩阵
        :param df:
        :param col_name:
        :param threhold:
        :return:
        """
        df2 = df[col_name].str.split(cfg.seperator.value)
        # 根据对角线是否有值，决定使用哪个函数
        sfunc = (
            itertools.combinations_with_replacement
            if diagonal_values
            else itertools.combinations
        )
        logger.debug("{} {}".format(1, arrow.now()))
        df2 = df2.apply(
            lambda x: [cfg.seperator.value.join(sorted(item)) for item in sfunc(x, 2)]
        )
        logger.debug("{} {}".format(2, arrow.now()))
        total_pairs = collections.defaultdict(int)
        logger.debug("{} {}".format(3, arrow.now()))
        for row in df2:
            for pair in row:
                total_pairs[pair] += 1
        logger.debug("{} {}".format(4, arrow.now()))
        total_pairs = {k: v for k, v in total_pairs.items() if v > threhold}
        logger.debug("{} {}".format(5, arrow.now()))
        total_words = set()
        for k, v in total_pairs.items():
            total_words.update(k.split(cfg.seperator.value))
        logger.debug("{} {}".format(6, arrow.now()))
        result = pd.DataFrame(
            index=list(total_words), columns=list(total_words), dtype=np.uint8
        )
        for k, v in total_pairs.items():
            ss = k.split(cfg.seperator.value)
            i, j = ss[0], ss[1]
            result.loc[i, j] = v
            result.loc[j, i] = v
        logger.debug("{} {}".format(7, arrow.now()))
        result.fillna(0, inplace=True)
        result.reset_index(inplace=False, drop=False)
        result = result.astype(np.uint8)
        return result

    @staticmethod
    def heter_matrix(df, col_name1, col_name2, threshold):
        df.fillna("", inplace=True)
        df1 = df[col_name1].str.split(cfg.seperator.value)
        df2 = df[col_name2].str.split(cfg.seperator.value)

        pair_dict = collections.defaultdict(int)
        for i in range(len(df1)):
            for arr in itertools.product(df1[i], df2[i]):
                pair_dict[cfg.seperator.value.join(arr)] += 1

        columns = set()
        index = set()
        for item, v in pair_dict.items():
            arr = str(item).split(cfg.seperator.value)
            index.add(arr[0])
            columns.add(arr[1])

        result = pd.DataFrame(columns=list(columns), index=list(index), dtype=np.uint8)

        for item, v in pair_dict.items():
            arr = str(item).split(cfg.seperator.value)
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
        cosine_sim_matrix = cosine_similarity(df)
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
        euclidean_dist_matrix = euclidean_distances(df.T)

        # 转换成 Pandas DataFrame
        euclidean_dist_df = pd.DataFrame(euclidean_dist_matrix, index=df.columns,
                                         columns=df.columns)
        return euclidean_dist_df

    @staticmethod
    def z_score_matrix(df):
        # 使用 Z-Score 进行标准化
        zscore_matrix = df.apply(zscore)
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

