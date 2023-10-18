# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolbar_open = QPushButton(self.frame)
        self.toolbar_open.setObjectName(u"toolbar_open")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolbar_open.sizePolicy().hasHeightForWidth())
        self.toolbar_open.setSizePolicy(sizePolicy1)
        self.toolbar_open.setMaximumSize(QSize(16777215, 29))
        font = QFont()
        font.setPointSize(12)
        self.toolbar_open.setFont(font)

        self.horizontalLayout.addWidget(self.toolbar_open)

        self.toolbar_save = QPushButton(self.frame)
        self.toolbar_save.setObjectName(u"toolbar_save")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolbar_save.sizePolicy().hasHeightForWidth())
        self.toolbar_save.setSizePolicy(sizePolicy2)
        self.toolbar_save.setFont(font)

        self.horizontalLayout.addWidget(self.toolbar_save)

        self.toolbar_saveas = QPushButton(self.frame)
        self.toolbar_saveas.setObjectName(u"toolbar_saveas")
        self.toolbar_saveas.setFont(font)

        self.horizontalLayout.addWidget(self.toolbar_saveas)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.toolbar_previous = QPushButton(self.frame)
        self.toolbar_previous.setObjectName(u"toolbar_previous")
        self.toolbar_previous.setFont(font)

        self.horizontalLayout.addWidget(self.toolbar_previous)

        self.toolbar_next = QPushButton(self.frame)
        self.toolbar_next.setObjectName(u"toolbar_next")
        self.toolbar_next.setFont(font)

        self.horizontalLayout.addWidget(self.toolbar_next)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.act_resize = QPushButton(self.frame_3)
        self.act_resize.setObjectName(u"act_resize")

        self.verticalLayout_2.addWidget(self.act_resize)

        self.act1 = QPushButton(self.frame_3)
        self.act1.setObjectName(u"act1")

        self.verticalLayout_2.addWidget(self.act1)

        self.act2 = QPushButton(self.frame_3)
        self.act2.setObjectName(u"act2")

        self.verticalLayout_2.addWidget(self.act2)

        self.act3 = QPushButton(self.frame_3)
        self.act3.setObjectName(u"act3")

        self.verticalLayout_2.addWidget(self.act3)

        self.verticalSpacer = QSpacerItem(20, 360, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.canvas = QLabel(self.frame_4)
        self.canvas.setObjectName(u"canvas")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy3)
        self.canvas.setMaximumSize(QSize(1000, 800))
        self.canvas.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.canvas)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.stackedPanels = QStackedWidget(self.frame_2)
        self.stackedPanels.setObjectName(u"stackedPanels")
        self.stackedPanels.setMinimumSize(QSize(200, 0))
        self.stackedPanels.setMaximumSize(QSize(200, 16777215))
        self.stackedPanels.setFrameShape(QFrame.Box)
        self.stackedPanels.setFrameShadow(QFrame.Raised)
        self.page0 = QWidget()
        self.page0.setObjectName(u"page0")
        self.text_new_width = QTextEdit(self.page0)
        self.text_new_width.setObjectName(u"text_new_width")
        self.text_new_width.setGeometry(QRect(40, 20, 61, 21))
        self.text_new_height = QTextEdit(self.page0)
        self.text_new_height.setObjectName(u"text_new_height")
        self.text_new_height.setGeometry(QRect(40, 50, 61, 21))
        self.label_2 = QLabel(self.page0)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 31, 16))
        self.label = QLabel(self.page0)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 31, 16))
        self.btn_change_size = QPushButton(self.page0)
        self.btn_change_size.setObjectName(u"btn_change_size")
        self.btn_change_size.setGeometry(QRect(114, 20, 61, 51))
        self.stackedPanels.addWidget(self.page0)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.stackedPanels.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.stackedPanels.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.stackedPanels.addWidget(self.page3)

        self.horizontalLayout_2.addWidget(self.stackedPanels)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedPanels.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolbar_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.toolbar_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.toolbar_saveas.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.toolbar_previous.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u6b65", None))
        self.toolbar_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
        self.act_resize.setText(QCoreApplication.translate("MainWindow", u"\u6539\u53d8\u5927\u5c0f", None))
        self.act1.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.act2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.act3.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.canvas.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u5ea6", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\u5ea6", None))
        self.btn_change_size.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
    # retranslateUi

