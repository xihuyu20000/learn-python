# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'count_stat.ui'
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
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.threhold_spinBox = QSpinBox(self.frame_3)
        self.threhold_spinBox.setObjectName(u"threhold_spinBox")

        self.horizontalLayout_2.addWidget(self.threhold_spinBox)

        self.horizontalSpacer = QSpacerItem(37, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_ok = QPushButton(self.frame_4)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);")

        self.horizontalLayout_3.addWidget(self.btn_ok)

        self.btn_export = QPushButton(self.frame_4)
        self.btn_export.setObjectName(u"btn_export")

        self.horizontalLayout_3.addWidget(self.btn_export)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8bcd\u9891\u7edf\u8ba1", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u591a\u9009", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u4e00\u9879\uff0c\u663e\u793a\u5728\u8868\u683c\u4e2d", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u591a\u9879\uff0c\u53ea\u80fd\u5bfc\u51faExcel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7edf\u8ba1\u9608\u503c>=", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.btn_export.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
    # retranslateUi

