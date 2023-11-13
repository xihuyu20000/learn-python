import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QScrollBar, QWidget


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QScrollBar-功能作用')
        self.resize(500, 500)
        self.widget_list()

    def widget_list(self):
        self.add_widget()

    def add_widget(self):
        v_scb = QScrollBar(self)
        h_scb = QScrollBar(Qt.Horizontal, self)

        v_scb.resize(20, self.height() - h_scb.height())
        h_scb.resize(self.width() - v_scb.width(), 20)

        v_scb.move(self.width() - v_scb.width(), 0)
        h_scb.move(0, self.height() - h_scb.height())

        # 控件值发生改变信号
        v_scb.valueChanged.connect(lambda val: print(val))
        # v_scb.setPageStep(50)

        # 设置v_scb控件捕获键盘
        v_scb.grabKeyboard()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Windows()

    window.show()
    sys.exit(app.exec())
