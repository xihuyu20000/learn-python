"""
核心业务逻辑，使用pandas实现，后期可以优化
必须有完整的测试和详细的说明
"""
import collections
import os
from typing import List, Set, Dict, Tuple, Union

import jieba
import pandas as pd

from log import logger
from mutil import Cfg, Utils, PandasUtil, FileFormat

Field = collections.namedtuple("Field", ['cn_name', 'en_name'])

class FieldStyle:

    def __init__(self):
        self.fields = [
            Field('作者', 'author'),
            Field('出版年', 'pubyear'),
            Field('关键字', 'keywords'),
            Field('标题', 'title')
        ]

class NormStyle:
    ochiia = 'ochiia'

class HierachyClusterStyle:
    average = 'average'
    ward = 'ward'
class DistanceStyle:
    correlation='correlation'
    euclidean='euclidean'
    cosine='cosine'
class Parser:
    """
    专门用于解析文件
    """
    @staticmethod
    def parse(filestyle: str, filelist: Union[str, List[str]], csv_seperator: str = Cfg.csv_seperator):
        """
        统一对外的接口
        """
        if FileFormat.CNKI == filestyle:
            return Parser.parse_cnki(filelist)
        if FileFormat.CNKI_PATENT == filestyle:
            return Parser.parse_cnki_patent(filelist)
        if FileFormat.WEIPU == filestyle:
            return Parser.parse_weipu(filelist)
        if FileFormat.WANFANG == filestyle:
            return Parser.parse_wanfang(filelist)
        if FileFormat.WOS == filestyle:
            return Parser.parse_wos(filelist)
        if FileFormat.CSV == filestyle:
            return Parser.parse_csv(filelist)
        if FileFormat.EXCEL == filestyle:
            return Parser.parse_excel(filelist)
        if FileFormat.PICKLE == filestyle:
            return Parser.parse_pickle(filelist)

        raise ValueError('不识别的文件类型' + filestyle)
    @staticmethod
    def parse_cnki(filelist: Union[str, List[str]]) -> pd.DataFrame:
        """
        解析cnki的refworks格式的数据
        """
        flags = (
            "RT",  # 文献类型
            "SR",
            "A1",  # 作者
            "AD",  # 工作单位
            "T1",  # 题名
            "JF",  # 来源
            "OP",
            "SN",
            "DS",
            "LK",
            "DO",
            "IS",
            "PB",
            "LA",
            "CN",
            "PP",
            "YR",  # 出版年
            "FD",  # 出版日期
            "K1",  # 关键词
            "AB",  # 摘要
            "vo"
        )

        ds = []
        if isinstance(filelist, str):
            filelist = [filelist]

        record = collections.defaultdict(list)
        for fname in filelist:
            with open(fname, encoding="utf-8") as f:
                # 所有行，去掉有空格
                lines = [line.rstrip() for line in f.readlines() if line.rstrip()]

                flag = ""

                # 前2行不重要，去掉
                for index, line in enumerate(lines[2:]):
                    # 每行的前2个字符
                    start = line[:2]
                    # 判断是否属于保留符号
                    if start in flags:
                        flag = start
                        # 是否记录结束
                        if flag == "A1":
                            if record:
                                ds.append(record)
                            record = {}

                    # 新的字段开始
                    if flag in record.keys():
                        record[flag].append(line)
                    else:
                        record[flag] = [line[2:]]
        if record:
            ds.append(record)

        for record in ds:
            for flag, values in record.items():
                record[flag] = ''.join([v.strip() for v in values])

        df = pd.DataFrame(ds, dtype=str)
        # 使用 fillna 将 NaN 替换为空字符串
        df.fillna("", inplace=True)
        return df

    @staticmethod
    def parse_cnki_patent(filelist: Union[str, List[str]]) -> pd.DataFrame:
        """
        解析cnki的refworks格式的专利
        """
        flags = (
            "RT", "SR", "A1", "A2", "T1", "AD", "FD", "ID", "CL", "AB", "DB", "DS"
        )

        ds = []
        if isinstance(filelist, str):
            filelist = [filelist]

        # 必须放到外面
        record = {}
        for filename in filelist:
            with open(filename, encoding="utf-8") as f:
                # 所有行，去掉有空格
                lines = [line.rstrip() for line in f.readlines() if line.rstrip()]

                flag = ""

                # 前2行不重要，去掉
                for index, line in enumerate(lines[2:]):
                    # 每行的前2个字符
                    start = line[:2]
                    # 判断是否属于保留符号
                    if start in flags:
                        flag = start
                        # 是否记录结束
                        if flag == "RT":
                            if record:
                                ds.append(record)
                            record = {}

                        # 新的字段开始
                        record[flag] = line[2:]
                    else:
                        raise Exception(f"第{index}行，出现新的字段类型{start} 完整行{line}")
        if record:
            ds.append(record)
        df = pd.DataFrame(ds, dtype=str)
        # 使用 fillna 将 NaN 替换为空字符串
        df.fillna("", inplace=True)
        return df

    @staticmethod
    def parse_weipu(filelist: Union[str, List[str]]) -> pd.DataFrame:
        """
        解析weipu的refworks格式的数据
        """
        flags = (
            "RT",  # 文献类型
            "SR",
            "A1",  # 作者
            "AD",  # 工作单位
            "T1",  # 题名
            "JF",  # 来源
            "OP",
            "SN",
            "DS",
            "LK",
            "DO",
            "IS",
            "PB",
            "LA",
            "CN",
            "PP",
            "YR",  # 出版年
            "FD",  # 出版日期
            "K1",  # 关键词
            "AB",  # 摘要
            "VO",
            "CL",
            "NO"
        )

        ds = []
        if isinstance(filelist, str):
            filelist = [filelist]

        record = {}
        for filename in filelist:
            with open(filename, encoding="utf-8") as f:
                # 所有行，去掉有空格
                lines = [line.rstrip() for line in f.readlines() if line.rstrip()]

                flag = ""

                for index, line in enumerate(lines):
                    # 每行的前2个字符
                    start = line[:2]
                    # 判断是否属于保留符号
                    if start in flags:
                        flag = start
                        # 是否记录结束
                        if flag == "A1":
                            if record:
                                ds.append(record)
                            record = {}

                        record[flag] = line[2:]
                        # 单独处理NO字段
                        if flag == 'NO':
                            arr = line[2:].split(';')
                            record['作者个数'] = arr[0][6:]
                            record['第一作者'] = arr[1][6:]

                    # elif start.strip() == "":
                    #     # 还是属于上一个字段的内容
                    #     record[flag].append(line[3:])
                    else:
                        raise Exception(f"第{index}行，出现新的字段类型{start} 完整行{line}")

        if record:
            ds.append(record)

        df = pd.DataFrame(ds, dtype=str)
        # 使用 fillna 将 NaN 替换为空字符串
        df.fillna("", inplace=True)
        return df

    @staticmethod
    def parse_wanfang(filelist: Union[str, List[str]]) -> pd.DataFrame:
        """
        解析wanfang的refworks格式的数据
        """
        flags = (
            "RT",  # 文献类型
            "SR",
            "A1",  # 作者
            "AD",  # 工作单位
            "T1",  # 题名
            "JF",  # 来源
            "OP",
            "SN",
            "DS",
            "LK",
            "DO",
            "IS",
            "PB",
            "LA",
            "CN",
            "PP",
            "YR",  # 出版年
            "FD",  # 出版日期
            "K1",  # 关键词
            "AB",  # 摘要
            "VO",
            "CL",
            "NO",
            "T2",
            "基金项目"
        )

        ds = []
        if isinstance(filelist, str):
            filelist = [filelist]

        record = {}
        for filename in filelist:
            with open(filename, encoding="utf-8") as f:
                # 所有行，去掉有空格
                lines = [line.rstrip() for line in f.readlines() if line.rstrip()]

                flag = ""

                for index, line in enumerate(lines):
                    # 每行的前2个字符
                    start = line[:2]
                    start2 = line[:4]

                    # 判断是否属于保留符号
                    if start in flags:
                        flag = start
                        # 是否记录结束
                        if flag == "A1":
                            if record:
                                ds.append(record)
                            record = {}

                        # 新的字段开始
                        record[flag] = line[2:]

                    # elif start.strip() == "":
                    #     # 还是属于上一个字段的内容
                    #     record[flag].append(line[3:])
                    elif start2 in flags:
                        record[start2] = line[5:]
                    else:
                        raise Exception(f"第{index}行，出现新的字段类型{start} 完整行{line}")

        if record:
            ds.append(record)

        df = pd.DataFrame(ds, dtype=str)
        # 使用 fillna 将 NaN 替换为空字符串
        df.fillna("", inplace=True)
        return df

    @staticmethod
    def parse_wos(filelist: Union[str, List[str]]) -> pd.DataFrame:
        """
        解析wos的数据
        ER记录结束
        """
        ds = []
        if isinstance(filelist, str):
            filelist = [filelist]
        # 字段说明参考https://www.jianshu.com/p/964f3e44e431

        for filename in filelist:
            with open(filename, encoding='utf-8') as f:
                flags = ['PT', 'AU', 'AF', 'BA', 'BF', 'CA', 'GP', 'BE', 'TI', 'SO', 'SE', 'BS', 'LA', 'DT', 'CT', 'CY',
                         'CL', 'SP', 'AB', 'C1', 'C3', 'RP', 'EM', 'RI', 'OI', 'CR', 'NR', 'TC', 'Z9', 'U1', 'U2', 'PU',
                         'PI', 'PA', 'BN', 'PY', 'BP', 'EP', 'DI', 'PG', 'WC', 'WE', 'SC', 'GA', 'UT', 'OA', 'DA', 'DE',
                         'SN', 'J9', 'JI', 'VL', 'AR', 'ID', 'EI', 'PD', 'IS', 'FU', 'FX', 'PM', 'SU', 'SI', 'EA', 'HO',
                         'D2', 'PN', 'ER', 'EF', 'MA']
                lines = [line.rstrip() for line in f.readlines() if line.rstrip()]

                flag = ''
                record = {}
                for line in lines[2:]:
                    start = line[:2]
                    if start in flags:
                        flag = start
                        # 是否记录结束
                        if flag == 'ER':
                            if record:
                                ds.append(record)
                            record = {}
                            continue
                        # 文件结束
                        elif flag == 'EF':
                            if record:
                                ds.append(record)
                            break
                        # 新的字段开始
                        record[flag] = [line[2:]]
                    elif start.strip() == '':
                        # 还是属于上一个字段的内容
                        record[flag].append(line[3:])
                    else:
                        raise Exception('出现新的字段类型 ' + line)
        # 可能多条记录，需要使用分隔符
        many_times = ['AU', 'AF', 'SO', 'SP', 'C1', 'C3', 'EM', 'CR']
        for record in ds:
            for k, v in record.items():
                separator = Cfg.seperator if k in many_times else ' '
                record[k] = separator.join(record[k])

        df = pd.DataFrame(ds, dtype='object')
        # 使用 fillna 将 NaN 替换为空字符串
        df.fillna('', inplace=True)
        df = df.astype(str)
        return df

    @staticmethod
    def parse_csv(filelist: Union[str, List[str]], seperator: str = Cfg.csv_seperator) -> pd.DataFrame:
        ds = []
        if isinstance(filelist, str):
            filelist = [filelist]

        for fname in [os.path.join(Cfg.datafiles, fname) for fname in filelist]:
            df = PandasUtil.read_csv(fname, sep=seperator)
            ds.append(df)
        df = pd.concat(ds, axis=0, ignore_index=True, sort=True)
        df.fillna("", inplace=True)
        df = df.astype(str)
        return df

    @staticmethod
    def parse_excel(filelist: Union[str, List[str]]) -> pd.DataFrame:
        ds = []
        if isinstance(filelist, str):
            filelist = [filelist]

        for fname in [os.path.join(Cfg.datafiles, fname) for fname in filelist]:
            df = PandasUtil.read_excel(fname)
            ds.append(df)
        df = pd.concat(ds, axis=0, ignore_index=True, sort=True)
        df.fillna("", inplace=True)
        df = df.astype(str)
        return df

    @staticmethod
    def parse_pickle(filelist: Union[str, List[str]]) -> pd.DataFrame:
        ds = []
        if isinstance(filelist, str):
            filelist = [filelist]

        for fname in filelist:
            df = PandasUtil.read_pickle(os.path.join(Cfg.datafiles, fname))
            ds.append(df)
        df = pd.concat(ds, axis=0, ignore_index=True, sort=True)
        df.fillna("", inplace=True)
        df = df.astype(str)
        return df


