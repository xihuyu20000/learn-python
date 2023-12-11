"""
数据处理的功能，封装在biz模块。
弹出窗口封装在popup模块。创建的窗口对象，必须使用self.xxx
多线程封装在runner模块。创建的线程对象，必须使用self.xxx

方法的logger下面，必须空一行
"""
import os.path
import time
from typing import List

import pandas as pd
from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QFileDialog, QToolBar
from loguru import logger

from mhelper import Cfg, ssignal, FileFormat
from mainui.ui_main import Ui_MainWindow
from popup.clean.main_cocon_stat import PopupFreqStat
from popup.clean.main_combine_synonym import PopupCombineSynonym
from popup.clean.main_compare_column import PopupCompareColumns
from popup.clean.main_copy_column import PopupCopyColumn
from popup.clean.main_wordcount_stat import PopupWordCountStat
from popup.clean.main_dataset_metadata import PopupCleanMetadata
from popup.clean.main_group_stat import WinGroupStat, PopupCleanGroupStat
from popup.clean.main_modify_values import PopupModifyValues
from popup.clean.main_parse_datafiles import PopupDatafilesParse
from popup.clean.main_rename_column import PopupCleanRename
from popup.clean.main_replace_column import PopupReplaceColumn
from popup.clean.main_row_distinct import PopupRowDistinct
from popup.clean.main_similarity_row import PopupSimilarityRows
from popup.clean.main_split_column import PopupSplitColumn
from popup.clean.main_stop_words import PopupStopWords
from mrunner import CleanSaveDatasetThread, CleanParseFileThread
from mtoolkit import PandasStack, TableKit


