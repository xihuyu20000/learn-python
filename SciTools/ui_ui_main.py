# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QMenuBar, QSizePolicy, QSpacerItem, QStackedWidget,
                               QStatusBar, QToolButton, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(80, 0))
        self.frame.setMaximumSize(QSize(80, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gbl_btn_menu = QToolButton(self.frame)
        self.gbl_btn_menu.setObjectName(u"gbl_btn_menu")
        self.gbl_btn_menu.setMinimumSize(QSize(60, 70))
        self.gbl_btn_menu.setMaximumSize(QSize(60, 70))
        font = QFont()
        font.setBold(True)
        self.gbl_btn_menu.setFont(font)
        self.gbl_btn_menu.setCursor(QCursor(Qt.OpenHandCursor))
        icon = QIcon()
        icon.addFile(u"icons/biaochaxun.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gbl_btn_menu.setIcon(icon)
        self.gbl_btn_menu.setIconSize(QSize(50, 50))
        self.gbl_btn_menu.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.gbl_btn_menu)

        self.gbl_btn_my_analysis = QToolButton(self.frame)
        self.gbl_btn_my_analysis.setObjectName(u"gbl_btn_my_analysis")
        self.gbl_btn_my_analysis.setMinimumSize(QSize(60, 70))
        self.gbl_btn_my_analysis.setMaximumSize(QSize(60, 70))
        self.gbl_btn_my_analysis.setFont(font)
        self.gbl_btn_my_analysis.setCursor(QCursor(Qt.OpenHandCursor))
        self.gbl_btn_my_analysis.setIcon(icon)
        self.gbl_btn_my_analysis.setIconSize(QSize(50, 50))
        self.gbl_btn_my_analysis.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.gbl_btn_my_analysis)

        self.gbl_btn_public_data = QToolButton(self.frame)
        self.gbl_btn_public_data.setObjectName(u"gbl_btn_public_data")
        self.gbl_btn_public_data.setMinimumSize(QSize(60, 70))
        self.gbl_btn_public_data.setMaximumSize(QSize(60, 70))
        self.gbl_btn_public_data.setFont(font)
        self.gbl_btn_public_data.setCursor(QCursor(Qt.OpenHandCursor))
        self.gbl_btn_public_data.setIcon(icon)
        self.gbl_btn_public_data.setIconSize(QSize(50, 50))
        self.gbl_btn_public_data.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.gbl_btn_public_data)

        self.gbl_btn_mis = QToolButton(self.frame)
        self.gbl_btn_mis.setObjectName(u"gbl_btn_mis")
        self.gbl_btn_mis.setMinimumSize(QSize(60, 70))
        self.gbl_btn_mis.setMaximumSize(QSize(60, 70))
        self.gbl_btn_mis.setFont(font)
        self.gbl_btn_mis.setCursor(QCursor(Qt.OpenHandCursor))
        self.gbl_btn_mis.setIcon(icon)
        self.gbl_btn_mis.setIconSize(QSize(50, 50))
        self.gbl_btn_mis.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.gbl_btn_mis)

        self.gbl_btn_user_center = QToolButton(self.frame)
        self.gbl_btn_user_center.setObjectName(u"gbl_btn_user_center")
        self.gbl_btn_user_center.setMinimumSize(QSize(60, 70))
        self.gbl_btn_user_center.setMaximumSize(QSize(60, 70))
        self.gbl_btn_user_center.setFont(font)
        self.gbl_btn_user_center.setCursor(QCursor(Qt.OpenHandCursor))
        self.gbl_btn_user_center.setIcon(icon)
        self.gbl_btn_user_center.setIconSize(QSize(50, 50))
        self.gbl_btn_user_center.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.gbl_btn_user_center)

        self.gbl_btn_bi_tool = QToolButton(self.frame)
        self.gbl_btn_bi_tool.setObjectName(u"gbl_btn_bi_tool")
        self.gbl_btn_bi_tool.setMinimumSize(QSize(60, 70))
        self.gbl_btn_bi_tool.setMaximumSize(QSize(60, 70))
        self.gbl_btn_bi_tool.setFont(font)
        self.gbl_btn_bi_tool.setCursor(QCursor(Qt.OpenHandCursor))
        self.gbl_btn_bi_tool.setIcon(icon)
        self.gbl_btn_bi_tool.setIconSize(QSize(50, 50))
        self.gbl_btn_bi_tool.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.gbl_btn_bi_tool)

        self.verticalSpacer = QSpacerItem(20, 61, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout.addWidget(self.frame)

        self.mainContainer = QStackedWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.page_menu = QWidget()
        self.page_menu.setObjectName(u"page_menu")
        self.mainContainer.addWidget(self.page_menu)
        self.page_my_analysis = QWidget()
        self.page_my_analysis.setObjectName(u"page_my_analysis")
        self.mainContainer.addWidget(self.page_my_analysis)
        self.page_public_data = QWidget()
        self.page_public_data.setObjectName(u"page_public_data")
        self.mainContainer.addWidget(self.page_public_data)
        self.page_mis = QWidget()
        self.page_mis.setObjectName(u"page_mis")
        self.mainContainer.addWidget(self.page_mis)
        self.page_user_center = QWidget()
        self.page_user_center.setObjectName(u"page_user_center")
        self.mainContainer.addWidget(self.page_user_center)
        self.page_bi_tool = QWidget()
        self.page_bi_tool.setObjectName(u"page_bi_tool")
        self.mainContainer.addWidget(self.page_bi_tool)

        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.mainContainer.setCurrentIndex(4)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gbl_btn_menu.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u5f55", None))
        self.gbl_btn_my_analysis.setText(QCoreApplication.translate("MainWindow", u"\u6211\u7684\u5206\u6790", None))
        self.gbl_btn_public_data.setText(QCoreApplication.translate("MainWindow", u"\u516c\u5171\u6570\u636e", None))
        self.gbl_btn_mis.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u7cfb\u7edf", None))
        self.gbl_btn_user_center.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u4e2d\u5fc3", None))
        self.gbl_btn_bi_tool.setText(QCoreApplication.translate("MainWindow", u"BI\u5de5\u5177", None))
    # retranslateUi
