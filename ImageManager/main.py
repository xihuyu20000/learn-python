import sys
import time

from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView

from ui_main import Ui_MainWindow

class MasterWindows(QMainWindow, Ui_MainWindow):
    def __init__(self): # 构造方法
        super(MasterWindows, self).__init__()  # 运行父类的构造方法
        self.setupUi(self)  # 传递自己

        self.editor.setPixmap(QPixmap(r'C:\Users\Administrator\Downloads\3.jpg'))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建GUI
    ui = MasterWindows()  # 创建PyQt设计的窗体对象
    ui.show()  # 显示窗体
    sys.exit(app.exec())  # 程序关闭时退出进程
