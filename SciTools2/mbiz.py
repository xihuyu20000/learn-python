"""
核心业务逻辑，使用pandas实现，后期可以优化
必须有完整的测试和详细的说明
"""
import collections
import os
from typing import List, Set

import numpy as np
import pandas as pd

from log import logger
from mhelper import Cfg, Utils, PandasUtil


class Parser:
    """
    导出txt时，文件末尾多2个空行
    """
    CORE_ITEMS = ('RT'  # 文献类型
                  , 'A1'  # 作者
                  , 'AD'  # 工作单位
                  , 'T1'  # 题名
                  , 'JF'  # 来源
                  , 'YR'  # 出版年
                  , 'FD'  # 出版日期
                  , 'K1'  # 关键词
                  , 'AB'  # 摘要
                  )

    @staticmethod
    def parse_cnki(filenames) -> pd.DataFrame:
        """
        解析cnki的refworks格式的数据
        """
        ds = []
        if isinstance(filenames, str):
            filenames = [filenames]

        for filename in filenames:
            with open(filename, encoding='utf-8') as f:

                values = {'RT': '', 'A1': '', 'AD': '', 'T1': '', 'JF': '', 'YR': '', 'FD': '', 'K1': '', 'AB': ''}
                for linone, line in enumerate(f.readlines()):
                    # 前2个字母是具体的key
                    name = line[:2].strip()
                    if name in Parser.CORE_ITEMS:
                        values[name] = line[2:].strip()

                    # 空行，表示上一条结束，新的一条开始
                    if len(line.strip()) == 0:
                        if values and len(values['RT']) > 0:
                            ds.append(values)
                        # 每次初始化数据

                        values = {'RT': '', 'A1': '', 'AD': '', 'T1': '', 'JF': '', 'YR': '', 'FD': '', 'K1': '',
                                  'AB': ''}

        df = pd.DataFrame(ds, dtype='object')
        # 使用 fillna 将 NaN 替换为空字符串
        df.fillna('', inplace=True)
        df = df.astype(str)
        return df

    @staticmethod
    def parse_wos(filenames) -> pd.DataFrame:
        """
        解析wos的数据
        ER记录结束
        """
        ds = []
        if isinstance(filenames, str):
            filenames = [filenames]
        # 字段说明参考https://www.jianshu.com/p/964f3e44e431

        for filename in filenames:
            with open(filename, encoding='utf-8') as f:
                flags = ['PT', 'AU', 'AF', 'BA', 'BF', 'CA', 'GP', 'BE', 'TI', 'SO', 'SE', 'BS', 'LA', 'DT', 'CT', 'CY',
                         'CL', 'SP', 'AB', 'C1', 'C3', 'RP', 'EM', 'RI', 'OI', 'CR', 'NR', 'TC', 'Z9', 'U1', 'U2', 'PU',
                         'PI', 'PA', 'BN', 'PY', 'BP', 'EP', 'DI', 'PG', 'WC', 'WE', 'SC', 'GA', 'UT', 'OA', 'DA', 'DE',
                         'SN', 'J9', 'JI', 'VL', 'AR', 'ID', 'EI', 'PD', 'IS', 'FU', 'FX', 'PM', 'SU', 'SI', 'EA', 'HO',
                         'D2', 'PN', 'ER', 'EF']
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
    def parse_csv(filenames, seperator) -> pd.DataFrame:
        df_list = []
        for fname in [os.path.join(Cfg.datafiles, fname) for fname in filenames]:
            df = PandasUtil.read_csv(fname, sep=seperator)
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
        df.fillna('', inplace=True)
        df = df.astype(str)
        return df

    @staticmethod
    def parse_excel(filenames) -> pd.DataFrame:
        df_list = []
        for fname in [os.path.join(Cfg.datafiles, fname) for fname in filenames]:
            df = PandasUtil.read_excel(fname)
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
        df.fillna('', inplace=True)
        df = df.astype(str)
        return df

    @staticmethod
    def parse_pickle(filenames) -> pd.DataFrame:
        df_list = []
        for fname in filenames:
            df = PandasUtil.read_pickle(os.path.join(Cfg.datafiles, fname))
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
        df.fillna('', inplace=True)
        df = df.astype(str)
        return df

    @staticmethod
    def parse_parquet(filenames) -> pd.DataFrame:
        df_list = []
        for fname in filenames:
            df = PandasUtil.read_parquet(os.path.join(Cfg.datafiles, fname))
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
        df.fillna('', inplace=True)
        df = df.astype(str)
        return df


