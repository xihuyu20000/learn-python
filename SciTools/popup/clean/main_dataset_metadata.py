
from PySide2.QtWidgets import QDialog


from popup.clean.uipy import ui_dataset_metadata

from mrunner import CleanMetadataThread
from mtoolkit import PandasTableModel, TableKit, FrameKit


class PopupCleanMetadata(QDialog, ui_dataset_metadata.Ui_Form):

    def __init__(self, parent=None):
        super(PopupCleanMetadata, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.tableView.horizontalHeader().setStyleSheet(f"QHeaderView::section{{background:#abfaa6;}}");
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
            table1 = TableKit(vertical_header_hide=True)
            table1.set_dataset(vlist[0])

            table2 = TableKit(vertical_header_hide=True)
            table2.set_dataset(vlist[1])

            widget = FrameKit()
            widget.add_widgets(table1, table2)
            self.tabWidget.addTab(widget.show(), col_name)

    def get_dataset(self):
        return self.parent.master_get_clean_df()
