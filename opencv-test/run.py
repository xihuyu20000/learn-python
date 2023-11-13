import sys
from queue import LifoQueue
import cv2
from PIL import Image
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from numpy import ndarray

from ui_main import Ui_MainWindow

cache = LifoQueue()

class Operation:
    @staticmethod
    def resite(w, h):
        pass
class MasterWindows(QMainWindow, Ui_MainWindow):
    def __init__(self): # 构造方法
        super(MasterWindows, self).__init__()  # 运行父类的构造方法
        self.setupUi(self)  # 传递自己
        # 工具栏
        self.act1.clicked.connect(self.click_act1)
        self.act2.clicked.connect(self.click_act2)
        self.act3.clicked.connect(self.click_act3)
        # 操作
        self.toolbar_open.clicked.connect(self.click_toolbar_open)
        self.act_resize.clicked.connect(self.click_act_resize)
        #
        self.btn_change_size.clicked.connect(self.click_btn_change_size)

    def show_graph(self) -> ndarray:
        img = cache.get()
        cache.put(img)
        assert isinstance(img, ndarray)
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img3 = Image.fromarray(img2)
        img4 = img3.toqpixmap()
        self.canvas.setPixmap(img4)
        return img


    def click_act1(self):
        self.stackedPanels.setCurrentIndex(1)

    def click_act2(self):
        self.stackedPanels.setCurrentIndex(2)

    def click_act3(self):
        self.stackedPanels.setCurrentIndex(3)


    def click_toolbar_open(self):
        imgpath, imgtype = QFileDialog.getOpenFileName(self, '打开图片')
        cache.put(cv2.imread(imgpath))
        img = self.show_graph()

        h, w = img.shape[0], img.shape[1]
        self.statusbar.showMessage(f'图片来源 {imgpath}  宽{w} 高{h}')

    def click_act_resize(self):
        self.stackedPanels.setCurrentIndex(0)

    def click_btn_change_size(self):
        img = cache.get()
        cache.put(img)
        img2 = cv2.resize(img, [int(self.text_new_width.toPlainText()), int(self.text_new_height.toPlainText())])
        cache.put(img2)
        print(img2.shape)
        self.show_graph()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建GUI
    ui = MasterWindows()  # 创建PyQt设计的窗体对象
    ui.show()  # 显示窗体
    sys.exit(app.exec())  # 程序关闭时退出进程
