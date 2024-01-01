"""
数据处理的功能，封装在biz模块。
弹出窗口封装在popup模块。创建的窗口对象，必须使用self.xxx
多线程封装在runner模块。创建的线程对象，必须使用self.xxx

方法的logger下面，必须空一行
"""
import collections
import os.path

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QFileDialog, QLabel

from core.const import Cfg, ssignal
from core.const import FileFormat
from core.log import logger
from core.mgraph import GraphData
from core.runner import (
    CleanSaveDatasetThread,
    CleanParseFileThread,
    WatchDataFilesChaningThread,
)
from core.runner.mrunner import CleanCompareDatasetThread, CleanLoadDatasetThread, CleanDeleteRowsThread, \
    CleanDeleteColumnsThread
from core.util import PandasCache
from uimain.ctx import MasterMainContext
from uimain.uipy.ui_main import Ui_MainWindow
from uipopup.main_cocon_stat import PopupCoconStat
from uipopup.main_combine_synonym import PopupCombineSynonym
from uipopup.main_compare_column import PopupCompareColumns
from uipopup.main_copy_column import PopupCopyColumn
from uipopup.main_dataset_metadata import PopupCleanMetadata
from uipopup.main_extract_features import PopupExtractFeatures
from uipopup.main_filter_row import PopupFilterRows
from uipopup.main_graph_config import PopupGraphConfig
from uipopup.main_group_stat import WinGroupStat
from uipopup.main_modify_values import PopupModifyValues
from uipopup.main_parse_datafiles import PopupDatafilesParse
from uipopup.main_rename_column import PopupCleanRename
from uipopup.main_replace_column import PopupReplaceColumn
from uipopup.main_row_deduplicate import PopupRowDeduplicate
from uipopup.main_similarity_row import PopupSimilarityRows
from uipopup.main_split_column import PopupSplitColumn
from uipopup.main_split_words import PopupSplitWords
from uipopup.main_stop_words import PopupStopWords
from uipopup.main_vertical_concat import PopupVerticalConcat
from uipopup.main_wordcount_stat import PopupWordCountStat

ActionCallback = collections.namedtuple("ActionCallback", ["id", "source", "event", 'callback'])
MenuTool = collections.namedtuple('MenuTool',
                                  ['id', 'label', 'icon', 'menubar', 'show_in_menubar', 'show_in_toolbar', 'callback'])


