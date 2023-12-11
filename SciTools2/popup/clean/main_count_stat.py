import os
import time

import numpy as np
import pandas as pd
from PySide2.QtWidgets import QDialog, QFileDialog
from log import logger
from helper import Utils, ssignal, Cfg
from popup.clean.uipy import ui_count_stat
from runner import CleanExportCountStatThread


class PopupCountStat(QDialog, ui_count_stat.Ui_Form):
    def __init__(self, parent):
        super(PopupCountStat, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent


        self.init_data()

        self.btn_ok.clicked.connect(self.ok_clicked)
        self.btn_export.clicked.connect(self.export_clicked)

    def init_data(self):
        self.listWidget.addItems(self.get_clean_columns())

    def ok_clicked(self):
        threshold = int(self.threhold_spinBox.text())
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) == 0:
            ssignal.error.send('请选择列')
            return
        if len(names) >1:
            ssignal.error.send('选择多列，请导出')
            return

        t1 = time.time()
        df = self.get_df()

        name = names[0]
        try:
            # 使用str.split进行拆分，并使用explode展开列表
            df_split = df[name].str.split(Cfg.seperator, expand=True).stack()

            # 使用value_counts进行统计
            counts = df_split.value_counts()
            counts = counts[counts>=threshold]

            # 使用reset_index()将Series转为DataFrame
            counts = counts.reset_index()
            # 替换空值
            counts.fillna('', inplace=True)
            # 为DataFrame的列命名
            counts.columns = [name, '次数']

            self.set_df(counts)
        except Exception as e:
            print(e)
            counts = pd.DataFrame(columns = [name, '次数'])
            self.set_df(counts)

        t2 = time.time()

        msg = '统计{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(names), round(t2 - t1, 2))
        ssignal.info.send(msg)
        self.close()

    def export_clicked(self):
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) == 0:
            ssignal.error.send('请选择列')
            return

        df = self.get_df()

        results = []
        for col in names:
            try:
                # 使用str.split进行拆分，并使用explode展开列表
                df_split = df[col].str.split(Cfg.seperator, expand=True).stack()

                # 使用value_counts进行统计
                counts = df_split.value_counts()
                # 使用reset_index()将Series转为DataFrame
                counts = counts.reset_index()
                # 替换空值
                counts.fillna('', inplace=True)
                # 为DataFrame的列命名
                counts.columns = [col, '次数']
                results.append(counts)
            except Exception as e:
                print(e)
                counts = pd.DataFrame(columns = [col, '次数'])
                results.append(counts)

        filePath, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "保存词频统计文件",  # 标题
            Cfg.datafiles,  # 起始目录
            "Excel (*.xlsx);;"  # 选择类型过滤项，过滤内容在括号中
        )

        if filePath:
            self.countStatThread = CleanExportCountStatThread(fpath=filePath, names=names, df_list=results)
            self.countStatThread.start()

        self.close()

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()


    def set_df(self, df):
        self.parent.master_set_clean_df(df)