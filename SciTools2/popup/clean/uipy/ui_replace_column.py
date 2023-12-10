# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'replace_column.ui'
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
        Form.resize(591, 443)
        self.horizontalLayout_6 = QHBoxLayout(Form)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.column_widget = QListWidget(self.frame)
        self.column_widget.setObjectName(u"column_widget")
        self.column_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.column_widget)


        self.horizontalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabwidget = QTabWidget(self.frame_2)
        self.tabwidget.setObjectName(u"tabwidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.old_lineEdit = QLineEdit(self.frame_5)
        self.old_lineEdit.setObjectName(u"old_lineEdit")

        self.horizontalLayout_2.addWidget(self.old_lineEdit)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.new_lineEdit = QLineEdit(self.frame_6)
        self.new_lineEdit.setObjectName(u"new_lineEdit")

        self.horizontalLayout_4.addWidget(self.new_lineEdit)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.tabwidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 0, 232, 48))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.other_linedit = QLineEdit(self.frame_4)
        self.other_linedit.setObjectName(u"other_linedit")

        self.horizontalLayout_3.addWidget(self.other_linedit)

        self.frame_7 = QFrame(self.tab_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 60, 220, 43))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.rbt00 = QRadioButton(self.frame_7)
        self.rbt00.setObjectName(u"rbt00")
        self.rbt00.setChecked(True)

        self.horizontalLayout_5.addWidget(self.rbt00)

        self.rbt11 = QRadioButton(self.frame_7)
        self.rbt11.setObjectName(u"rbt11")

        self.horizontalLayout_5.addWidget(self.rbt11)

        self.tabwidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabwidget)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rbt0 = QRadioButton(self.frame_3)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rbt0)
        self.rbt0.setObjectName(u"rbt0")
        self.rbt0.setChecked(True)

        self.horizontalLayout.addWidget(self.rbt0)

        self.rbt1 = QRadioButton(self.frame_3)
        self.buttonGroup.addButton(self.rbt1)
        self.rbt1.setObjectName(u"rbt1")

        self.horizontalLayout.addWidget(self.rbt1)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.ok_button = QPushButton(self.frame_2)
        self.ok_button.setObjectName(u"ok_button")

        self.verticalLayout_3.addWidget(self.ok_button)


        self.horizontalLayout_6.addWidget(self.frame_2)


        self.retranslateUi(Form)

        self.tabwidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u66ff\u6362\u503c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u591a\u9009", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u539f\u503c", None))
        self.old_lineEdit.setText(QCoreApplication.translate("Form", u",", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u65b0\u503c", None))
        self.new_lineEdit.setText(QCoreApplication.translate("Form", u";", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u65b9\u5f0f1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5b57\u7b26", None))
        self.rbt00.setText(QCoreApplication.translate("Form", u"\u4fdd\u7559", None))
        self.rbt11.setText(QCoreApplication.translate("Form", u"\u820d\u5f03", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u65b9\u5f0f2", None))
        self.rbt0.setText(QCoreApplication.translate("Form", u"\u66ff\u6362\u5f53\u524d\u503c", None))
        self.rbt1.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u65b0\u5217", None))
        self.ok_button.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

