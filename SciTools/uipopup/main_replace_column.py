from PySide2.QtWidgets import QDialog

from core.const import ssignal, Actions
from core.runner import CleanReplaceValueThread
from uipopup.uipy import ui_replace_column


class PopupReplaceColumn(QDialog, ui_replace_column.Ui_Form):

    def __init__(self, parent=None):
        super(PopupReplaceColumn, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.init_data()

        self.ok_button.clicked.connect(lambda: self.ok_clicked(self.tabwidget.currentIndex(),
                                                               self.old_lineEdit.text(),
                                                               self.new_lineEdit.text(),
                                                               self.other_linedit.text(),
                                                               self.rbt00.isChecked(),
                                                               self.rbt1.isChecked(), ))

    def init_data(self):
        self.column_widget.addItems(self.get_clean_columns())

    def ok_clicked(self, current_tab_index, old_sep, new_sep, other_char, is_reserved, is_new):
        """

        :param current_tab_index: 0是方式1，1是方式2
        :param old_sep: 方式1，旧的分隔符
        :param new_sep: 方式2，新的分隔符
        :param other_char: 方式2，字符
        :param is_reserved: 方式2，True表示保留，False表示舍弃
        :param is_new: False表示替换当前列，True表示添加新列
        :return:
        """
        names = [line.text() for line in self.column_widget.selectedItems()]

        if len(names) == 0:
            ssignal.error.emit('请选择列')
            return

        df = self.get_df()
        ssignal.push_cache.emit(Actions.replace_value.cn,self.get_df())

        self.cleanReplaceValueThread = CleanReplaceValueThread(df, names, current_tab_index, old_sep, new_sep,
                                                               other_char, is_reserved, is_new)
        self.cleanReplaceValueThread.start()
        self.close()

    def get_clean_columns(self):
        return self.parent.get_df_columns()

    def get_df(self):
        return self.parent.get_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
