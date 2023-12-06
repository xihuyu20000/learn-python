import os
import time

import pandas as pd
from PySide6.QtCore import QThread, Signal
from pandas import DataFrame

from helper import  Cfg, FileFormat


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
    def parse_wos(filenames):
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
                flags = ['PT','AU','AF','BA','BF','CA','GP','BE','TI','SO','SE','BS','LA','DT','CT','CY','CL'
                    ,'SP','AB','C1','C3','RP','EM','RI','OI','CR','NR','TC','Z9','U1','U2','PU','PI','PA'
                    ,'BN','PY','BP','EP','DI','PG','WC','WE','SC','GA','UT','OA','DA','DE','SN','J9','JI','VL','AR','ID','EI'
                    ,'PD','IS','FU','FX','PM','SU','SI','EA','HO','D2','PN'
                    ,'ER','EF']
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
                        elif flag =='EF':
                            if record:
                                ds.append(record)
                            break
                        # 新的字段开始
                        record[flag] = [line[2:]]
                    elif start.strip()=='':
                        # 还是属于上一个字段的内容
                        record[flag].append(line[3:])
                    else:
                        raise Exception('出现新的字段类型 '+line)
        # 可能多条记录，需要使用分隔符
        many_times = ['AU', 'AF', 'SO', 'SP', 'C1', 'C3', 'EM', 'CR']
        for record in ds:
            for k,v in record.items():
                separator = Cfg.seperator if k in many_times else ' '
                record[k] = separator.join(record[k])

        df = pd.DataFrame(ds, dtype='object')
        # 使用 fillna 将 NaN 替换为空字符串
        df.fillna('', inplace=True)
        return df


class Worker(QThread):
    # 实例化一个信号对象
    valve = Signal(int)
    q = True
    pause = False
    a = 0

    def __int__(self):
        super(Worker, self).__init__()

    def run(self):
        while self.q:  # self.q控制程序是否执行
            if self.pause:
                time.sleep(0.2)
                continue
            while not self.pause and self.a < 2000:  # self.pause控制程序是否暂停
                self.a += 1
                time.sleep(0.1)
                self.valve.emit(self.a)
            if self.a >= 2000:  # self.a>2000程序结束
                return


class ParseFileThread(QThread):
    signal_start = Signal()
    signal_stop = Signal(str, object)
    def __init__(self, filenames, format):
        super(ParseFileThread, self).__init__()
        self.filenames = filenames
        self.format = format

    def run(self) -> None:
        self.signal_start.emit()

        try:
            df =pd.DataFrame()
            if self.format == FileFormat.CNKI:
                df = Parser.parse_cnki(self.filenames)
            if self.format == FileFormat.WOS:
                df = Parser.parse_wos(self.filenames)
            msg = '解析{0}条记录，{1}个列'.format(df.shape[0], df.shape[1])
            self.signal_stop.emit(msg, df)
        except Exception as e:
            msg = '解析出错:{0}'.format(str(e))
            self.signal_stop.emit(msg, None)


class ParseModelThread(QThread):
    signal_start = Signal()
    signal_stop = Signal(str, object)

    def __init__(self, fnames):
        super(ParseModelThread, self).__init__()
        self.fnames = fnames

    def run(self) -> None:
        self.signal_start.emit()

        try:
            df_list = []
            for fname in self.fnames:
                df = pd.read_pickle(os.path.join(Cfg.models, fname), compression='gzip')
                df_list.append(df)
            df = pd.concat(df_list, axis=0, ignore_index=True, sort=True)
            msg = '解析{0}条记录，{1}个列'.format(df.shape[0], df.shape[1])
            self.signal_stop.emit(msg, df)
        except Exception as e:
            print(e)
            msg = '解析出错:{0}'.format(str(e))
            self.signal_stop.emit(msg, None)

class SavingModelThread(QThread):
    signal_start = Signal()
    signal_stop = Signal(str, object)

    def __init__(self, df, fpath):
        super(SavingModelThread, self).__init__()
        self.df = df
        self.fpath = fpath

    def run(self) -> None:
        self.signal_start.emit()
        self.df.to_pickle(self.fpath, compression="gzip")
        msg = '成功保存模型'
        self.signal_stop.emit(msg, None)

class DownloadThread(QThread):
    signal_start = Signal()
    signal_stop = Signal(str)


    def __init__(self, df, fpath):
        super(DownloadThread, self).__init__()
        self.df = df
        self.fpath = fpath

    def run(self) -> None:
        self.signal_start.emit()
        self.df.to_excel(self.fpath, index=False)
        msg = '成功下载数据'
        self.signal_stop.emit(msg)




if __name__ == '__main__':
    Parser.parse_wos('../files/WOS-NLP-1000.txt')