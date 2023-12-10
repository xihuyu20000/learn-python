import os
import time
import traceback

import pandas as pd
from PySide2.QtCore import QThread, Signal
from blinker import signal
from pandas import DataFrame

from helper import Cfg, FileFormat, MySignal, PandasUtil


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
    def parse_cnki(filenames) -> DataFrame:
        """
        解析cnki的refworks格式的数据
        """
        ds = []
        if isinstance(filenames, str):
            filenames = [filenames]

        for filename in filenames:
            with open(filename, encoding='utf-8') as f:

                values = {'RT': '', 'A1': '', 'AD': '', 'T1': '', 'JF': '', 'YR': '',
                          'FD': '',
                          'K1': '',
                          'AB': ''}
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

                        values = {'RT': '', 'A1': '', 'AD': '', 'T1': '', 'JF': '', 'YR': '', 'FD': '',
                                  'K1': '',
                                  'AB': ''}

        df = pd.DataFrame(ds, dtype='object')
        # 使用 fillna 将 NaN 替换为空字符串
        df.fillna('', inplace=True)
        return df

    @staticmethod
    def parse_wos(filenames) -> DataFrame:
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
                         'CL'
                    , 'SP', 'AB', 'C1', 'C3', 'RP', 'EM', 'RI', 'OI', 'CR', 'NR', 'TC', 'Z9', 'U1', 'U2', 'PU', 'PI',
                         'PA'
                    , 'BN', 'PY', 'BP', 'EP', 'DI', 'PG', 'WC', 'WE', 'SC', 'GA', 'UT', 'OA', 'DA', 'DE', 'SN', 'J9',
                         'JI', 'VL', 'AR', 'ID', 'EI'
                    , 'PD', 'IS', 'FU', 'FX', 'PM', 'SU', 'SI', 'EA', 'HO', 'D2', 'PN'
                    , 'ER', 'EF']
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
    def parse_csv(filenames, seperator) -> DataFrame:
        df_list = []
        for fname in [os.path.join(Cfg.datafiles, fname) for fname in filenames]:
            df = pd.read_csv(fname, sep=seperator, encoding='UTF-8', dtype=str)
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
        return df

    @staticmethod
    def parse_excel(filenames, count) -> DataFrame:
        # excel解析的索引从0开始
        count = count - 1
        df_list = []
        for fname in [os.path.join(Cfg.datafiles, fname) for fname in filenames]:
            df = pd.read_excel(fname, sheet_name=count, engine='openpyxl', dtype=str)
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
        return df

    @staticmethod
    def parse_pickle(filenames) -> DataFrame:
        df_list = []
        for fname in filenames:
            df = pd.read_pickle(os.path.join(Cfg.datafiles, fname), compression='gzip')
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)

        return df


class ParseFileThread(QThread):
    def __init__(self, filenames, format, sep, count):
        super(ParseFileThread, self).__init__()
        self.filenames = filenames
        self.format = format
        self.sep = sep
        self.count = count

        # print('参数', self.filenames, self.format, self.sep, self.count)

    def run(self) -> None:
        try:
            t1 = time.time()

            if self.format == FileFormat.CNKI:
                df = Parser.parse_cnki(self.filenames)
            elif self.format == FileFormat.WOS:
                df = Parser.parse_wos(self.filenames)
            elif self.format == FileFormat.CSV:
                df = Parser.parse_csv(self.filenames, self.sep)
            elif self.format == FileFormat.EXCEL:
                df = Parser.parse_excel(self.filenames, self.count)
            elif self.format == FileFormat.PICKLE:
                df = Parser.parse_pickle(self.filenames)
            else:
                raise Exception("没有处理的数据类型" + self.format)
            t2 = time.time()
            msg = '解析{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], df.shape[1], round(t2 - t1, 2))
            MySignal.info.send(msg)
            MySignal.clean_dataset.send(df)
        except Exception as e:
            traceback.print_exc()
            msg = '解析出错:{0}'.format(str(e))
            MySignal.error.send(msg)



class DownloadThread(QThread):

    def __init__(self, df, fpath):
        super(DownloadThread, self).__init__()
        self.df = df
        self.fpath = fpath

    def run(self) -> None:
        try:
            t1 = time.time()
            if self.fpath.endswith('.csv'):
                self.df.to_csv(self.fpath, index=False)
            elif self.fpath.endswith('.xlsx') or self.fpath.endswith('.xls'):
                self.df.to_excel(self.fpath, index=True)
            elif self.fpath.endswith('pkl'):
                self.df.to_pickle(self.fpath, compression="gzip")
            else:
                raise Exception("没有处理的保存类型 " + self.fpath)
            t2 = time.time()
            msg = '保存{0}，耗时{1}秒'.format(self.fpath, round(t2 - t1, 2))
            MySignal.info.send(msg)

        except Exception as e:
            traceback.print_exc()
            msg = '解析出错:{0}'.format(str(e))
            MySignal.error.send(msg)

class CountStatThread(QThread):

    def __init__(self, fpath, names, df_list):
        super(CountStatThread, self).__init__()
        self.fpath = fpath
        self.names = names
        self.df_list = df_list

    def run(self) -> None:
        try:
            t1 = time.time()

            with pd.ExcelWriter(self.fpath) as writer:
                for i, name in enumerate(self.names):
                    self.df_list[i].to_excel(writer, sheet_name=self.names[i], index=False)

            t2 = time.time()
            msg = '保存词频统计文件 {0}，耗时{1}秒'.format(self.fpath, round(t2 - t1, 2))
            MySignal.info.send(msg)

        except Exception as e:
            traceback.print_exc()
            msg = '解析出错:{0}'.format(str(e))
            MySignal.error.send(msg)

class CoconStatThread(QThread):

    def __init__(self, fpath, df):
        super(CoconStatThread, self).__init__()
        self.fpath = fpath
        self.df = df

    def run(self) -> None:
        try:
            t1 = time.time()

            with pd.ExcelWriter(self.fpath) as writer:
                self.df.to_excel(writer, index=False)

            t2 = time.time()
            msg = '保存统计文件 {0}，耗时{1}秒'.format(self.fpath, round(t2 - t1, 2))
            MySignal.info.send(msg)

        except Exception as e:
            traceback.print_exc()
            msg = '解析出错:{0}'.format(str(e))
            MySignal.error.send(msg)

class CleanMetadataThread(QThread):
    clean_metadata = signal('clean_metadata')
    def __init__(self, df:DataFrame):
        super(CleanMetadataThread, self).__init__()
        self.df = df

    def run(self) -> None:
        # 判断nulls必须放在这里，不能放到下面
        nulls = (self.df.isna().sum() + self.df.eq('').sum())
        df = self.df.describe(include=[object])
        # 丢掉行
        df.drop('top', axis=0, inplace=True)
        # 空值情况
        df.loc['nulls'] = nulls
        # 重命名索引
        df.rename(index={'count': '总数', 'unique': '唯一', 'freq': '众频', 'nulls': '空值'}, inplace=True)
        CleanMetadataThread.clean_metadata.send(df)
