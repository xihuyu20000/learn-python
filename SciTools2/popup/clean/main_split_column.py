import re
import time
from typing import List
from log import logger
from PySide2.QtWidgets import QDialog

from helper import Utils, ssignal
from popup.clean.uipy import ui_split_column


class PopupSplitColumn(QDialog, ui_split_column.Ui_Form):
    def __init__(self, parent):
        super(PopupSplitColumn, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.init_data()

        self.pushButton.clicked.connect(self.on_clicked)

    def init_data(self):
        self.listWidget.addItems(self.get_clean_columns())

    def on_clicked(self):
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) == 0:
            return

        name = names[0]

        split_style_text = self.cb1.currentText()
        le1_text = self.le1.text()
        get_style_text = self.cb2.currentText()
        le2_text = self.le2.text()

        m = re.compile(r'^[1-9]\d*$')
        if '字符' in split_style_text and not m.match(le1_text):
            ssignal.error.send('拆分方式是按字符数，后面请填写正整数')
            return

        if not m.match(le2_text):
            ssignal.error.send('拆分结果后面请填写正整数')
            return

        le2 = int(le2_text)
        df = self.get_df()

        t1 = time.time()
        if '分隔符' in split_style_text:
            df['xxxyyyzzz'] = df[name].apply(lambda x: str(x).split(le1_text))
        if '字符' in split_style_text:
            df['xxxyyyzzz'] = df[name].apply(lambda x: self.split_string_by_length(x, le1_text))

        new_names = []
        if '前' in get_style_text:
            for i in range(le2):
                new_name = f'{name}-{i + 1}'
                new_names.append(new_name)
                df[new_name] = df['xxxyyyzzz'].map(lambda x: self.get_from_limit(i, x, le2))
        if '第' in get_style_text:
            new_name = f'{name}-1'
            new_names.append(new_name)
            df[new_name] = df['xxxyyyzzz'].map(lambda x: self.get_from_limit(le2, x, le2))

        df.drop('xxxyyyzzz', axis=1, inplace=True)
        old_names = df.columns.tolist()
        # 下面的new_names一定要倒序
        old_names = Utils.resort_columns(old_names, sorted(new_names, reverse=True))
        df = df[old_names]
        self.set_df(df)
        t2 = time.time()
        error = '分隔符含有中文或中文字符\r\n' if Utils.has_Chinese_or_punctuation(le1_text) else ''
        msg = error + '拆分{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], 1, round(t2 - t1, 2))
        ssignal.info.send(msg)
        self.close()

    def get_from_limit(self, i: int, arr: List[str], limit: int):
        if limit <= len(arr):
            return arr[i]
        else:
            if i < len(arr):
                return arr[i]
            else:
                return ''

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()
    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)