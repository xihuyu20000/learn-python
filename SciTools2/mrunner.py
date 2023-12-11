"""
这是对biz模块业务逻辑的多线程封装。需要处理异常

在运行开始、结束、出错时，都要发送信号。

"""
import time
from typing import List

import pandas as pd
from PySide2 import QtCore

from PySide2.QtCore import QThread

from pandas import DataFrame

from mbiz import Parser, CleanBiz
from mhelper import FileFormat, ssignal
from log import logger


class CleanParseFileThread(QThread):
    """
    解析数据文件
    """

    def __init__(self, filenames: List[str], format: str, sep: str):
        """

        :param filenames: 传入的文件名称（完整路径）
        :param format: 参考FileFormat类定义的格式
        :param sep: 指定csv文件的分隔符
        """
        super(CleanParseFileThread, self).__init__()
        self.filenames = filenames
        self.format = format
        self.sep = sep

    def run(self) -> None:
        ssignal.info.send('开始解析文件，请稍等')

        try:
            t1 = time.time()

            if self.format == FileFormat.CNKI:
                df = Parser.parse_cnki(self.filenames)
            elif self.format == FileFormat.WOS:
                df = Parser.parse_wos(self.filenames)
            elif self.format == FileFormat.CSV:
                df = Parser.parse_csv(self.filenames, self.sep)
            elif self.format == FileFormat.EXCEL:
                df = Parser.parse_excel(self.filenames)
            elif self.format == FileFormat.PICKLE:
                df = Parser.parse_pickle(self.filenames)
            elif self.format == FileFormat.PARQUET:
                df = Parser.parse_pickle(self.filenames)
            else:
                raise Exception("没有处理的数据类型" + self.format)

            t2 = time.time()
            msg = '解析{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], df.shape[1], round(t2 - t1, 2))
            ssignal.info.send(msg)
            ssignal.set_clean_dataset.send(df)
        except Exception as e:
            logger.exception(e)
            msg = '解析出错:{0}'.format(str(e))
            ssignal.error.send(msg)


class CleanSaveDatasetThread(QThread):
    """
    清洗，导出数据集
    """

    def __init__(self, df, fpath):
        """

        :param df: 数据集
        :param fpath: 文件的完整路径
        """
        super(CleanSaveDatasetThread, self).__init__()
        self.df = df
        self.fpath = fpath

    def run(self) -> None:
        ssignal.info.send('开始下载文件，请稍等')
        try:
            t1 = time.time()
            if self.fpath.endswith('.csv'):
                self.df.to_csv(self.fpath, index=False)
            elif self.fpath.endswith('.xlsx') or self.fpath.endswith('.xls'):
                self.df.to_excel(self.fpath, index=True)
            elif self.fpath.endswith('pkl'):
                self.df.to_pickle(self.fpath, compression="gzip")
            elif self.fpath.endswith('pqt'):
                self.df.to_parquet(self.fpath, engine="fastparquet", compression="snappy")
            else:
                raise Exception("没有处理的保存类型 " + self.fpath)
            t2 = time.time()
            msg = '保存{0}，耗时{1}秒'.format(self.fpath, round(t2 - t1, 2))
            ssignal.info.send(msg)

        except Exception as e:
            logger.exception(e)
            msg = '出错:{0}'.format(str(e))
            ssignal.error.send(msg)


class CleanMetadataThread(QThread):
    """
    清洗，元数据
    """
    dataset = QtCore.Signal(object, object)
    def __init__(self, df: DataFrame):
        """

        :param df: 数据集
        """
        super(CleanMetadataThread, self).__init__()
        self.df = df

    def run(self) -> None:
        ssignal.info.send('开始分析，请稍等')
        try:
            t1 = time.time()

            stat_df, pairs = CleanBiz.metadata(self.df)

            t2 = time.time()
            msg = '解析{0}条记录，{1}个列，耗时{2}秒'.format(self.df.shape[0], self.df.shape[1], round(t2 - t1, 2))
            ssignal.info.send(msg)
            self.dataset.emit(stat_df, pairs)
        except Exception as e:
            logger.exception(e)
            msg = '解析出错:{0}'.format(str(e))
            ssignal.error.send(msg)


class CleanExportCountStatThread(QThread):
    """
    词频统计导出
    """

    def __init__(self, fpath, names, df_list):
        super(CleanExportCountStatThread, self).__init__()
        self.fpath = fpath
        self.names = names
        self.df_list = df_list

    def run(self) -> None:
        ssignal.info.send('开始下载文件，请稍等')
        try:
            t1 = time.time()

            for i, name in enumerate(self.names):
                CleanBiz.save_excel(self.df_list[i], self.fpath, self.names[i])

            t2 = time.time()
            msg = '保存词频统计文件 {0}，耗时{1}秒'.format(self.fpath, round(t2 - t1, 2))
            ssignal.info.send(msg)

        except Exception as e:
            logger.exception(e)
            msg = '解析出错:{0}'.format(str(e))
            ssignal.error.send(msg)


