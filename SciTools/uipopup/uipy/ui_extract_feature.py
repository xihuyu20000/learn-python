# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extract_feature.ui'
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
        Form.resize(658, 597)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.listWidget_colnames = QListWidget(self.frame)
        self.listWidget_colnames.setObjectName(u"listWidget_colnames")
        self.listWidget_colnames.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_2.addWidget(self.listWidget_colnames)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.listWidget_speech = QListWidget(self.frame_4)
        self.listWidget_speech.setObjectName(u"listWidget_speech")
        self.listWidget_speech.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_3.addWidget(self.listWidget_speech)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox_threshold = QSpinBox(self.frame_3)
        self.spinBox_threshold.setObjectName(u"spinBox_threshold")
        self.spinBox_threshold.setValue(5)

        self.horizontalLayout_2.addWidget(self.spinBox_threshold)


        self.verticalLayout.addWidget(self.frame_3)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u63d0\u53d6\u7279\u5f81\u8bcd", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u591a\u9009", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8bcd\u6027\u9009\u62e9\u3010\u53ef\u4ee5\u591a\u9009\u3011", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7279\u5f81\u8bcd\u6570\u91cf:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4f1a\u4f7f\u7528\u5230\u505c\u7528\u8bcd\u8868\u548c\u53d7\u63a7\u8bcd\u8868", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

