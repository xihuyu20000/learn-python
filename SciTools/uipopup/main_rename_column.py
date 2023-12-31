import time

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QTableWidgetItem

from core.const import ssignal, Actions
from core.log import logger
from uipopup.uipy import ui_rename_column


class PopupCleanRename(QDialog, ui_rename_column.Ui_Form):

    def __init__(self, parent=None):
        super(PopupCleanRename, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.init_table()

        self.pushButton.clicked.connect(self.ok_clicked)

    def init_table(self):
        columns = self.get_clean_columns()

        self.tableWidget.setRowCount(len(columns))
        for i, col_name in enumerate(columns):
            item1 = QTableWidgetItem(str(col_name))
            item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item1.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.tableWidget.setItem(i, 0, item1)

            item2 = QTableWidgetItem('')
            item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item2.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable)
            self.tableWidget.setItem(i, 1, item2)

    def ok_clicked(self):
        logger.info('清洗，重命名')

        t1 = time.time()
        df = self.get_df()

        name_pairs = {}
        for i in range(self.tableWidget.rowCount()):
            new_value = self.tableWidget.item(i, 1).text().strip()
            if len(new_value) > 0:
                old_value = self.tableWidget.item(i, 0).text()
                name_pairs[old_value] = new_value

        # 重命名
        for old_name, new_name in name_pairs.items():
            df.rename(columns={old_name: new_name}, inplace=True)

        self.set_df(df)
        t2 = time.time()

        msg = '重命名列，耗时{0}秒'.format(round(t2 - t1, 2))
        ssignal.info.emit(msg)

        ssignal.push_cache.emit(Actions.rename_cols.cn, self.get_df())

        self.close()

    def get_clean_columns(self):
        return self.parent.get_df_columns()

    def get_df(self):
        return self.parent.get_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
