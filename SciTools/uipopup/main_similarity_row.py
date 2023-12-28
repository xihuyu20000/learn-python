from PySide2.QtWidgets import QDialog

from core.const import ssignal
from core.log import logger
from core.runner import CleanRowSimilarityThread
from uipopup.uipy import ui_similarity_row


class PopupSimilarityRows(QDialog, ui_similarity_row.Ui_Form):
    GROUP_LABEL_TEXT = '组号'
    ORIGINAL_LABEL_TEXT = '原行号'

    def __init__(self, parent):
        super(PopupSimilarityRows, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.column_names.addItems(self.get_clean_columns())
        self.column_names.setCurrentRow(0)

        self.slider_horizon.valueChanged.connect(lambda: self.value_changed(self.vaLable, self.slider_horizon.value()))
        self.btn_ok.clicked.connect(lambda: self.action_ok(self.slider_horizon.value()))

    def action_ok(self, limited):
        logger.info('相似度')

        column_names = self.column_names.selectedItems()
        if len(column_names) == 0:
            ssignal.error.emit('请选择列')
            return

        column_names = [item.text() for item in column_names]
        df = self.get_df()
        ssignal.push_cache.emit(self.get_df())

        # 缩小到[0,1]
        limited = float(limited / 100)

        self.cleanRowSimilarityThread = CleanRowSimilarityThread(df, column_names, limited)
        self.cleanRowSimilarityThread.start()

    def value_changed(self, lbl, val):
        lbl.setText(str(val))

    def get_clean_columns(self):
        return self.parent.get_df_columns()

    def get_df(self):
        return self.parent.get_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
