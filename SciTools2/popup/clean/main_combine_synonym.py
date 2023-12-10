import os.path
import time

from PySide2.QtWidgets import QDialog, QFileDialog
from loguru import logger

from helper import Cfg, Utils, MySignal
from popup.clean.uipy import ui_combine_synonym


class WinCombineSynonym(QDialog, ui_combine_synonym.Ui_Form):
    def __init__(self, parent):
        super(WinCombineSynonym, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.column_names.addItems(self.get_clean_columns())
        self.column_names.setCurrentRow(0)

        self.le1.setText(os.path.join(Cfg.dicts, '合并词表.txt'))

        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn_ok.clicked.connect(lambda: self.action_ok(self.le1.text(), self.rbt1.isChecked()))

    def action_ok(self, dict_path, is_new: bool):
        logger.info('同义词合并')
        names = self.column_names.selectedItems()
        if len(names) == 0:
            return

        names = [item.text() for item in names ]

        if dict_path is None or dict_path.strip() == "":
            MySignal.error.send('请选择词典')
            return

        t1 = time.time()
        # key是被替换的词，value是新词【第1个】
        words_dict = {}
        with open(dict_path, encoding='utf-8') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines if not line.strip().startswith('#')]
            for line in lines:
                words = line.split(';')
                # 一行一个词，那么长度是1
                if len(words) > 1:
                    tgt = words[0]
                    for org in words[1:]:
                        words_dict[org] = tgt

        df = self.get_df()

        new_names = []
        # 遍历每一列，对每一列的每一个值，进行替换处理
        for col in names:
            col_new = col + '-new' if is_new else col
            if is_new:
                new_names.append(col_new)
            df[col_new] = df[col].apply(lambda x: self.__replace(x, words_dict))

        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, new_names)
        df = df[old_names]
        self.set_df(df)
        t2 = time.time()

        msg = '合并{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(names), round(t2 - t1, 2))
        MySignal.info.send(msg)
        self.close()

    def btn1_clicked(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择词典",  # 标题
            Cfg.dicts,  # 起始目录
            "文件类型 (*.csv *.txt *.xls *.xlsx)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.le1.setText(filePath)

    def __replace(self, line, words_dict):
        keys = words_dict.keys()
        words = [str(words_dict[w]) if w in keys else w for w in line.split(Cfg.seperator)]
        return ';'.join(words)

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)