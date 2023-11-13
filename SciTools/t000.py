"""

"""
import sys
from functools import partial

import pandas as pd
from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem, QScrollBar, QHBoxLayout, QMenu
from pandas import DataFrame, isnull

from core.parse_data import cnki_refworks

## 参考  https://blog.csdn.net/weixin_44247218/article/details/115213652
"""
python表格，表头有右键菜单
"""


class DataTable(QWidget):
    rowCount = 0  # 单页可以显示的数据条数
    df = DataFrame()

    def __init__(self, *args):
        super(DataTable, self).__init__()
        self.ui_setup()
        self.signal_setup()

    def ui_setup(self):
        # self.setGeometry(100, 200, 800, 600)
        # 使用竖直Layout
        self.horizontalLayout = QHBoxLayout(self)
        # 建立一个QTableWidget
        self.table: QTableWidget = QTableWidget(self)
        self.table.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.horizontalHeader().customContextMenuRequested.connect(self.showContextMenu)
        # self.table.verticalHeader().setStretchLastSection(True)

        # 建立一个竖直QScrollBar
        self.scrollbar = QScrollBar(self)
        self.scrollbar.setOrientation(Qt.Vertical)
        self.scrollbar.setSingleStep(1)

        self.horizontalLayout.addWidget(self.table)
        self.horizontalLayout.addWidget(self.scrollbar)

    def showContextMenu(self, pos):

        contextMenu = QMenu(self)
        actionA = contextMenu.addAction(u'添加')
        actionB = contextMenu.addAction(u'删除')
        actionA.triggered.connect(partial(self.cmHandler, 'a'))
        actionB.triggered.connect(partial(self.cmHandler, 'b'))
        # 菜单显示前，将它移动到鼠标点击的位置
        contextMenu.move(QtGui.QCursor().pos())
        contextMenu.show()

    def cmHandler(self, ll):
        print(self, ll)

    def signal_setup(self):
        self.scrollbar.valueChanged.connect(self.scrollbar_emit)

    def scrollbar_emit(self, e: int):
        self.pdToQTableWidget()

    def setDfData(self, df: DataFrame):
        self.df = df
        # 先计算 后预览
        self.calculateRowCountParams()
        self.pdToQTableWidget()

    def calculateRowCountParams(self):
        if any(self.df):
            # 先计算
            rowHeight = self.table.rowHeight(0)
            rowHeight = 30 if rowHeight == 0 else rowHeight
            tableHeight = self.table.height()
            self.rowCount = int(tableHeight / rowHeight) - 1
            # print("每页行数", self.rowCount, sep=":")
            # 更新table的行数
            self.table.setRowCount(self.rowCount)

            # 滑块的长度
            scrollbar_count = int(self.df.index.size / self.rowCount)
            # print("滑块长度", scrollbar_count, sep=":")
            self.scrollbar.setMaximum(scrollbar_count * 9)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.calculateRowCountParams()
        self.pdToQTableWidget()
        if a0:
            super().resizeEvent(a0)

    def pdToQTableWidget(self):
        """
        更新页面数据
        :return:
        """
        if any(self.df):
            df_columns = self.df.columns.size
            df_header = self.df.columns.values.tolist()
            self.table.setColumnCount(df_columns)
            self.table.setHorizontalHeaderLabels(df_header)

            start_row = int(self.scrollbar.value() / 9 * self.rowCount)
            end_row = int((self.scrollbar.value() / 9 + 1) * self.rowCount)
            # 数据预览窗口
            for row in range(start_row, end_row):
                for column in range(df_columns):
                    value = ''
                    if row < self.df.index.size:
                        value = '' if isnull(self.df.iloc[row, column]) else str(self.df.iloc[row, column])
                    tempItem = QTableWidgetItem(value)
                    self.table.setItem((row - start_row), column, tempItem)
                    self.table.item((row - start_row), column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


if __name__ == '__main__':
    te_data = cnki_refworks.parse_file('files/CNKI-refworks2.txt')
    # 转为dict类型
    te_data = [model.to_dict() for model in te_data]
    df = pd.DataFrame(te_data)

    app = QApplication(sys.argv)
    table = DataTable()
    table.show()
    table.setDfData(df)
    sys.exit(app.exec())
