import re

from PySide2.QtWidgets import QDialog

from core.const import ssignal
from core.runner import CleanSplitColumnThread
from uipopup.uipy import ui_split_column


class PopupSplitColumn(QDialog, ui_split_column.Ui_Form):
    def __init__(self, parent):
        super(PopupSplitColumn, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.listWidget.addItems(self.get_clean_columns())

        self.pushButton.clicked.connect(self.on_clicked)

    def on_clicked(self):
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) == 0:
            ssignal.error.emit('请选择列')
            return

        name = names[0]

        split_style_text = self.cb1.currentText()
        le1_text = self.le1.text()
        get_style_text = self.cb2.currentText()
        le2_text = self.le2.text()

        m = re.compile(r'^[1-9]\d*$')
        if '字符' in split_style_text and not m.match(le1_text):
            ssignal.error.emit('拆分方式是按字符数，后面请填写正整数')
            return

        if not m.match(le2_text):
            ssignal.error.emit('拆分结果后面请填写正整数')
            return

        le2_text = int(le2_text)
        df = self.get_df()
        ssignal.push_cache.emit(self.get_df())

        self.cleanSplitColumnThread = CleanSplitColumnThread(df, name, split_style_text, le1_text, get_style_text,
                                                             le2_text)
        self.cleanSplitColumnThread.start()
        self.close()

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
