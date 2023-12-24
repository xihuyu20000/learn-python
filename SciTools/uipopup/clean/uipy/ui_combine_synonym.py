# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'combine_synonym.ui'
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
        Form.resize(517, 410)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
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

        self.verticalLayout.addWidget(self.column_names)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.le1 = QLineEdit(self.frame_3)
        self.le1.setObjectName(u"le1")
        self.le1.setReadOnly(True)

        self.horizontalLayout.addWidget(self.le1)

        self.btn1 = QPushButton(self.frame_3)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.btn1)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rbt0 = QRadioButton(self.frame_4)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rbt0)
        self.rbt0.setObjectName(u"rbt0")
        self.rbt0.setChecked(True)

        self.horizontalLayout_2.addWidget(self.rbt0)

        self.rbt1 = QRadioButton(self.frame_4)
        self.buttonGroup.addButton(self.rbt1)
        self.rbt1.setObjectName(u"rbt1")

        self.horizontalLayout_2.addWidget(self.rbt1)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.btn_ok = QPushButton(self.frame_2)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);")

        self.verticalLayout_2.addWidget(self.btn_ok)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5408\u5e76\u8bcd", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u591a\u9009", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bcd\u5178", None))
        self.btn1.setText(QCoreApplication.translate("Form", u"...", None))
        self.rbt0.setText(QCoreApplication.translate("Form", u"\u66ff\u6362\u5f53\u524d\u503c", None))
        self.rbt1.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u65b0\u5217", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