class CleanBiz:
    @staticmethod
    def metadata(df: pd.DataFrame):
        # 判断nulls必须放在这里，不能放到下面
        stat_df = df.copy()
        nulls = (stat_df.isna().sum() + stat_df.eq('').sum())
        stat_df = stat_df.describe(include=[object])
        # 丢掉行
        stat_df.drop('top', axis=0, inplace=True)
        # 空值情况
        stat_df.loc['nulls'] = nulls
        # 重命名索引
        stat_df.rename(index={'count': '总数', 'unique': '唯一', 'freq': '众频', 'nulls': '空值'}, inplace=True)

        ##########################################################################

        result = {}
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
            item_df = pd.DataFrame(datalist, columns=['词语', '频次'])

            # 频次统计
            datalist = [item[1] for item in datalist]
            datalist = collections.Counter(datalist)
            datalist = sorted(datalist.items(), key=lambda x: x[1], reverse=True)
            freq_df = pd.DataFrame(datalist, columns=['词语频次', '次数'])

            result[col_name] = [item_df, freq_df]

        return stat_df, result

    @staticmethod
    def copy_column(df, names):
        new_names = []
        for col in names:
            new_names.append(col + '-new')
            df[col + '-new'] = df[col]

        old_names = df.columns.tolist()
        new_names = Utils.resort_columns(old_names, new_names)
        df = df[new_names]
        return df

    @staticmethod
    def split_column(df: pd.DataFrame, name: str, split_style: str, style_le1: str, get_style: str, style_le2: int):

        if '分隔符' in split_style:
            df['xxxyyyzzz'] = df[name].apply(lambda x: str(x).split(style_le1))
        if '字符' in split_style:
            df['xxxyyyzzz'] = df[name].apply(lambda x: Utils.split_string_by_length(x, style_le1))

        new_names = []
        if '前' in get_style:
            for i in range(style_le2):
                new_name = f'{name}-{i + 1}'
                new_names.append(new_name)
                df[new_name] = df['xxxyyyzzz'].map(lambda x: Utils.get_from_limit(i, x, style_le2))
        if '第' in get_style:
            new_name = f'{name}-1'
            new_names.append(new_name)
            df[new_name] = df['xxxyyyzzz'].map(lambda x: Utils.get_from_limit(style_le2, x, style_le2))

        df.drop('xxxyyyzzz', axis=1, inplace=True)
        old_names = df.columns.tolist()
        # 下面的new_names一定要倒序
        old_names = Utils.resort_columns(old_names, sorted(new_names, reverse=True))
        df = df[old_names]

        return df

    @staticmethod
    def repalce_values(df, names, current_tab_index, old_sep, new_sep, other_char, is_reserved, is_new):
        new_names = []
        for col in names:
            new_col = col + '-new' if is_new else col
            if is_new:
                new_names.append(new_col)

            if current_tab_index == 0:
                df[new_col] = df[col].astype(str).str.replace(old_sep, new_sep).fillna(df[col])
            if current_tab_index == 1:
                if is_reserved:
                    # 只保留该字符
                    df[new_col] = df[col].apply(lambda x: Utils.reserve_chars(other_char, x))
                else:
                    # 删除该字符
                    df[new_col] = df[col].astype(str).str.replace(other_char, '').fillna(df[col])

        # 下面的new_names一定要倒序
        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, sorted(new_names, reverse=True))
        df = df[old_names]

        return df

    @staticmethod
    def combine_synonym(df: pd.DataFrame, synonym_dict_path: str, names: List[str], is_new: bool) -> pd.DataFrame:
        """

        :param df:  数据集
        :param synonym_dict_path:   同义词典完整路径
        :param names: 需要替换的列名
        :param is_new: 是否生成新的列
        :return:
        """
        # key是被替换的词，value是新词【第1个】
        words_dict = {}
        with open(synonym_dict_path, encoding='utf-8') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines if not line.strip().startswith('#')]
            for line in lines:
                words = line.split(';')
                # 一行一个词，那么长度是1
                if len(words) > 1:
                    tgt = words[0]
                    for org in words[1:]:
                        words_dict[org] = tgt

        new_names = []
        # 遍历每一列，对每一列的每一个值，进行替换处理
        for col in names:
            col_new = col + '-new' if is_new else col
            if is_new:
                new_names.append(col_new)
            df[col_new] = df[col].apply(lambda x: Utils.replace(x, words_dict))

        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, new_names)
        df = df[old_names]

        return df

    @staticmethod
    def stop_words(df: pd.DataFrame, names: List[str], words_set: Set[str], is_new: bool):

        new_names = []
        # 遍历每一列，对每一列的每一个值，进行替换处理
        for col in names:
            col_new = col + '-new' if is_new else col
            if is_new:
                new_names.append(col_new)
            df[col_new] = df[col].apply(lambda x: Utils.replace2(x, words_set))

        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, new_names)
        df = df[old_names]

        return df

    @staticmethod
    def wordcount_stat(df: pd.DataFrame, col_name: str, threshold: int):
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
        counts.fillna('', inplace=True)
        # 为DataFrame的列命名
        counts.columns = [col_name, '次数']
        # 讲col_name改为索引
        counts.set_index([col_name], inplace=True)

        return counts

    @staticmethod
    def cocon_stat(df: pd.DataFrame, names: List[str], threshold: int):
        df2 = pd.DataFrame()

        if len(names) == 1:
            df2 = PandasUtil.cocon_matrix(df, names[0], threhold=threshold)
        if len(names) == 2:
            df2 = PandasUtil.heter_matrix(df, names[0], names[1], threshold=threshold)

        df2 = df2.astype(np.uint8, errors='raise')

        return df2

    @staticmethod
    def row_similarity(df: pd.DataFrame, column_names: List[str], limited: float):

        UUID = 'uuid'
        JOINED_WORDS = 'joined_words'

        GROUP_LABEL = '组号'
        SIMILARITY_LABEL = '相似度'

        assert limited<=1
        # 增加一列uuid
        df[UUID] = [str(i) for i in range(df.shape[0])]
        df_uuid = df.copy(True)
        # 需要进行相似度判断的words
        df[JOINED_WORDS] = df.apply(lambda row: Utils.join_values(row, column_names), axis=1)

        # 带有分组的df
        df_3 = pd.DataFrame(columns=[UUID, GROUP_LABEL, SIMILARITY_LABEL])
        # 新分组的uuid集合
        new_group_uuids = []

        # 组号
        group_index:int = 0
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
                    df_3.loc[len(df_3.index)] = [current_uuid, group_index, int(sim_val * 100)]
            # 循环结束后，做3件事
            # 1、循环完后，退出
            if df.shape[0] <= 1:
                break
            # 2、缩短df
            if new_group_uuids:
                condition = (df[UUID].isin(new_group_uuids))
                df.drop(df[condition].index, inplace=True)
                df_3.loc[len(df_3.index)] = [s1_row[UUID], group_index, int(100)]
            df.reset_index(drop=True, inplace=True)
            # 3、清空new_group_uuids
            new_group_uuids.clear()

        # 通过uuid join到一起
        df_new = pd.merge(df_uuid, df_3, how='left', on=UUID)
        # 删除uuid列
        df_new.drop(UUID, axis=1, inplace=True)

        # 把组号、相似度，从以前的列中删除，然后插入到最前面
        new_cols = df_new.columns.tolist()
        new_cols.remove(GROUP_LABEL)
        new_cols.remove(SIMILARITY_LABEL)
        new_cols = [GROUP_LABEL, SIMILARITY_LABEL] + new_cols
        df_new = df_new[new_cols]

        # 排序
        df_new.sort_values(by=[GROUP_LABEL], ascending=True, na_position='last', inplace=True)
        df_new._reset_index(drop=True, inplace=True)
        df_new.fillna('', inplace=True)
        return df_new
