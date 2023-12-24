"""
这是对biz模块业务逻辑的多线程封装。需要处理异常

在运行开始、结束、出错时，都要发送信号。

"""
import time
from typing import List, Set

import pandas as pd
from PySide2 import QtCore

from PySide2.QtCore import QThread
from PySide2.QtGui import QDesktopServices

from pandas import DataFrame
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from core import CleanBiz
from core.clean import AnalyzeBiz, Parser
from core.mgraph import GraphData, Draw
from core.util.mutil import Config, PandasUtil, DictReader
from core.const import ssignal
from core.log import logger


class WatchDataFilesChaningThread(QThread):
    def run(self) -> None:
        event_handler = WatchDataFilesChaningThread.DataFilesChaningHandler()
        observer = Observer()
        observer.schedule(event_handler, path=".", recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    class DataFilesChaningHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            try:
                ssignal.datafiles_changing.emit()
            except Exception as e:
                logger.exception(e)


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
        ssignal.info.emit("开始解析文件，请稍等")

        try:
            t1 = time.time()

            df = Parser.parse(self.format, self.filenames)

            t2 = time.time()

            msg = "解析{0}条记录，{1}个列，耗时{2}秒".format(
                df.shape[0], df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.reset_cache.emit()
            ssignal.push_cache.emit(df)
            ssignal.set_clean_dataset.emit(df)
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            ssignal.error.emit(msg)


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
        ssignal.info.emit("开始下载文件，请稍等")
        try:
            t1 = time.time()
            if self.fpath.endswith(".csv"):
                PandasUtil.write_csv(self.df, self.fpath, index=False)
            elif self.fpath.endswith(".xlsx") or self.fpath.endswith(".xls"):
                PandasUtil.write_excel(self.df, self.fpath, "Sheet0", False)
            elif self.fpath.endswith("pkl"):
                PandasUtil.write_pickle(self.df, self.fpath, compression="gzip")
            elif self.fpath.endswith("pqt"):
                PandasUtil.write_parquet(self.df, self.fpath)
            else:
                raise Exception("没有处理的保存类型 " + self.fpath)
            t2 = time.time()
            msg = "保存{0}，耗时{1}秒".format(self.fpath, round(t2 - t1, int(Config.precision_point.value)))
            ssignal.info.emit(msg)
        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


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
        ssignal.info.emit("开始分析，请稍等")
        try:
            t1 = time.time()

            stat_df, pairs = CleanBiz.metadata(self.df)

            t2 = time.time()
            msg = "解析{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            self.dataset.emit(stat_df, pairs)
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            ssignal.error.emit(msg)


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
        ssignal.info.emit("开始下载文件，请稍等")
        try:
            t1 = time.time()

            for i, name in enumerate(self.names):
                PandasUtil.write_excel(self.df_list[i], self.fpath, self.names[i], save_index=False)

            t2 = time.time()
            msg = "保存词频统计文件 {0}，耗时{1}秒".format(
                self.fpath, round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)

        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            ssignal.error.emit(msg)


# class CleanExportCoconStatThread(QThread):
#     """
#     导出共现统计文件
#     """
#
#     def __init__(self, fpath, df, threshold):
#         super(CleanExportCoconStatThread, self).__init__()
#         self.fpath = fpath
#         self.df = df
#         self.threshold = threshold
#
#     def run(self) -> None:
#         ssignal.info.emit("开始下载文件，请稍等")
#         try:
#             t1 = time.time()
#
#             CleanBiz.save_excel(self.df, self.fpath, "Sheet1", save_index=True)
#
#             t2 = time.time()
#             msg = "保存统计文件 {0}，耗时{1}秒".format(
#                 self.fpath, round(t2 - t1, int(cfg.precision_point.value))
#             )
#             ssignal.info.emit(msg)
#
#         except Exception as e:
#             logger.exception(e)
#             msg = "解析出错:{0}".format(str(e))
#             ssignal.error.emit(msg)


class CleanReplaceValuesThread(QThread):
    """
    同义词
    """

    def __init__(self, fpath, df):
        super(CleanReplaceValuesThread, self).__init__()
        self.fpath = fpath
        self.df = df

    def run(self) -> None:
        ssignal.info.emit("开始替换值，请稍等")
        try:
            t1 = time.time()

            PandasUtil.write_excel(self.df, self.fpath, "0", save_index=False)

            t2 = time.time()
            msg = "保存统计文件 {0}，耗时{1}秒".format(
                self.fpath, round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)

        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanCopyColumnThread(QThread):
    def __init__(self, df: pd.DataFrame, names: List[str]):
        super(CleanCopyColumnThread, self).__init__()
        self.df = df
        self.names = names

    def run(self) -> None:
        ssignal.info.emit("复制列，请稍等")
        try:
            t1 = time.time()

            df = CleanBiz.copy_column(self.df, self.names)

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.set_clean_dataset.emit(df)

        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanSplitColumnThread(QThread):
    def __init__(
            self,
            df: pd.DataFrame,
            name: str,
            split_style: str,
            le1_text: str,
            get_style: str,
            le2_text: int,
    ):
        super(CleanSplitColumnThread, self).__init__()
        self.df = df
        self.name = name
        self.split_style = split_style
        self.le1_text = le1_text
        self.get_style = get_style
        self.le2_text = le2_text

    def run(self) -> None:
        ssignal.info.emit("开始拆分列，请稍等")
        try:
            t1 = time.time()

            df = CleanBiz.split_column(
                self.df,
                self.name,
                self.split_style,
                self.le1_text,
                self.get_style,
                self.le2_text,
            )

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.set_clean_dataset.emit(df)
        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanReplaceValueThread(QThread):
    def __init__(
            self,
            df: pd.DataFrame,
            names: List[str],
            current_tab_index: int,
            old_sep: str,
            new_sep: str,
            other_char: str,
            is_reserved: str,
            is_new: str,
    ):
        super(CleanReplaceValueThread, self).__init__()
        self.df = df
        self.names = names
        self.current_tab_index = current_tab_index
        self.old_sep = old_sep
        self.new_sep = new_sep
        self.other_char = other_char
        self.is_reserved = is_reserved
        self.is_new = is_new

    def run(self) -> None:
        ssignal.info.emit("开始替换值，请稍等")
        try:
            t1 = time.time()

            if self.current_tab_index==0:
                df = CleanBiz.repalce_values1(
                    self.df,
                    self.names,
                    self.old_sep,
                    self.new_sep,
                    self.is_new,
                )
            if self.current_tab_index==1:
                df = CleanBiz.repalce_values2(
                    self.df,
                    self.names,
                    self.other_char,
                    self.is_reserved,
                    self.is_new,
                )

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.set_clean_dataset.emit(df)

        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanCombineSynonymThread(QThread):
    def __init__(
            self, df: pd.DataFrame, synonym_dict_path: str, names: List[str], is_new: bool
    ):
        super(CleanCombineSynonymThread, self).__init__()
        self.df = df
        self.fpath = synonym_dict_path
        self.names = names
        self.is_new = is_new

    def run(self) -> None:
        ssignal.info.emit("开始同义词，请稍等")
        try:
            t1 = time.time()

            df = CleanBiz.combine_synonym(self.df, DictReader.combine_words_file(self.fpath), self.names, self.is_new)

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.set_clean_dataset.emit(df)
        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanStopWordsThread(QThread):
    def __init__(
            self, df: pd.DataFrame, names: List[str], words_set: Set[str], is_new: bool
    ):
        super(CleanStopWordsThread, self).__init__()
        self.df = df
        self.names = names
        self.words_set = words_set
        self.is_new = is_new

    def run(self) -> None:
        ssignal.info.emit("开始停用词，请稍等")
        try:
            t1 = time.time()

            df = CleanBiz.stop_words(self.df, self.names, self.words_set, self.is_new)

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.set_clean_dataset.emit(df)
        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanWordCountThread(QThread):
    def __init__(self, df: pd.DataFrame, col_name: str, threshold: int):
        super(CleanWordCountThread, self).__init__()
        self.df = df
        self.col_name = col_name
        self.threshold = threshold

    def run(self) -> None:
        ssignal.info.emit("开始词频统计，请稍等")
        try:
            t1 = time.time()

            df = CleanBiz.wordcount_stat(self.df, self.col_name, self.threshold)

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.set_clean_dataset.emit(df)
        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanWordCountExportThread(QThread):
    def __init__(
            self, df: pd.DataFrame, col_names: List[str], threshold: int, fpath: str
    ):
        super(CleanWordCountExportThread, self).__init__()
        self.df = df
        self.col_names = col_names
        self.threshold = threshold
        self.fpath = fpath

    def run(self) -> None:
        ssignal.info.emit("开始词频统计文件导出，请稍等")
        try:
            t1 = time.time()

            sheet_name_and_df = {}

            for col_name in self.col_names:
                sheet_name_and_df[col_name] = CleanBiz.wordcount_stat(
                    self.df, col_name, self.threshold
                )

            PandasUtil.write_excel_many_sheet(
                fpath=self.fpath, sheet_name_and_df=sheet_name_and_df
            )

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)

        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanCoconStatThread(QThread):
    def __init__(self, df: pd.DataFrame, fpath: str, names: List[str], threshold: int):
        super(CleanCoconStatThread, self).__init__()
        self.df = df
        self.fpath = fpath
        self.names = names
        self.threshold = threshold

    def run(self) -> None:
        ssignal.info.emit("开始共现分析，请稍等")
        try:
            t1 = time.time()

            # 共现矩阵
            if len(self.names) == 1:
                matrix = PandasUtil.cocon_matrix(self.df, self.names[0], threhold=self.threshold, diagonal_values=True)
            if len(self.names) == 2:
                matrix = PandasUtil.heter_matrix(self.df, self.names[0], self.names[1], threshold=self.threshold)
            assert isinstance(matrix, pd.DataFrame)
            # 相异矩阵
            diss_matrix = PandasUtil.dissimilarity_matrix(matrix.copy(deep=True))
            assert isinstance(diss_matrix, pd.DataFrame)
            # 余弦相似度矩阵
            cosine_matrix = PandasUtil.cosine_similarity_matrix(matrix.copy(deep=True))
            assert isinstance(cosine_matrix, pd.DataFrame)
            # 相关系数矩阵
            corr_matrix = PandasUtil.correlation_matrix(matrix.copy(deep=True))
            assert isinstance(corr_matrix, pd.DataFrame)
            # 欧式距离矩阵
            eucli_matrix = PandasUtil.euclidean_distances_matrix(matrix.copy(deep=True))
            assert isinstance(eucli_matrix, pd.DataFrame)
            # z-score矩阵
            z_score_matrix = PandasUtil.z_score_matrix(matrix.copy(deep=True))
            assert isinstance(z_score_matrix, pd.DataFrame)

            PandasUtil.write_excel_many_sheet(self.fpath, {'共现矩阵': matrix,
                                                           '相异矩阵': diss_matrix,
                                                           '余弦相似度矩阵': cosine_matrix,
                                                           '相关系数矩阵': corr_matrix,
                                                           '欧氏距离矩阵': eucli_matrix,
                                                           'z-score矩阵': z_score_matrix}, index=True)

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            msg.replace('Permission', '文件正在打开中,请关闭该文件')
            print(msg)
            ssignal.error.emit(msg)


class CleanRowSimilarityThread(QThread):
    def __init__(self, df: pd.DataFrame, column_names: List[str], limited: int):
        super(CleanRowSimilarityThread, self).__init__()
        self.df = df
        self.column_names = column_names
        self.limited = limited

    def run(self) -> None:
        ssignal.info.emit("开始分析相似度，请稍等")
        try:
            t1 = time.time()

            df_new = CleanBiz.row_similarity(self.df, self.column_names, self.limited)

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.set_clean_dataset.emit(df_new)
        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanVerticalConcatThread(QThread):
    def __init__(self, abs_paths: List[str]):
        super(CleanVerticalConcatThread, self).__init__()
        self.abs_paths = abs_paths

    def run(self) -> None:
        ssignal.info.emit("开始数据合并，请稍等")

        try:
            t1 = time.time()

            ddss = []

            for abs_path in self.abs_paths:
                ddss.append(Parser.parse_csv([abs_path], ','))

            # 使用 concat 沿着行的方向连接
            df_new = pd.concat(ddss, ignore_index=True)
            df_new.fillna('', inplace=True)
            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                df_new.shape[0], df_new.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.set_clean_dataset.emit(df_new)
        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanSplitWordsThread(QThread):
    def __init__(self, df: pd.DataFrame, names: List[str]):
        super(CleanSplitWordsThread, self).__init__()
        self.df = df
        self.names = names

    def run(self) -> None:
        ssignal.info.emit("正在切分词，请稍等")
        try:
            t1 = time.time()

            df = CleanBiz.split_words(self.df, self.names)

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.set_clean_dataset.emit(df)

        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)


