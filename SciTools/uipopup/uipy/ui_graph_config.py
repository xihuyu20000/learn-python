# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graph_config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(702, 578)
        self.verticalLayout = QVBoxLayout(widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.graph_styles_widget = QListWidget(self.tab_3)
        self.graph_styles_widget.setObjectName(u"graph_styles_widget")
        self.graph_styles_widget.setGeometry(QRect(0, 0, 331, 491))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 21, 661, 47))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.comboBox_graph_x_axis = QComboBox(self.frame_5)
        self.comboBox_graph_x_axis.setObjectName(u"comboBox_graph_x_axis")

        self.horizontalLayout_5.addWidget(self.comboBox_graph_x_axis)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.comboBox_graph_y_axis = QComboBox(self.frame_6)
        self.comboBox_graph_y_axis.setObjectName(u"comboBox_graph_y_axis")

        self.horizontalLayout_6.addWidget(self.comboBox_graph_y_axis)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.tab_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 60, 661, 50))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.comboBox_graph_orderby = QComboBox(self.frame_10)
        self.comboBox_graph_orderby.addItem("")
        self.comboBox_graph_orderby.addItem("")
        self.comboBox_graph_orderby.addItem("")
        self.comboBox_graph_orderby.setObjectName(u"comboBox_graph_orderby")

        self.horizontalLayout_8.addWidget(self.comboBox_graph_orderby)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_7.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.spinBox_graph_stat_threshold = QSpinBox(self.frame_11)
        self.spinBox_graph_stat_threshold.setObjectName(u"spinBox_graph_stat_threshold")
        self.spinBox_graph_stat_threshold.setValue(0)

        self.horizontalLayout_9.addWidget(self.spinBox_graph_stat_threshold)

        self.horizontalSpacer_8 = QSpacerItem(76, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_7.addWidget(self.frame_11)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 661, 72))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.slider_canvas_width = QSlider(self.frame)
        self.slider_canvas_width.setObjectName(u"slider_canvas_width")
        self.slider_canvas_width.setMinimum(100)
        self.slider_canvas_width.setMaximum(2000)
        self.slider_canvas_width.setPageStep(50)
        self.slider_canvas_width.setValue(900)
        self.slider_canvas_width.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider_canvas_width)

        self.label_canvas_width = QLabel(self.frame)
        self.label_canvas_width.setObjectName(u"label_canvas_width")

        self.horizontalLayout.addWidget(self.label_canvas_width)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.slider_canvas_height = QSlider(self.frame_2)
        self.slider_canvas_height.setObjectName(u"slider_canvas_height")
        self.slider_canvas_height.setMinimum(100)
        self.slider_canvas_height.setMaximum(1500)
        self.slider_canvas_height.setPageStep(50)
        self.slider_canvas_height.setValue(600)
        self.slider_canvas_height.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.slider_canvas_height)

        self.label_canvas_height = QLabel(self.frame_2)
        self.label_canvas_height.setObjectName(u"label_canvas_height")

        self.horizontalLayout_2.addWidget(self.label_canvas_height)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.btn_ok = QPushButton(widget)
        self.btn_ok.setObjectName(u"btn_ok")

        self.verticalLayout.addWidget(self.btn_ok)

        self.retranslateUi(widget)
        self.slider_canvas_width.valueChanged.connect(self.label_canvas_width.setNum)
        self.slider_canvas_height.valueChanged.connect(self.label_canvas_height.setNum)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(widget)

    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u56fe\u8868\u914d\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QCoreApplication.translate("widget", u"\u56fe\u8868\u7c7b\u578b", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"\u6a2a\u8f74", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"\u7eb5\u8f74", None))
        self.label_7.setText(QCoreApplication.translate("widget", u"\u7edf\u8ba1\u503c\u6392\u5e8f", None))
        self.comboBox_graph_orderby.setItemText(0, "")
        self.comboBox_graph_orderby.setItemText(1, QCoreApplication.translate("widget", u"\u5347\u5e8f", None))
        self.comboBox_graph_orderby.setItemText(2, QCoreApplication.translate("widget", u"\u964d\u5e8f", None))

        self.label_8.setText(QCoreApplication.translate("widget", u"\u7edf\u8ba1\u9608\u503c>=", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("widget", u"\u5750\u6807\u8f74", None))
        self.label.setText(QCoreApplication.translate("widget", u"\u753b\u5e03\u5bbd\u5ea6", None))
        self.label_canvas_width.setText(QCoreApplication.translate("widget", u"900", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"\u753b\u5e03\u9ad8\u5ea6", None))
        self.label_canvas_height.setText(QCoreApplication.translate("widget", u"600", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("widget", u"\u5c3a\u5bf8\u548c\u8ddd\u79bb", None))
        self.btn_ok.setText(QCoreApplication.translate("widget", u"OK", None))
    # retranslateUi
