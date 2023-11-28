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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QSizePolicy, QSpacerItem, QSplitter,
    QStatusBar, QTableView, QToolBar, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1096, 652)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_workspace_set = QAction(MainWindow)
        self.action_workspace_set.setObjectName(u"action_workspace_set")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_pubmed = QAction(MainWindow)
        self.action_pubmed.setObjectName(u"action_pubmed")
        self.action_cssci = QAction(MainWindow)
        self.action_cssci.setObjectName(u"action_cssci")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter_3 = QSplitter(self.frame_5)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.frame_3 = QFrame(self.splitter_3)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.frame_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_datafiles_dir = QToolButton(self.frame)
        self.btn_datafiles_dir.setObjectName(u"btn_datafiles_dir")

        self.horizontalLayout.addWidget(self.btn_datafiles_dir)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_datafiles_load = QToolButton(self.frame)
        self.btn_datafiles_load.setObjectName(u"btn_datafiles_load")

        self.horizontalLayout.addWidget(self.btn_datafiles_load)

        self.btn_datafiles_combine = QToolButton(self.frame)
        self.btn_datafiles_combine.setObjectName(u"btn_datafiles_combine")

        self.horizontalLayout.addWidget(self.btn_datafiles_combine)

        self.btn_datafiles_parse_cnki = QToolButton(self.frame)
        self.btn_datafiles_parse_cnki.setObjectName(u"btn_datafiles_parse_cnki")

        self.horizontalLayout.addWidget(self.btn_datafiles_parse_cnki)

        self.btn_datafiles_parse_wos = QToolButton(self.frame)
        self.btn_datafiles_parse_wos.setObjectName(u"btn_datafiles_parse_wos")

        self.horizontalLayout.addWidget(self.btn_datafiles_parse_wos)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listView_datafiles = QListView(self.frame)
        self.listView_datafiles.setObjectName(u"listView_datafiles")

        self.verticalLayout.addWidget(self.listView_datafiles)

        self.splitter.addWidget(self.frame)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_datamodel_show = QToolButton(self.frame_2)
        self.btn_datamodel_show.setObjectName(u"btn_datamodel_show")

        self.horizontalLayout_2.addWidget(self.btn_datamodel_show)

        self.toolButton_4 = QToolButton(self.frame_2)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.horizontalLayout_2.addWidget(self.toolButton_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.listView_datamodels = QListView(self.frame_2)
        self.listView_datamodels.setObjectName(u"listView_datamodels")

        self.verticalLayout_2.addWidget(self.listView_datamodels)

        self.splitter.addWidget(self.frame_2)

        self.horizontalLayout_3.addWidget(self.splitter)

        self.splitter_3.addWidget(self.frame_3)
        self.frame_4 = QFrame(self.splitter_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(9)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.frame_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.tableView_data = QTableView(self.splitter_2)
        self.tableView_data.setObjectName(u"tableView_data")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(9)
        sizePolicy3.setHeightForWidth(self.tableView_data.sizePolicy().hasHeightForWidth())
        self.tableView_data.setSizePolicy(sizePolicy3)
        self.splitter_2.addWidget(self.tableView_data)
        self.plainTextEdit = QPlainTextEdit(self.splitter_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy4)
        self.plainTextEdit.setBaseSize(QSize(0, 0))
        self.splitter_2.addWidget(self.plainTextEdit)

        self.verticalLayout_4.addWidget(self.splitter_2)

        self.splitter_3.addWidget(self.frame_4)

        self.verticalLayout_6.addWidget(self.splitter_3)


        self.verticalLayout_5.addWidget(self.frame_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1096, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_6 = QMenu(self.menubar)
        self.menu_6.setObjectName(u"menu_6")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMinimumSize(QSize(0, 16))
        self.toolBar.setIconSize(QSize(16, 16))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menu_4.addAction(self.action_workspace_set)
        self.menu_6.addAction(self.action_2)
        self.menu_6.addAction(self.action_5)
        self.menu_6.addAction(self.action_pubmed)
        self.menu_6.addAction(self.action_cssci)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SciTools\u2014\u2014\u6e05\u6d17\u6570\u636e", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76\u6587\u4ef6", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6587\u4ef6", None))
        self.action_workspace_set.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790cnki", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790wos", None))
        self.action_pubmed.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790pubmed", None))
        self.action_cssci.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790cssci", None))
        self.btn_datafiles_dir.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u76ee\u5f55", None))
        self.btn_datafiles_load.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d", None))
        self.btn_datafiles_combine.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76", None))
        self.btn_datafiles_parse_cnki.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790cnki", None))
        self.btn_datafiles_parse_wos.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790wos", None))
        self.btn_datamodel_show.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8bcd\u8868", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u4f5c\u7a7a\u95f4", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_6.setTitle(QCoreApplication.translate("MainWindow", u"\u89e3\u6790", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

