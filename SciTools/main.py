import os
import sys

from PySide2.QtWidgets import QApplication

from mainui.main_main import MasterWindows

if __name__ == "__main__":
    # print("PyInstaller temporary directory:", sys._MEIPASS)
    # print("Contents of temporary directory:")
    # print(os.listdir(sys._MEIPASS))

    app = QApplication(sys.argv)  # 创建GUI

    # font = app.font()
    # font.setPointSize(int(Cfg.global_font_size))
    # font.setFamily("Microsoft YaHei")
    # app.setFont(font)

    ui = MasterWindows()  # 创建PyQt设计的窗体对象
    ui.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
