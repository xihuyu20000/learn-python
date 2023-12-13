# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify_value.ui'
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
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_start = QPushButton(self.frame)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);")

        self.horizontalLayout.addWidget(self.btn_start)

        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);")

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u9ed8\u8ba4\u60c5\u51b5\u4e0b\uff0c\u503c\u4e0d\u80fd\u4fee\u6539\u3002", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u7ed3\u675f\uff0c\u8bf7\u4fdd\u5b58\u4fee\u6539\u7ed3\u679c\u3002", None))
        self.btn_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u4fee\u6539", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u4fee\u6539", None))
    # retranslateUi

