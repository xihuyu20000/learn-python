import os.path

from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QFileDialog, QToolBar
from loguru import logger

from helper import Cfg, MySignal, FileFormat
from mainui.ui_main import Ui_MainWindow
from popup.clean.main_cocon_stat import WinFreqStat
from popup.clean.main_combine_synonym import WinCombineSynonym
from popup.clean.main_compare_column import WinCompareColumns
from popup.clean.main_copy_column import WinCopyColumn
from popup.clean.main_count_stat import WinCountStat
from popup.clean.main_dataset_metadata import WidCleanMetadata
from popup.clean.main_modify_values import WinModifyValues
from popup.clean.main_parse_datafiles import WinDatafilesParse
from popup.clean.main_rename_column import WinCleanRename
from popup.clean.main_replace_column import WinReplaceColumn
from popup.clean.main_row_distinct import WinRowDistinct
from popup.clean.main_similarity_row import WinSimilarityRows
from popup.clean.main_split_column import WinSplitColumn
from popup.clean.main_stop_words import WinStopWords
from runner import DownloadThread, ParseFileThread
from toolkit import PandasStack, TableKit


class MasterWindows(QMainWindow, Ui_MainWindow):
    def __init__(self):  # 构造方法
        super(MasterWindows, self).__init__()  # 运行父类的构造方法
        self.setupUi(self)  # 传递自己

        self.master_init_ui()
        self.master_init_action()
        self.master_init_config()

        # 绑定信息处理器
        MySignal.info.connect(self.master_show_info)
        MySignal.error.connect(self.master_show_error)
        MySignal.clean_dataset.connect(self.master_set_clean_df)

        ########################################################################
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
        #########################################################################
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

    def master_init_ui(self):
        # splitter左右比例
        self.main_splitter.setStretchFactor(0, 2)
        self.main_splitter.setStretchFactor(1, 8)

    def master_init_action(self):
        # 数据文件列表，双击
        self.datafiles_list.itemDoubleClicked.connect(self.master_action_dblclick_datafiles_list)
        # 数据文件列表，刷新加载列表
        self.datafiles_btn_list.clicked.connect(self.master_action_datafiles_list)
        # 数据文件列表，显示
        self.datafiles_btn_parse.clicked.connect(self.master_action_datafiles_parse)
        # 配置项，保存
        self.btn_save_config.clicked.connect(self.master_action_save_configs)

    def master_init_config(self):
        cfg = Cfg()
        self.config_synonym_dict_file.setText(cfg.get(Cfg.synonyms_file))
        self.config_stop_words_file.setText(cfg.get(Cfg.stopwords_file))
        self.config_datafiles_excel_n.setText(cfg.get(Cfg.excel_count))
        self.config_datafiles_csv_seperator.setText(cfg.get(Cfg.csv_seperator))

    def master_show_info(self, val):
        self.statusBar().setStyleSheet("color: blue;font-weight: bold;font-size: 16px;")
        self.statusBar().showMessage(val, 10000)

    def master_show_error(self, val):
        self.statusBar().setStyleSheet("color: red;font-weight: bold;font-size: 16px;")
        self.statusBar().showMessage(val, 10000)

    def master_get_clean_df(self):
        return self.clean_datatable.get_dataset()

    def master_set_clean_df(self, df, inplace_index=True, drop_index=True, show_color=False):
        self.clean_datatable.set_dataset(df, inplace_index=inplace_index, drop_index=drop_index)
        self.mainTabWidget.setCurrentIndex(0)
        self.cleanTableStack.push(df)

        if not show_color:
            table = self.master_get_clean_table()
            for i in range(df.shape[0]):
                for col in range(df.shape[1]):
                    table.set_bgcolor(i, col, '#FFFFFF')

    def master_get_clean_columns(self):
        return self.master_get_clean_df().columns

    def master_get_clean_table(self):
        return self.clean_datatable

    def master_action_dblclick_datafiles_list(self, item):
        logger.info('双击，解析数据文件')
        fname = item.text()

        if fname.endswith('.xls') or fname.endswith('.xlsx'):
            format = FileFormat.EXCEL
        elif fname.endswith('.csv'):
            format = FileFormat.CSV
        elif fname.endswith('.pkl'):
            format = FileFormat.PICKLE
        else:
            format = 'error'

        if format == 'error':
            MySignal.error.send('不识别的文件格式，请点击解析按钮')
            return

        abs_datafiles = os.path.join(Cfg.datafiles, fname)
        print(abs_datafiles)
        # csv文件分隔符
        sep = self.config_datafiles_csv_seperator.text()
        # excel解析sheet数量
        count = int(self.config_datafiles_excel_n.text())
        self.parseFileThread = ParseFileThread([abs_datafiles], format, sep, count)
        self.parseFileThread.start()

    def master_action_datafiles_list(self):
        logger.info('按钮，加载数据列表')
        fnames = [fname for fname in os.listdir(Cfg.datafiles)]
        # 过滤文件夹，只保留文件
        fnames = [fname for fname in fnames if os.path.isfile(os.path.join(Cfg.datafiles, fname))]
        self.datafiles_list.clear()
        self.datafiles_list.addItems(fnames)
        self.datafiles_list.setCurrentRow(0)
        self.master_show_info(f'加载{len(fnames)}个数据文件')

    def master_action_datafiles_parse(self):
        logger.info('按钮，解析数据文件')
        selected_fnames = [item.text() for item in self.datafiles_list.selectedItems()]
        if len(selected_fnames) == 0:
            self.master_show_error(f'错误，请选择同一种类型的数据文件')
            return
        # 获取所有的扩展名
        suffixes = [str(fname).split(".")[1] for fname in selected_fnames]
        if len(set(suffixes)) != 1:
            self.master_show_error(f'错误，请选择同一种类型的数据文件')
            return

        abs_datafiles = [os.path.join(Cfg.datafiles, fname) for fname in selected_fnames]
        # csv文件分隔符
        sep = self.config_datafiles_csv_seperator.text()
        # excel解析sheet数量
        count = int(self.config_datafiles_excel_n.text())

        self.widDatafilesParse = WinDatafilesParse(self, abs_datafiles, sep, count)
        self.widDatafilesParse.show()

    def master_action_save_configs(self):
        cfg = Cfg()
        cfg.set(Cfg.synonyms_file, self.config_synonym_dict_file.text())
        cfg.set(Cfg.stopwords_file, self.config_stop_words_file.text())
        cfg.set(Cfg.csv_seperator, self.config_datafiles_csv_seperator.text())
        cfg.set(Cfg.excel_count, self.config_datafiles_excel_n.text())

        MySignal.info.send('保存成功')

    ########################################################################

    def clean_init_menubar(self):
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
        self.menu_count_stat.triggered.connect(self.clean_do_menu_count_stat)
        self.menu_cocon_stat.triggered.connect(self.clean_do_menu_cocon_stat)
        self.menu_compare_columns.triggered.connect(self.clean_do_menu_compare_columns)
        self.menu_modify_value.triggered.connect(self.clean_do_menu_modify_value)
        self.menu_row_distinct.triggered.connect(self.clean_do_menu_row_distinct)
        self.menu_row_similarity.triggered.connect(self.clean_do_menu_row_similarity)
        self.menu_row_delete.triggered.connect(self.clean_do_menu_row_delete)
        self.menu_column_delete.triggered.connect(self.clean_do_menu_column_delete)
        self.menu_group_stat.triggered.connect(self.clean_do_menu_group_stat)

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
        # self.clean_toolbar.addAction(self.menu_group_stat)

    #######################################################################

    def clean_do_menu_undo(self):
        logger.info('清洗，撤销')

        df = self.cleanTableStack.undo()
        if df is not None:
            self.clean_datatable.set_dataset(df)
            MySignal.info.send('撤销')
        else:
            MySignal.error.send('无法撤销')

    def clean_do_menu_redo(self):
        logger.info('清洗，恢复')

        df = self.cleanTableStack.redo()
        if df is not None:
            self.clean_datatable.set_dataset(df)
            MySignal.info.send('恢复')
        else:
            MySignal.error.send('无法恢复')

    def clean_do_menu_metadata(self):
        logger.info('清洗，元数据')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.widCleanMetadata = WidCleanMetadata(self)
        self.widCleanMetadata.show()

    def clean_do_menu_save(self):
        logger.info('清洗，保存')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        filePath, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "保存数据文件",  # 标题
            Cfg.datafiles,  # 起始目录
            "Excel (*.xlsx);;Csv (*.csv);;模型 (*.pkl);;"  # 选择类型过滤项，过滤内容在括号中
        )

        if filePath:
            self.master_show_info('开始保存')
            self.parseFileThread = DownloadThread(self.master_get_clean_df(), filePath)
            self.parseFileThread.start()

    def clean_do_menu_rename(self):
        logger.info('清洗，重命名')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winCleanRename = WinCleanRename(self)
        self.winCleanRename.show()

    def clean_do_menu_copy_column(self):
        logger.info('清洗，复制列')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winCopyColumn = WinCopyColumn(self)
        self.winCopyColumn.show()

    def clean_do_menu_split_column(self):
        logger.info('清洗，拆分列')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winSplitColumn = WinSplitColumn(self)
        self.winSplitColumn.show()

    def clean_do_menu_replace_column(self):
        logger.info('清洗，替换值')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winReplaceColumn = WinReplaceColumn(self)
        self.winReplaceColumn.show()

    def clean_do_menu_combine_synonym(self):
        logger.info('清洗，合并词')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winCombineSynonym = WinCombineSynonym(self)
        self.winCombineSynonym.show()

    def clean_do_menu_stop_words(self):
        logger.info('清洗，停用词')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winStopWords = WinStopWords(self)
        self.winStopWords.show()

    def clean_do_menu_count_stat(self):
        logger.info('清洗，词频统计')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winCountStat = WinCountStat(self)
        self.winCountStat.show()

    def clean_do_menu_cocon_stat(self):
        logger.info('清洗，共现分析')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winFreqStat = WinFreqStat(self)
        self.winFreqStat.show()

    def clean_do_menu_compare_columns(self):
        logger.info('清洗，对比列')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winCompareColumns = WinCompareColumns(self)
        self.winCompareColumns.show()

    def clean_do_menu_modify_value(self):
        logger.info('清洗，修改值')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winModifyValues = WinModifyValues(self)
        self.winModifyValues.show()

    def clean_do_menu_row_distinct(self):
        logger.info('清洗，行去重')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winRowDistinct = WinRowDistinct(self)
        self.winRowDistinct.show()

    def clean_do_menu_row_similarity(self):
        logger.info('清洗，相似度')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.winSimilarityRows = WinSimilarityRows(self)
        self.winSimilarityRows.show()

    def clean_do_menu_row_delete(self):
        logger.info('清洗，删除行')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.clean_datatable.remove_selected_rows()
        self.master_set_clean_df(self.master_get_clean_df())
        MySignal.info.send('删除行')

    def clean_do_menu_column_delete(self):
        logger.info('清洗，删除列')

        if not self.clean_datatable.has_dataset():
            MySignal.error.send('没有数据')
            return

        self.clean_datatable.remove_selected_columns()
        self.master_set_clean_df(self.master_get_clean_df())
        MySignal.info.send('删除列')

    def clean_do_menu_group_stat(self):
        logger.info('清洗，分组统计')
        MySignal.error.send('还没有实现')
        # if not self.clean_datatable.has_dataset():
        #     MySignal.error.send('没有数据')
        #     return
        #
        # self.winGroupStat = WinGroupStat(self)
        # self.winGroupStat.show()

    #######################################################################
    def library_init_menubar(self):
        pass

    def library_init_toolbar(self):
        pass

    #######################################################################

    #######################################################################

    #######################################################################
