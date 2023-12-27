from PySide2.QtWidgets import QDialog, QFileDialog

from core.const import ssignal, Cfg
from core.runner import CleanCoconStatThread
from uipopup.uipy import ui_cocon_stat


class PopupCoconStat(QDialog, ui_cocon_stat.Ui_Form):
    """
    频次统计
    """

    def __init__(self, parent):
        super(PopupCoconStat, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.init_data()

        self.btn_export.clicked.connect(self.export_clicked)

    def init_data(self):
        self.listWidget.addItems(self.get_clean_columns())

    def export_clicked(self):
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) != 1:
            ssignal.error.emit('只能选择1')
            return

        df = self.get_df()
        threshold = self.threshold_spinBox.value()
        filePath, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "保存统计文件",  # 标题
            Cfg.datafiles.value,  # 起始目录
            "Excel (*.xlsx);;"  # 选择类型过滤项，过滤内容在括号中
        )

        if filePath:
            self.coconStatThread = CleanCoconStatThread(df=df, fpath=filePath, names=names, threshold=threshold)
            self.coconStatThread.start()

        self.close()

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df, inplace_index=False, drop_index=False)

    def get_table(self):
        return self.parent.master_get_clean_table()
