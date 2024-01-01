from PySide2.QtWidgets import QDialog

from core.const import ssignal
from core.log import logger
from core.runner.mrunner import CleanFilterRowsThread
from uipopup.uipy import ui_filter_row


class PopupFilterRows(QDialog, ui_filter_row.Ui_Form):

    def __init__(self, parent):
        super(PopupFilterRows, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.init_data()

        self.btn_ok.clicked.connect(self.action_ok)

    def init_data(self):
        self.column_names.addItems(self.get_clean_columns())

    def action_ok(self):
        logger.info('过滤行')

        column_names = self.column_names.selectedItems()
        if len(column_names) == 0:
            ssignal.error.emit('请选择列')
            return

        column_names = [item.text() for item in column_names]

        df = self.get_df()

        has_null = self.checkBox_null.isChecked()
        has_tougao = self.checkBox_tougao.isChecked()
        has_bianjibu = self.checkBox_bianjibu.isChecked()

        self.cleanFilterRowsThread = CleanFilterRowsThread(df, column_names, has_null, has_tougao, has_bianjibu)
        self.cleanFilterRowsThread.start()

        self.close()

    def get_clean_columns(self):
        return self.parent.get_df_columns()

    def get_df(self):
        return self.parent.get_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
