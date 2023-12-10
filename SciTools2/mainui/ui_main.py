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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1179, 856)
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.main_splitter = QSplitter(self.centralwidget)
        self.main_splitter.setObjectName(u"main_splitter")
        self.main_splitter.setOrientation(Qt.Horizontal)
        self.frame = QFrame(self.main_splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.frame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.frame_3 = QFrame(self.splitter_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.datafiles_btn_list = QPushButton(self.frame_5)
        self.datafiles_btn_list.setObjectName(u"datafiles_btn_list")

        self.horizontalLayout_2.addWidget(self.datafiles_btn_list)

        self.datafiles_btn_parse = QPushButton(self.frame_5)
        self.datafiles_btn_parse.setObjectName(u"datafiles_btn_parse")

        self.horizontalLayout_2.addWidget(self.datafiles_btn_parse)

        self.horizontalSpacer = QSpacerItem(392, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.datafiles_list = QListWidget(self.frame_3)
        self.datafiles_list.setObjectName(u"datafiles_list")
        self.datafiles_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_2.addWidget(self.datafiles_list)

        self.splitter_2.addWidget(self.frame_3)

        self.verticalLayout.addWidget(self.splitter_2)

        self.main_splitter.addWidget(self.frame)
        self.frame_2 = QFrame(self.main_splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainTabWidget = QTabWidget(self.frame_2)
        self.mainTabWidget.setObjectName(u"mainTabWidget")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tab1_layout = QVBoxLayout(self.tab1)
        self.tab1_layout.setSpacing(0)
        self.tab1_layout.setObjectName(u"tab1_layout")
        self.tab1_layout.setContentsMargins(0, 0, 0, 0)
        self.mainTabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tab2_layout = QVBoxLayout(self.tab2)
        self.tab2_layout.setSpacing(0)
        self.tab2_layout.setObjectName(u"tab2_layout")
        self.tab2_layout.setContentsMargins(0, 0, 0, 0)
        self.mainTabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.mainTabWidget.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.horizontalLayout_17 = QHBoxLayout(self.tab4)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.tab4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_11)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.groupBox)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.groupBox)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.verticalLayout_8.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_11)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_9 = QFrame(self.groupBox_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_9)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.groupBox_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.frame_10)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_8.addWidget(self.lineEdit_4)


        self.verticalLayout_5.addWidget(self.frame_10)


        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.horizontalLayout_17.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.tab4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_5 = QGroupBox(self.frame_12)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_17 = QFrame(self.groupBox_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_13.addWidget(self.label_9)

        self.config_synonym_dict_file = QLineEdit(self.frame_17)
        self.config_synonym_dict_file.setObjectName(u"config_synonym_dict_file")

        self.horizontalLayout_13.addWidget(self.config_synonym_dict_file)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.groupBox_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_14.addWidget(self.label_10)

        self.config_stop_words_file = QLineEdit(self.frame_18)
        self.config_stop_words_file.setObjectName(u"config_stop_words_file")

        self.horizontalLayout_14.addWidget(self.config_stop_words_file)


        self.verticalLayout_11.addWidget(self.frame_18)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.frame_12)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_19 = QFrame(self.groupBox_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_13.addWidget(self.label_11)

        self.config_datafiles_csv_seperator = QLineEdit(self.frame_19)
        self.config_datafiles_csv_seperator.setObjectName(u"config_datafiles_csv_seperator")

        self.verticalLayout_13.addWidget(self.config_datafiles_csv_seperator)


        self.verticalLayout_12.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.groupBox_6)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_14.addWidget(self.label_12)

        self.config_datafiles_excel_n = QLineEdit(self.frame_20)
        self.config_datafiles_excel_n.setObjectName(u"config_datafiles_excel_n")

        self.verticalLayout_14.addWidget(self.config_datafiles_excel_n)


        self.verticalLayout_12.addWidget(self.frame_20)


        self.verticalLayout_3.addWidget(self.groupBox_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btn_save_config = QPushButton(self.frame_12)
        self.btn_save_config.setObjectName(u"btn_save_config")

        self.verticalLayout_3.addWidget(self.btn_save_config)


        self.horizontalLayout_17.addWidget(self.frame_12)

        self.mainTabWidget.addTab(self.tab4, "")

        self.horizontalLayout_4.addWidget(self.mainTabWidget)

        self.main_splitter.addWidget(self.frame_2)

        self.verticalLayout_6.addWidget(self.main_splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1179, 26))
        self.menu_clean = QMenu(self.menubar)
        self.menu_clean.setObjectName(u"menu_clean")
        self.menu_library = QMenu(self.menubar)
        self.menu_library.setObjectName(u"menu_library")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_clean.menuAction())
        self.menubar.addAction(self.menu_library.menuAction())
        self.menu_clean.addAction(self.menu_clean_undo)
        self.menu_clean.addAction(self.menu_clean_redo)
        self.menu_clean.addAction(self.menu_clean_save)
        self.menu_clean.addAction(self.menu_clean_metadata)
        self.menu_clean.addAction(self.menu_clean_rename)
        self.menu_clean.addAction(self.menu_copy_column)
        self.menu_clean.addAction(self.menu_split_column)
        self.menu_clean.addAction(self.menu_replace_column)
        self.menu_clean.addAction(self.menu_combine_synonym)
        self.menu_clean.addAction(self.menu_stop_words)
        self.menu_clean.addAction(self.menu_count_stat)
        self.menu_clean.addAction(self.menu_cocon_stat)
        self.menu_clean.addAction(self.menu_compare_columns)
        self.menu_clean.addAction(self.menu_modify_value)
        self.menu_clean.addAction(self.menu_row_distinct)
        self.menu_clean.addAction(self.menu_row_similarity)
        self.menu_clean.addAction(self.menu_row_delete)
        self.menu_clean.addAction(self.menu_column_delete)
        self.menu_clean.addAction(self.menu_split_words)
        self.menu_clean.addAction(self.menu_group_stat)

        self.retranslateUi(MainWindow)

        self.mainTabWidget.setCurrentIndex(0)


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
        self.datafiles_btn_list.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5217\u8868", None))
        self.datafiles_btn_parse.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"\u6e05\u6d17", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"\u5206\u6790", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"\u56fe\u8868", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u5e38\u7528\u5b57\u5178", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76\u8bcd\u8868", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u505c\u7528\u8bcd\u8868", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u89e3\u6790\u6570\u636e\u6587\u4ef6\u53c2\u6570", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"csv\u6587\u4ef6\u5206\u9694\u7b26", None))
        self.config_datafiles_csv_seperator.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"excel\u6587\u4ef6\u52a0\u8f7d\u524dN\u4e2a", None))
        self.config_datafiles_excel_n.setText("")
        self.btn_save_config.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab4), QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.menu_clean.setTitle(QCoreApplication.translate("MainWindow", u"\u6e05\u6d17", None))
        self.menu_library.setTitle(QCoreApplication.translate("MainWindow", u"\u5206\u6790", None))
    # retranslateUi

