import time

from PySide2.QtWidgets import QDialog
from core.log import logger
from core.const import ssignal
from uipopup.uipy import ui_distinct_row


class PopupRowDistinct(QDialog, ui_distinct_row.Ui_Form):
    def __init__(self, parent):
        super(PopupRowDistinct, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.column_names.addItems(self.get_clean_columns())
        self.column_names.setCurrentRow(0)

        self.btn_ok.clicked.connect(self.action_ok)


    def action_ok(self):
        logger.info('列对比')
        names = [item.text() for item in self.column_names.selectedItems()]
        if len(names) == 0:
            ssignal.error.emit('请选择列')
            return

        t1 = time.time()

        df = self.get_df()
        ssignal.push_cache.emit(self.get_df())

        shape = df.shape
        df.drop_duplicates(subset=names, keep='first', inplace=True)
        self.set_df(df)
        t2 = time.time()
        msg = '对比{0}条记录，{1}个列，耗时{2}秒'.format(shape[0], len(names), round(t2 - t1, 2))
        ssignal.info.emit(msg)

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
