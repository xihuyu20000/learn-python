import os
from typing import List
from diskcache import Cache
import shutil
import pandas
import pandas as pd
from PySide2 import QtCore, QtWidgets
from PySide2 import QtGui
from PySide2.QtCore import Qt, Signal, QModelIndex, QTimer
from PySide2.QtGui import QBrush, QColor
from PySide2.QtWidgets import (
    QFrame,
    QPushButton,
    QListWidget,
    QAbstractItemView,
    QTableView,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QWidget,
    QLCDNumber,
)
from log import logger
from mhelper import ssignal


class InfoKit(QWidget):
    def __init__(
            self,
    ):
        super().__init__()
        self.resize(300, 200)

        # 隐藏标题栏
        self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint)
        #
        self.setWindowTitle("消息")
        # 设置边框样式
        self.setStyleSheet("QWidget { background-color: #cbeae7; }")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.elapsed_time = 0

        vbox = VBoxKit(self)
        vbox.setContentsMargins(20, 20, 20, 20)

        self.lcd_number = QLCDNumber(self)
        self.lcd_number.display(0)

        # 设置QLCDNumber的样式表
        style_sheet = """
            QLCDNumber {
                background-color: white;
                color: blue;
                border: 2px solid gray;
                border-radius: 10px;
                padding:20px;
            }
        """
        self.lcd_number.setStyleSheet(style_sheet)
        vbox.addWidget(self.lcd_number)

        self.label_msg = QLabel()
        self.label_msg.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.label_msg.setStyleSheet(
            "text-align: center; color: red;font-weight: bold; font-size: 18px;"
        )
        vbox.addWidget(self.label_msg)

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setPointSize(20)
        font.setWeight(QtGui.QFont.Weight.Bold)

        self.ok_button = OKButtonKit("关闭", callback=self.action_ok)
        self.ok_button.setFont(font)
        vbox.addWidget(self.ok_button)

    def msg(self, msg="运行中,请稍等", start=False, stop=False):
        self.label_msg.setText(msg)

        if start:
            self.reset_timer()
            if not self.timer.isActive():
                self.timer.start(1)  # 启动定时器，每秒触发一次

        if stop:
            self.stop_timer()

    def update_time(self):
        self.elapsed_time += 1
        milliseconds = self.elapsed_time % 1000
        seconds = (self.elapsed_time // 1000) % 60
        minutes = (self.elapsed_time // 60000) % 60
        hours = self.elapsed_time // 3600000
        time_str = "{:02}:{:02}:{:02}:{:03}".format(
            hours, minutes, seconds, milliseconds
        )
        self.lcd_number.display(time_str)

    def stop_timer(self):
        self.timer.stop()
        self.elapsed_time = 0

    def reset_timer(self):
        if self.timer.isActive():
            self.timer.stop()
        self.elapsed_time = 0
        self.lcd_number.display("00:00:000")

    def action_ok(self):
        self.close()


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
    def __init__(self, text, fix_width=None, callback=None):
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
        self.setStyleSheet(
            "color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);"
        )
        self.clicked.connect(callback)


class FrameKit(QtWidgets.QFrame):
    """
    水平容器
    """

    def __init__(self, vertical=False):
        super().__init__()
        self.frame = QtWidgets.QFrame()

        self.main_layout = (
            QVBoxLayout(self.frame) if vertical else QHBoxLayout(self.frame)
        )
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

    def add_widgets(self, *widgets):
        for w in widgets:
            self.main_layout.addWidget(w)
        return self.frame

    def show(self):
        return self.frame


class PandasTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=pd.DataFrame()):
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
        if role in (Qt.DisplayRole, Qt.EditRole):
            value = self._data.iloc[index.row(), index.column()]

            return str(value)
        elif role == Qt.BackgroundRole:
            i = "{0}_{1}".format(index.row(), index.column())
            return self._backgrounds[i] if i in self._backgrounds else ""

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
            sort_order = True if order == Qt.AscendingOrder else False
            self._data = self._data.sort_values(
                self._data.columns[column], ascending=sort_order
            )
            self.layoutChanged.emit()

    def removeRow(self, row, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        self._data = self._data.drop(self._data.index[row])
        self.endRemoveRows()

    def pub_remove_rows_reserve_index(self, indexes):
        for i in indexes:
            self.removeRow(i)

    def pub_set_dataset(self, df, inplace_index=True, drop_index=True):
        self.beginResetModel()
        self._data = df
        self._data._reset_index(inplace=inplace_index, drop=drop_index)
        self.endResetModel()

    def pub_get_dataset(self):
        return self._data.copy()

    def pub_has_dataset(self):
        return len(self._data) > 0

    def pub_set_user_header(self, data):
        self._user_headers = data

    def pub_set_item_writable(self, writable: bool):
        self._cell_writable = writable

    def pub_set_bgcolor(self, i: int, j: int, color: str):
        index = self.index(i, j)
        i = "{0}_{1}".format(i, j)
        self._backgrounds[i] = QBrush(QColor(color))
        self.dataChanged.emit(index, index)


class ListKit(QFrame):
    """
    封装所有的列表操作
    """

    signal_load = Signal(int)

    def __init__(self, single_selection: bool = False):
        super().__init__()
        self._layout = QtWidgets.QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
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
            self.setSelectionMode(
                QAbstractItemView.SingleSelection
                if single
                else QAbstractItemView.ExtendedSelection
            )

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


class TableKit(QFrame):
    """
    封装所有的表格操作
    """

    signal_info = Signal(str)

    def __init__(
            self,
            parent=None,
            single_select=False,
            column_sortable=False,
            header_horizontal_movable=False,
            vertical_header_hide=False,
            horizontal_header_color="#abfaa6",
    ):
        super(TableKit, self).__init__(parent)
        self._layout = QtWidgets.QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._table = TableKit.InnerTable()

        self._layout.addWidget(self._table)
        self._model = TableKit.InnerModel(pd.DataFrame(columns=[], index=[], data=[]))
        self._table.setModel(self._model)

        self.__init_table(
            single_select,
            column_sortable,
            header_horizontal_movable,
            vertical_header_hide,
            horizontal_header_color,
        )

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

    def remove_rows_reserve_index(self, indexes: List[int]):
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

    def set_dataset(self, df: pd.DataFrame, inplace_index=True, drop_index=True):
        if not isinstance(df.index, pandas.RangeIndex):
            inplace_index = False
            drop_index = False
        # 1、更新模型
        self._model.pub_update_dataset(
            df, inplace_index=inplace_index, drop_index=drop_index
        )
        # 2、更新表格视图
        self._table.reset()

    def set_bgcolor(self, i, j, color):
        self._model.pub_set_bgcolor(i, j, color)

    def set_user_header(self, data):
        self._model.pub_set_user_header(data)

    def set_item_writable(self, writable=False):
        self._model.pub_set_item_writable(writable)

    def __init_table(
            self,
            single_select,
            column_sortable,
            header_movable,
            vertical_header_hide,
            horizontal_header_color,
    ):
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
        self._table.horizontalHeader().setStyleSheet(
            f"QHeaderView::section{{background:{horizontal_header_color};}}"
        )

    class InnerModel(QtCore.QAbstractTableModel):
        def __init__(self, data=None):
            super().__init__()
            # self._user_headers = dict()
            self._data = data
            # 存储背景颜色，key是i_j
            self._backgrounds = {}
            # 是否允许修改
            self._cell_writable = False

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

        def data(self, index, role):
            """
            获取单元格中的数据
            """
            if role in (Qt.DisplayRole, Qt.EditRole):
                try:
                    value = self._data.iloc[index.row(), index.column()]
                    return str(value)
                except IndexError:
                    return ""
            elif role == Qt.BackgroundRole:
                i = "{0}_{1}".format(index.row(), index.column())
                return self._backgrounds[i] if i in self._backgrounds else ""

        def headerData(self, section, orientation, role):
            """
            设置行标题和列标题
            """
            if role == Qt.DisplayRole:
                if orientation == Qt.Horizontal:
                    try:
                        label = str(self._data.columns[section])
                        return label
                    except (IndexError,):
                        return None

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
                sort_order = True if order == Qt.AscendingOrder else False
                self._data = self._data.sort_values(
                    self._data.columns[column], ascending=sort_order
                )
                self.layoutChanged.emit()

        def removeRow(self, row, parent=QModelIndex()):
            self.beginRemoveRows(parent, row, row)
            self._data = self._data.drop(self._data.index[row])
            self.endRemoveRows()

        def pub_remove_rows_reserve_index(self, indexes):
            for i in indexes:
                self.removeRow(i)

        def pub_update_dataset(self, df: pd.DataFrame, inplace_index, drop_index):
            self.beginResetModel()
            self._data = df.copy()
            self._data.reset_index(inplace=inplace_index, drop=drop_index)
            self.endResetModel()

        def pub_get_dataset(self):
            return self._data.copy()

        def pub_has_dataset(self):
            return len(self._data) > 0

        def pub_set_user_header(self, data):
            self._user_headers = data

        def pub_set_item_writable(self, writable: bool):
            self._cell_writable = writable

        def pub_set_bgcolor(self, i: int, j: int, color: str):
            index = self.index(i, j)
            i = "{0}_{1}".format(i, j)
            self._backgrounds[i] = QBrush(QColor(color))
            self.dataChanged.emit(index, index)

    class InnerTable(QTableView):
        def __init__(self):
            super().__init__()
            # 不可编辑
            self.setEditTriggers(QAbstractItemView.NoEditTriggers)
            # 选中
            self.setSelectionBehavior(QAbstractItemView.SelectItems)

        def pub_selected_indexes(self):
            return [(index.row(), index.column()) for index in self.selectedIndexes()]

        def pub_selectedItems(self):
            return self.selectedItems()

        def sortByColumn(self, column, order):
            print("视图排序")


class PandasStack:
    cache_dir = os.path.join(os.path.expanduser("~"), ".clean-cache")

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.cache = Cache(PandasStack.cache_dir)
        self.index = 0
        self.highest = 0
        self.current = None

        ssignal.reset_cache.connect(self.reset_cache)
        ssignal.push_cache.connect(self.push_cache)

        self.reset_cache()

    def reset_cache(self, *args):
        """
        当加载新的数据文件时，或者保存之后，就需要重置
        :return:
        """
        self.cache.clear()
        self.index = 0
        self.highest = 0
        self.current = None
        try:
            shutil.rmtree(PandasStack.cache_dir)
        except OSError:  # Windows wonkiness
            pass

    def push_cache(self, df):
        """
        如果是多次undo后push的流程如下：
        假设原始数据是[1,2,3,4] undo三次后，当前是[1]；再次push，结果是[1,2]

        :param df:
        :return:
        """
        self.current = df
        self.index += 1
        self.cache.set(self.index, df)
        for i in range(self.index + 1, self.highest + 1):
            del self.cache[i]
        self.highest = self.index

        self.show()

    def undo(self) -> pd.DataFrame:
        val = None
        if self.index > 1:
            self.index -= 1
            self.current = self.cache.get(self.index)
            val = self.current

        self.show()
        return val

    def redo(self) -> pd.DataFrame:
        """
        redo会影响当前的index，从而index+1;但是不会影响highest的值
        :return:
        """
        val = None
        if self.index < self.highest:
            self.index += 1
            self.current = self.cache.get(self.index)
            val = self.current
        self.show()
        return val

    def show(self):
        logger.debug(
            "当前位置{}  最高水位线{}  缓存内容{}",
            f"{self.index}",
            f"{self.highest}",
            str([i for i in self.cache.iterkeys()]),
        )
