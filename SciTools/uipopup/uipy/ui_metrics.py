# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'metrics.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from core.toolkit import TableKit


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1146, 730)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_stat_yearly = QPushButton(self.frame)
        self.btn_stat_yearly.setObjectName(u"btn_stat_yearly")

        self.verticalLayout_2.addWidget(self.btn_stat_yearly)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 5))

        self.verticalLayout_2.addWidget(self.label_4)

        self.btn_stat_kw = QPushButton(self.frame)
        self.btn_stat_kw.setObjectName(u"btn_stat_kw")

        self.verticalLayout_2.addWidget(self.btn_stat_kw)

        self.btn_stat_author = QPushButton(self.frame)
        self.btn_stat_author.setObjectName(u"btn_stat_author")

        self.verticalLayout_2.addWidget(self.btn_stat_author)

        self.btn_stat_org = QPushButton(self.frame)
        self.btn_stat_org.setObjectName(u"btn_stat_org")

        self.verticalLayout_2.addWidget(self.btn_stat_org)

        self.btn_stat_source = QPushButton(self.frame)
        self.btn_stat_source.setObjectName(u"btn_stat_source")

        self.verticalLayout_2.addWidget(self.btn_stat_source)

        self.btn_stat_country = QPushButton(self.frame)
        self.btn_stat_country.setObjectName(u"btn_stat_country")

        self.verticalLayout_2.addWidget(self.btn_stat_country)

        self.btn_stat_subject = QPushButton(self.frame)
        self.btn_stat_subject.setObjectName(u"btn_stat_subject")

        self.verticalLayout_2.addWidget(self.btn_stat_subject)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 5))

        self.verticalLayout_2.addWidget(self.label_3)

        self.btn_cocon_kw = QPushButton(self.frame)
        self.btn_cocon_kw.setObjectName(u"btn_cocon_kw")

        self.verticalLayout_2.addWidget(self.btn_cocon_kw)

        self.btn_cocon_author = QPushButton(self.frame)
        self.btn_cocon_author.setObjectName(u"btn_cocon_author")

        self.verticalLayout_2.addWidget(self.btn_cocon_author)

        self.btn_cocon_org = QPushButton(self.frame)
        self.btn_cocon_org.setObjectName(u"btn_cocon_org")

        self.verticalLayout_2.addWidget(self.btn_cocon_org)

        self.btn_cocon_country = QPushButton(self.frame)
        self.btn_cocon_country.setObjectName(u"btn_cocon_country")

        self.verticalLayout_2.addWidget(self.btn_cocon_country)

        self.btn_cocon_subject = QPushButton(self.frame)
        self.btn_cocon_subject.setObjectName(u"btn_cocon_subject")

        self.verticalLayout_2.addWidget(self.btn_cocon_subject)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 5))

        self.verticalLayout_2.addWidget(self.label_2)

        self.btn_matrix2_doc_kw = QPushButton(self.frame)
        self.btn_matrix2_doc_kw.setObjectName(u"btn_matrix2_doc_kw")

        self.verticalLayout_2.addWidget(self.btn_matrix2_doc_kw)

        self.btn_matrix2_author_kw = QPushButton(self.frame)
        self.btn_matrix2_author_kw.setObjectName(u"btn_matrix2_author_kw")

        self.verticalLayout_2.addWidget(self.btn_matrix2_author_kw)

        self.btn_matrix2_org_kw = QPushButton(self.frame)
        self.btn_matrix2_org_kw.setObjectName(u"btn_matrix2_org_kw")

        self.verticalLayout_2.addWidget(self.btn_matrix2_org_kw)

        self.btn_matrix2_country_kw = QPushButton(self.frame)
        self.btn_matrix2_country_kw.setObjectName(u"btn_matrix2_country_kw")

        self.verticalLayout_2.addWidget(self.btn_matrix2_country_kw)

        self.btn_matrix2_subject_kw = QPushButton(self.frame)
        self.btn_matrix2_subject_kw.setObjectName(u"btn_matrix2_subject_kw")

        self.verticalLayout_2.addWidget(self.btn_matrix2_subject_kw)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 5))

        self.verticalLayout_2.addWidget(self.label)

        self.btn_coupled_author_kw = QPushButton(self.frame)
        self.btn_coupled_author_kw.setObjectName(u"btn_coupled_author_kw")

        self.verticalLayout_2.addWidget(self.btn_coupled_author_kw)

        self.btn_coupled_org_kw = QPushButton(self.frame)
        self.btn_coupled_org_kw.setObjectName(u"btn_coupled_org_kw")

        self.verticalLayout_2.addWidget(self.btn_coupled_org_kw)

        self.btn_coupled_country_kw = QPushButton(self.frame)
        self.btn_coupled_country_kw.setObjectName(u"btn_coupled_country_kw")

        self.verticalLayout_2.addWidget(self.btn_coupled_country_kw)

        self.btn_coupled_subject_kw = QPushButton(self.frame)
        self.btn_coupled_subject_kw.setObjectName(u"btn_coupled_subject_kw")

        self.verticalLayout_2.addWidget(self.btn_coupled_subject_kw)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 30))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(400, 30))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_15)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_13.addWidget(self.label_13)

        self.lineEdit_axis_X = QLineEdit(self.frame_15)
        self.lineEdit_axis_X.setObjectName(u"lineEdit_axis_X")
        self.lineEdit_axis_X.setMinimumSize(QSize(80, 0))
        self.lineEdit_axis_X.setMaximumSize(QSize(99999, 30))

        self.horizontalLayout_13.addWidget(self.lineEdit_axis_X)

        self.label_14 = QLabel(self.frame_15)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_13.addWidget(self.label_14)

        self.lineEdit_axis_Y = QLineEdit(self.frame_15)
        self.lineEdit_axis_Y.setObjectName(u"lineEdit_axis_Y")
        self.lineEdit_axis_Y.setMinimumSize(QSize(80, 0))
        self.lineEdit_axis_Y.setMaximumSize(QSize(99999, 30))

        self.horizontalLayout_13.addWidget(self.lineEdit_axis_Y)

        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.lineEdit_value = QLineEdit(self.frame_15)
        self.lineEdit_value.setObjectName(u"lineEdit_value")
        self.lineEdit_value.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_13.addWidget(self.lineEdit_value)

        self.btn_2_matrix = QPushButton(self.frame_15)
        self.btn_2_matrix.setObjectName(u"btn_2_matrix")
        self.btn_2_matrix.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_13.addWidget(self.btn_2_matrix)


        self.horizontalLayout_14.addWidget(self.frame_15)

        self.horizontalSpacer_2 = QSpacerItem(413, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)

        self.btn_graph = QPushButton(self.frame_14)
        self.btn_graph.setObjectName(u"btn_graph")
        self.btn_graph.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_14.addWidget(self.btn_graph)


        self.verticalLayout.addWidget(self.frame_14)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.frame_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame_tablekit = TableKit(self.splitter)
        self.frame_tablekit.setObjectName(u"frame_tablekit")
        self.frame_tablekit.setFrameShape(QFrame.StyledPanel)
        self.frame_tablekit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_tablekit)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.frame_tablekit)
        self.frame_5 = QFrame(self.splitter)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(250, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_field_keyword = QLineEdit(self.frame_7)
        self.lineEdit_field_keyword.setObjectName(u"lineEdit_field_keyword")

        self.horizontalLayout_6.addWidget(self.lineEdit_field_keyword)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.lineEdit_field_title = QLineEdit(self.frame_13)
        self.lineEdit_field_title.setObjectName(u"lineEdit_field_title")

        self.horizontalLayout_12.addWidget(self.lineEdit_field_title)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_field_year = QLineEdit(self.frame_6)
        self.lineEdit_field_year.setObjectName(u"lineEdit_field_year")

        self.horizontalLayout_5.addWidget(self.lineEdit_field_year)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_field_author = QLineEdit(self.frame_8)
        self.lineEdit_field_author.setObjectName(u"lineEdit_field_author")

        self.horizontalLayout_7.addWidget(self.lineEdit_field_author)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_field_org = QLineEdit(self.frame_9)
        self.lineEdit_field_org.setObjectName(u"lineEdit_field_org")

        self.horizontalLayout_8.addWidget(self.lineEdit_field_org)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.lineEdit_field_source = QLineEdit(self.frame_12)
        self.lineEdit_field_source.setObjectName(u"lineEdit_field_source")

        self.horizontalLayout_11.addWidget(self.lineEdit_field_source)


        self.verticalLayout_3.addWidget(self.frame_12)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lineEdit_field_country = QLineEdit(self.frame_10)
        self.lineEdit_field_country.setObjectName(u"lineEdit_field_country")

        self.horizontalLayout_9.addWidget(self.lineEdit_field_country)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lineEdit_field_subject = QLineEdit(self.frame_11)
        self.lineEdit_field_subject.setObjectName(u"lineEdit_field_subject")

        self.horizontalLayout_10.addWidget(self.lineEdit_field_subject)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 5))

        self.verticalLayout_3.addWidget(self.label_16)

        self.verticalSpacer_2 = QSpacerItem(20, 284, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.splitter.addWidget(self.frame_5)

        self.horizontalLayout_4.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_msg = QLabel(self.frame_4)
        self.label_msg.setObjectName(u"label_msg")
        self.label_msg.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_3.addWidget(self.label_msg)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u91cf\u7edf\u8ba1", None))
        self.btn_stat_yearly.setText(QCoreApplication.translate("Form", u"\u5386\u5e74\u53d1\u6587\u7edf\u8ba1", None))
        self.label_4.setText("")
        self.btn_stat_kw.setText(QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd\u7edf\u8ba1", None))
        self.btn_stat_author.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7edf\u8ba1", None))
        self.btn_stat_org.setText(QCoreApplication.translate("Form", u"\u673a\u6784\u7edf\u8ba1", None))
        self.btn_stat_source.setText(QCoreApplication.translate("Form", u"\u671f\u520a\u7edf\u8ba1", None))
        self.btn_stat_country.setText(QCoreApplication.translate("Form", u"\u56fd\u5bb6\u7edf\u8ba1", None))
        self.btn_stat_subject.setText(QCoreApplication.translate("Form", u"\u5b66\u79d1\u7edf\u8ba1", None))
        self.label_3.setText("")
        self.btn_cocon_kw.setText(QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd\u5171\u73b0\u77e9\u9635", None))
        self.btn_cocon_author.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u5171\u73b0\u77e9\u9635", None))
        self.btn_cocon_org.setText(QCoreApplication.translate("Form", u"\u673a\u6784\u5171\u73b0\u77e9\u9635", None))
        self.btn_cocon_country.setText(QCoreApplication.translate("Form", u"\u56fd\u5bb6\u5171\u73b0\u77e9\u9635", None))
        self.btn_cocon_subject.setText(QCoreApplication.translate("Form", u"\u5b66\u79d1\u5171\u73b0\u77e9\u9635", None))
        self.label_2.setText("")
        self.btn_matrix2_doc_kw.setText(QCoreApplication.translate("Form", u"\u8bcd\u7bc7\u77e9\u9635", None))
        self.btn_matrix2_author_kw.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u2014\u5173\u952e\u8bcd\u77e9\u9635", None))
        self.btn_matrix2_org_kw.setText(QCoreApplication.translate("Form", u"\u673a\u6784\u2014\u5173\u952e\u8bcd\u77e9\u9635", None))
        self.btn_matrix2_country_kw.setText(QCoreApplication.translate("Form", u"\u56fd\u5bb6\u2014\u5173\u952e\u8bcd\u77e9\u9635", None))
        self.btn_matrix2_subject_kw.setText(QCoreApplication.translate("Form", u"\u5b66\u79d1\u2014\u5173\u952e\u8bcd\u77e9\u9635", None))
        self.label.setText("")
        self.btn_coupled_author_kw.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u2014\u5173\u952e\u8bcd\u8026\u5408\u77e9\u9635", None))
        self.btn_coupled_org_kw.setText(QCoreApplication.translate("Form", u"\u673a\u6784\u2014\u5173\u952e\u8bcd\u8026\u5408\u77e9\u9635", None))
        self.btn_coupled_country_kw.setText(QCoreApplication.translate("Form", u"\u56fd\u5bb6\u2014\u5173\u952e\u8bcd\u8026\u5408\u77e9\u9635", None))
        self.btn_coupled_subject_kw.setText(QCoreApplication.translate("Form", u"\u5b66\u79d1\u2014\u5173\u952e\u8bcd\u8026\u5408\u77e9\u9635", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u6a2a\u8f74", None))
        self.lineEdit_axis_X.setText(QCoreApplication.translate("Form", u"field1", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u7eb5\u8f74", None))
        self.lineEdit_axis_Y.setText(QCoreApplication.translate("Form", u"field2", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u503c", None))
        self.lineEdit_value.setText(QCoreApplication.translate("Form", u"times", None))
        self.btn_2_matrix.setText(QCoreApplication.translate("Form", u"\u8f6c\u77e9\u9635", None))
        self.btn_graph.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u56fe\u50cf", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd\u5b57\u6bb5", None))
        self.lineEdit_field_keyword.setText(QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"  \u6807\u9898\u5b57\u6bb5", None))
        self.lineEdit_field_title.setText(QCoreApplication.translate("Form", u"\u6807\u9898", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"  \u5e74\u4efd\u5b57\u6bb5", None))
        self.lineEdit_field_year.setText(QCoreApplication.translate("Form", u"\u5e74\u4efd", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"  \u4f5c\u8005\u5b57\u6bb5", None))
        self.lineEdit_field_author.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"  \u673a\u6784\u5b57\u6bb5", None))
        self.lineEdit_field_org.setText(QCoreApplication.translate("Form", u"\u4e00\u7ea7\u673a\u6784", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"  \u671f\u520a\u5b57\u6bb5", None))
        self.lineEdit_field_source.setText(QCoreApplication.translate("Form", u"\u6765\u6e90", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"  \u56fd\u5bb6\u5b57\u6bb5", None))
        self.lineEdit_field_country.setText(QCoreApplication.translate("Form", u"\u56fd\u5bb6", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"  \u5b66\u79d1\u5b57\u6bb5", None))
        self.lineEdit_field_subject.setText(QCoreApplication.translate("Form", u"\u5b66\u79d1", None))
        self.label_16.setText("")
        self.label_msg.setText("")
    # retranslateUi

