from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar, QToolButton, QVBoxLayout, QWidget
from PySide2.QtCore import Qt, QMimeData
from PySide2.QtGui import QDrag

class DraggableToolButton(QToolButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setAcceptDrops(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setText(self.text())
            drag.setMimeData(mime_data)

            # 设置拖拽时显示的图标
            drag.setPixmap(self.icon().pixmap(32, 32))

            drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        # 处理拖拽事件，你可以在这里实现按钮的顺序改变逻辑
        print(f"Button dropped: {self.text()}")

class DraggableToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        button1 = DraggableToolButton("Button 1")
        button2 = DraggableToolButton("Button 2")
        button3 = DraggableToolButton("Button 3")

        self.addWidget(button1)
        self.addWidget(button2)
        self.addWidget(button3)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = QMainWindow()
    draggable_toolbar = DraggableToolBar()
    main_window.addToolBar(draggable_toolbar)

    main_window.show()
    sys.exit(app.exec_())
