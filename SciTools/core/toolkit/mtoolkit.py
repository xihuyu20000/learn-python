from typing import List

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
    QLCDNumber, QScrollArea, QToolButton, QItemDelegate, QLineEdit, )

from core.log import logger


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
            column_sortable=True,
            header_horizontal_movable=True,
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

    def get_selected_row_indexes(self):
        return [index[0] for index in self._table.pub_selected_indexes()]

    def get_selected_col_indexes(self):
        return [index[1] for index in self._table.pub_selected_indexes()]

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
        logger.debug('刷新数据模型和视图')
        logger.debug(df.columns)

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
            self._cell_writable = True

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
            self.setEditTriggers(QTableView.DoubleClicked)
            self.setItemDelegate(TableKit.EditDelegate())

            # 选中
            self.setSelectionBehavior(QAbstractItemView.SelectItems)

        def pub_selected_indexes(self):
            return [(index.row(), index.column()) for index in self.selectedIndexes()]

        def pub_selectedItems(self):
            return self.selectedItems()

        def sortByColumn(self, column, order):
            print("视图排序")

    class EditDelegate(QItemDelegate):
        def __init__(self, parent=None):
            super().__init__(parent)

        def createEditor(self, parent, option, index):
            editor = QLineEdit(parent)
            return editor

        def setEditorData(self, editor, index):
            value = index.model().data(index, Qt.DisplayRole)
            editor.setText(str(value))

        def setModelData(self, editor, model, index):
            value = editor.text()
            model.setData(index, value, Qt.EditRole)

        def updateEditorGeometry(self, editor, option, index):
            editor.setGeometry(option.rect)


class ScrollWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(ScrollWidget, self).__init__(parent)

        # 创建一个 QWidget 作为外部容器
        container = QWidget(self)

        # 创建一个 QVBoxLayout 作为外部容器的布局管理器
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        # 设置外部容器的布局管理器
        container.setLayout(container_layout)

        # 创建一个 QScrollArea
        scroll_area = QScrollArea(container)
        # 隐藏垂直滚动条
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)

        # 创建一个 QWidget 作为 QScrollArea 的内部容器
        scroll_content = QWidget(scroll_area)

        # 在 QScrollArea 内的 QWidget 上设置布局管理器，这里用 QVBoxLayout 作为示例
        self.scroll_layout = QHBoxLayout(scroll_content)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(0)

        # 设置内部容器的布局管理器
        scroll_content.setLayout(self.scroll_layout)

        # 设置 QScrollArea 的内部容器
        scroll_area.setWidget(scroll_content)

        # 将 QScrollArea 添加到外部容器的布局中
        container_layout.addWidget(scroll_area)

        # 设置外部容器为主窗口的中央部件
        self.setLayout(container_layout)

        # 修改水平滚动条的宽度（这里设置为10像素）
        scroll_bar_style = """
            QScrollBar:horizontal {
                height: 10px;
            }

            QScrollBar::handle:horizontal {
                background: #606060;
                min-width: 20px;
            }

            QScrollBar::add-line:horizontal {
                background: #F0F0F0;
                border: 2px solid #7F7F7F;
                width: 20px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:horizontal {
                background: #F0F0F0;
                border: 2px solid #7F7F7F;
                width: 20px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }
        """
        scroll_area.horizontalScrollBar().setStyleSheet(scroll_bar_style)

    def addAction(self, action, callback):
        btn = QToolButton()
        btn.setIcon(action.icon())
        btn.setText(action.text())
        btn.clicked.connect(callback)
        self.addToolButton(btn)

    def addToolButton(self, btn: QToolButton):
        btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.scroll_layout.addWidget(btn)

    def addToolButtons(self, tbns: List[QToolButton]):
        for btn in tbns:
            btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
            self.scroll_layout.addWidget(btn)