class CleanExportCoconStatThread(QThread):
    """
    导出共现统计文件
    """
    def __init__(self, fpath, df):
        super(CleanExportCoconStatThread, self).__init__()
        self.fpath = fpath
        self.df = df

    def run(self) -> None:
        ssignal.info.send('开始下载文件，请稍等')
        try:
            t1 = time.time()

            CleanBiz.save_excel(self.df, self.fpath, '0')

            t2 = time.time()
            msg = '保存统计文件 {0}，耗时{1}秒'.format(self.fpath, round(t2 - t1, 2))
            ssignal.info.send(msg)

        except Exception as e:
            logger.exception(e)
            msg = '解析出错:{0}'.format(str(e))
            ssignal.error.send(msg)


class CleanReplaceValuesThread(QThread):
    """
    同义词
    """
    def __init__(self, fpath, df):
        super(CleanReplaceValuesThread, self).__init__()
        self.fpath = fpath
        self.df = df

    def run(self) -> None:
        ssignal.info.send('开始替换值，请稍等')
        try:
            t1 = time.time()

            CleanBiz.save_excel(self.df, self.fpath, '0')

            t2 = time.time()
            msg = '保存统计文件 {0}，耗时{1}秒'.format(self.fpath, round(t2 - t1, 2))
            ssignal.info.send(msg)

        except Exception as e:
            logger.exception(e)
            msg = '出错:{0}'.format(str(e))
            ssignal.error.send(msg)


class CleanCopyColumnThread(QThread):
    def __init__(self, df:pd.DataFrame, names:List[str]):
        super(CleanCopyColumnThread, self).__init__()
        self.df = df
        self.names = names


    def run(self) -> None:
        ssignal.info.send('复制列，请稍等')
        try:
            t1 = time.time()

            df = CleanBiz.copy_column(self.df, self.names)

            t2 = time.time()
            msg = '执行{0}条记录，{1}个列，耗时{2}秒'.format(self.df.shape[0], self.df.shape[1], round(t2 - t1, 2))
            ssignal.info.send(msg)
            ssignal.set_clean_dataset.send(df)
        except Exception as e:
            logger.exception(e)
            msg = '出错:{0}'.format(str(e))
            ssignal.error.send(msg)

class CleanSplitColumnThread(QThread):
    def __init__(self, df:pd.DataFrame, name:str, split_style:str, le1_text:str, get_style:str, le2_text:int):
        super(CleanSplitColumnThread, self).__init__()
        self.df = df
        self.name = name
        self.split_style = split_style
        self.le1_text = le1_text
        self.get_style = get_style
        self.le2_text = le2_text


    def run(self) -> None:
        ssignal.info.send('开始拆分列，请稍等')
        try:
            t1 = time.time()

            df = CleanBiz.split_column(self.df, self.name, self.split_style, self.le1_text, self.get_style, self.le2_text)

            t2 = time.time()
            msg = '执行{0}条记录，{1}个列，耗时{2}秒'.format(self.df.shape[0], self.df.shape[1], round(t2 - t1, 2))
            ssignal.info.send(msg)
            ssignal.set_clean_dataset.send(df)
        except Exception as e:
            logger.exception(e)
            msg = '出错:{0}'.format(str(e))
            ssignal.error.send(msg)

class CleanCombineSynonymThread(QThread):
    def __init__(self, df:pd.DataFrame, synonym_dict_path:str, names:List[str], is_new:bool):
        super(CleanCombineSynonymThread, self).__init__()
        self.df = df
        self.fpath = synonym_dict_path
        self.names = names
        self.is_new = is_new


    def run(self) -> None:
        ssignal.info.send('开始同义词，请稍等')
        try:
            t1 = time.time()

            df = CleanBiz.combine_synonym(self.df, self.fpath, self.names, self.is_new)

            t2 = time.time()
            msg = '执行{0}条记录，{1}个列，耗时{2}秒'.format(self.df.shape[0], self.df.shape[1], round(t2 - t1, 2))
            ssignal.info.send(msg)
            ssignal.set_clean_dataset.send(df)
        except Exception as e:
            logger.exception(e)
            msg = '出错:{0}'.format(str(e))
            ssignal.error.send(msg)