import sys

from PySide2.QtCore import Qt, QMimeData
from PySide2.QtGui import QDrag, QIcon
from PySide2.QtWidgets import QDialog, QApplication, QHBoxLayout, QToolButton, QWidget, QComboBox, QSizePolicy, \
    QSpacerItem

from core.util.mutil import Config
from uipopup.clean.uipy import ui_group_stat


class PopupCleanGroupStat(QWidget, ui_group_stat.Ui_Form):

    def __init__(self, txt):
        super(PopupCleanGroupStat, self).__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.btn = ClosableButton(txt)
        self.btn.setMinimumWidth(100)
        self.layout.addWidget(self.btn)
        self.combox = QComboBox(self)
        self.combox.setFixedHeight(30)
        self.combox.addItems(['计数'])
        self.combox.setMinimumWidth(50)
        self.layout.addWidget(self.combox)

        self.btn.clicked.connect(lambda: self.close())

    def get_value(self):
        return Config.seperator.join([self.btn.get_value(), self.combox.currentText()])


class ClosableButton(QToolButton):
    def __init__(self, txt):
        super(ClosableButton, self).__init__()
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.setIcon(QIcon("./icons/shanchu.png"))
        self.setText(txt)

    def get_value(self):
        return self.text()


class WinGroupStat(QDialog, ui_group_stat.Ui_Form):
    def __init__(self, parent):
        super(WinGroupStat, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.listWidget.setDragEnabled(True)
        self.listWidget.mousePressEvent = lambda e: self.soure_drag_start(self.listWidget, e)
        self.listWidget.addItems(['张三', '李四', '王五', '赵六'])

        self.layout1 = QHBoxLayout(self.widget_group)
        self.widget_group.dragEnterEvent = lambda e: e.acceptProposedAction()
        self.widget_group.dropEvent = lambda e: self.do_drop_event(self.widget_group, e)

        self.layout2 = QHBoxLayout(self.widget_stat)
        self.widget_stat.dragEnterEvent = lambda e: e.acceptProposedAction()
        self.widget_stat.dropEvent = lambda e: self.do_drop_event(self.widget_stat, e)

        self.btn_ok.clicked.connect(self.action_ok)

    def soure_drag_start(self, source, event):
        if event.button() == Qt.LeftButton:
            src_txt = source.itemAt(event.pos()).text()
            mimedata = QMimeData()
            mimedata.setText(src_txt)  # 放入数据
            drag = QDrag(self)
            drag.setMimeData(mimedata)
            drag.exec_()  # exec()函数并不会阻塞主函数

    def do_drop_event(self, target, e):
        # 添加拖曳文本到条目中
        mimedata = e.mimeData()
        if mimedata.hasText():
            e.acceptProposedAction()
            if target.objectName() == 'widget_group':
                btn = ClosableButton(mimedata.text())
                btn.clicked.connect(lambda e: btn.close())
                target.layout().addWidget(btn)
            if target.objectName() == 'widget_stat':
                stat_wdt = PopupCleanGroupStat(mimedata.text())
                stat_wdt.btn.clicked.connect(lambda e: stat_wdt.close())
                target.layout().addWidget(stat_wdt)

    def action_ok(self):
        group_children = [item.get_value() for item in self.widget_group.findChildren(ClosableButton)]
        stat_children = [item.get_value() for item in self.widget_stat.findChildren(PopupCleanGroupStat)]


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建GUI
    ui = WinGroupStat(app)  # 创建PyQt设计的窗体对象
    ui.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
