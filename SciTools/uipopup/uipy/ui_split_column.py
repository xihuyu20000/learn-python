# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'split_column.ui'
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
        Form.resize(731, 344)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.cb1 = QComboBox(self.frame_3)
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.setObjectName(u"cb1")

        self.horizontalLayout.addWidget(self.cb1)

        self.le1 = QLineEdit(self.frame_3)
        self.le1.setObjectName(u"le1")

        self.horizontalLayout.addWidget(self.le1)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.cb2 = QComboBox(self.frame_4)
        self.cb2.addItem("")
        self.cb2.addItem("")
        self.cb2.setObjectName(u"cb2")

        self.horizontalLayout_2.addWidget(self.cb2)

        self.le2 = QLineEdit(self.frame_4)
        self.le2.setObjectName(u"le2")

        self.horizontalLayout_2.addWidget(self.le2)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u62c6\u5206\u5217", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53ea\u80fd\u5355\u9009", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u62c6\u5206\u65b9\u5f0f", None))
        self.cb1.setItemText(0, QCoreApplication.translate("Form", u"\u6309\u5206\u9694\u7b26", None))
        self.cb1.setItemText(1, QCoreApplication.translate("Form", u"\u6309\u5b57\u7b26\u6570", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u6309\u5206\u9694\u7b26\uff0c\u540e\u9762\u586b\u5199\u5b57\u7b26\uff1b\u6309\u5b57\u7b26\u6570\uff0c\u540e\u9762\u586b\u5199\u6570\u5b57", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u62c6\u5206\u7ed3\u679c", None))
        self.cb2.setItemText(0, QCoreApplication.translate("Form", u"\u524dN\u4e2a\u5217", None))
        self.cb2.setItemText(1, QCoreApplication.translate("Form", u"\u7b2cN\u5217", None))

        self.pushButton.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

