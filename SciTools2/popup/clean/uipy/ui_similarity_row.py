# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'similarity_row.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(548, 482)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.column_names = QListWidget(self.frame_4)
        self.column_names.setObjectName(u"column_names")
        self.column_names.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.column_names)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.slider_horizon = QSlider(self.frame_5)
        self.slider_horizon.setObjectName(u"slider_horizon")
        self.slider_horizon.setMinimum(1)
        self.slider_horizon.setMaximum(100)
        self.slider_horizon.setValue(85)
        self.slider_horizon.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.slider_horizon)

        self.vaLable = QLabel(self.frame_5)
        self.vaLable.setObjectName(u"vaLable")
        self.vaLable.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.vaLable)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.btn_ok = QPushButton(self.frame_6)
        self.btn_ok.setObjectName(u"btn_ok")

        self.verticalLayout_2.addWidget(self.btn_ok)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.btn_combine_current_group = QPushButton(self.frame)
        self.btn_combine_current_group.setObjectName(u"btn_combine_current_group")

        self.horizontalLayout.addWidget(self.btn_combine_current_group)

        self.btn_save_current_group = QPushButton(self.frame)
        self.btn_save_current_group.setObjectName(u"btn_save_current_group")

        self.horizontalLayout.addWidget(self.btn_save_current_group)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.group_table = QTableView(Form)
        self.group_table.setObjectName(u"group_table")

        self.verticalLayout_4.addWidget(self.group_table)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u76f8\u4f3c\u5ea6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u591a\u9009", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6309\u7167\u9009\u7684\u5217\uff0c\u8fdb\u884c\u76f8\u4f3c\u5ea6\u5224\u65ad", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u76f8\u4f3c\u5ea6\u9608\u503c", None))
        self.vaLable.setText(QCoreApplication.translate("Form", u"85", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.btn_combine_current_group.setText(QCoreApplication.translate("Form", u"\u5408\u5e76\u8be5\u5206\u7ec4", None))
        self.btn_save_current_group.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u4fee\u6539", None))
    # retranslateUi

