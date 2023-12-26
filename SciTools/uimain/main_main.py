"""
数据处理的功能，封装在biz模块。
弹出窗口封装在popup模块。创建的窗口对象，必须使用self.xxx
多线程封装在runner模块。创建的线程对象，必须使用self.xxx

方法的logger下面，必须空一行
"""
import collections
import os.path
from typing import List
import pandas as pd
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QFileDialog, QLabel
from loguru import logger

from core.const import FileFormat
from core.mgraph import GraphData
from core.const import Config, ssignal
from core.util import PandasCache, PandasUtil
from uimain.uipy.ui_main import Ui_MainWindow
from uipopup.main_cocon_stat import PopupCoconStat
from uipopup.main_combine_synonym import PopupCombineSynonym
from uipopup.main_compare_column import PopupCompareColumns
from uipopup.main_copy_column import PopupCopyColumn
from uipopup.main_extract_features import PopupExtractFeatures
from uipopup.main_graph_config import PopupGraphConfig
from uipopup.main_split_words import PopupSplitWords
from uipopup.main_vertical_concat import PopupVerticalConcat
from uipopup.main_wordcount_stat import PopupWordCountStat
from uipopup.main_dataset_metadata import PopupCleanMetadata
from uipopup.main_modify_values import PopupModifyValues
from uipopup.main_parse_datafiles import PopupDatafilesParse
from uipopup.main_rename_column import PopupCleanRename
from uipopup.main_replace_column import PopupReplaceColumn
from uipopup.main_row_distinct import PopupRowDistinct
from uipopup.main_similarity_row import PopupSimilarityRows
from uipopup.main_split_column import PopupSplitColumn
from uipopup.main_stop_words import PopupStopWords
from mrunner import (
    CleanSaveDatasetThread,
    CleanParseFileThread,
    WatchDataFilesChaningThread,
)
from core.toolkit.mtoolkit import TableKit

