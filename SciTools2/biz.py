"""
核心业务逻辑，使用pandas实现，后期可以优化
必须有完整的测试和详细的说明
"""
import collections
import os
from typing import List

import pandas as pd
from PySide2.QtCore import QThread

import log
from helper import Cfg, Utils
from log import logger


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
        return df

    @staticmethod
    def parse_csv(filenames, seperator) -> pd.DataFrame:
        df_list = []
        for fname in [os.path.join(Cfg.datafiles, fname) for fname in filenames]:
            df = pd.read_csv(fname, sep=seperator, encoding='UTF-8', dtype=str)
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
        df.fillna('', inplace=True)

        return df

    @staticmethod
    def parse_excel(filenames) -> pd.DataFrame:
        df_list = []
        for fname in [os.path.join(Cfg.datafiles, fname) for fname in filenames]:
            df = pd.read_excel(fname, sheet_name=0, engine='openpyxl', dtype=str)
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
        df.fillna('', inplace=True)

        return df

    @staticmethod
    def parse_pickle(filenames) -> pd.DataFrame:
        df_list = []
        for fname in filenames:
            df = pd.read_pickle(os.path.join(Cfg.datafiles, fname), compression='gzip')
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
        df.fillna('', inplace=True)

        return df

    @staticmethod
    def parse_parquet(filenames) -> pd.DataFrame:
        df_list = []
        for fname in filenames:
            df = pd.read_parquet(os.path.join(Cfg.datafiles, fname))
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
        df.fillna('', inplace=True)

        return df

class CleanBiz:
    @staticmethod
    def metadata(df:pd.DataFrame):
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
    def save_excel(df, fpath, name):
        """

        :param df: 数据集
        :param fpath: 保存路径
        :param name: sheet名称
        :return:
        """
        with pd.ExcelWriter(fpath) as writer:
                df.to_excel(writer, sheet_name=name, index=False)

    @staticmethod
    def combine_synonym(df:pd.DataFrame, synonym_dict_path:str, names:List[str], is_new:bool) -> pd.DataFrame:
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
            df[col_new] = df[col].apply(lambda x: CleanBiz.__replace(x, words_dict))

        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, new_names)
        df = df[old_names]

        return df

    @staticmethod
    def __replace(line, words_dict):
        keys = words_dict.keys()
        words = [str(words_dict[w]) if w in keys else w for w in line.split(Cfg.seperator)]
        return ';'.join(words)