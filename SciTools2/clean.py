from collections import Counter

import pandas as pd
from PySide2.QtWidgets import QFrame, QLabel, QTabWidget

from helper import Cfg
from toolkit import VBoxKit, OKButtonKit, FrameKit, TableKit


class PopupMetadata(QFrame):
    """
    元数据，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(700, 600)
        main_layout = VBoxKit(self)

        main_layout.addWidget(QLabel('数据统计'))
        table_stat = TableKit()
        main_layout.addWidget(table_stat)

        main_layout.addWidget(QLabel('数据分布'))
        tab_freq = QTabWidget()
        main_layout.addWidget(tab_freq)

        btn_ok = OKButtonKit('OK', self.action_ok)
        main_layout.addWidget(btn_ok)

        self.init_table_stat(table_stat)
        self.init_table_freq(tab_freq)

    def init_table_stat(self, table_stat):
        df = self.get_dataset()
        # 判断nulls必须放在这里，不能放到下面
        nulls = (df.isna().sum() + df.eq('').sum())
        df = df.describe()
        # 丢掉行
        df.drop('top', axis=0, inplace=True)
        # 空值情况
        df.loc['nulls'] = nulls
        # 重命名索引
        df.rename(index={'count': '总数', 'unique': '唯一', 'freq': '众频', 'nulls': '空值'}, inplace=True)
        # 填充表格
        table_stat.init_dataset(df)

    def init_table_freq(self, tab_freq):
        df = self.get_dataset()

        columns = df.columns.tolist()
        for i, name in enumerate(columns):
            tab_freq.addTab(self.__create_tab_widget(df.loc[:, name].tolist()), name)

    def action_ok(self):
        self.close()

    def get_dataset(self):
        return self.parent.tableKit.get_dataset()

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


