from PySide2.QtWidgets import QDialog
from core.log import logger
from core.const import ssignal
from uipopup.uipy import ui_modify_value


class PopupModifyValues(QDialog, ui_modify_value.Ui_Form):
    def __init__(self, parent):
        super(PopupModifyValues, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.btn_start.clicked.connect(self.action_start)
        self.btn_save.clicked.connect(self.action_save)

    def action_start(self):
        logger.info('开始修改值')

        self.get_table().set_item_writable(True)

        ssignal.push_cache.emit(self.get_df())

        msg = '开始修改'
        ssignal.info.emit(msg)

    def action_save(self):
        logger.info('保存修改')

        self.get_table().set_item_writable(False)

        msg = '停止修改'
        ssignal.info.emit(msg)

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)

    def get_table(self):
        return self.parent.master_get_clean_table()