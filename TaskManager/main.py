import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView

from ui_main import Ui_MainWindow


class MasterWindows(QMainWindow, Ui_MainWindow):
    def __init__(self): # 构造方法
        super(MasterWindows, self).__init__()  # 运行父类的构造方法
        self.setupUi(self)  # 传递自己

        self.show_table()

    def show_table(self):
        model = QStandardItemModel(self)

        model.setHorizontalHeaderLabels(['程序名称', '大小', '安装时间'])
        self.fill_table(model)
        self.tableView.setModel(model)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
    def fill_table(self, model):
        for i in range(5):
            name_item = QStandardItem(f'程序名称{i}')
            name_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
            model.setItem(i, 0, name_item)

            size_item = QStandardItem(f'大小称{i}')
            size_item.setTextAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
            model.setItem(i, 1, size_item)

            installdate_item = QStandardItem(f'安装时间{i}')
            installdate_item.setTextAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
            model.setItem(i, 2, installdate_item)
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建GUI
    ui = MasterWindows()  # 创建PyQt设计的窗体对象
    ui.show()  # 显示窗体
    sys.exit(app.exec())  # 程序关闭时退出进程
