import collections

from PySide2.QtWidgets import QDialog, QListWidgetItem

from core.const import ssignal
from core.runner import CleanExtractFeaturesThread
from uipopup.uipy import ui_extract_feature

SpeechItem = collections.namedtuple('SpeechItem', ['en', 'cn', 'checked'])
speech_list = [
    SpeechItem('a', '形容词', False),
    SpeechItem('c', '连词', False),
    SpeechItem('d', '副词', False),
    SpeechItem('i', '成语', False),
    SpeechItem('j', '简称略语', False),
    SpeechItem('m', '数词', False),
    SpeechItem('mq', '数量词', False),
    SpeechItem('n', '名词', True),
    SpeechItem('ng', '名语素', True),
    SpeechItem('nr', '人名', True),
    SpeechItem('nrfg', '古近代人名', True),
    SpeechItem('nrt', '音译人名', True),
    SpeechItem('ns', '地名', True),
    SpeechItem('nt', '机构团体', True),
    SpeechItem('nz', '其他专名', True),
    SpeechItem('r', '代词', False),
    SpeechItem('s', '处所词', False),
    SpeechItem('t', '时间词', False),
    SpeechItem('tg', '时间语素', False),
    SpeechItem('v', '动词', True),
    SpeechItem('vd', '副动词', True),
    SpeechItem('vg', '动语素', True),
    SpeechItem('vn', '名动词', True),
]


class PopupExtractFeatures(QDialog, ui_extract_feature.Ui_Form):
    def __init__(self, parent):
        super(PopupExtractFeatures, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.init_data()

        self.pushButton.clicked.connect(self.on_clicked)

    def init_data(self):
        self.listWidget_colnames.addItems(self.get_clean_columns())

        for speech_item in speech_list:
            item = QListWidgetItem(speech_item.cn)
            self.listWidget_speech.addItem(item)
            self.listWidget_speech.setItemSelected(item, speech_item.checked)

    def on_clicked(self):
        colnames = [line.text() for line in self.listWidget_colnames.selectedItems()]

        if len(colnames) == 0:
            ssignal.error.emit('请选择列')
            return

        choosed_speeches = [line.text() for line in self.listWidget_speech.selectedItems()]
        choosed_speeches = [item.en for item in speech_list if item.cn in choosed_speeches]

        df = self.get_df()

        self.cleanExtractFeaturesThread = CleanExtractFeaturesThread(df, colnames, choosed_speeches)
        self.cleanExtractFeaturesThread.start()

    def get_clean_columns(self):
        return self.parent.get_df_columns()

    def get_df(self):
        return self.parent.get_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
