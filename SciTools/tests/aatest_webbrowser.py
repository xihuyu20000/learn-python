import os
from pathlib import Path
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
from PySide2.QtWebChannel import QWebChannel
from PySide2.QtCore import QUrl, Slot, QObject, QUrl

data_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'dist'


class Handler(QObject):
    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)

    # @Slot是关键,是js中调用的接口,经测试,只能传一个参数,传对象参数时需要把它专为json字符串
    @Slot(str, result=str)
    def sayHello(self, name):
        return f"Hello from the other side, {name}"


class WebEnginePage(QWebEnginePage):
    def __init__(self, *args, **kwargs):
        super(WebEnginePage, self).__init__(*args, **kwargs)

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceId):
        print("WebEnginePage Console: ", level, message, lineNumber, sourceId)


if __name__ == "__main__":
    # Set up the main application
    app = QApplication([])
    app.setApplicationDisplayName("Greetings from the other side")

    # Use a webengine view
    view = QWebEngineView()
    view.resize(1000, 800)

    # Set up backend communication via web channel
    handler = Handler()
    # channel是页面中可以拿到的,顾名思义,一个通道
    channel = QWebChannel()
    # Make the handler object available, naming it "backend"
    channel.registerObject("backend", handler)
    # Use a custom page that prints console messages to make debugging easier
    page = WebEnginePage()
    page.setDevToolsPage(page)
    page.setWebChannel(channel)
    view.setPage(page)

    # 启用开发者工具
    view.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)


    # Finally, load our file in the view
    # url = QUrl.fromLocalFile(f"{data_dir}/index.html")
    view.load(QUrl.fromLocalFile(f"{data_dir}/index.html"))
    # view.load(QUrl("http://localhost:5173/"))
    view.show()

    app.exec_()
