import os
import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QMessageBox

from clean import CleanWidget
from toolkit import VBoxKit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowIcon(QIcon('./icons/1.png'))
        # 创建主窗口中的中心部件
        main_widget = QWidget(self)

        self.setCentralWidget(main_widget)
        # 创建布局管理器
        main_layout = VBoxKit(main_widget)

        # 菜单栏
        self.init_menubar()

        # 创建tabwidget
        main_tabWidget = QTabWidget(main_widget)
        main_tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        tab0 = CleanWidget(self)
        tab1 = QWidget()
        main_tabWidget.addTab(tab0, '清洗')
        main_tabWidget.addTab(tab1, '分析')

        main_layout.addWidget(main_tabWidget)

        self.showStatusbarMessage('欢迎使用本软件，祝您有愉快的一天!')


    def init_menubar(self):
        help_menu = self.menuBar().addMenu('帮助')
        help_action = QAction('使用教程', self)
        help_menu.triggered.connect(self.action_help_clb)
        help_menu.addAction(help_action)
        # contact_author_action = QAction('联系作者', self)
        # help_menu.addAction(contact_author_action)

    def action_help_clb(self):
        QMessageBox.information(None, "Title", "点击'数据文件'，选择需要解析的文件，然后点击'解析'.")
    def showStatusbarMessage(self, val):
        self.statusBar().setStyleSheet("color: red;font-weight: bold;font-size: 16px;")
        self.statusBar().showMessage(val, 10000)
if __name__ == '__main__':

    print()


    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()