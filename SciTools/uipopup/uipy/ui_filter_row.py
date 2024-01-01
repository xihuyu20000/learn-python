# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter_row.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 280)
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
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.checkBox_null = QCheckBox(self.frame_7)
        self.checkBox_null.setObjectName(u"checkBox_null")

        self.horizontalLayout_4.addWidget(self.checkBox_null)

        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_tougao = QCheckBox(self.frame_5)
        self.checkBox_tougao.setObjectName(u"checkBox_tougao")
        self.checkBox_tougao.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox_tougao)

        self.checkBox_bianjibu = QCheckBox(self.frame_5)
        self.checkBox_bianjibu.setObjectName(u"checkBox_bianjibu")
        self.checkBox_bianjibu.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox_bianjibu)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_ok = QPushButton(self.frame)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                  "                                                                background-color: rgb(28, 177, 245);\n"
                                  "                                                            ")

        self.horizontalLayout.addWidget(self.btn_ok)

        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_3.addWidget(self.frame_6)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8fc7\u6ee4\u884c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u591a\u9009", None))
        self.label_2.setText(
            QCoreApplication.translate("Form", u"\u67e5\u770b\u540e\uff0c\u53ef\u4ee5\u5220\u9664", None))
        self.checkBox_null.setText(QCoreApplication.translate("Form", u"\u542b\u6709\u7a7a\u503c", None))
        self.checkBox_tougao.setText(QCoreApplication.translate("Form", u"\u542b\u6709\u6295\u7a3f", None))
        self.checkBox_bianjibu.setText(
            QCoreApplication.translate("Form", u"\u542b\u6709\u300a\u7f16\u8f91\u90e8\u300b", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
    # retranslateUi
