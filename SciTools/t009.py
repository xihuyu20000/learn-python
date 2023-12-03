import sys
from PySide6.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QModelIndex, QAbstractTableModel
import pandas as pd

class PandasTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data.columns) if not self._data.empty else 0

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            return str(self._data.iloc[row, col])

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return str(self._data.columns[section])

        return None

    def sort(self, column, order):
        if order == Qt.AscendingOrder:
            self._data = self._data.sort_values(self._data.columns[column], ascending=True)
        else:
            self._data = self._data.sort_values(self._data.columns[column], ascending=False)

        self.layoutChanged.emit()

class TableViewExample(QWidget):
    def __init__(self, data):
        super().__init__()

        self.model = PandasTableModel(data)

        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        # 允许表头点击进行排序
        self.table_view.setSortingEnabled(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.table_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建示例 DataFrame
    data = {
        'Name': ['John', 'Jane', 'Bob', 'Alice'],
        'Age': [30, 25, 40, 35],
        'Salary': [50000, 60000, 55000, 70000]
    }
    df = pd.DataFrame(data)

    # 创建 TableViewExample 实例
    window = TableViewExample(df)
    window.show()

    sys.exit(app.exec())
