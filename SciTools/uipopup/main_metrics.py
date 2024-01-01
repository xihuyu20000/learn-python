from PySide2.QtWidgets import QDialog

from core import MetricsStat
from core.const import ssignal
from core.log import logger
from uipopup.uipy import ui_metrics


class PopupMetrics(QDialog, ui_metrics.Ui_Form):
    """
    频次统计
    """

    def __init__(self, parent):
        super(PopupMetrics, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent.context

        self.btn_2_matrix.clicked.connect(self.to_matrix)
        ##########################################################
        self.btn_stat_yearly.clicked.connect(self.stat_yearly)
        self.btn_stat_kw.clicked.connect(self.stat_kw)
        self.btn_graph.clicked.connect(self.export_clicked)
        self.btn_stat_author.clicked.connect(self.stat_author)
        self.btn_stat_org.clicked.connect(self.stat_org)
        self.btn_stat_source.clicked.connect(self.stat_source)
        self.btn_stat_country.clicked.connect(self.stat_country)
        self.btn_stat_subject.clicked.connect(self.stat_subject)
        ##########################################################
        self.btn_cocon_kw.clicked.connect(self.cocon_kw)
        self.btn_cocon_author.clicked.connect(self.cocon_author)
        self.btn_cocon_org.clicked.connect(self.cocon_org)
        self.btn_cocon_country.clicked.connect(self.cocon_country)
        self.btn_cocon_subject.clicked.connect(self.cocon_subject)
        ###########################################################
        self.btn_matrix2_doc_kw.clicked.connect(self.matrix2_doc_kw)
        self.btn_matrix2_author_kw.clicked.connect(self.matrix2_author_kw)
        self.btn_matrix2_org_kw.clicked.connect(self.matrix2_org_kw)
        self.btn_matrix2_country_kw.clicked.connect(self.matrix2_country_kw)
        self.btn_matrix2_subject_kw.clicked.connect(self.matrix2_subject_kw)
        ##############################################################
        self.btn_coupled_author_kw.clicked.connect(self.coupled_author_kw)
        self.btn_coupled_org_kw.clicked.connect(self.coupled_org_kw)
        self.btn_coupled_country_kw.clicked.connect(self.coupled_country_kw)
        self.btn_coupled_subject_kw.clicked.connect(self.coupled_subject_kw)

    def to_matrix(self):
        try:
            df = self.frame_tablekit.get_dataset()
            # 列转行，形成共现矩阵
            logger.debug('形成共现矩阵')
            df = df.pivot_table(index=self.lineEdit_axis_X.text().strip(), columns=self.lineEdit_axis_Y.text().strip(), values=self.lineEdit_value.text().strip())
            # 填充空值
            df.fillna(0, inplace=True)
            # 类型转换
            df = df.astype(int)
            df = df.reset_index()
            self.frame_tablekit.set_dataset(df)
            self.show_info('转矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def stat_yearly(self):
        try:
            df = MetricsStat.yearly_count(self.get_df(), self.lineEdit_field_year.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('历年发文统计')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def stat_kw(self):
        try:
            df = MetricsStat.freq_count(self.get_df(), by=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('关键词统计')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def stat_author(self):
        try:
            df = MetricsStat.freq_count(self.get_df(), by=self.lineEdit_field_author.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('作者统计')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def stat_org(self):
        try:
            df = MetricsStat.freq_count(self.get_df(), by=self.lineEdit_field_org.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('机构统计')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def stat_source(self):
        try:
            df = MetricsStat.freq_count(self.get_df(), by=self.lineEdit_field_source.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('期刊统计')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)


    def stat_country(self):
        try:
            df = MetricsStat.freq_count(self.get_df(), by=self.lineEdit_field_country.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('国家统计')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)


    def stat_subject(self):
        try:
            df = MetricsStat.freq_count(self.get_df(), by=self.lineEdit_field_subject.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('学科统计')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)


    def cocon_kw(self):
        try:
            df = MetricsStat.matrix1(self.get_df(), item=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('关键词共现矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)



    def cocon_author(self):
        try:
            df = MetricsStat.matrix1(self.get_df(), item=self.lineEdit_field_author.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('作者共现矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def cocon_org(self):
        try:
            df = MetricsStat.matrix1(self.get_df(), item=self.lineEdit_field_org.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('机构共现矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def cocon_country(self):
        try:
            df = MetricsStat.matrix1(self.get_df(), item=self.lineEdit_field_country.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('国家共现矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def cocon_subject(self):
        try:
            df = MetricsStat.matrix1(self.get_df(), item=self.lineEdit_field_subject.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('学科共现矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def matrix2_doc_kw(self):
        try:
            df = MetricsStat.matrix2(self.get_df(), item1=self.lineEdit_field_title.text().strip(), item2=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('词篇矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def matrix2_author_kw(self):
        try:
            df = MetricsStat.matrix2(self.get_df(), item1=self.lineEdit_field_author.text().strip(), item2=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('作者——关键词矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def matrix2_org_kw(self):
        try:
            df = MetricsStat.matrix2(self.get_df(), item1=self.lineEdit_field_org.text().strip(), item2=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('机构——关键词矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def matrix2_country_kw(self):
        try:
            df = MetricsStat.matrix2(self.get_df(), item1=self.lineEdit_field_country.text().strip(), item2=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('国家——关键词矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def matrix2_subject_kw(self):
        try:
            df = MetricsStat.matrix2(self.get_df(), item1=self.lineEdit_field_subject.text().strip(), item2=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('学科——关键词矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    #
    def coupled_author_kw(self):
        try:
            df = MetricsStat.coupled_matrix(self.get_df(), item1=self.lineEdit_field_author.text().strip(), kw=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('作者——关键词耦合矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def coupled_org_kw(self):
        try:
            df = MetricsStat.coupled_matrix(self.get_df(), item1=self.lineEdit_field_org.text().strip(), kw=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('机构——关键词耦合矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def coupled_country_kw(self):
        try:
            df = MetricsStat.coupled_matrix(self.get_df(), item1=self.lineEdit_field_country.text().strip(), kw=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('国家——关键词耦合矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)

    def coupled_subject_kw(self):
        try:
            df = MetricsStat.coupled_matrix(self.get_df(), item1=self.lineEdit_field_subject.text().strip(), kw=self.lineEdit_field_keyword.text().strip())
            self.frame_tablekit.set_dataset(df)
            self.show_info('学科——关键词耦合矩阵')
        except Exception as e:
            logger.exception(e)
            msg = "解析出错:{0}".format(str(e))
            self.show_error(msg)






    def export_clicked(self):
        pass


    def show_info(self, val) -> None:
        self.label_msg.setStyleSheet("color: blue;font-weight: bold;")
        self.label_msg.setText(val)

    def show_error(self, val) -> None:
        self.label_msg.setStyleSheet("color: red;font-weight: bold;")
        self.label_msg.setText(val)

    def get_clean_columns(self):
        return self.parent.get_df_columns()

    def get_df(self):
        return self.parent.get_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df, inplace_index=False, drop_index=False)

    def get_table(self):
        return self.parent.get_table_widget()