class CleanExtractFeaturesThread(QThread):
    def __init__(self, df: pd.DataFrame, names: List[str], speeches: List[str]):
        super(CleanExtractFeaturesThread, self).__init__()
        self.df = df
        self.names = names
        self.speeches = speeches

    def run(self) -> None:
        ssignal.info.emit("正在提取特征词，请稍等")
        try:
            t1 = time.time()

            df = CleanBiz.extract_features(self.df, self.names, self.speeches)

            t2 = time.time()
            msg = "执行{0}条记录，{1}个列，耗时{2}秒".format(
                self.df.shape[0], self.df.shape[1], round(t2 - t1, int(Config.precision_point.value))
            )
            ssignal.info.emit(msg)
            ssignal.set_clean_dataset.emit(df)

        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)

import collections
class CleanDrawGraphThread(QThread):
    ConfigTuple = collections.namedtuple('ConfigTuple', ['chart_style','xlabel','ylabel','stat_threshold', 'orderby','canvas_width','canvas_height'])
    def __init__(self, df: pd.DataFrame, configTuple: ConfigTuple):
        super(CleanDrawGraphThread, self).__init__()
        self.df = df
        self.config = configTuple

    def run(self) -> None:
        ssignal.info.emit("正在画图，请稍等")
        try:
            t1 = time.time()

            data = GraphData()
            data.chart_style = self.config.chart_style
            stat_result = None

            if len(self.config.ylabel) == 0:
                stat_result = AnalyzeBiz.count(self.df, by=self.config.xlabel)
            else:
                stat_result = AnalyzeBiz.count_by(self.df, stat_column=self.config.ylabel, by=self.config.xlabel)

            # 过滤阈值
            stat_result = stat_result[stat_result['Count'] >= self.config.stat_threshold].reset_index(
                drop=True)

            # 结果排序
            if '升' in self.config.orderby:
                stat_result.sort_values('Count', ascending=True, inplace=True)
            elif '降' in self.config.orderby:
                stat_result.sort_values('Count', ascending=False, inplace=True)

            data.xaxis = stat_result.loc[:, self.config.xlabel].tolist()
            data.yaxis = stat_result.loc[:, 'Count'].tolist()

            data.canvas_width = self.config.canvas_width
            data.canvas_height = self.config.canvas_height

            logger.info(data)

            t2 = time.time()
            ssignal.info.emit('开始图表数据，耗时{0}秒'.format(round(t2 - t1, int(Config.precision_point.value))))

            draw = Draw()
            local_file = draw.draw(data)
            QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(local_file))

        except Exception as e:
            logger.exception(e)
            msg = "出错:{0}".format(str(e))
            ssignal.error.emit(msg)
