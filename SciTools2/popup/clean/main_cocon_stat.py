import sys
import time
import traceback
from log import logger
import numpy as np
import pandas as pd
from PySide2.QtWidgets import QDialog, QFileDialog

from mhelper import ssignal, PandasUtil, Cfg
from popup.clean.uipy import ui_cocon_stat
from mrunner import CleanExportCoconStatThread, CleanCoconStatThread


class PopupFreqStat(QDialog, ui_cocon_stat.Ui_Form):
    def __init__(self, parent):
        super(PopupFreqStat, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.init_data()

        self.btn_ok.clicked.connect(self.on_clicked)
        self.btn_export.clicked.connect(self.export_clicked)

    def init_data(self):
        self.listWidget.addItems(self.get_clean_columns())

    def on_clicked(self):
        names = [line.text() for line in self.listWidget.selectedItems()]
        threshold = self.threshold_spinBox.value()

        if len(names) == 0 or len(names) > 2:
            ssignal.error.emit('只能选择1或者2列')
            return

        df = self.get_df()

        self.cleanCoconStatThread = CleanCoconStatThread(df, names, threshold)
        self.cleanCoconStatThread.start()
        self.hide()

    def export_clicked(self):
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) == 0 or len(names) > 2:
            ssignal.error.emit('只能选择1或者2列')
            return

        t1 = time.time()
        df = self.get_df()

        df2 = pd.DataFrame()
        try:
            threshold = 0

            if len(names) == 1:
                df2 = PandasUtil.cocon_matrix(df, names[0], threhold=threshold)
            if len(names) == 2:
                df2 = PandasUtil.heter_matrix(df, names[0], names[1], threshold=threshold)

        except Exception as e:
            print(e)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback)

        df2 = df2.astype(np.uint8, errors='raise')
        self.set_df(df2)

        # table = self.get_table()
        # for i, col in enumerate(df2.index):
        #     for j, row in enumerate(df2.columns):
        #         print(row, col)
        #         if df2.loc[row, col] > 0:
        #             table.set_bgcolor(i, j, '#a3a9a8')

        t2 = time.time()


        filePath, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "保存统计文件",  # 标题
            Cfg.datafiles,  # 起始目录
            "Excel (*.xlsx);;"  # 选择类型过滤项，过滤内容在括号中
        )

        if filePath:
            self.coconStatThread = CleanExportCoconStatThread(fpath=filePath, df=df2)
            self.coconStatThread.start()


        msg = '分析{0}条记录，{1}个列，耗时{2}秒'.format(df2.shape[0], len(names), round(t2 - t1, Cfg.precision_point))
        ssignal.info.emit(msg)
        self.close()

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df, inplace_index=False, drop_index=False, show_color=True)

    def get_table(self):
        return self.parent.master_get_clean_table()
