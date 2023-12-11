import time

from PySide2.QtWidgets import QDialog
from log import logger
from helper import ssignal, Utils, Cfg
from popup.clean.uipy import ui_replace_column


class PopupReplaceColumn(QDialog, ui_replace_column.Ui_Form):

    def __init__(self, parent=None):
        super(PopupReplaceColumn, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.init_data()

        self.ok_button.clicked.connect(lambda: self.ok_clicked(self.tabwidget.currentIndex(), self.old_lineEdit.text(), self.new_lineEdit.text(), self.rbt1.isChecked(),
                               self.other_linedit.text(), self.rbt00.isChecked()))

    def init_data(self):
        self.column_widget.addItems(self.get_clean_columns())

    def ok_clicked(self, current_tab_index, old_sep, new_sep, is_new, other_char, is_reserved):
        names = [line.text() for line in self.column_widget.selectedItems()]

        if len(names) == 0:
            return

        df = self.get_df()

        new_names = []
        t1 = time.time()
        for col in names:
            new_col = col + '-new' if is_new else col
            if is_new:
                new_names.append(new_col)

            if current_tab_index == 0:
                df[new_col] = df[col].astype(str).str.replace(old_sep, new_sep).fillna(df[col])
            if current_tab_index == 1:
                if is_reserved:
                    # 只保留该字符
                    df[new_col] = df[col].apply(lambda x: self.__reserve_chars(other_char, x))
                else:
                    # 删除该字符
                    df[new_col] = df[col].astype(str).str.replace(other_char, '').fillna(df[col])

        # 下面的new_names一定要倒序
        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, sorted(new_names, reverse=True))
        df = df[old_names]
        self.set_df(df)
        t2 = time.time()

        error1 = '原值含有中文或中文字符\r\n' if Utils.has_Chinese_or_punctuation(old_sep) else ''
        error2 = error1 + '新值含有中文或中文字符\r\n' if Utils.has_Chinese_or_punctuation(new_sep) else ''
        msg = error2 + '替换{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(names), round(t2 - t1, 2))
        if error1 or error2:
            ssignal.error.send(msg)
        else:
            ssignal.info.send(msg)
            self.close()



    def __reserve_chars(self, other_char, line: str):
        rr = []
        for word in line.split(Cfg.seperator):
            if other_char in word:
                rr.append(other_char)
            else:
                rr.append(word)
        return Cfg.seperator.join(rr)

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)