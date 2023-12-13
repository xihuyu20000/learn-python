
from PySide2.QtWidgets import QDialog
from mhelper import ssignal
from popup.clean.uipy import ui_count_stat
from mrunner import CleanWordCountThread


class PopupWordCountStat(QDialog, ui_count_stat.Ui_Form):
    def __init__(self, parent):
        super(PopupWordCountStat, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.init_data()

        self.btn_ok.clicked.connect(self.ok_clicked)
        self.btn_export.clicked.connect(self.export_clicked)

    def init_data(self):
        self.listWidget.addItems(self.get_clean_columns())

    def ok_clicked(self):
        threshold = int(self.threhold_spinBox.text())
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) == 0:
            ssignal.error.emit('请选择列')
            return

        if len(names) >1:
            ssignal.error.emit('选择多列，请直接导出')
            return

        df = self.get_df()

        name = names[0]

        self.cleanWordCountThread = CleanWordCountThread(df, name, threshold)
        self.cleanWordCountThread.start()
        self.close()

    def export_clicked(self):
        ssignal.error.emit('暂时不导出')
        return
        # names = [line.text() for line in self.listWidget.selectedItems()]
        #
        # if len(names) == 0:
        #     ssignal.error.emit('请选择列')
        #     return
        #
        # df = self.get_df()
        #
        # results = []
        # for col in names:
        #     try:
        #         # 使用str.split进行拆分，并使用explode展开列表
        #         df_split = df[col].str.split(Cfg.seperator, expand=True).stack()
        #
        #         # 使用value_counts进行统计
        #         counts = df_split.value_counts()
        #         # 使用reset_index()将Series转为DataFrame
        #         counts = counts.reset_index()
        #         # 替换空值
        #         counts.fillna('', inplace=True)
        #         # 为DataFrame的列命名
        #         counts.columns = [col, '次数']
        #         results.append(counts)
        #     except Exception as e:
        #         print(e)
        #         counts = pd.DataFrame(columns = [col, '次数'])
        #         results.append(counts)
        #
        # filePath, _ = QFileDialog.getSaveFileName(
        #     self,  # 父窗口对象
        #     "保存词频统计文件",  # 标题
        #     Cfg.datafiles,  # 起始目录
        #     "Excel (*.xlsx);;"  # 选择类型过滤项，过滤内容在括号中
        # )
        #
        # if filePath:
        #     self.countStatThread = CleanExportCountStatThread(fpath=filePath, names=names, df_list=results)
        #     self.countStatThread.start()
        #
        # self.close()

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()


    def set_df(self, df):
        self.parent.master_set_clean_df(df)