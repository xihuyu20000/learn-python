import sys
import time

from PySide6.QtCore import QObject, Slot
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication

"""
使用QWebEngineWidget显示html内容
"""


class Handlers(QObject):

    def __init__(self):
        super().__init__(None)
        self.view = QWebEngineView()
        self.page = self.view.page()

    @Slot(str, result=str)
    def hello(self, message):
        """js调用python测试"""
        print('call received')
        return f'hello from python: {message}'

    def send_time(self):
        """python调用js测试"""
        self.page.runJavaScript(f'sysTime("python 本地时间: {time.time()}")')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    channel = QWebChannel()
    handlers = Handlers()
    channel.registerObject('py', handlers)
    handlers.page.setWebChannel(channel)

    handlers.view.load('http://127.0.0.1:5000/')
    handlers.view.show()
    sys.exit(app.exec())