class MasterWindows(QMainWindow, Ui_MainWindow):
    """
    本窗口的代码，使用master开头。放在最前面。
    清洗代码，使用clean开头。
    """

    def __init__(self):
        super(MasterWindows, self).__init__()
        self.setupUi(self)

        ## 1、初始化本窗口的内容 ##################################################

        self.master_init_ui()
        self.master_init_action()
        self.master_init_config()

        ## 2、绑定信息处理器 #####################################################

        ssignal.info.connect(self.master_show_info)
        ssignal.error.connect(self.master_show_error)
        ssignal.set_clean_dataset.connect(self.master_set_clean_df)

        ## 3、清洗部分初始化 #####################################################

        # clean 工具栏
        self.clean_toolbar = QToolBar()
        self.clean_toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        # clean 数据栈
        self.cleanTableStack = PandasStack(self)
        # clean 数据表
        self.clean_datatable = TableKit(column_sortable=True, header_horizontal_movable=True)
        # clean 布局管理器
        self.tab1_layout.addWidget(self.clean_toolbar)
        self.tab1_layout.addWidget(self.clean_datatable)

        # clean 菜单栏、工具栏
        self.clean_init_menubar()
        self.clean_init_toolbar()

        ## 4、 可视化部分初始化 ###################################################

        # library 工具栏
        self.library_toolbar = QToolBar()
        self.library_toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        # library 数据表
        self.library_datatable = TableKit(column_sortable=True, header_horizontal_movable=True)
        # library 布局管理器
        self.tab2_layout.addWidget(self.library_toolbar)
        self.tab2_layout.addWidget(self.library_datatable)

        # library 菜单栏、工具栏
        self.library_init_menubar()
        self.library_init_toolbar()




        self.master_show_info('欢迎使用本软件，祝您有愉快的一天')

    def master_init_ui(self) -> None:
        # splitter左右比例
        self.main_splitter.setStretchFactor(0, 2)
        self.main_splitter.setStretchFactor(1, 8)

    def master_init_action(self) -> None:
        """
        main.ui所有的事件槽函数，都在这里
        :return:
        """
        # 数据文件列表，双击
        self.datafiles_list.itemDoubleClicked.connect(self.master_action_dblclick_datafiles_list)
        # 数据文件列表，按钮，刷新加载列表
        self.datafiles_btn_list.clicked.connect(self.master_action_datafiles_list)
        # 数据文件列表，按钮，显示
        self.datafiles_btn_parse.clicked.connect(self.master_action_datafiles_parse)
        # 配置项，保存
        self.btn_save_config.clicked.connect(self.master_action_save_configs)

    def master_init_config(self) -> None:
        """
        初始化配置项中的参数
        :return:
        """
        cfg = Cfg()
        self.config_datafiles_csv_seperator.setText(cfg.get(Cfg.csv_seperator))

    def master_show_info(self, val) -> None:
        """
        状态栏，显示信息
        :param val:
        :return:
        """
        self.statusBar().setStyleSheet("color: blue;font-weight: bold;font-size: 16px;")
        self.statusBar().showMessage(val, 10000)

    def master_show_error(self, val) -> None:
        self.statusBar().setStyleSheet("color: red;font-weight: bold;font-size: 16px;")
        self.statusBar().showMessage(val, 10000)

    def master_get_clean_df(self) -> pd.DataFrame:
        return self.clean_datatable.get_dataset()

    def master_set_clean_df(self, df, inplace_index=True, drop_index=True) -> None:
        self.clean_datatable.set_dataset(df, inplace_index=inplace_index, drop_index=drop_index)
        self.mainTabWidget.setCurrentIndex(0)
        self.cleanTableStack.push(df)

    def master_get_clean_columns(self) -> List[str]:
        return self.master_get_clean_df().columns

    def master_get_clean_table(self) -> TableKit:
        return self.clean_datatable

    def master_clean_no_data(self) -> bool:
        return not self.clean_datatable.has_dataset()

    def master_action_dblclick_datafiles_list(self, item):
        logger.info('双击数据文件列表，解析数据文件')

        fname = item.text()

        if fname.endswith('.xls') or fname.endswith('.xlsx'):
            format = FileFormat.EXCEL
        elif fname.endswith('.csv'):
            format = FileFormat.CSV
        elif fname.endswith('.pkl'):
            format = FileFormat.PICKLE
        elif fname.endswith('.pqt'):
            format = FileFormat.PARQUET
        else:
            format = 'error'

        if format == 'error':
            ssignal.error.send('不识别的文件格式，请点击解析按钮')
            return

        # 双击，只会选择一个文件，所以包装成list
        abs_datafiles = os.path.join(Cfg.datafiles, fname)
        abs_datafiles = [abs_datafiles]
        # csv文件分隔符
        sep = self.config_datafiles_csv_seperator.text()

        self.cleanSaveDatasetThread = CleanParseFileThread(abs_datafiles, format, sep)
        self.cleanSaveDatasetThread.start()

    def master_action_datafiles_list(self):
        logger.info('数据文件列表按钮，加载数据列表')

        fnames = [fname for fname in os.listdir(Cfg.datafiles)]
        # 过滤文件夹，只保留文件
        fnames = [fname for fname in fnames if os.path.isfile(os.path.join(Cfg.datafiles, fname))]

        self.datafiles_list.clear()
        self.datafiles_list.addItems(fnames)
        self.datafiles_list.setCurrentRow(0)

        ssignal.info.send(f'加载{len(fnames)}个数据文件')

    def master_action_datafiles_parse(self):
        logger.info('数据文件列表按钮，解析数据文件')

        selected_fnames = [item.text() for item in self.datafiles_list.selectedItems()]

        if len(selected_fnames) == 0:
            ssignal.error.send(f'错误，请选择同一种类型的数据文件')
            return

        # 获取所有的扩展名
        suffixes = [str(fname).split(".")[1] for fname in selected_fnames]

        if len(set(suffixes)) != 1:
            self.master_show_error(f'错误，请选择同一种类型的数据文件')
            return

        abs_datafiles = [os.path.join(Cfg.datafiles, fname) for fname in selected_fnames]
        sep = self.config_datafiles_csv_seperator.text()

        self.popupDatafilesParse = PopupDatafilesParse(self, abs_datafiles, sep)
        self.popupDatafilesParse.show()

    def master_action_save_configs(self):
        cfg = Cfg()
        cfg.set(Cfg.synonyms_file, self.config_synonym_dict_file.text())
        cfg.set(Cfg.stopwords_file, self.config_stop_words_file.text())
        cfg.set(Cfg.csv_seperator, self.config_datafiles_csv_seperator.text())

        ssignal.info.send('保存成功')

    ########################################################################

    def clean_init_menubar(self):
        """
        槽函数，必须是clean_do_menu_开头
        :return:
        """
        self.menu_clean_undo.triggered.connect(self.clean_do_menu_undo)
        self.menu_clean_redo.triggered.connect(self.clean_do_menu_redo)
        self.menu_clean_save.triggered.connect(self.clean_do_menu_save)
        self.menu_clean_metadata.triggered.connect(self.clean_do_menu_metadata)
        self.menu_clean_rename.triggered.connect(self.clean_do_menu_rename)
        self.menu_copy_column.triggered.connect(self.clean_do_menu_copy_column)
        self.menu_split_column.triggered.connect(self.clean_do_menu_split_column)
        self.menu_replace_column.triggered.connect(self.clean_do_menu_replace_column)
        self.menu_combine_synonym.triggered.connect(self.clean_do_menu_combine_synonym)
        self.menu_stop_words.triggered.connect(self.clean_do_menu_stop_words)
        self.menu_count_stat.triggered.connect(self.clean_do_menu_wordcount_stat)
        self.menu_cocon_stat.triggered.connect(self.clean_do_menu_cocon_stat)
        self.menu_compare_columns.triggered.connect(self.clean_do_menu_compare_columns)
        self.menu_modify_value.triggered.connect(self.clean_do_menu_modify_value)
        self.menu_row_distinct.triggered.connect(self.clean_do_menu_row_distinct)
        self.menu_row_similarity.triggered.connect(self.clean_do_menu_row_similarity)
        self.menu_row_delete.triggered.connect(self.clean_do_menu_row_delete)
        self.menu_column_delete.triggered.connect(self.clean_do_menu_column_delete)
        self.menu_group_stat.triggered.connect(self.clean_do_menu_group_stat)
        self.menu_clean_filter.triggered.connect(self.clean_do_menu_clean_filter)
        self.menu_clean_makeup.triggered.connect(self.clean_do_menu_clean_makeup)

    def clean_init_toolbar(self):
        self.clean_toolbar.addAction(self.menu_clean_undo)
        self.clean_toolbar.addAction(self.menu_clean_redo)
        self.clean_toolbar.addAction(self.menu_clean_save)
        self.clean_toolbar.addAction(self.menu_clean_metadata)
        self.clean_toolbar.addAction(self.menu_clean_rename)
        self.clean_toolbar.addAction(self.menu_copy_column)
        self.clean_toolbar.addAction(self.menu_split_column)
        self.clean_toolbar.addAction(self.menu_replace_column)
        self.clean_toolbar.addAction(self.menu_combine_synonym)
        self.clean_toolbar.addAction(self.menu_stop_words)
        self.clean_toolbar.addAction(self.menu_count_stat)
        self.clean_toolbar.addAction(self.menu_cocon_stat)
        self.clean_toolbar.addAction(self.menu_compare_columns)
        self.clean_toolbar.addAction(self.menu_modify_value)
        self.clean_toolbar.addAction(self.menu_row_distinct)
        self.clean_toolbar.addAction(self.menu_row_similarity)
        self.clean_toolbar.addAction(self.menu_row_delete)
        self.clean_toolbar.addAction(self.menu_column_delete)
        self.clean_toolbar.addAction(self.menu_group_stat)
        self.clean_toolbar.addAction(self.menu_clean_filter)
        self.clean_toolbar.addAction(self.menu_clean_makeup)
    #######################################################################

    def clean_do_menu_undo(self):
        logger.info('清洗，撤销')

        df = self.cleanTableStack.undo()
        if df is not None:
            ssignal.set_clean_dataset.send(df)
            ssignal.info.send('撤销')
        else:
            ssignal.error.send('无法撤销')

    def clean_do_menu_redo(self):
        logger.info('清洗，恢复')

        df = self.cleanTableStack.redo()
        if df is not None:
            ssignal.set_clean_dataset.send(df)
            ssignal.info.send('恢复')
        else:
            ssignal.error.send('无法恢复')

    def clean_do_menu_metadata(self):
        logger.info('清洗，元数据')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupCleanMetadata = PopupCleanMetadata(self)
        self.popupCleanMetadata.show()

    def clean_do_menu_save(self):
        logger.info('清洗，保存')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        filePath, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "保存数据文件",  # 标题
            Cfg.datafiles,  # 起始目录
            "Excel (*.xlsx);;Csv (*.csv);;Pickle (*.pkl);;Parquet (*.pqt);;"  # 选择类型过滤项，过滤内容在括号中
        )

        if filePath:
            self.cleanSaveDatasetThread = CleanSaveDatasetThread(self.master_get_clean_df(), filePath)
            self.cleanSaveDatasetThread.start()

    def clean_do_menu_rename(self):
        logger.info('清洗，重命名')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupCleanRename = PopupCleanRename(self)
        self.popupCleanRename.show()

    def clean_do_menu_copy_column(self):
        logger.info('清洗，复制列')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupCopyColumn = PopupCopyColumn(self)
        self.popupCopyColumn.show()

    def clean_do_menu_split_column(self):
        logger.info('清洗，拆分列')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupSplitColumn = PopupSplitColumn(self)
        self.popupSplitColumn.show()

    def clean_do_menu_replace_column(self):
        logger.info('清洗，替换值')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupReplaceColumn = PopupReplaceColumn(self)
        self.popupReplaceColumn.show()

    def clean_do_menu_combine_synonym(self):
        logger.info('清洗，合并词')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupCombineSynonym = PopupCombineSynonym(self)
        self.popupCombineSynonym.show()

    def clean_do_menu_stop_words(self):
        logger.info('清洗，停用词')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupStopWords = PopupStopWords(self)
        self.popupStopWords.show()

    def clean_do_menu_wordcount_stat(self):
        logger.info('清洗，词频统计')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupWordCountStat = PopupWordCountStat(self)
        self.popupWordCountStat.show()


    def clean_do_menu_cocon_stat(self):
        logger.info('清洗，共现分析')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupFreqStat = PopupFreqStat(self)
        self.popupFreqStat.show()

    def clean_do_menu_compare_columns(self):
        logger.info('清洗，对比列')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupCompareColumns = PopupCompareColumns(self)
        self.popupCompareColumns.show()

    def clean_do_menu_modify_value(self):
        logger.info('清洗，修改值')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupModifyValues = PopupModifyValues(self)
        self.popupModifyValues.show()

    def clean_do_menu_row_distinct(self):
        logger.info('清洗，行去重')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupRowDistinct = PopupRowDistinct(self)
        self.popupRowDistinct.show()

    def clean_do_menu_row_similarity(self):
        logger.info('清洗，相似度')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupSimilarityRows = PopupSimilarityRows(self)
        self.popupSimilarityRows.show()

    def clean_do_menu_row_delete(self):
        logger.info('清洗，删除行')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.clean_datatable.remove_selected_rows()
        self.master_set_clean_df(self.master_get_clean_df())
        ssignal.info.send('删除行')

    def clean_do_menu_column_delete(self):
        logger.info('清洗，删除列')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.clean_datatable.remove_selected_columns()
        self.master_set_clean_df(self.master_get_clean_df())
        ssignal.info.send('删除列')

    def clean_do_menu_group_stat(self):
        logger.info('清洗，分组统计')
        ssignal.error.send('还没有实现')

        if self.master_clean_no_data():
            ssignal.error.send('没有数据')
            return

        self.popupCleanGroupStat = PopupCleanGroupStat(self)
        self.popupCleanGroupStat.show()

    def clean_do_menu_clean_filter(self):
        logger.info('清洗，过滤')
        ssignal.error.send('还没有实现')

    def clean_do_menu_clean_makeup(self):
        logger.info('清洗，补全值')
        ssignal.error.send('还没有实现')

    #######################################################################
    def library_init_menubar(self):
        pass

    def library_init_toolbar(self):
        pass

    #######################################################################

    #######################################################################

    #######################################################################
