from PySide2.QtWidgets import QDialog, QPushButton, QSizePolicy
from loguru import logger

from popup.clean.uipy import ui_datafiles_parse
from helper import FileFormat, MySignal
from runner import ParseFileThread


class WinDatafilesParse(QDialog, ui_datafiles_parse.Ui_Form):
    def __init__(self, parent, abs_datafiles, sep, count):
        super(WinDatafilesParse, self).__init__(parent)

        self.abs_datafiles = abs_datafiles
        self.sep = sep
        self.count = count

        self.setupUi(self)

        btns_arr = [[FileFormat.CNKI, FileFormat.WOS],
                [FileFormat.CSV, FileFormat.EXCEL],
                [FileFormat.PICKLE]]
        for i, btns in enumerate(btns_arr):
            for j, label in enumerate(btns):
                btn = QPushButton(label)
                btn.setStyleSheet('color:red;font-weight: bold; font-size:40px;')
                btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                btn.clicked.connect(self.action_format)
                self.gridLayout.addWidget(btn, i, j)

    def action_format(self):
        style = self.sender().text()
        logger.info(f'解析文件，格式 {style} 文件'+'  '.join(self.abs_datafiles))
        MySignal.info.send('开始解析文件，请稍等')

        # 启用多线程，必须self
        self.parseFileThread = ParseFileThread(self.abs_datafiles, style, self.sep, self.count)
        self.parseFileThread.start()
        self.hide()