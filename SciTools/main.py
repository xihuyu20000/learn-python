import atexit
import sys

from PySide2.QtWidgets import QApplication

from uimain.main_main import MasterMainWindows


@atexit.register
def exit_app():
    print('正在退出程序')


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建GUI

    ui = MasterMainWindows()  # 创建PyQt设计的窗体对象
    # ui.show()  # 显示窗体
    ui.showMaximized()
    sys.exit(app.exec_())  # 程序关闭时退出进程
