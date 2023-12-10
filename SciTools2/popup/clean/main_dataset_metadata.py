from collections import Counter

import pandas as pd
from PySide2.QtWidgets import QDialog

from popup.clean.uipy import ui_dataset_metadata
from helper import Cfg, MySignal
from runner import CleanMetadataThread
from toolkit import PandasTableModel, TableKit, FrameKit


class WidCleanMetadata(QDialog, ui_dataset_metadata.Ui_Form):

    def __init__(self, parent=None):
        super(WidCleanMetadata, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent



        MySignal.info.send('开始计算元数据信息')

        # 数据统计
        df = self.get_dataset()
        self.cleanMetadataThread = CleanMetadataThread(df)
        CleanMetadataThread.clean_metadata.connect(self.fill_tableView)
        self.cleanMetadataThread.start()
        # 数据分布
        self.init_table_freq()
        MySignal.info.send('计算元数据信息成功')

    def fill_tableView(self, df):
        # 填充表格
        self.tableView.setModel(PandasTableModel(df))

    ###############################################################################

    def init_table_freq(self):
        df = self.get_dataset()

        columns = df.columns.tolist()
        for i, name in enumerate(columns):
            self.tabWidget.addTab(self.__create_tab_widget(df.loc[:, name].tolist()), name)


    def __create_tab_widget(self, datalist):
        datalist = sum([str(row).split(Cfg.seperator) for row in datalist], [])
        datalist = Counter(datalist)
        datalist = sorted(datalist.items(), key=lambda x: x[1], reverse=True)
        df = pd.DataFrame(datalist, columns=['词语', '频次'])
        table1 = TableKit(vertical_header_hide=True)
        table1.init_dataset(df)

        ########################################################################
        # 统计频次的出现次数
        datalist = [item[1] for item in datalist]
        datalist = Counter(datalist)
        datalist = sorted(datalist.items(), key=lambda x: x[1], reverse=True)
        df2 = pd.DataFrame(datalist, columns=['词语频次', '次数'])
        table2 = TableKit(vertical_header_hide=True)
        table2.init_dataset(df2)

        widget = FrameKit()
        return widget.add_widgets(table1, table2)

    def get_dataset(self):
        return self.parent.master_get_clean_df()