MenuTool = collections.namedtuple('MenuTool', ['id' , 'label', 'icon', 'menubar', 'show_in_menubar', 'show_in_toolbar', 'callback'])
MenubarSeperator = collections.namedtuple('MenubarSeperator', ['menubar'])
ToolbarSeperator = collections.namedtuple('ToolbarSeperator', [])
class MasterMainWindows(QMainWindow, Ui_MainWindow):
    """
    本窗口的代码，使用master开头。放在最前面。
    清洗代码，使用clean开头。
    """

    def __init__(self):
        super(MasterMainWindows, self).__init__()
        self.setupUi(self)

        # 1、初始化本窗口的内容 ##################################################
        if Config.get('geometry'):
            self.restoreGeometry(Config.get('geometry'))
            self.restoreState(Config.get('windowState'))
        else:
            self.master_init_dock()

        self.master_init_action()


        ## 2、绑定信息处理器 #####################################################

        ssignal.info.connect(self.master_show_info)
        ssignal.error.connect(self.master_show_error)
        ssignal.set_clean_dataset.connect(self.master_set_clean_df)
        ssignal.datafiles_changing.connect(self.master_action_datafiles_list)
        ssignal.update_cache.connect(self.master_show_in_stack)

        ## 3、清洗部分初始化 #####################################################

        # clean 数据缓存
        self.pandasCache = PandasCache()

        # clean 菜单栏、工具栏
        self.menutool_list = []
        self.master_init_menubar_list()
        self.init_menutool()
        # ## 4、 数据分析部分初始化 ###################################################


        ## 5、  图表部分初始化 ######################################################################
        self.graph_data = GraphData()


        ## 6、  数据初始化 ######################################################################
        self.watchDataFilesChangingThread = WatchDataFilesChaningThread()
        self.watchDataFilesChangingThread.start()

        self.master_action_datafiles_list()
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
        self.resizeDocks([self.dockWidget_datafiles, self.dockWidget_table, self.dockWidget_config], [2,5,1], QtCore.Qt.Orientation.Horizontal)
    def master_init_action(self) -> None:
        """
        main.ui所有的事件槽函数，都在这里
        :return:
        """
        # 监听datafiles目录的文件变化
        # 数据文件列表，双击
        self.datafiles_list.itemDoubleClicked.connect(
            self.master_action_dblclick_datafiles_list
        )


        # # 配置项，停用词
        self.btn_stop_words_dict.clicked.connect(self.master_action_datafiles_stop_words_dict)
        # # 配置项，合并词
        self.btn_combine_words_dict.clicked.connect(self.master_action_datafiles_combine_words_dict)
        # # 配置项，受控词
        self.btn_controlled_words_dict.clicked.connect(self.master_action_datafiles_controlled_words_dict)
        # # 配置项，保存
        self.btn_save_config.clicked.connect(self.master_action_save_configs)

    def master_init_config(self) -> None:
        """
        初始化配置项中的参数
        :return:
        """
        self.config_datafiles_csv_seperator.setText(Config.csv_seperator.value)
        self.config_stop_words_dict.setText(Config.stop_words.value)
        self.config_combine_words_dict.setText(Config.combine_words.value)
        self.config_controlled_words_dict.setText(Config.controlled_words.value)

    ###############################################################################################

    def master_init_menubar_list(self):
        """
        槽函数，必须是clean_do_menu_开头
        :return:
        """

        ## 文件 ############################################################
        # 解析
        self.menutool_list.append(
            MenuTool(id='parse_file', label='解析', icon='aislogo.png', menubar='menu_file', show_in_menubar=True, show_in_toolbar=True, callback=self.master_action_datafiles_parse)
                    )

        # 保存
        self.menutool_list.append(
            MenuTool(id='save_file', label='保存', icon='xiazai.png', menubar='menu_file', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.clean_do_menu_save)
        )

        ## 编辑 ############################################################
        # 撤回
        self.menutool_list.append(
            MenuTool(id='undo', label='撤回', icon='chexiao.png', menubar='menu_edit', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.clean_do_menu_undo)
        )

        # 恢复
        self.menutool_list.append(
            MenuTool(id='redo', label='恢复', icon='huifu.png', menubar='menu_edit', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.clean_do_menu_redo)
        )

        # 删除行
        self.menutool_list.append(
            MenuTool(id='delete_row', label='删除行', icon='yichu.png', menubar='menu_edit', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.clean_do_menu_row_delete)
        )

        # 删除列
        self.menutool_list.append(
            MenuTool(id='delete_column', label='删除列', icon='yichu2.png', menubar='menu_edit', show_in_menubar=True,
                     show_in_toolbar=True, callback=self.clean_do_menu_column_delete)
        )


        # 重命名
        self.menutool_list.append(
            MenuTool(id='rename_column', label='重命名', icon='gengduo.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_rename)
        )

        # 复制列
        self.menutool_list.append(
            MenuTool(id='copy_column', label='复制列', icon='lieziduan.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_copy_column)
        )

        # 拆分列
        self.menutool_list.append(
            MenuTool(id='split_column', label='拆分列', icon='zhongmingming.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_split_column)
        )

        # 替换值
        self.menutool_list.append(
            MenuTool(id='replace_column', label='替换值', icon='bumenpaixu.png', menubar='menu_edit',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_replace_column)
        )

        # self.clean_toolbar.addSeparator()

        ## 清洗 ############################################################

        # 元数据
        self.menutool_list.append(
            MenuTool(id='metadata', label='元数据', icon='biaoge.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_metadata)
        )

        # 列比较
        self.menutool_list.append(
            MenuTool(id='compare_column', label='比较列', icon='lieziduan.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_compare_columns)
        )

        # 修改值
        self.menutool_list.append(
            MenuTool(id='modify_value', label='修改值', icon='riqi.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_modify_value)
        )

        # 数据合并
        self.menutool_list.append(
            MenuTool(id='vertical_concat', label='合并列', icon='vertical_concat.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_vertical_concat)
        )

        # 补全值
        self.menutool_list.append(
            MenuTool(id='fill_value', label='补全值', icon='jiekoupeizhi.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_clean_fill_value)
        )

        # 合并词
        self.menutool_list.append(
            MenuTool(id='combine_synonym', label='合并词', icon='shujufenxi.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_combine_synonym)
        )

        # 行去重
        self.menutool_list.append(
            MenuTool(id='distinct_row', label='去重行', icon='shuzi.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_row_distinct)
        )

        # 停用词
        self.menutool_list.append(
            MenuTool(id='stop_words', label='停用词', icon='wenben.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_stop_words)
        )

        # 切分词
        self.menutool_list.append(
            MenuTool(id='split_words', label='切分词', icon='xianshi.png', menubar='menu_clean',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_split_words)
        )
        #
        # self.clean_toolbar.addSeparator()

        ## 分析 ############################################################

        # 词频统计
        self.menutool_list.append(
            MenuTool(id='count_stat', label='词频统计', icon='yingyongchangjing.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_wordcount_stat)
        )

        # 共现分析
        self.menutool_list.append(
            MenuTool(id='cocon_stat', label='共现统计', icon='yingyongzhongxin.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_cocon_stat)
        )

        # 相似度
        self.menutool_list.append(
            MenuTool(id='similarity_row', label='相似比较', icon='biaochaxun.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_row_similarity)
        )

        # 分组统计
        self.menutool_list.append(
            MenuTool(id='group_stat', label='分组统计', icon='biaochaxun.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_group_stat)
        )

        # 过滤值
        self.menutool_list.append(
            MenuTool(id='filter_row', label='过滤行', icon='biaochaxun.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_clean_filter)
        )

        # 特征提取
        self.menutool_list.append(
            MenuTool(id='extract_feature', label='特征提取', icon='zhenshikexin.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_extract_features)
        )

        # 图表配置
        self.menutool_list.append(
            MenuTool(id='graph_config', label='图表配置', icon='app.png', menubar='menu_analysis',
                     show_in_menubar=True,
                     show_in_toolbar=True,
                     callback=self.clean_do_menu_graph_config)
        )

        ## 窗口 ############################################################
        self.menu_window_savestore.triggered.connect(self.clean_do_menu_window_savestore)
        self.menu_window_restore.triggered.connect(self.master_init_dock)





    def init_menutool(self):
        idset = set([menutool.id for menutool in self.menutool_list])
        iconset = set([menutool.icon for menutool in self.menutool_list])
        assert len(self.menutool_list) == len(idset)
        # assert len(self.menutool_list) == len(iconset)

        for menutool in self.menutool_list:
            icon = QtGui.QIcon(os.path.join('icons', menutool.icon),color='blue')

            if menutool.show_in_menubar:
                action = QtWidgets.QAction(icon, menutool.label, self)
                action.setProperty('id', menutool.id)
                getattr(self, menutool.menubar).addAction(action)
                action.triggered.connect(self.menutool_callback)

            if menutool.show_in_toolbar:
                button = QtWidgets.QToolButton(self)
                button.setIcon(icon)
                button.setText(menutool.label)
                button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
                button.setProperty('id', menutool.id)
                self.clean_toolbar.addWidget(button)
                button.clicked.connect(self.menutool_callback)

    def menutool_callback(self):
        id = self.sender().property('id')
        logger.info('使用功能  {}', id)
        for menutool in self.menutool_list:
            if id == menutool.id:
                menutool.callback()
                return
        raise ValueError(f'不识别的操作id={id}')

    def master_show_info(self, val) -> None:
        """
        状态栏，显示信息
        :param val:
        :return:
        """
        self.statusBar().setStyleSheet("color: blue;font-weight: bold;")
        self.statusBar().showMessage(val)

    def master_show_error(self, val) -> None:
        self.statusBar().setStyleSheet("color: red;font-weight: bold;")
        self.statusBar().showMessage(val)

    def master_show_permanent(self, msg)->None:
        self.statusBar().addPermanentWidget(QLabel(msg), stretch=0)
    def master_get_clean_df(self) -> pd.DataFrame:
        return self.clean_datatable.get_dataset()

    def master_set_clean_df(self, df, inplace_index=True, drop_index=True) -> None:
        self.clean_datatable.set_dataset(
            df, inplace_index=inplace_index, drop_index=drop_index
        )

    def master_get_clean_columns(self) -> List[str]:
        return self.master_get_clean_df().columns

    def master_get_clean_table(self) -> TableKit:
        return self.clean_datatable

    def master_clean_no_data(self) -> bool:
        return not self.clean_datatable.has_dataset()

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
        abs_datafiles = os.path.join(Config.datafiles.value, fname)
        abs_datafiles = [abs_datafiles]
        # csv文件分隔符
        sep = Config.csv_seperator.value

        self.cleanSaveDatasetThread = CleanParseFileThread(abs_datafiles, format, sep)
        self.cleanSaveDatasetThread.start()

    def master_action_datafiles_list(self, *args):
        fnames = [fname for fname in os.listdir(Config.datafiles.value)]
        # 过滤文件夹，只保留文件
        fnames = [
            fname
            for fname in fnames
            if os.path.isfile(os.path.join(Config.datafiles.value, fname))
        ]

        self.datafiles_list.clear()
        self.datafiles_list.addItems(fnames)

    def master_show_in_stack(self):
        self.listWidget_stack.clear()
        logger.debug('数据栈显示缓存')
        for id in PandasCache.allinfo():
            self.listWidget_stack.addItem(str(id))

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
            os.path.join(Config.datafiles.value, fname) for fname in selected_fnames
        ]
        sep = self.config_datafiles_csv_seperator.text()

        self.popupDatafilesParse = PopupDatafilesParse(self, abs_datafiles, sep)
        self.popupDatafilesParse.show()

    def master_action_datafiles_stop_words_dict(self):

        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择停用词典",  # 标题
            Config.dicts,  # 起始目录
            "词典类型 (*.txt)"
        )

        if filePath:
            self.config_stop_words_dict.setText(filePath)

    def master_action_datafiles_combine_words_dict(self):

        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择合并词典",  # 标题
            Config.dicts.value,  # 起始目录
            "词典类型 (*.txt)"
        )

        if filePath:
            self.config_combine_words_dict.setText(filePath)

    def master_action_datafiles_controlled_words_dict(self):

        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择受控词典",  # 标题
            Config.dicts.value,  # 起始目录
            "词典类型 (*.txt)"
        )

        if filePath:
            self.config_controlled_words_dict.setText(filePath)

    def master_action_save_configs(self):
        logger.info("保存配置信息")

        Config.set(Config.csv_seperator.key, self.config_datafiles_csv_seperator.text().strip())
        Config.set(Config.stop_words.key, self.config_stop_words_dict.text())
        Config.set(Config.combine_words.key, self.config_combine_words_dict.text())
        Config.set(Config.controlled_words.key, self.config_controlled_words_dict.text())

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

    def clean_do_menu_metadata(self):
        logger.info("清洗，元数据")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCleanMetadata = PopupCleanMetadata(self)
        self.popupCleanMetadata.show()

    def clean_do_menu_graph_config(self):
        logger.info("清洗，图表配置")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popSizeDistance = PopupGraphConfig(self)
        self.popSizeDistance.show()

    def clean_do_menu_save(self):
        logger.info("清洗，保存")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        filePath, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "保存数据文件",  # 标题
            Config.datafiles.value,  # 起始目录
            "Excel (*.xlsx);;Csv (*.csv);;Pickle (*.pkl)",  # 选择类型过滤项，过滤内容在括号中
        )

        if filePath:
            self.cleanSaveDatasetThread = CleanSaveDatasetThread(
                self.master_get_clean_df(), filePath
            )
            self.cleanSaveDatasetThread.start()

    def clean_do_menu_rename(self):
        logger.info("清洗，重命名")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCleanRename = PopupCleanRename(self)
        self.popupCleanRename.show()

    def clean_do_menu_copy_column(self):
        logger.info("清洗，复制列")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCopyColumn = PopupCopyColumn(self)
        self.popupCopyColumn.show()

    def clean_do_menu_split_column(self):
        logger.info("清洗，拆分列")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupSplitColumn = PopupSplitColumn(self)
        self.popupSplitColumn.show()

    def clean_do_menu_replace_column(self):
        logger.info("清洗，替换值")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupReplaceColumn = PopupReplaceColumn(self)
        self.popupReplaceColumn.show()

    def clean_do_menu_combine_synonym(self):
        logger.info("清洗，合并词")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCombineSynonym = PopupCombineSynonym(self)
        self.popupCombineSynonym.show()

    def clean_do_menu_stop_words(self):
        logger.info("清洗，停用词")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupStopWords = PopupStopWords(self)
        self.popupStopWords.show()

    def clean_do_menu_wordcount_stat(self):
        logger.info("清洗，词频统计")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupWordCountStat = PopupWordCountStat(self)
        self.popupWordCountStat.show()

    def clean_do_menu_cocon_stat(self):
        logger.info("清洗，共现分析")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCoconStat = PopupCoconStat(self)
        self.popupCoconStat.show()

    def clean_do_menu_compare_columns(self):
        logger.info("清洗，对比列")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupCompareColumns = PopupCompareColumns(self)
        self.popupCompareColumns.show()

    def clean_do_menu_modify_value(self):
        logger.info("清洗，修改值")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupModifyValues = PopupModifyValues(self)
        self.popupModifyValues.show()

    def clean_do_menu_row_distinct(self):
        logger.info("清洗，行去重")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupRowDistinct = PopupRowDistinct(self)
        self.popupRowDistinct.show()

    def clean_do_menu_row_similarity(self):
        logger.info("清洗，相似度")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        self.popupSimilarityRows = PopupSimilarityRows(self)
        self.popupSimilarityRows.show()

    def clean_do_menu_row_delete(self):
        logger.info("清洗，删除行")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        df = self.master_get_clean_df()
        df2 = PandasUtil.delete_rows(df, self.clean_datatable.get_selected_rows())
        ssignal.push_cache.emit(df2)
        self.master_set_clean_df(df2)
        ssignal.info.emit("删除行")

    def clean_do_menu_column_delete(self):
        logger.info("清洗，删除列")

        if self.master_clean_no_data():
            ssignal.error.emit("没有数据")
            return

        df = self.master_get_clean_df()
        df2 = PandasUtil.delete_columns(df, self.clean_datatable.get_selected_cols())
        ssignal.push_cache.emit(df2)
        self.master_set_clean_df(df2)
        ssignal.info.emit("删除列")

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
            os.path.join(Config.datafiles.value, fname) for fname in selected_fnames
        ]

        self.popupVerticalConcat = PopupVerticalConcat(self, abs_datafiles)
        self.popupVerticalConcat.show()

    def clean_do_menu_group_stat(self):
        logger.info("清洗，分组统计")
        ssignal.error.emit("还没有实现")

        # if self.master_clean_no_data():
        #     ssignal.error.emit('没有数据')
        #     return

        # self.popupCleanGroupStat = PopupCleanGroupStat(self)
        # self.popupCleanGroupStat.show()

    def clean_do_menu_split_words(self):
        logger.info("清洗，分词")

        if self.master_clean_no_data():
            ssignal.error.emit('没有数据')
            return

        self.popupSplitWords = PopupSplitWords(self)
        self.popupSplitWords.show()

    def clean_do_menu_extract_features(self):
        logger.info("清洗，特征提取")

        if self.master_clean_no_data():
            ssignal.error.emit('没有数据')
            return

        self.popupExtractFeatures = PopupExtractFeatures(self)
        self.popupExtractFeatures.show()

    def clean_do_menu_clean_filter(self):
        logger.info("清洗，过滤")
        ssignal.error.emit("还没有实现")

    def clean_do_menu_clean_fill_value(self):
        logger.info("清洗，补全值")
        ssignal.error.emit("还没有实现")

    #######################################################################
    def clean_do_menu_window_savestore(self):
        logger.info('保存布局')

        Config.set('geometry', self.saveGeometry())
        Config.set('windowState', self.saveState())


    #######################################################################

    def graph_set_graphdata(self, data:GraphData):
        self.graph_data = data
    #######################################################################

    #######################################################################