class CleanBiz:
    @staticmethod
    def metadata(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        # 判断nulls必须放在这里，不能放到下面
        stat_df = df.copy()
        nulls = stat_df.isna().sum() + stat_df.eq("").sum()
        stat_df = stat_df.describe(include=[object])
        # 丢掉行
        stat_df.drop("top", axis=0, inplace=True)
        # 添加新列，空值情况
        stat_df.loc["nulls"] = nulls
        # 重命名索引
        stat_df.rename(
            index={"count": "总数", "unique": "唯一", "freq": "众频", "nulls": "空值"},
            inplace=True,
        )

        ##########################################################################

        freq_df = {}
        for col_name in df.columns.tolist():
            # 词频统计
            datalist = df.loc[:, col_name].tolist()

            wordslist = []
            for row in datalist:
                for word in str(row).split(Cfg.seperator):
                    wordslist.append(word)
            datalist = wordslist

            datalist = collections.Counter(datalist)
            datalist = sorted(datalist.items(), key=lambda x: x[1], reverse=True)
            item_df = pd.DataFrame(datalist, columns=["词语", "频次"])

            # 频次统计
            datalist = [item[1] for item in datalist]
            datalist = collections.Counter(datalist)
            datalist = sorted(datalist.items(), key=lambda x: x[1], reverse=True)
            freq_df = pd.DataFrame(datalist, columns=["词语频次", "次数"])

            freq_df[col_name] = (item_df, freq_df)

        return stat_df, freq_df

    @staticmethod
    def rename_columns(df: pd.DataFrame, new_names_pair: Dict[str, str]) -> pd.DataFrame:
        df.rename(columns=new_names_pair, inplace=True)
        return df

    @staticmethod
    def copy_column(df, names: List[str]):
        """
        复制列
        :param df:
        :param names:
        :return:
        """
        new_names = []
        for col in names:
            new_names.append(col + "-new")
            df[col + "-new"] = df[col]

        old_names = df.columns.tolist()
        new_names = Utils.resort_columns(old_names, new_names)
        df = df[new_names]
        return df

    @staticmethod
    def split_column(
            df: pd.DataFrame,
            name: str,
            split_style: str,
            style_le1: str,
            get_style: str,
            style_le2: int,
    ):
        """
        拆分列
        :param df:
        :param name:
        :param split_style:
        :param style_le1:
        :param get_style:
        :param style_le2:
        :return:
        """
        if "分隔符" in split_style:
            df["xxxyyyzzz"] = df[name].apply(lambda x: str(x).split(style_le1))
        if "字符" in split_style:
            df["xxxyyyzzz"] = df[name].apply(
                lambda x: Utils.split_string_by_length(x, style_le1)
            )

        new_names = []
        if "前" in get_style:
            for i in range(style_le2):
                new_name = f"{name}-{i + 1}"
                new_names.append(new_name)
                df[new_name] = df["xxxyyyzzz"].map(
                    lambda x: Utils.get_from_limit(i, x, style_le2)
                )
        if "第" in get_style:
            new_name = f"{name}-1"
            new_names.append(new_name)
            df[new_name] = df["xxxyyyzzz"].map(
                lambda x: Utils.get_from_limit(style_le2, x, style_le2)
            )

        df.drop("xxxyyyzzz", axis=1, inplace=True)
        old_names = df.columns.tolist()
        # 下面的new_names一定要倒序
        old_names = Utils.resort_columns(old_names, sorted(new_names, reverse=True))
        df = df[old_names]

        return df

    @staticmethod
    def repalce_values1(df: pd.DataFrame, names: Union[str, List[str]], old_sep: str, new_sep: str, is_new: bool):
        """
        替换值
        :param df:
        :param names: 列名
        :param old_sep: 方式1，原先字符
        :param new_sep: 方式1， 新字符
        :param is_new: 替换当前列，还是新列
        :return:
        """
        if isinstance(names, str):
            names = [names]

        new_names = []
        for col in names:
            new_col = col + "-new" if is_new else col
            if is_new:
                new_names.append(new_col)

            df[new_col] = (
                df[col].astype(str).str.replace(old_sep, new_sep).fillna(df[col])
            )

        # 下面的new_names一定要倒序
        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, sorted(new_names, reverse=True))
        df = df[old_names]

        return df

    @staticmethod
    def repalce_values2(
            df: pd.DataFrame, names: List[str], other_char: str,
            is_reserved: bool, is_new: bool
    ):
        """
        替换值
        :param df:
        :param names: 列名
        :param other_char: 方式2，字符
        :param is_reserved:方式2，是否保留
        :param is_new: 替换当前列，还是新列
        :return:
        """
        new_names = []
        for col in names:
            new_col = col + "-new" if is_new else col
            if is_new:
                new_names.append(new_col)

            if is_reserved:
                # 只保留该字符
                df[new_col] = df[col].apply(
                    lambda x: Utils.reserve_chars(other_char, x)
                )
            else:
                # 删除该字符
                df[new_col] = (
                    df[col].astype(str).str.replace(other_char, "").fillna(df[col])
                )

        # 下面的new_names一定要倒序
        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, sorted(new_names, reverse=True))
        df = df[old_names]

        return df

    @staticmethod
    def combine_synonym(
            df: pd.DataFrame, words_dict: Dict[str, str], names: Union[str, List[str]], is_new: bool
    ) -> pd.DataFrame:
        """
        合并词
        :param df:  数据集
        :param words_dict:   同义词典
        :param names: 需要替换的列名
        :param is_new: 是否生成新的列
        :return:
        """
        assert isinstance(words_dict, dict)

        new_names = []

        if isinstance(names, str):
            names = [names]

        # 遍历每一列，对每一列的每一个值，进行替换处理
        for col in names:
            col_new = col + "-new" if is_new else col
            if is_new:
                new_names.append(col_new)
            df[col_new] = df[col].apply(lambda x: Utils.replace(x, words_dict))

        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, new_names)
        df = df[old_names]

        return df

    @staticmethod
    def stop_words(
            df: pd.DataFrame, names: Union[List[str], str], words_set: Set[str], is_new: bool
    ):
        """
        停用词
        :param df:
        :param names:
        :param words_set:
        :param is_new:
        :return:
        """
        new_names = []

        if isinstance(names, str):
            names = [names]

        # 遍历每一列，对每一列的每一个值，进行替换处理
        for col in names:
            col_new = col + "-new" if is_new else col
            if is_new:
                new_names.append(col_new)
            df[col_new] = df[col].apply(lambda x: Utils.replace2(x, words_set))

        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, new_names)
        df = df[old_names]

        return df

    @staticmethod
    def _jieba_cut(stop_words, line):
        logger.debug(stop_words)
        return [w.strip() for w in jieba.cut(line, cut_all=False) if w.strip() and w not in stop_words]

    @staticmethod
    def split_words(df, names: List[str]):
        """
        切分词
        :param df:
        :param names:
        :return:
        """
        stop_words = []
        with open(Cfg.stopwords_abs_path, encoding="utf-8") as f:
            stop_words = [line.strip() for line in f.readlines() if line.strip()]

        jieba.load_userdict(Cfg.controlledwords_abs_path)
        jieba.initialize()

        new_names = []
        for col in names:
            new_names.append(col + "-切词")
            df[col + "-切词"] = df[col].astype(str).apply(lambda x: CleanBiz._jieba_cut(stop_words, x))

        old_names = df.columns.tolist()
        new_names = Utils.resort_columns(old_names, new_names)
        df = df[new_names]
        return df

    @staticmethod
    def wordcount_stat(df: pd.DataFrame, col_name: str, threshold: int):
        """
        词频统计
        :param df:
        :param col_name:
        :param threshold:
        :return:
        """
        # 使用str.split进行拆分，并使用explode展开多列，每个单词是一列
        df_split = df[col_name].str.split(Cfg.seperator, expand=True)
        # 然后使用stack把列转为行
        df_stacked = df_split.stack()
        # 使用value_counts进行统计
        counts = df_stacked.value_counts()
        # 阈值过滤
        counts = counts[counts >= threshold]

        # 使用reset_index()将Series转为DataFrame
        counts: pd.DataFrame = counts.reset_index()
        # 替换空值
        counts.fillna("", inplace=True)
        # 为DataFrame的列命名
        counts.columns = [col_name, "次数"]
        # 讲col_name改为索引
        # counts.set_index([col_name], inplace=True)

        return counts

    @staticmethod
    def cocon_stat(df: pd.DataFrame, names: List[str], threshold: int):
        """
        共现分析
        :param df:
        :param names:
        :param threshold:
        :return:
        """
        df2 = pd.DataFrame()

        if len(names) == 1:
            df2 = PandasUtil.cocon_matrix(df, names[0], threhold=threshold)
        if len(names) == 2:
            df2 = PandasUtil.heter_matrix(df, names[0], names[1], threshold=threshold)

        # df2 = df2.astype(np.uint8, errors="raise")

        return df2

    @staticmethod
    def row_similarity(df: pd.DataFrame, column_names: List[str], limited: float):
        """
        相似度
        :param df:
        :param column_names:
        :param limited:
        :return:
        """
        UUID = "uuid"
        JOINED_WORDS = "joined_words"

        GROUP_LABEL = "组号"
        SIMILARITY_LABEL = "相似度"

        assert limited <= 1
        # 增加一列uuid
        df[UUID] = [str(i) for i in range(df.shape[0])]
        df_uuid = df.copy(True)
        # 需要进行相似度判断的words
        df[JOINED_WORDS] = df.apply(
            lambda row: Utils.join_values(row, column_names), axis=1
        )

        # 带有分组的df
        df_3 = pd.DataFrame(columns=[UUID, GROUP_LABEL, SIMILARITY_LABEL])
        # 新分组的uuid集合
        new_group_uuids = []

        # 组号
        group_index: int = 0
        while True:
            s1_row = df.loc[0]
            s1 = s1_row[JOINED_WORDS]
            df.drop(index=[0], inplace=True)
            df.reset_index(drop=True, inplace=True)

            for j in range(df.shape[0]):
                s2 = df.loc[j, JOINED_WORDS]
                # 计算相似度
                sim_val = Utils.jaccard_similarity(s1, s2)

                if sim_val >= limited:
                    group_index += 1

                    current_uuid = df.loc[j, UUID]
                    # 一定插入到新分组的uuid集合
                    new_group_uuids.append(current_uuid)
                    # 插入新的行
                    df_3.loc[len(df_3.index)] = [
                        current_uuid,
                        group_index,
                        int(sim_val * 100),
                    ]
            # 循环结束后，做3件事
            # 1、循环完后，退出
            if df.shape[0] <= 1:
                break
            # 2、缩短df
            if new_group_uuids:
                condition = df[UUID].isin(new_group_uuids)
                df.drop(df[condition].index, inplace=True)
                df_3.loc[len(df_3.index)] = [s1_row[UUID], group_index, int(100)]
            df.reset_index(drop=True, inplace=True)
            # 3、清空new_group_uuids
            new_group_uuids.clear()

        # 通过uuid join到一起
        df_new = pd.merge(df_uuid, df_3, how="left", on=UUID)
        # 删除uuid列
        df_new.drop(UUID, axis=1, inplace=True)

        # 把组号、相似度，从以前的列中删除，然后插入到最前面
        new_cols = df_new.columns.tolist()
        new_cols.remove(GROUP_LABEL)
        new_cols.remove(SIMILARITY_LABEL)
        new_cols = [GROUP_LABEL, SIMILARITY_LABEL] + new_cols
        df_new = df_new[new_cols]

        # 排序
        df_new.sort_values(
            by=[GROUP_LABEL], ascending=True, na_position="last", inplace=True
        )
        df_new.reset_index(drop=True, inplace=True)
        df_new.fillna("", inplace=True)
        return df_new


