import time

from PySide2.QtWidgets import QDialog

from core.const import ssignal, Actions
from core.log import logger
from uipopup.uipy import ui_row_deduplicate


class PopupRowDeduplicate(QDialog, ui_row_deduplicate.Ui_Form):
    def __init__(self, parent):
        super(PopupRowDeduplicate, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.column_names.addItems(self.get_clean_columns())
        for i in range(len(self.get_clean_columns())):
            self.column_names.setItemSelected(self.column_names.item(i), True)

        self.btn_ok.clicked.connect(self.action_ok)

    def action_ok(self):
        logger.debug('行去重')
        logger.info(Actions.row_deduplicate.cn)
        names = [item.text() for item in self.column_names.selectedItems()]
        if len(names) == 0:
            ssignal.error.emit('请选择列')
            return

        t1 = time.time()

        df = self.get_df()

        shape = df.shape
        df.drop_duplicates(subset=names, keep='first', inplace=True)
        df.reset_index(drop=True, inplace=True)
        self.set_df(df)

        t2 = time.time()
        msg = '对比{0}条记录，{1}个列，耗时{2}秒'.format(shape[0], len(names), round(t2 - t1, 2))
        ssignal.info.emit(msg)

        ssignal.push_cache.emit(Actions.row_deduplicate.cn, self.get_df())

        self.close()

    def get_clean_columns(self):
        return self.parent.get_df_columns()

    def get_df(self):
        return self.parent.get_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
