import time

from PySide2.QtWidgets import QDialog
from log import logger

from mhelper import ssignal, Cfg
from popup.clean.uipy import ui_compare_columns


class PopupCompareColumns(QDialog, ui_compare_columns.Ui_Form):
    def __init__(self, parent):
        super(PopupCompareColumns, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.column_names.addItems(self.get_clean_columns())
        self.column_names.setCurrentRow(0)

        self.btn_reset.clicked.connect(self.action_reset)
        self.btn_ok.clicked.connect(self.action_ok)


    def action_reset(self):
        logger.info('列对比')
        indexes = [item.row() for item in self.column_names.selectedIndexes()]

        t1 = time.time()
        df = self.get_df()
        table = self.get_table()
        for i in range(df.shape[0]):
            for col in indexes:
                table.set_bgcolor(i, col, '#FFFFFF')

        t2 = time.time()
        msg = '清除{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(indexes), round(t2 - t1, 2))
        ssignal.error.send(msg)

    def action_ok(self):
        logger.info('列对比')
        indexes = [item.row() for item in self.column_names.selectedIndexes()]
        if len(indexes) != 2:
            ssignal.error.send('只能选择2列')
            return

        t1 = time.time()
        df = self.get_df()
        table = self.get_table()
        for i in range(df.shape[0]):
            if df.iloc[i, indexes[0]] != df.iloc[i, indexes[1]]:
                table.set_bgcolor(i, indexes[1], '#a3a9a8')
        t2 = time.time()
        msg = '对比{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(indexes), round(t2 - t1, 2))
        ssignal.info.send(msg)
        self.close()

    def __replace(self, line, words_set):
        words = [w for w in line.split(Cfg.seperator) if w not in words_set]
        return ';'.join(words)

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)

    def get_table(self):
        return self.parent.master_get_clean_table()