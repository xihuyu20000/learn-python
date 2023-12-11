import sys

from PySide2.QtWidgets import QApplication

from mainui.main_main import MasterWindows


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建GUI
    ui = MasterWindows()  # 创建PyQt设计的窗体对象
    ui.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
