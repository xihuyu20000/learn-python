# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from core.toolkit import TableKit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1174, 872)
        self.menu_clean_save = QAction(MainWindow)
        self.menu_clean_save.setObjectName(u"menu_clean_save")
        icon = QIcon()
        icon.addFile(u"icons/xiazai.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_clean_save.setIcon(icon)
        self.menu_clean_metadata = QAction(MainWindow)
        self.menu_clean_metadata.setObjectName(u"menu_clean_metadata")
        icon1 = QIcon()
        icon1.addFile(u"icons/biaoge.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_clean_metadata.setIcon(icon1)
        self.menu_clean_rename = QAction(MainWindow)
        self.menu_clean_rename.setObjectName(u"menu_clean_rename")
        icon2 = QIcon()
        icon2.addFile(u"icons/gengduo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_clean_rename.setIcon(icon2)
        self.menu_copy_column = QAction(MainWindow)
        self.menu_copy_column.setObjectName(u"menu_copy_column")
        icon3 = QIcon()
        icon3.addFile(u"icons/lieziduan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_copy_column.setIcon(icon3)
        self.menu_split_column = QAction(MainWindow)
        self.menu_split_column.setObjectName(u"menu_split_column")
        icon4 = QIcon()
        icon4.addFile(u"icons/zhongmingming.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_split_column.setIcon(icon4)
        self.menu_replace_column = QAction(MainWindow)
        self.menu_replace_column.setObjectName(u"menu_replace_column")
        icon5 = QIcon()
        icon5.addFile(u"icons/bumenpaixu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_replace_column.setIcon(icon5)
        self.menu_combine_synonym = QAction(MainWindow)
        self.menu_combine_synonym.setObjectName(u"menu_combine_synonym")
        icon6 = QIcon()
        icon6.addFile(u"icons/shujufenxi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_combine_synonym.setIcon(icon6)
        self.menu_stop_words = QAction(MainWindow)
        self.menu_stop_words.setObjectName(u"menu_stop_words")
        icon7 = QIcon()
        icon7.addFile(u"icons/wenben.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_stop_words.setIcon(icon7)
        self.menu_compare_columns = QAction(MainWindow)
        self.menu_compare_columns.setObjectName(u"menu_compare_columns")
        self.menu_compare_columns.setIcon(icon3)
        self.menu_modify_value = QAction(MainWindow)
        self.menu_modify_value.setObjectName(u"menu_modify_value")
        icon8 = QIcon()
        icon8.addFile(u"icons/riqi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_modify_value.setIcon(icon8)
        self.menu_row_distinct = QAction(MainWindow)
        self.menu_row_distinct.setObjectName(u"menu_row_distinct")
        icon9 = QIcon()
        icon9.addFile(u"icons/shuzi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_row_distinct.setIcon(icon9)
        self.menu_row_similarity = QAction(MainWindow)
        self.menu_row_similarity.setObjectName(u"menu_row_similarity")
        icon10 = QIcon()
        icon10.addFile(u"icons/biaochaxun.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_row_similarity.setIcon(icon10)
        self.menu_row_delete = QAction(MainWindow)
        self.menu_row_delete.setObjectName(u"menu_row_delete")
        icon11 = QIcon()
        icon11.addFile(u"icons/yichu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_row_delete.setIcon(icon11)
        self.menu_column_delete = QAction(MainWindow)
        self.menu_column_delete.setObjectName(u"menu_column_delete")
        icon12 = QIcon()
        icon12.addFile(u"icons/yichu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_column_delete.setIcon(icon12)
        self.menu_split_words = QAction(MainWindow)
        self.menu_split_words.setObjectName(u"menu_split_words")
        icon13 = QIcon()
        icon13.addFile(u"icons/xianshi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_split_words.setIcon(icon13)
        self.menu_column_delete_2 = QAction(MainWindow)
        self.menu_column_delete_2.setObjectName(u"menu_column_delete_2")
        self.menu_clean_undo = QAction(MainWindow)
        self.menu_clean_undo.setObjectName(u"menu_clean_undo")
        icon14 = QIcon()
        icon14.addFile(u"icons/chexiao.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_clean_undo.setIcon(icon14)
        self.menu_clean_redo = QAction(MainWindow)
        self.menu_clean_redo.setObjectName(u"menu_clean_redo")
        icon15 = QIcon()
        icon15.addFile(u"icons/huifu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_clean_redo.setIcon(icon15)
        self.menu_group_stat = QAction(MainWindow)
        self.menu_group_stat.setObjectName(u"menu_group_stat")
        self.menu_library_freq_stat = QAction(MainWindow)
        self.menu_library_freq_stat.setObjectName(u"menu_library_freq_stat")
        self.menu_library_cocon_stat = QAction(MainWindow)
        self.menu_library_cocon_stat.setObjectName(u"menu_library_cocon_stat")
        self.menu_cocon_stat = QAction(MainWindow)
        self.menu_cocon_stat.setObjectName(u"menu_cocon_stat")
        icon16 = QIcon()
        icon16.addFile(u"icons/yingyongzhongxin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_cocon_stat.setIcon(icon16)
        self.menu_count_stat = QAction(MainWindow)
        self.menu_count_stat.setObjectName(u"menu_count_stat")
        icon17 = QIcon()
        icon17.addFile(u"icons/yingyongchangjing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_count_stat.setIcon(icon17)
        self.menu_clean_filter = QAction(MainWindow)
        self.menu_clean_filter.setObjectName(u"menu_clean_filter")
        self.menu_clean_makeup = QAction(MainWindow)
        self.menu_clean_makeup.setObjectName(u"menu_clean_makeup")
        self.menu_vertical_concat = QAction(MainWindow)
        self.menu_vertical_concat.setObjectName(u"menu_vertical_concat")
        icon18 = QIcon()
        icon18.addFile(u"icons/vertical_concat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_vertical_concat.setIcon(icon18)
        self.menu_clean_parse = QAction(MainWindow)
        self.menu_clean_parse.setObjectName(u"menu_clean_parse")
        icon19 = QIcon()
        icon19.addFile(u"icons/aislogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_clean_parse.setIcon(icon19)
        self.menu_clean_graph_config = QAction(MainWindow)
        self.menu_clean_graph_config.setObjectName(u"menu_clean_graph_config")
        icon20 = QIcon()
        icon20.addFile(u"icons/app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_clean_graph_config.setIcon(icon20)
        self.menu_clean_extract_feature = QAction(MainWindow)
        self.menu_clean_extract_feature.setObjectName(u"menu_clean_extract_feature")
        icon21 = QIcon()
        icon21.addFile(u"icons/zhenshikexin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_clean_extract_feature.setIcon(icon21)
        self.menu_window_savestore = QAction(MainWindow)
        self.menu_window_savestore.setObjectName(u"menu_window_savestore")
        self.menu_window_restore = QAction(MainWindow)
        self.menu_window_restore.setObjectName(u"menu_window_restore")
        self.menu_window_file = QAction(MainWindow)
        self.menu_window_file.setObjectName(u"menu_window_file")
        self.menu_window_stack = QAction(MainWindow)
        self.menu_window_stack.setObjectName(u"menu_window_stack")
        self.menu_window_table = QAction(MainWindow)
        self.menu_window_table.setObjectName(u"menu_window_table")
        self.menu_window_graph = QAction(MainWindow)
        self.menu_window_graph.setObjectName(u"menu_window_graph")
        self.menu_window_config = QAction(MainWindow)
        self.menu_window_config.setObjectName(u"menu_window_config")
        self.menu_window_history = QAction(MainWindow)
        self.menu_window_history.setObjectName(u"menu_window_history")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1174, 22))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_clean = QMenu(self.menubar)
        self.menu_clean.setObjectName(u"menu_clean")
        self.menu_analysis = QMenu(self.menubar)
        self.menu_analysis.setObjectName(u"menu_analysis")
        self.menu_window = QMenu(self.menubar)
        self.menu_window.setObjectName(u"menu_window")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_datafiles = QDockWidget(MainWindow)
        self.dockWidget_datafiles.setObjectName(u"dockWidget_datafiles")
        self.dockWidget_datafiles.setMaximumSize(QSize(300, 524287))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.datafiles_list = QListWidget(self.dockWidgetContents)
        self.datafiles_list.setObjectName(u"datafiles_list")

        self.verticalLayout.addWidget(self.datafiles_list)

        self.dockWidget_datafiles.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget_datafiles)
        self.dockWidget_config = QDockWidget(MainWindow)
        self.dockWidget_config.setObjectName(u"dockWidget_config")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, -1, 5, 5)
        self.groupBox_6 = QGroupBox(self.dockWidgetContents_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.groupBox_6)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_20)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.config_datafiles_csv_seperator = QLineEdit(self.frame_20)
        self.config_datafiles_csv_seperator.setObjectName(u"config_datafiles_csv_seperator")

        self.verticalLayout_2.addWidget(self.config_datafiles_csv_seperator)


        self.verticalLayout_14.addWidget(self.frame_20)


        self.verticalLayout_4.addWidget(self.groupBox_6)

        self.groupBox_2 = QGroupBox(self.dockWidgetContents_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.groupBox_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.config_stop_words_dict = QLineEdit(self.frame_11)
        self.config_stop_words_dict.setObjectName(u"config_stop_words_dict")
        self.config_stop_words_dict.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.config_stop_words_dict)

        self.btn_stop_words_dict = QPushButton(self.frame_11)
        self.btn_stop_words_dict.setObjectName(u"btn_stop_words_dict")
        self.btn_stop_words_dict.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_10.addWidget(self.btn_stop_words_dict)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.groupBox_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_11.addWidget(self.label_7)

        self.config_combine_words_dict = QLineEdit(self.frame_12)
        self.config_combine_words_dict.setObjectName(u"config_combine_words_dict")
        self.config_combine_words_dict.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.config_combine_words_dict)

        self.btn_combine_words_dict = QPushButton(self.frame_12)
        self.btn_combine_words_dict.setObjectName(u"btn_combine_words_dict")
        self.btn_combine_words_dict.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_11.addWidget(self.btn_combine_words_dict)


        self.verticalLayout_6.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.groupBox_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.config_controlled_words_dict = QLineEdit(self.frame_14)
        self.config_controlled_words_dict.setObjectName(u"config_controlled_words_dict")
        self.config_controlled_words_dict.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.config_controlled_words_dict)

        self.btn_controlled_words_dict = QPushButton(self.frame_14)
        self.btn_controlled_words_dict.setObjectName(u"btn_controlled_words_dict")
        self.btn_controlled_words_dict.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_12.addWidget(self.btn_controlled_words_dict)


        self.verticalLayout_6.addWidget(self.frame_14)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.btn_save_config = QPushButton(self.dockWidgetContents_2)
        self.btn_save_config.setObjectName(u"btn_save_config")

        self.verticalLayout_4.addWidget(self.btn_save_config)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.dockWidget_config.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_config)
        self.dockWidget_history = QDockWidget(MainWindow)
        self.dockWidget_history.setObjectName(u"dockWidget_history")
        self.dockWidget_history.setMaximumSize(QSize(300, 524287))
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.dockWidget_history.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_history)
        self.dockWidget_stack = QDockWidget(MainWindow)
        self.dockWidget_stack.setObjectName(u"dockWidget_stack")
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.listWidget_stack = QListWidget(self.dockWidgetContents_4)
        self.listWidget_stack.setObjectName(u"listWidget_stack")

        self.verticalLayout_3.addWidget(self.listWidget_stack)

        self.dockWidget_stack.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget_stack)
        self.dockWidget_table = QDockWidget(MainWindow)
        self.dockWidget_table.setObjectName(u"dockWidget_table")
        self.dockWidget_table.setStyleSheet(u"")
        self.dockWidget_table.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.horizontalLayout = QHBoxLayout(self.dockWidgetContents_5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.clean_datatable = TableKit(self.dockWidgetContents_5)
        self.clean_datatable.setObjectName(u"clean_datatable")

        self.horizontalLayout.addWidget(self.clean_datatable)

        self.dockWidget_table.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(Qt.TopDockWidgetArea, self.dockWidget_table)
        self.dockWidget_graph = QDockWidget(MainWindow)
        self.dockWidget_graph.setObjectName(u"dockWidget_graph")
        self.dockWidgetContents_6 = QWidget()
        self.dockWidgetContents_6.setObjectName(u"dockWidgetContents_6")
        self.dockWidget_graph.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidget_graph)
        self.clean_toolbar = QToolBar(MainWindow)
        self.clean_toolbar.setObjectName(u"clean_toolbar")
        self.clean_toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.clean_toolbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_clean.menuAction())
        self.menubar.addAction(self.menu_analysis.menuAction())
        self.menubar.addAction(self.menu_window.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_window.addAction(self.menu_window_file)
        self.menu_window.addAction(self.menu_window_stack)
        self.menu_window.addAction(self.menu_window_table)
        self.menu_window.addAction(self.menu_window_graph)
        self.menu_window.addAction(self.menu_window_config)
        self.menu_window.addAction(self.menu_window_history)
        self.menu_window.addSeparator()
        self.menu_window.addAction(self.menu_window_savestore)
        self.menu_window.addAction(self.menu_window_restore)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_clean_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.menu_clean_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.menu_clean_metadata.setText(QCoreApplication.translate("MainWindow", u"\u5143\u6570\u636e", None))
        self.menu_clean_rename.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u547d\u540d", None))
        self.menu_copy_column.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u5217", None))
        self.menu_split_column.setText(QCoreApplication.translate("MainWindow", u"\u62c6\u5206\u5217", None))
        self.menu_replace_column.setText(QCoreApplication.translate("MainWindow", u"\u66ff\u6362\u503c", None))
        self.menu_combine_synonym.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76\u8bcd", None))
        self.menu_stop_words.setText(QCoreApplication.translate("MainWindow", u"\u505c\u7528\u8bcd", None))
        self.menu_compare_columns.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4\u5217", None))
        self.menu_modify_value.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u503c", None))
        self.menu_row_distinct.setText(QCoreApplication.translate("MainWindow", u"\u884c\u53bb\u91cd", None))
        self.menu_row_similarity.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u4f3c\u5ea6", None))
        self.menu_row_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u884c", None))
        self.menu_column_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5217", None))
        self.menu_split_words.setText(QCoreApplication.translate("MainWindow", u"\u5207\u5206\u8bcd", None))
        self.menu_column_delete_2.setText(QCoreApplication.translate("MainWindow", u"\u8865\u5168\u503c", None))
        self.menu_clean_undo.setText(QCoreApplication.translate("MainWindow", u"\u64a4\u9500", None))
#if QT_CONFIG(shortcut)
        self.menu_clean_undo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.menu_clean_redo.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d", None))
#if QT_CONFIG(shortcut)
        self.menu_clean_redo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.menu_group_stat.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7ec4\u7edf\u8ba1", None))
        self.menu_library_freq_stat.setText(QCoreApplication.translate("MainWindow", u"\u9891\u6b21\u7edf\u8ba1", None))
        self.menu_library_cocon_stat.setText(QCoreApplication.translate("MainWindow", u"\u5171\u73b0\u7edf\u8ba1", None))
        self.menu_cocon_stat.setText(QCoreApplication.translate("MainWindow", u"\u5171\u73b0\u5206\u6790", None))
        self.menu_count_stat.setText(QCoreApplication.translate("MainWindow", u"\u8bcd\u9891\u7edf\u8ba1", None))
        self.menu_clean_filter.setText(QCoreApplication.translate("MainWindow", u"\u8fc7\u6ee4\u884c", None))
        self.menu_clean_makeup.setText(QCoreApplication.translate("MainWindow", u"\u8865\u5168\u503c", None))
        self.menu_vertical_concat.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5408\u5e76", None))
        self.menu_clean_parse.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790", None))
        self.menu_clean_graph_config.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u8868\u914d\u7f6e", None))
        self.menu_clean_extract_feature.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u63d0\u53d6", None))
        self.menu_window_savestore.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5e03\u5c40", None))
        self.menu_window_restore.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u5e03\u5c40", None))
        self.menu_window_file.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7a97\u53e3", None))
        self.menu_window_stack.setText(QCoreApplication.translate("MainWindow", u"\u6808\u7a97\u53e3", None))
        self.menu_window_table.setText(QCoreApplication.translate("MainWindow", u"\u8868\u683c\u7a97\u53e3", None))
        self.menu_window_graph.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7a97\u53e3", None))
        self.menu_window_config.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u7a97\u53e3", None))
        self.menu_window_history.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u7a97\u53e3", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_clean.setTitle(QCoreApplication.translate("MainWindow", u"\u6e05\u6d17", None))
        self.menu_analysis.setTitle(QCoreApplication.translate("MainWindow", u"\u5206\u6790", None))
        self.menu_window.setTitle(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.dockWidget_datafiles.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.dockWidget_config.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u914d\u7f6e", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u89e3\u6790\u6570\u636e\u6587\u4ef6\u53c2\u6570", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"csv\u6587\u4ef6\u5206\u9694\u7b26", None))
        self.config_datafiles_csv_seperator.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bcd\u5178", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u505c\u7528\u8bcd\u5178", None))
        self.btn_stop_words_dict.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76\u8bcd\u5178", None))
        self.btn_combine_words_dict.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u63a7\u8bcd\u5178", None))
        self.btn_controlled_words_dict.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_save_config.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.dockWidget_history.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u65e5\u5fd7", None))
        self.dockWidget_stack.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6808", None))
        self.dockWidget_table.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8868\u683c", None))
        self.dockWidget_graph.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf", None))
        self.clean_toolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi
