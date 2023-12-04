import sys
import time
from collections import defaultdict
from typing import List, Dict

import numpy as np
import pandas as pd
from PySide6 import QtCore, QtWidgets
from PySide6 import QtGui
from PySide6.QtCore import Qt, Signal, QModelIndex
from PySide6.QtGui import QAction, QBrush, QColor
from PySide6.QtWidgets import QFrame, QPushButton, QMenu, \
    QListWidget, \
    QAbstractItemView, QTableView, QHBoxLayout, QVBoxLayout, QLabel, QWidget
from loguru import logger

class VBoxKit(QVBoxLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

class HBoxKit(QHBoxLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

class PushButtonKit(QPushButton):
    def __init__(self, text, fix_width = None, callback=None):
        super().__init__()
        self.setText(text)
        if fix_width is not None:
            self.setFixedWidth(fix_width)
        if callback is not None:
            self.clicked.connect(callback)
class OKButtonKit(QPushButton):
    def __init__(self, text, callback=None):
        super().__init__()
        self.setText(text)
        self.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        self.clicked.connect(callback)
class FrameKit(QtWidgets.QFrame):
    """
    水平容器
    """
    def __init__(self, vertical=False ):
        super().__init__()
        self.frame = QtWidgets.QFrame()

        self.main_layout = QVBoxLayout(self.frame) if vertical else QHBoxLayout(self.frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

    def add_widgets(self, *widgets):
        for w in widgets:
            self.main_layout.addWidget(w)
        return self.frame

    def show(self):
        return self.frame


class TableKit(QFrame):
    """
    封装所有的表格操作
    """
    signal_info = Signal(str)

    def __init__(self, parent=None, single_select=False, column_sortable=False, header_horizontal_movable=False, vertical_header_hide=False, horizontal_header_color='#abfaa6'):
        super(TableKit, self).__init__(parent)
        self._layout = QtWidgets.QVBoxLayout(self)
        self._table = TableKit.InnerTable()

        self._layout.addWidget(self._table)
        self._model = TableKit.InnerModel(pd.DataFrame(columns=[], index=[], data=[]))
        self._table.setModel(self._model)

        self.__init_table(single_select, column_sortable, header_horizontal_movable, vertical_header_hide, horizontal_header_color)

    def has_dataset(self):
        return self._model.pub_has_dataset()

    def get_dataset(self):
        """
        获取数据的copy
        """
        df = self._model.pub_get_dataset()
        return df

    def remove_rows(self, rows: List[int]):
        """
        删除多行
        """
        if rows is not None and len(rows) > 0:
            ds = self.get_dataset()
            ds.drop(index=ds.index[rows], inplace=True)
            self.set_dataset(ds)

    def remove_rows_reserve_index(self, indexes:List[int]):
        """
        删除行，但是不改变索引
        """
        self._model.pub_remove_rows_reserve_index(indexes)

    def remove_columns(self, columns: List[int]):
        """
        删除多列
        """
        if columns is not None and len(columns) > 0:
            ds = self.get_dataset()
            ds.drop(columns=ds.columns[columns], inplace=True)
            self.set_dataset(ds)

    def remove_selected_columns(self):
        """
        删除选中列
        """
        col_indexes = [index[1] for index in self._table.pub_selected_indexes()]
        self.remove_columns(col_indexes)

    def remove_selected_rows(self):
        """
        删除选中行
        """
        row_indexes = [index[0] for index in self._table.pub_selected_indexes()]
        self.remove_rows(row_indexes)


    def get_selected_rows(self):
        return [index[0] for index in self._table.pub_selected_indexes()]

    def set_dataset(self, df, inplace_index=True, drop_index=True):
        # 1、更新模型
        self._model.pub_update_dataset(df, inplace_index=inplace_index, drop_index=drop_index)
        # 2、更新表格视图
        self._table.reset()


    def set_bgcolor(self, i, j, color):
        self._model.pub_set_bgcolor(i, j, color)
    def set_user_header(self, data):
        self._model.pub_set_user_header(data)

    def set_item_writable(self,writable=False):
        self._model.pub_set_item_writable(writable)
    def init_dataset(self, df):
        # 1、更新模型
        self._model.pub_update_dataset(df, inplace_index=False, drop_index=False)
        # 2、更新表格视图
        self._table.reset()


    def __init_table(self, single_select, column_sortable, header_movable, vertical_header_hide, horizontal_header_color):
        """
        设置表参数
        """
        if single_select:
            self._table.setSelectionMode(QAbstractItemView.SingleSelection)
            self._table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self._table.setSortingEnabled(column_sortable)
        self._table.horizontalHeader().setSectionsMovable(header_movable)
        if vertical_header_hide:
            self._table.verticalHeader().hide()
        self._table.horizontalHeader().setStyleSheet(f"QHeaderView::section{{background:{horizontal_header_color};}}");
    class InnerModel(QtCore.QAbstractTableModel):

        def __init__(self, data=None):
            super().__init__()
            self._user_headers = dict()
            self._data = data
            # 存储背景颜色，key是i_j
            self._backgrounds = {}
            # 是否允许修改
            self._cell_writable = False

        def data(self, index, role):
            """
            获取单元格中的数据
            """
            if role in (Qt.DisplayRole , Qt.EditRole):
                value = self._data.iloc[index.row(), index.column()]

                return str(value)
            elif role == Qt.BackgroundRole:
                i = '{0}_{1}'.format(index.row(), index.column())
                return self._backgrounds[i] if i in self._backgrounds else ''

        def rowCount(self, index):
            """
            获取总行数
            """
            return self._data.shape[0]

        def columnCount(self, index):
            """
            获取总列数
            """
            return self._data.shape[1]

        def headerData(self, section, orientation, role):
            """
            设置行标题和列标题
            """

            if role == Qt.DisplayRole:
                if orientation == Qt.Horizontal:
                    key = str(self._data.columns[section])
                    return self._user_headers[key] if key in self._user_headers else key

                if orientation == Qt.Vertical:
                    return str(self._data.index[section])

        def flags(self, index):
            # 设置单元格的标志，允许编辑
            if self._cell_writable:
                return Qt.ItemIsEnabled | Qt.ItemIsEditable
            else:
                return Qt.ItemIsEnabled | Qt.ItemIsSelectable

        def setData(self, index, value, role=Qt.EditRole):
            if index.isValid() and role == Qt.EditRole:
                # 在这里保存修改后的数据
                self._data.iloc[index.row(), index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            return False

        def sort(self, column, order):
            if not self._data.empty:
                if order == Qt.AscendingOrder:
                    self._data = self._data.sort_values(self._data.columns[column], ascending=True)
                else:
                    self._data = self._data.sort_values(self._data.columns[column], ascending=False)

                self.layoutChanged.emit()

        def removeRow(self, row, parent=QModelIndex()):
            self.beginRemoveRows(parent, row, row)
            self._data = self._data.drop(self._data.index[row])
            self.endRemoveRows()

        def pub_remove_rows_reserve_index(self, indexes):
            for i in indexes:
                self.removeRow(i)


        def pub_update_dataset(self, df, inplace_index, drop_index):
            self.beginResetModel()
            self._data = df
            self._data.reset_index(inplace=inplace_index, drop= drop_index)
            self.endResetModel()

        def pub_get_dataset(self):
            return self._data.copy()

        def pub_has_dataset(self):
            return len(self._data)>0

        def pub_set_user_header(self, data):
            self._user_headers = data

        def pub_set_item_writable(self, writable:bool):
            self._cell_writable = writable


        def pub_set_bgcolor(self, i:int, j:int, color:str):
            index = self.index(i, j)
            i = '{0}_{1}'.format(i, j)
            self._backgrounds[i] = QBrush(QColor(color))
            self.dataChanged.emit(index, index)
    class InnerTable(QTableView):
        def __init__(self):
            super().__init__()

        def pub_selected_indexes(self):
            return [(index.row(), index.column()) for index in self.selectedIndexes()]

        def pub_selectedItems(self):
            return self.selectedItems()


        def sortByColumn(self, column, order):
            print('视图排序')

class ListKit(QFrame):
    """
    封装所有的列表操作
    """
    signal_load = Signal(int)

    def __init__(self, single_selection: bool = False):
        super().__init__()
        self._layout = QtWidgets.QVBoxLayout(self)
        self.inner_list = ListKit.InnerListWidget()
        self._layout.addWidget(self.inner_list)

        self.inner_list.selection_style(single_selection)

    def set_dataset(self, ds, init_choose=0):
        """
        填充数据
        """
        self.inner_list.set_dataset(ds, init_choose)
        self.signal_load.emit(len(ds))

    def selected_indexes(self):
        return self.inner_list.selected_indexes()

    def selected_names(self):
        return self.inner_list.selected_textes()

    class InnerListWidget(QListWidget):
        def __init__(self):
            super().__init__()

        def selection_style(self, single: bool):
            self.setSelectionMode(QAbstractItemView.SingleSelection if single else QAbstractItemView.ExtendedSelection)

        def set_dataset(self, ds, init_choose):
            self.clear()
            self.addItems(ds)
            self.setCurrentRow(init_choose)

        def selected_textes(self):
            names = [name.text() for name in self.selectedItems()]
            return names

        def selected_indexes(self):
            indexes = [index.row() for index in self.selectedIndexes()]
            return indexes

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        main_frame = QtWidgets.QFrame()
        self.setCentralWidget(main_frame)

        vlayout = QtWidgets.QVBoxLayout(main_frame)

        toolbar = QtWidgets.QFrame()
        vlayout.addWidget(toolbar)
        hlayout = QtWidgets.QHBoxLayout(toolbar)

        act1 = QPushButton("加载数据")
        act1.clicked.connect(self.load_data)
        act2 = QPushButton("删除行")
        act2.clicked.connect(self.remove_rows)
        hlayout.addWidget(act1)
        hlayout.addWidget(act2)

        self.table = TableKit(column_sortable=True, header_horizontal_movable=True)
        vlayout.addWidget(self.table)


    def load_data(self):
        self.data = pd.DataFrame(np.random.randint(0, 10000, size=(50000, 300)),
                                 columns=[f'col-{i}' for i in range(1, 301)])
        self.table.set_dataset(self.data)

    def remove_rows(self):
        ds = self.table.get_dataset()
        t1 = time.time()
        self.table.remove_rows([0, 1, 2, 3, 5])
        t2 = time.time()
        print('pandas删除耗时', (t2 - t1))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # mylist = ListKit()
    # mylist.set_dataset(['a', 'b', 'c', 'd', 'e'])
    # mylist.show()
    # win = MainWindow()
    # win.show()

    frame = FrameKit()
    frame.add_widgets(QLabel("aaaaaaaaa"), QPushButton("bbbbbbbbb")).show()

    app.exec()
