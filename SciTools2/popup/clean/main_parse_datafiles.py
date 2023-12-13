from PySide2.QtWidgets import QDialog, QPushButton, QSizePolicy
from log import logger
from popup.clean.uipy import ui_datafiles_parse
from mhelper import FileFormat, ssignal
from mrunner import CleanParseFileThread


class PopupDatafilesParse(QDialog, ui_datafiles_parse.Ui_Form):
    def __init__(self, parent, abs_datafiles, sep):
        super(PopupDatafilesParse, self).__init__(parent)

        self.abs_datafiles = abs_datafiles
        self.sep = sep

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
        style = self.emiter().text()
        logger.info(f'解析文件，格式 {style} 文件'+'  '.join(self.abs_datafiles))
        ssignal.info.emit('开始解析文件，请稍等')

        # 启用多线程，必须self
        self.parseFileThread = CleanParseFileThread(self.abs_datafiles, style, self.sep)
        self.parseFileThread.start()
        self.hide()