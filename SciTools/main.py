import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_ui_main import Ui_MainWindow


class MasterWindows(QMainWindow, Ui_MainWindow):
    def __init__(self):  # 构造方法
        super(MasterWindows, self).__init__()  # 运行父类的构造方法
        self.setupUi(self)  # 传递自己

        self.gbl_btn_menu.clicked.connect(lambda: self.mainContainer.setCurrentIndex(0))
        self.gbl_btn_my_analysis.clicked.connect(lambda: self.mainContainer.setCurrentIndex(1))
        self.gbl_btn_public_data.clicked.connect(lambda: self.mainContainer.setCurrentIndex(2))
        self.gbl_btn_mis.clicked.connect(lambda: self.mainContainer.setCurrentIndex(3))
        self.gbl_btn_user_center.clicked.connect(lambda: self.mainContainer.setCurrentIndex(4))
        self.gbl_btn_bi_tool.clicked.connect(lambda: self.mainContainer.setCurrentIndex(5))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    masterWindow = MasterWindows()
    masterWindow.show()

    sys.exit(app.exec())
