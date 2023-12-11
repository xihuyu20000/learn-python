import time

from PySide2.QtWidgets import QDialog
from log import logger
from mhelper import Utils, ssignal
from mrunner import CleanCopyColumnThread
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
            ssignal.error.send('请选择列')
            return

        df = self.get_df()

        cleanCopyColumnThread = CleanCopyColumnThread(df, names)
        cleanCopyColumnThread.start()

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)