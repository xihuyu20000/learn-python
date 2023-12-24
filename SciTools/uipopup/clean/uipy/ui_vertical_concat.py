# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vertical_concat.ui'
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
        Form.resize(462, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.btn_start = QPushButton(Form)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);")

        self.verticalLayout.addWidget(self.btn_start)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6570\u636e\u5408\u5e76", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6bd4\u5982\u5bf9\u77e5\u7f51\u3001\u4e07\u65b9\u3001\u7ef4\u666e\u7684\u6570\u636e\u8fdb\u884c\u5408\u5e76\uff0c\u4f7f\u7528\u6b64\u529f\u80fd", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5982\u679c\u540c\u4e00\u5185\u5bb9\u4f7f\u7528\u4e0d\u540c\u5217\u540d\uff0c\u8bf7\u7edf\u4e00\u5217\u540d\u540e\u518d\u4f7f\u7528\u6b64\u529f\u80fd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u683c\u5f0f\u5fc5\u987b\u662fcsv\u7c7b\u578b\uff0c\u4f7f\u7528\u9017\u53f7\u505a\u4e3a\u5206\u9694\u7b26\uff0c\u5176\u4ed6\u683c\u5f0f\u4e0d\u652f\u6301", None))
        self.btn_start.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

