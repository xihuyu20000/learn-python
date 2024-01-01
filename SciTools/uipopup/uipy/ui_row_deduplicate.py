# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'row_deduplicate.ui'
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
        Form.resize(700, 242)
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
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.btn_ok = QPushButton(self.frame_2)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(28, 177,\n"
"                                        245);\n"
"                                    ")

        self.verticalLayout_2.addWidget(self.btn_ok)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u884c\u53bb\u91cd", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u591a\u9009", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5982\u679c\u9009\u62e9\u7684\u5217\u7684\u503c\u5b8c\u5168\u76f8\u540c\uff0c\u53ea\u4fdd\u7559\u7b2c\u4e00\u884c", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

