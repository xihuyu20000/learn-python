from PySide2.QtWidgets import QDialog, QFileDialog

from core.const import ssignal, Cfg
from core.runner import CleanWordCountThread, CleanWordCountExportThread
from uipopup.uipy import ui_count_stat


class PopupWordCountStat(QDialog, ui_count_stat.Ui_Form):
    def __init__(self, parent):
        super(PopupWordCountStat, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.init_data()

        self.btn_ok.clicked.connect(self.ok_clicked)
        self.btn_export.clicked.connect(self.export_clicked)

    def init_data(self):
        self.listWidget.addItems(self.get_clean_columns())

    def ok_clicked(self):
        threshold = int(self.threhold_spinBox.text())
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) == 0:
            ssignal.error.emit("请选择列")
            return

        if len(names) > 1:
            ssignal.error.emit("选择多列，请直接导出")
            return

        name = names[0]

        df = self.get_df()
        # ssignal.push_cache.emit(self.get_df())

        self.cleanWordCountThread = CleanWordCountThread(df, name, threshold)
        self.cleanWordCountThread.start()
        self.close()

    def export_clicked(self):
        threshold = int(self.threhold_spinBox.text())
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) == 0:
            ssignal.error.emit("请选择列")
            return

        df = self.get_df()

        filePath, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "保存词频统计文件",  # 标题
            Cfg.datafiles.value,  # 起始目录
            "Excel (*.xlsx);;",  # 选择类型过滤项，过滤内容在括号中
        )

        self.cleanWordCountExportThread = CleanWordCountExportThread(
            df, names, threshold, filePath
        )
        self.cleanWordCountExportThread.start()
        self.close()

    def get_clean_columns(self):
        return self.parent.get_df_columns()

    def get_df(self):
        return self.parent.get_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
