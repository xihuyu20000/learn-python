import time

from PySide2.QtWidgets import QDialog
from log import logger
from helper import Utils, ssignal
from popup.clean.uipy import ui_copy_column


class PopupCopyColumn(QDialog, ui_copy_column.Ui_Form):
    def __init__(self, parent):
        super(PopupCopyColumn, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.init_data()

        self.pushButton.clicked.connect(self.on_clicked)

    def init_data(self):
        self.listWidget.addItems(self.get_clean_columns())

    def on_clicked(self):
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) == 0:
            return

        t1 = time.time()
        df = self.get_df()
        new_names = []
        for col in names:
            new_names.append(col + '-new')
            df[col + '-new'] = df[col]

        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, new_names)
        df = df[old_names]

        self.set_df(df)
        t2 = time.time()

        msg = '复制{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(names), round(t2 - t1, 2))
        ssignal.info.send(msg)
        self.close()

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()
    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)