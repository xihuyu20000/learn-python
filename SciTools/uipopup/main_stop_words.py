import os.path

from PySide2.QtWidgets import QDialog, QFileDialog

from core.const import Cfg, ssignal
from core.log import logger
from core.runner import CleanStopWordsThread
from uipopup.uipy import ui_stop_words


class PopupStopWords(QDialog, ui_stop_words.Ui_Form):
    def __init__(self, parent):
        super(PopupStopWords, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.column_names.addItems(self.get_clean_columns())
        self.column_names.setCurrentRow(0)

        self.le1.setText(os.path.join(Cfg.dicts.value, Cfg.stop_words.value))

        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn_ok.clicked.connect(lambda: self.action_ok(self.le1.text(), self.rbt1.isChecked()))

    def action_ok(self, dict_path, is_new: bool):
        logger.info('停用词表')
        names = self.column_names.selectedItems()

        if len(names) == 0:
            ssignal.error.emit('请选择列')
            return

        names = [item.text() for item in names]

        if dict_path is None or dict_path.strip() == "":
            ssignal.error.emit('请选择词典')
            return

        # key是被替换的词，value是新词【第1个】
        words_set = set()
        with open(dict_path, encoding='utf-8') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines if not line.strip().startswith('#')]
            for line in lines:
                words_set.update(line.split(';'))

        df = self.get_df()
        # ssignal.push_cache.emit(self.get_df())

        self.cleanStopWordsThread = CleanStopWordsThread(df, names, words_set, is_new)
        self.cleanStopWordsThread.start()
        self.close()

    def btn1_clicked(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择词典",  # 标题
            Cfg.dicts.value,  # 起始目录
            "文件类型 (*.csv *.txt *.xls *.xlsx)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.le1.setText(filePath)

    def get_clean_columns(self):
        return self.parent.get_df_columns()

    def get_df(self):
        return self.parent.get_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
