from PySide2.QtWidgets import QDialog

from core.const import ssignal
from core.runner import CleanCopyColumnThread
from core.runner.mrunner import CleanLevel1OrgThread
from uipopup.uipy import ui_level1_org


class PopupLevel1Org(QDialog, ui_level1_org.Ui_Form):
    def __init__(self, parent):
        super(PopupLevel1Org, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.init_data()

        self.pushButton.clicked.connect(self.on_clicked)

    def init_data(self):
        self.listWidget.addItems(self.get_clean_columns())

        for i, row in enumerate(self.get_clean_columns()):
            if row == '机构':
                self.listWidget.setItemSelected(self.listWidget.item(i), True)
                return


    def on_clicked(self):
        names = [line.text() for line in self.listWidget.selectedItems()]

        if len(names) == 0:
            ssignal.error.emit('请选择列')
            return

        df = self.get_df()

        name = names[0]
        self.cleanLevel1OrgThread = CleanLevel1OrgThread(df, name)
        self.cleanLevel1OrgThread.start()

    def get_clean_columns(self):
        return self.parent.get_df_columns()

    def get_df(self):
        return self.parent.get_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)
