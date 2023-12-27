# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compare_columns.ui'
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
        Form.resize(467, 410)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.column_names = QListWidget(self.frame)
        self.column_names.setObjectName(u"column_names")
        self.column_names.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.column_names)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_reset = QPushButton(self.frame_2)
        self.btn_reset.setObjectName(u"btn_reset")

        self.verticalLayout_2.addWidget(self.btn_reset)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.btn_ok = QPushButton(self.frame_2)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);")

        self.verticalLayout_2.addWidget(self.btn_ok)

        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5bf9\u6bd4\u5217", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53ea\u80fd\u9009\u62e9\u4e24\u5217", None))
        self.btn_reset.setText(QCoreApplication.translate("Form", u"\u6062\u590d\u989c\u8272", None))
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"\u53ea\u80fd\u5bf9\u4e24\u4e2a\u5217\u8fdb\u884c\u5bf9\u6bd4\uff0c\u4e0d\u540c\u503c\u4f7f\u7528\u989c\u8272\u6807\u6ce8",
                                                        None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi
