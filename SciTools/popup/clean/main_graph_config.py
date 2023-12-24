from PySide2.QtWidgets import QDialog
from core.log import logger

from core.mgraph import Draw
from mrunner import CleanDrawGraphThread
from core.const import ssignal
from popup.clean.uipy import ui_graph_config


class PopupGraphConfig(QDialog, ui_graph_config.Ui_widget):
    def __init__(self, parent):
        super(PopupGraphConfig, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent


        for info in Draw.infos:
            self.graph_styles_widget.addItem(info.label)
        self.graph_styles_widget.setCurrentRow(0)

        self.comboBox_graph_x_axis.addItems(self.get_clean_columns())

        self.comboBox_graph_y_axis.addItem('')
        self.comboBox_graph_y_axis.addItems(self.get_clean_columns())

        self.btn_ok.clicked.connect(self.action_ok)

    def action_ok(self):
        logger.info('图表配置')


        #########################################################################
        selectedItems = self.graph_styles_widget.selectedItems()
        if len(selectedItems) == 0:
            ssignal.error.emit('请选择图表类型')
            return

        #########################################################################
        if len(self.comboBox_graph_x_axis.currentText())==0:
            ssignal.error.emit('必须选择横轴')
            return

        xlabel = self.comboBox_graph_x_axis.currentText()
        ylabel = self.comboBox_graph_y_axis.currentText()
        logger.debug('{0} {1}', xlabel, ylabel)


        configTuple = CleanDrawGraphThread.ConfigTuple(
            chart_style = selectedItems[0].text()
            ,xlabel=xlabel
            ,ylabel=ylabel
            ,stat_threshold=self.spinBox_graph_stat_threshold.value()
            ,orderby=self.comboBox_graph_orderby.currentText()
            ,canvas_width=self.slider_canvas_width.value()
            ,canvas_height=self.slider_canvas_height.value()
        )

        self.cleanDrawGraphThread = CleanDrawGraphThread(self.get_df(), configTuple)
        self.cleanDrawGraphThread.start()

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_graphdata(self, data):
        self.parent.graph_set_graphdata(data)