from PySide2.QtWidgets import QDialog
from core.log import logger
from mrunner import CleanVerticalConcatThread
from uipopup.uipy import ui_vertical_concat


class PopupVerticalConcat(QDialog, ui_vertical_concat.Ui_Form):
    def __init__(self, parent, abs_paths):
        super(PopupVerticalConcat, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.abs_paths = abs_paths

        self.btn_start.clicked.connect(self.action_start)

    def action_start(self):
        logger.info('开始数据合并')

        self.cleanVerticalConcatThread = CleanVerticalConcatThread(self.abs_paths)
        self.cleanVerticalConcatThread.start()
        self.close()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)

    def get_table(self):
        return self.parent.master_get_clean_table()
