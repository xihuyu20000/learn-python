from PySide2.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QVBoxLayout, QWidget
import sys

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        # 创建两个 QDockWidget
        dock_widget1 = QDockWidget('Dock 1', self)
        dock_widget2 = QDockWidget('Dock 2', self)

        # 在 QDockWidget 中添加一些内容（这里使用 QTextEdit 作为示例）
        text_edit1 = QTextEdit()
        text_edit2 = QTextEdit()

        dock_widget1.setWidget(text_edit1)
        dock_widget2.setWidget(text_edit2)

        # 创建一个 QWidget 作为中央部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 创建水平布局管理器
        layout = QVBoxLayout(central_widget)

        # 将 QDockWidget 添加到布局中
        layout.addWidget(dock_widget1)
        layout.addWidget(dock_widget2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())
