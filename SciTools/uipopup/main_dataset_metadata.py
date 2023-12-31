from PySide2 import QtWidgets
from PySide2.QtWidgets import QDialog

from core.runner import CleanMetadataThread
from core.toolkit import TableKit, FrameKit, PandasTableModel
from uipopup.uipy import ui_dataset_metadata


class PopupCleanMetadata(QDialog, ui_dataset_metadata.Ui_Form):

    def __init__(self, parent):
        super(PopupCleanMetadata, self).__init__(parent)
        self.setupUi(self)
        self.context = parent.context

        self.tableView.horizontalHeader().setStyleSheet(f"QHeaderView::section{{background:#abfaa6;}}");
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # 数据统计
        df = self.get_dataset()
        self.cleanMetadataThread = CleanMetadataThread(df)
        self.cleanMetadataThread.dataset.connect(self.fill_table_stat)
        self.cleanMetadataThread.start()

    def fill_table_stat(self, stat_df, pairs):
        # 填充表格
        self.tableView.setModel(PandasTableModel(stat_df))


        ###############################################################################

        for col_name, vlist in pairs.items():
            table1 = QtWidgets.QTableView()
            table1.setModel(PandasTableModel(vlist[0]))
            table1.verticalHeader().hide()
            table1.horizontalHeader().setStyleSheet(f"QHeaderView::section{{background:#abfaa6;}}");
            table1.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)


            table2 = QtWidgets.QTableView()
            table2.setModel(PandasTableModel(vlist[1]))
            table2.verticalHeader().hide()
            table2.horizontalHeader().setStyleSheet(f"QHeaderView::section{{background:#abfaa6;}}");
            table2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)


            widget = FrameKit()
            widget.add_widgets(table1, table2)
            self.tabWidget.addTab(widget.show(), col_name)

    def get_dataset(self):
        return self.context.get_df()
