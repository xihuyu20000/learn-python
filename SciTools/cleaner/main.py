import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QTabWidget, QWidget, QLabel

from cleaner.clean import CleanWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建主窗口中的中心部件
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        # 创建布局管理器
        main_layout = QVBoxLayout(main_widget)
        # 设置布局为中心部件的布局
        main_widget.setLayout(main_layout)

        # 布局管理器，清除空白区域
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 创建tabwidget
        main_tabWidget = QTabWidget(main_widget)
        main_tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        tab0 = CleanWidget()
        tab1 = QWidget()
        main_tabWidget.addTab(tab0, '清洗')
        main_tabWidget.addTab(tab1, '分析')

        main_layout.addWidget(main_tabWidget)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()