class AnalyzeBiz:

    @staticmethod
    def count(df: pd.DataFrame, by: str) -> Dict[str, int]:
        """
        :param df:
        :param by: 一个分组字段
        """

        df2 = df[by].str.split(Cfg.seperator, expand=True).stack().reset_index(drop=True)
        df2 = df2.rename(by).to_frame()
        df2 = df2.groupby(by).size().reset_index(name='Count')
        count_result = df2.drop(df2[df2[by].str.len() == 0].index)
        return count_result

    @staticmethod
    def count_by(df: pd.DataFrame, stat_column: str, by: str) -> pd.DataFrame:
        """
        :param df:
        :param stat_column: 被统计的列
        :param by: 一个分组字段
        """
        assert isinstance(stat_column, str)
        assert isinstance(by, str)
        for i, row in df.iterrows():
            row[by]
        df = df.loc[:, [stat_column, by]]

        splited = df[stat_column].str.split(Cfg.seperator, expand=True)
        df2 = splited.stack().reset_index(level=1, drop=True)
        df2 = df2.rename(stat_column).to_frame()
        df2 = df2.join(df[by])
        df2 = df2.groupby([by, stat_column]).size().reset_index(name='Count')
        result = df2.drop(df2[df2[stat_column].str.len() == 0].index)

        return result


if __name__ == '__main__':
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)

    df = Parser.parse_pickle([r'D:\workspace\github\learn-python\SciTools\datafiles\146万记录.pkl'])
    result = AnalyzeBiz.count(df, by='A1')
    print(result)
    # print(AnalyzeBiz.count_by())