class MasterMainWindows(QMainWindow, Ui_MainWindow):
    """
    本窗口的代码，使用master开头。放在最前面。
    清洗代码，使用clean开头。
    """

    def __init__(self):
        super(MasterMainWindows, self).__init__()

        # 1、初始化本窗口的内容 ##################################################

        self.setupUi(self)

        if Cfg.get('geometry'):
            self.restoreGeometry(Cfg.get('geometry'))
            self.restoreState(Cfg.get('windowState'))
        else:
            self.master_init_dock()

        ## 2、绑定信息处理器 #####################################################

        self.master_init_actions()

        self.master_init_menubar()

        self.master_init_signal()

        # ## 4、 数据分析部分初始化 ###################################################

        ## 5、  图表部分初始化 ######################################################################
        self.graph_data = GraphData()

        ## 6、  数据初始化 ######################################################################
        self.master_init_config()

        self.context = MasterMainContext(self)
        self.pandasCache = PandasCache()

        self.watchDataFilesChangingThread = WatchDataFilesChaningThread()
        self.watchDataFilesChangingThread.start()

        ssignal.datafiles_changing.emit()

        self.master_show_permanent("欢迎使用本软件，祝您有愉快的一天")

    def master_init_dock(self):
        logger.info('恢复布局')
        # 移除中间部件
        self.takeCentralWidget()
        # 启用嵌套布局
        self.setDockNestingEnabled(True);
        # 先左右布局
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockWidget_datafiles)
        self.splitDockWidget(self.dockWidget_datafiles, self.dockWidget_table, QtCore.Qt.Orientation.Horizontal)
        self.splitDockWidget(self.dockWidget_table, self.dockWidget_config, QtCore.Qt.Orientation.Horizontal)
        # 然后左侧，上下布局
        self.splitDockWidget(self.dockWidget_datafiles, self.dockWidget_stack, QtCore.Qt.Orientation.Vertical)
        # 然后中间，上下布局
        self.splitDockWidget(self.dockWidget_table, self.dockWidget_graph, QtCore.Qt.Orientation.Vertical)
        self.tabifyDockWidget(self.dockWidget_table, self.dockWidget_graph)
        self.dockWidget_table.raise_()
        # 然后右侧，上下布局
        self.splitDockWidget(self.dockWidget_config, self.dockWidget_history, QtCore.Qt.Orientation.Vertical)
        # 大小设置
        self.resizeDocks([self.dockWidget_datafiles, self.dockWidget_table, self.dockWidget_config], [2, 5, 1],
                         QtCore.Qt.Orientation.Horizontal)

    def master_init_actions(self) -> None:
        """
        main.ui所有的事件槽函数，都在这里
        :return:
        """
        action_callback_list = []

        #
        # 数据文件列表，双击
        action_callback_list.append(
            ActionCallback(id='dbclick_parsefile', source=self.datafiles_list, event='itemDoubleClicked',
                           callback=self.master_action_dblclick_datafiles_list))
        # 比较数据集
        action_callback_list.append(
            ActionCallback(id='compare_stack', source=self.btn_compare_stack, event='clicked',
                           callback=self.master_action_btn_compare_stack)
        )
        # 双击，加载数据集
        action_callback_list.append(
            ActionCallback(id='dbclick_load_dataset', source=self.listWidget_stack, event='itemDoubleClicked',
                           callback=self.master_action_dblclick_load_dataset)
        )
        # 配置项，停用词
        action_callback_list.append(
            ActionCallback(id='choose_stop_words', source=self.btn_stop_words_dict, event='clicked',
                           callback=self.master_action_datafiles_stop_words_dict))

        # 配置项，合并词
        action_callback_list.append(
            ActionCallback(id='choose_combine_words', source=self.btn_combine_words_dict, event='clicked',
                           callback=self.master_action_datafiles_combine_words_dict))

        # 配置项，受控词
        action_callback_list.append(
            ActionCallback(id='choose_controlled_words', source=self.btn_controlled_words_dict, event='clicked',
                           callback=self.master_action_datafiles_controlled_words_dict))

        # 配置项，保存
        action_callback_list.append(ActionCallback(id='save_config', source=self.btn_save_config, event='clicked',
                                                   callback=self.master_action_save_configs))

        ##########################################################################################################################

        for action in action_callback_list:
            getattr(action.source, action.event).connect(action.callback)

    def master_init_config(self) -> None:
        """
        初始化配置项中的参数
        :return:
        """
        self.config_datafiles_csv_seperator.setText(Cfg.csv_seperator.value)
        self.config_stop_words_dict.setText(Cfg.stop_words.value)
        self.config_combine_words_dict.setText(Cfg.combine_words.value)
        self.config_controlled_words_dict.setText(Cfg.controlled_words.value)

    ###############################################################################################

    def master_init_menubar(self):
        self.menutool_list = []
        ## 文件 ####################################################################################################

        self.menutool_list.append(
            MenuTool(id='parse_file', label='解析', icon='aislogo.png', menubar='menu_file', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.master_action_datafiles_parse)
        )

        self.menutool_list.append(
            MenuTool(id='save_file', label='保存', icon='xiazai.png', menubar='menu_file', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.clean_do_menu_save)
        )
        ## 编辑 ####################################################################################################

        self.menutool_list.append(
            MenuTool(id='undo', label='撤回', icon='chexiao.png', menubar='menu_edit', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.clean_do_menu_undo)
        )

        self.menutool_list.append(
            MenuTool(id='redo', label='恢复', icon='huifu.png', menubar='menu_edit', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.clean_do_menu_redo)
        )

        self.menutool_list.append(
            MenuTool(id='delete_row', label='删除行', icon='yichu.png', menubar='menu_edit', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.clean_do_menu_delete_row)
        )

        self.menutool_list.append(
            MenuTool(id='delete_column', label='删除列', icon='yichu2.png', menubar='menu_edit', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.clean_do_menu_delete_column)
        )

        self.menutool_list.append(
            MenuTool(id='rename_column', label='重命名', icon='gengduo.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_rename)
        )

        self.menutool_list.append(
            MenuTool(id='copy_column', label='复制列', icon='lieziduan.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_copy_column)
        )

        self.menutool_list.append(
            MenuTool(id='split_column', label='拆分列', icon='zhongmingming.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_split_column)
        )

        self.menutool_list.append(
            MenuTool(id='replace_column', label='替换值', icon='bumenpaixu.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_replace_column)
        )

        self.menutool_list.append(
            MenuTool(id='compare_column', label='比较列', icon='lieziduan.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_compare_columns)
        )

        self.menutool_list.append(
            MenuTool(id='modify_value', label='修改值', icon='riqi.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_modify_value)
        )

        self.menutool_list.append(
            MenuTool(id='vertical_concat', label='合并文件', icon='vertical_concat.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_vertical_concat)
        )
        ## 清洗 ####################################################################################################

        self.menutool_list.append(
            MenuTool(id='metadata', label='元数据', icon='biaoge.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_metadata)
        )

        self.menutool_list.append(
            MenuTool(id='distinct_row', label='行去重', icon='shuzi.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_row_deduplicate)
        )

        self.menutool_list.append(
            MenuTool(id='combine_synonym', label='同义词', icon='shujufenxi.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_combine_synonym)
        )

        self.menutool_list.append(
            MenuTool(id='stop_words', label='停用词', icon='wenben.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_stop_words)
        )

        self.menutool_list.append(
            MenuTool(id='filter_row', label='过滤行', icon='tubiaozhutu.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_clean_filter)
        )

        ## 分析 ####################################################################################################

        self.menutool_list.append(
            MenuTool(id='split_words', label='切分词', icon='xianshi.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_split_words)
        )

        self.menutool_list.append(
            MenuTool(id='count_stat', label='词频统计', icon='yingyongchangjing.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_wordcount_stat)
        )

        self.menutool_list.append(
            MenuTool(id='cocon_stat', label='共现统计', icon='yingyongzhongxin.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_cocon_stat)
        )

        self.menutool_list.append(
            MenuTool(id='similarity_row', label='相似比较', icon='biaochaxun.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_row_similarity)
        )

        self.menutool_list.append(
            MenuTool(id='group_stat', label='分组统计', icon='biaochaxun.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_group_stat)
        )

        self.menutool_list.append(
            MenuTool(id='extract_feature', label='特征提取', icon='zhenshikexin.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_extract_features)
        )

        self.menutool_list.append(
            MenuTool(id='graph_config', label='图表配置', icon='app.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_graph_config)
        )
        ## 计量 ####################################################################################################
        self.menutool_list.append(
            MenuTool(id='metrics_yearly_stat', label='年份统计', icon='app.png', menubar='menu_metrics',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_window_savestore)
        )
        self.menutool_list.append(
            MenuTool(id='metrics_build_matrix', label='矩阵构建', icon='app.png', menubar='menu_metrics',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_window_savestore)
        )
        ## 窗口 ####################################################################################################
        self.menutool_list.append(
            MenuTool(id='window_savestore', label='保存布局', icon='app.png', menubar='menu_window',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_window_savestore)
        )

        self.menutool_list.append(
            MenuTool(id='window_restore', label='恢复布局', icon='app.png', menubar='menu_window',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.master_init_dock)
        )

        ######################################################################################################

        idset = set([menutool.id for menutool in self.menutool_list])
        iconset = set([menutool.icon for menutool in self.menutool_list])
        assert len(self.menutool_list) == len(idset)
        # assert len(self.menutool_list) == len(iconset)

        for menutool in self.menutool_list:
            icon = QtGui.QIcon(os.path.join('icons', menutool.icon), color='blue')

            if menutool.show_in_menubar:
                action = QtWidgets.QAction(icon, menutool.label, self)
                action.setProperty('id', menutool.id)
                getattr(self, menutool.menubar).addAction(action)
                action.triggered.connect(self.__menutool_callback)

            if menutool.show_in_toolbar:
                button = QtWidgets.QToolButton(self)
                button.setIcon(icon)
                button.setText(menutool.label)
                button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
                button.setProperty('id', menutool.id)
                self.clean_toolbar.addWidget(button)
                button.clicked.connect(self.__menutool_callback)

    def __menutool_callback(self):
        id = self.sender().property('id')
        logger.info('使用功能  {}', id)
        for menutool in self.menutool_list:
            if id == menutool.id:
                menutool.callback()
                return
        raise ValueError(f'不识别的操作id={id}')

    def master_init_signal(self):
        ssignal.info.connect(self.master_show_info)
        ssignal.error.connect(self.master_show_error)
        ssignal.set_clean_dataset.connect(self.master_set_clean_df)
        ssignal.datafiles_changing.connect(self.master_action_datafiles_list)
        ssignal.update_cache.connect(self.master_show_in_stack)

    #################################################################################################33
    def master_show_info(self, val) -> None:
        self.statusBar().setStyleSheet("color: blue;font-weight: bold;")
        self.statusBar().showMessage(val)

    def master_show_error(self, val) -> None:
        self.statusBar().setStyleSheet("color: red;font-weight: bold;")
        self.statusBar().showMessage(val)

    def master_show_permanent(self, msg) -> None:
        self.statusBar().addPermanentWidget(QLabel(msg), stretch=0)

    #######################################################################################33

    def master_set_clean_df(self, df, inplace_index=True, drop_index=True) -> None:
        self.clean_datatable.set_dataset(
            df, inplace_index=inplace_index, drop_index=drop_index
        )

    #################################################
    def master_action_btn_compare_stack(self):
        logger.info("比较数据栈文件异同")

        selected_fnames = [item.text() for item in self.listWidget_stack.selectedItems()]

        if len(selected_fnames) != 2:
            ssignal.error.emit(f"错误，请选择2个数据集")
            return

        # 提取id
        ids = [str(item).split('\t')[0] for item in selected_fnames]
        # 提取DataFrame
        dfs = [PandasCache.get(int(id)) for id in ids]
        self.cleanCompareDatasetThread = CleanCompareDatasetThread(dfs[0], dfs[1])
        self.cleanCompareDatasetThread.start()

    def master_action_dblclick_load_dataset(self, item) -> None:
        logger.info("加载数据集")

        row = item.text()
        id = row.split('\t')[0]
        df = PandasCache.get(int(id))

        self.cleanLoadDatasetThread = CleanLoadDatasetThread(df)
        self.cleanLoadDatasetThread.start()

    def master_action_dblclick_datafiles_list(self, item):
        logger.info("双击数据文件列表，解析数据文件")

        fname = item.text()

        if fname.endswith(".xls") or fname.endswith(".xlsx"):
            format = FileFormat.EXCEL
        elif fname.endswith(".csv"):
            format = FileFormat.CSV
        elif fname.endswith(".pkl"):
            format = FileFormat.PICKLE
        else:
            format = "error"

        if format == "error":
            ssignal.error.emit("不识别的文件格式，请点击解析按钮")
            return

        # 双击，只会选择一个文件，所以包装成list
        abs_datafiles = os.path.join(Cfg.datafiles.value, fname)
        abs_datafiles = [abs_datafiles]
        # csv文件分隔符
        sep = Cfg.csv_seperator.value

        self.cleanSaveDatasetThread = CleanParseFileThread(abs_datafiles, format, sep)
        self.cleanSaveDatasetThread.start()

    def master_action_datafiles_list(self, *args):
        fnames = [fname for fname in os.listdir(Cfg.datafiles.value)]
        # 过滤文件夹，只保留文件
        fnames = [
            fname
            for fname in fnames
            if os.path.isfile(os.path.join(Cfg.datafiles.value, fname))
        ]
        self.datafiles_list.clear()
        self.datafiles_list.addItems(fnames)

    def master_show_in_stack(self):
        self.listWidget_stack.clear()
        logger.debug('数据栈显示缓存')
        for id, name, value in PandasCache.allinfo():
            self.listWidget_stack.addItem(f'{id}\t{name}')

    def master_action_datafiles_parse(self):
        logger.info("数据文件列表按钮，解析数据文件")

        selected_fnames = [item.text() for item in self.datafiles_list.selectedItems()]

        if len(selected_fnames) == 0:
            ssignal.error.emit(f"错误，请选择同一种类型的数据文件")
            return

        # 获取所有的扩展名
        suffixes = [str(fname).split(".")[1] for fname in selected_fnames]

        if len(set(suffixes)) != 1:
            self.master_show_error(f"错误，请选择同一种类型的数据文件")
            return

        abs_datafiles = [
            os.path.join(Cfg.datafiles.value, fname) for fname in selected_fnames
        ]
        sep = self.config_datafiles_csv_seperator.text()

        self.popupDatafilesParse = PopupDatafilesParse(self, abs_datafiles, sep)
        self.popupDatafilesParse.show()

    def master_action_datafiles_stop_words_dict(self):

        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择停用词典",  # 标题
            Cfg.dicts.value,  # 起始目录
            "词典类型 (*.txt)"
        )

        if filePath:
            self.config_stop_words_dict.setText(filePath)

    def master_action_datafiles_combine_words_dict(self):

        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择合并词典",  # 标题
            Cfg.dicts.value,  # 起始目录
            "词典类型 (*.txt)"
        )

        if filePath:
            self.config_combine_words_dict.setText(filePath)

    def master_action_datafiles_controlled_words_dict(self):

        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择受控词典",  # 标题
            Cfg.dicts.value,  # 起始目录
            "词典类型 (*.txt)"
        )

        if filePath:
            self.config_controlled_words_dict.setText(filePath)

    def master_action_save_configs(self):
        logger.info("保存配置信息")

        Cfg.set(Cfg.csv_seperator.key, self.config_datafiles_csv_seperator.text().strip())
        Cfg.set(Cfg.stop_words.key, self.config_stop_words_dict.text())
        Cfg.set(Cfg.combine_words.key, self.config_combine_words_dict.text())
        Cfg.set(Cfg.controlled_words.key, self.config_controlled_words_dict.text())

        ssignal.info.emit("保存成功")

    ########################################################################

    #######################################################################

    def clean_do_menu_undo(self):
        logger.info("清洗，撤销")

        df = self.pandasCache.undo()

        if df is not None:
            ssignal.set_clean_dataset.emit(df)
            ssignal.info.emit("撤销")
        else:
            ssignal.error.emit("无法撤销")

    def clean_do_menu_redo(self):
        logger.info("清洗，恢复")

        df = self.pandasCache.redo()

        if df is None:
            ssignal.error.emit("无法恢复")
            return

        ssignal.info.emit("恢复")
        ssignal.set_clean_dataset.emit(df)

    def clean_do_menu_delete_row(self):
        logger.info("清洗，删除行")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        df = self.context.get_df()
        self.cleanDeleteRowsThread = CleanDeleteRowsThread(df, self.clean_datatable.get_selected_row_indexes())
        self.cleanDeleteRowsThread.start()

    def clean_do_menu_delete_column(self):
        logger.info("清洗，删除列")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        df = self.context.get_df()
        self.cleanDeleteColsThread = CleanDeleteColumnsThread(df, self.clean_datatable.get_selected_col_indexes())
        self.cleanDeleteColsThread.start()

    def clean_do_menu_metadata(self):
        logger.info("清洗，元数据")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCleanMetadata = PopupCleanMetadata(self)
        self.popupCleanMetadata.show()

    def clean_do_menu_graph_config(self):
        logger.info("清洗，图表配置")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popSizeDistance = PopupGraphConfig(self)
        self.popSizeDistance.show()

    def clean_do_menu_save(self):
        logger.info("清洗，保存")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        filePath, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "保存数据文件",  # 标题
            Cfg.datafiles.value,  # 起始目录
            "Excel (*.xlsx);;Csv (*.csv);;Pickle (*.pkl)",  # 选择类型过滤项，过滤内容在括号中
        )

        if filePath:
            self.cleanSaveDatasetThread = CleanSaveDatasetThread(
                self.context.get_df(), filePath
            )
            self.cleanSaveDatasetThread.start()

    def clean_do_menu_rename(self):
        logger.info("清洗，重命名")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCleanRename = PopupCleanRename(self)
        self.popupCleanRename.show()

    def clean_do_menu_copy_column(self):
        logger.info("清洗，复制列")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCopyColumn = PopupCopyColumn(self)
        self.popupCopyColumn.show()

    def clean_do_menu_split_column(self):
        logger.info("清洗，拆分列")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupSplitColumn = PopupSplitColumn(self)
        self.popupSplitColumn.show()

    def clean_do_menu_replace_column(self):
        logger.info("清洗，替换值")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupReplaceColumn = PopupReplaceColumn(self)
        self.popupReplaceColumn.show()

    def clean_do_menu_combine_synonym(self):
        logger.info("清洗，同义词")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCombineSynonym = PopupCombineSynonym(self)
        self.popupCombineSynonym.show()

    def clean_do_menu_stop_words(self):
        logger.info("清洗，停用词")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupStopWords = PopupStopWords(self)
        self.popupStopWords.show()

    def clean_do_menu_wordcount_stat(self):
        logger.info("清洗，词频统计")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupWordCountStat = PopupWordCountStat(self)
        self.popupWordCountStat.show()

    def clean_do_menu_cocon_stat(self):
        logger.info("清洗，共词分析")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCoconStat = PopupCoconStat(self)
        self.popupCoconStat.show()

    def clean_do_menu_compare_columns(self):
        logger.info("清洗，对比列")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCompareColumns = PopupCompareColumns(self)
        self.popupCompareColumns.show()

    def clean_do_menu_modify_value(self):
        logger.info("清洗，修改值")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupModifyValues = PopupModifyValues(self)
        self.popupModifyValues.show()

    def clean_do_menu_row_deduplicate(self):
        logger.info("清洗，行去重")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupRowDistinct = PopupRowDeduplicate(self)
        self.popupRowDistinct.show()

    def clean_do_menu_row_similarity(self):
        logger.error("清洗，相似度， 有个difflib模块，可以做相似比较")

        if self.context.table_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupSimilarityRows = PopupSimilarityRows(self)
        self.popupSimilarityRows.show()

    def clean_do_menu_vertical_concat(self):
        logger.info("清洗，数据合并")

        selected_fnames = [item.text() for item in self.datafiles_list.selectedItems()]

        if len(selected_fnames) < 2:
            ssignal.error.emit(f"错误，请选择至少2个csv类型的数据文件")
            return

        # 获取所有的扩展名
        suffixes = [str(fname).split(".")[1] for fname in selected_fnames]

        if len(set(suffixes)) != 1:
            self.master_show_error(f"错误，请选择csv类型的数据文件")
            return

        abs_datafiles = [
            os.path.join(Cfg.datafiles.value, fname) for fname in selected_fnames
        ]

        self.popupVerticalConcat = PopupVerticalConcat(self, abs_datafiles)
        self.popupVerticalConcat.show()

    def clean_do_menu_group_stat(self):
        logger.info("清洗，分组统计")

        if self.context.table_no_data():
            ssignal.error.emit('没有数据')
            return

        self.popupCleanGroupStat = WinGroupStat(self)
        self.popupCleanGroupStat.show()

    def clean_do_menu_split_words(self):
        logger.info("清洗，分词")

        if self.context.table_no_data():
            ssignal.error.emit('没有数据')
            return

        self.popupSplitWords = PopupSplitWords(self)
        self.popupSplitWords.show()

    def clean_do_menu_extract_features(self):
        logger.info("清洗，特征提取")

        if self.context.table_no_data():
            ssignal.error.emit('没有数据')
            return

        self.popupExtractFeatures = PopupExtractFeatures(self)
        self.popupExtractFeatures.show()

    def clean_do_menu_clean_filter(self):
        logger.debug("清洗，过滤行")

        self.popupFilterRows = PopupFilterRows(self)
        self.popupFilterRows.show()

    #######################################################################
    def clean_do_menu_window_savestore(self):
        logger.info('保存布局')

        Cfg.set('geometry', self.saveGeometry())
        Cfg.set('windowState', self.saveState())

    #######################################################################

    def graph_set_graphdata(self, data: GraphData):
        self.graph_data = data
    #######################################################################

    #######################################################################
