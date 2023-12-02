import os
import re
import sys
import time
from collections import Counter
from typing import List
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from PySide6 import QtGui
from PySide6.QtCore import Qt, Signal, QThread
from PySide6.QtGui import QIcon, QAction, QBrush, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QSplitter, QSizePolicy, \
    QFrame, QHBoxLayout, QPushButton, QSpacerItem, QToolButton, QToolBar, QTabWidget, QFileDialog, QLineEdit, QMenu, \
    QTableWidgetItem, QTableWidget, QListWidget, \
    QAbstractItemView, QMessageBox, QMainWindow, QTextEdit, QLabel, QButtonGroup, QRadioButton, QComboBox, QSlider, \
    QHeaderView
from loguru import logger
from pandas import DataFrame
from zhon.hanzi import punctuation

logger.add("clean.log", encoding="utf-8", enqueue=True, rotation="500MB", retention="10 days")

import secrets
class Utils:
    @staticmethod
    def resort_columns(old_names, new_names):
        """
        新插入的列，位于原有列的后面
        """
        for new1 in new_names:
            old_names.remove(new1)

        for new1 in new_names:
            i = old_names.index(new1[:new1.rfind('-')])
            old_names.insert(i + 1, new1)

        return old_names


    @staticmethod
    def generate_random_color():
        """
        生成任意颜色
        """
        red = secrets.randbelow(256)
        green = secrets.randbelow(256)
        blue = secrets.randbelow(256)
        return red, green, blue

    @staticmethod
    def has_Chinese_or_punctuation( ws):
        return Utils.has_Chinese(ws) or Utils.has_punctuation(ws)
    @staticmethod
    def has_Chinese(ws):
        return any([True if '\u4e00' <= w <= '\u9fff' else False for w in jieba.lcut(ws)])
    @staticmethod
    def has_punctuation(ws):
        # 中文符号
        return any([True if w in punctuation else False for w in jieba.lcut(ws)])

class Worker(QThread):
    # 实例化一个信号对象
    valve = Signal(int)
    q = True
    pause = False
    a = 0

    def __int__(self):
        super(Worker, self).__init__()

    def run(self):
        while self.q:  # self.q控制程序是否执行
            if self.pause:
                time.sleep(0.2)
                continue
            while not self.pause and self.a < 2000:  # self.pause控制程序是否暂停
                self.a += 1
                time.sleep(0.1)
                self.valve.emit(self.a)
            if self.a >= 2000:  # self.a>2000程序结束
                return



class Cfg:
    table_header_bgcolor = 'lightblue'
    seperator = ';'
    workspace = 'D:\工作空间'
    datafiles = os.path.join(workspace, 'datafiles')
    models = os.path.join(workspace, 'models')
    formats = os.path.join(workspace, 'formats')
    dicts = os.path.join(workspace, 'dicts')


class Parser:
    """
    导出txt时，文件末尾多2个空行
    """
    CORE_ITEMS = ('RT'  # 文献类型
                  , 'A1'  # 作者
                  , 'AD'  # 工作单位
                  , 'T1'  # 题名
                  , 'JF'  # 来源
                  , 'YR'  # 出版年
                  , 'FD'  # 出版日期
                  , 'K1'  # 关键词
                  , 'AB'  # 摘要
                  )

    @staticmethod
    def parse_cnki(filenames) -> DataFrame:
        """
        解析cnki的refworks格式的数据
        """
        ds = []
        if isinstance(filenames, str):
            filenames = [filenames]

        for filename in filenames:
            with open(filename, encoding='utf-8') as f:

                values = {'RT': '', 'A1': '', 'AD': '', 'T1': '', 'JF': '', 'YR': '',
                          'FD': '',
                          'K1': '',
                          'AB': ''}
                for linone, line in enumerate(f.readlines()):
                    # 前2个字母是具体的key
                    name = line[:2].strip()
                    if name in Parser.CORE_ITEMS:
                        values[name] = line[2:].strip()

                    # 空行，表示上一条结束，新的一条开始
                    if len(line.strip()) == 0:
                        if values and len(values['RT']) > 0:
                            ds.append(values)
                        # 每次初始化数据

                        values = {'RT': '', 'A1': '', 'AD': '', 'T1': '', 'JF': '', 'YR': '', 'FD': '',
                                  'K1': '',
                                  'AB': ''}

        df = pd.DataFrame(ds, dtype='object')
        return df


class DataFileWidget(QFrame):
    signal_dataset = Signal(pd.DataFrame)
    signal_statusbar = Signal(str)

    def __init__(self, parent=None):
        super(DataFileWidget, self).__init__(parent)
        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        # 工具栏
        toolbar = QFrame()
        toolbar.setFixedHeight(20)
        mainLayout.addWidget(toolbar)

        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(0)
        toolbar.setLayout(toolbar_layout)
        btn1 = QPushButton()
        btn1.setText('数据文件')
        btn1.clicked.connect(self.action_datafiles_load)
        toolbar_layout.addWidget(btn1)

        # 选项1
        option1 = QFrame()
        option1.setFixedHeight(20)
        mainLayout.addWidget(option1)
        option1_layout = QHBoxLayout(option1)
        option1_layout.setContentsMargins(0, 0, 0, 0)
        option1_layout.setSpacing(0)

        option1_btn = QPushButton('格式：')
        option1_btn.setFixedWidth(50)
        option1_btn.clicked.connect(lambda: self.action_option1_btn(option1_format))
        option1_layout.addWidget(option1_btn)

        option1_format = QLineEdit()
        option1_format.setDisabled(True)
        option1_layout.addWidget(option1_format)

        # 按钮——解析
        btn2 = QToolButton()
        btn2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        btn2.setText('解析')
        toolbar_layout.addWidget(btn2)
        btn2.clicked.connect(lambda: self.action_datafiles_parse(option1_format))
        # 弹簧条
        toolbar_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 列表
        self.listView_datafiles = QListWidget()
        self.listView_datafiles.setSelectionMode(QAbstractItemView.ExtendedSelection)
        mainLayout.addWidget(self.listView_datafiles)

        self.default_value(option1_format)

    def default_value(self, option1_format):
        self.action_datafiles_load()
        paths = [os.path.join(Cfg.formats, name) for name in os.listdir(Cfg.formats) if
                 os.path.isfile(os.path.join(Cfg.formats, name))]
        if paths:
            option1_format.setText(paths[0])

    def action_datafiles_load(self):
        """
        单击，刷新列表
        """
        self.listView_datafiles.clear()
        fnames = [fname for fname in os.listdir(Cfg.datafiles) if os.path.isfile(os.path.join(Cfg.datafiles, fname))]
        for fname in fnames:
            self.listView_datafiles.addItem(fname)
        if fnames:
            self.listView_datafiles.setCurrentRow(0)
        self.signal_statusbar.emit('加载 {0} 个数据文件'.format(len(fnames)))

    def action_datafiles_parse(self, option1_format):
        if len(self.listView_datafiles.selectedIndexes()) == 0:
            QMessageBox.critical(self, '错误', '请在下面选择1个文件，才可以解析')
            return
        if len(option1_format.text()) == 0:
            QMessageBox.critical(self, '错误', '请在下面选择格式文件，才可以解析')
            return
        logger.info('解析数据文件')
        t1 = time.time()
        filenames = [os.path.join(Cfg.datafiles, name.text()) for name in self.listView_datafiles.selectedItems()]
        df = Parser.parse_cnki(filenames)
        t2 = time.time()

        msg = '解析{0}条记录，{1}个列，耗时{2}秒。'.format(df.shape[0], df.shape[1], round(t2 - t1, 2))
        QMessageBox.information(self, '成功', msg)

        self.signal_dataset.emit(df)

    def action_option1_btn(self, option1_format):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择格式文件",  # 标题
            Cfg.formats,  # 起始目录
            "文件类型 (*.csv *.txt *.xls *.xlsx)"  # 选择类型过滤项，过滤内容在括号中
        )
        option1_format.clear()
        option1_format.setText(filePath)

    def setMain(self, main):
        self.main = main


class DataModelWidget(QFrame):
    signal_dataset = Signal(pd.DataFrame)
    signal_statusbar = Signal(str)

    def __init__(self, parent=None):
        super(DataModelWidget, self).__init__(parent)
        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        toolbar = QWidget()
        toolbar.setFixedHeight(20)
        self.listView_datamodels = QListWidget()
        self.listView_datamodels.setSelectionMode(QAbstractItemView.SingleSelection)
        mainLayout.addWidget(toolbar)
        mainLayout.addWidget(self.listView_datamodels)

        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(0)
        toolbar.setLayout(toolbar_layout)
        btn1 = QToolButton()
        btn1.setText('数据模型')
        btn1.clicked.connect(self.action_datamodel_load)
        toolbar_layout.addWidget(btn1)

        btn2 = QToolButton()
        btn2.setText('显示')
        btn2.clicked.connect(self.action_datamodel_parse)
        toolbar_layout.addWidget(btn2)

        toolbar_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.default_value()

    def default_value(self):
        self.action_datamodel_load()

    def setMain(self, main):
        self.main = main

    def action_datamodel_load(self):
        """
        单击，刷新列表
        """
        self.listView_datamodels.clear()
        fnames = [fname for fname in os.listdir(Cfg.models) if os.path.isfile(os.path.join(Cfg.models, fname))]
        for fname in fnames:
            self.listView_datamodels.addItem(fname)
        if fnames:
            self.listView_datamodels.setCurrentRow(0)

        self.signal_statusbar.emit('加载 {0} 个数据模型'.format(len(fnames)))

    def action_datamodel_parse(self):
        """
        加载数据文件
        """
        if len(self.listView_datamodels.selectedIndexes()) == 0:
            QMessageBox.critical(self, '错误', '请在下面选择1个文件，才可以解析')
            return
        fname = self.listView_datamodels.selectedItems()[0].text()
        t1 = time.time()
        df = pd.read_pickle(os.path.join(Cfg.models, fname), compression='gzip')
        t2 = time.time()

        msg = '解析{0}条记录，{1}个列，耗时{2}秒。'.format(df.shape[0], df.shape[1], round(t2 - t1, 2))
        QMessageBox.information(self, '成功', msg)

        self.signal_dataset.emit(df)


class PopupMetadata(QFrame):
    """
    复制列，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(700, 600)
        main_layout = QVBoxLayout(self)

        main_layout.addWidget(QLabel('数据统计'))
        table_stat = QTableWidget()
        main_layout.addWidget(table_stat)

        main_layout.addWidget(QLabel('数据分布'))
        tab_freq = QTabWidget()
        main_layout.addWidget(tab_freq)

        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        btn_ok.clicked.connect(self.action_ok)
        main_layout.addWidget(btn_ok)

        self.init_table_stat(table_stat)
        self.init_table_freq(tab_freq)

    def init_table_stat(self, table_stat):
        df = self.get_dataset()
        nulls = (df.isna().sum() + df.eq('').sum())
        df = df.describe()
        # 丢掉行
        df.drop('top', axis=0, inplace=True)
        # 空值情况
        df.loc['nulls'] = nulls
        # 重命名索引
        df.rename(index={'count':'总数', 'unique':'唯一', 'freq':'众频', 'nulls':'空值'}, inplace=True)

        table_stat.setColumnCount(df.shape[1])
        table_stat.setRowCount(df.shape[0])
        table_stat.setHorizontalHeaderLabels(df.columns)

        for i, row in enumerate(df.index):
            for j, col in enumerate(df.columns):
                item = QTableWidgetItem(str(df.at[row, col]))
                table_stat.setItem(i, j, item)
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

        for i, row in enumerate(df.index.tolist()):
            table_stat.setVerticalHeaderItem(i, QTableWidgetItem(row))

    def init_table_freq(self, tab_freq):
        df = self.get_dataset()
        for i, name in enumerate(df.columns):
            tab_freq.addTab(self.__create_tab_widget(df.loc[:, name].tolist()), name)


    def __create_tab_widget(self, datalist):
        datalist = sum([row.split(Cfg.seperator) for row in datalist],[])
        datalist = Counter(datalist)
        datalist = sorted(datalist.items(), key=lambda x:x[1], reverse=True)

        table1 = QTableWidget()
        table1.verticalHeader().hide()
        table1.setColumnCount(2)
        table1.setRowCount(len(datalist))
        table1.setHorizontalHeaderLabels(['词语','频次'])
        for i in range(len(datalist)):
            for j in range(2):
                item = QTableWidgetItem(str(datalist[i][j]))
                table1.setItem(i, j, item)
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)


        ########################################################################
        # 统计频次的出现次数
        datalist = [item[1] for item in datalist]
        datalist = Counter(datalist)
        datalist = sorted(datalist.items(), key=lambda x:x[1], reverse=True)

        table2 = QTableWidget()
        table2.verticalHeader().hide()
        table2.setColumnCount(2)
        table2.setRowCount(len(datalist))
        table2.setHorizontalHeaderLabels(['词语频次','次数'])
        for i in range(len(datalist)):
            for j in range(2):
                item = QTableWidgetItem(str(datalist[i][j]))
                table2.setItem(i, j, item)
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)


        widget = QFrame()
        hlayout = QHBoxLayout(widget)
        hlayout.setContentsMargins(15,10,5,5)
        hlayout.addWidget(table1)
        hlayout.addWidget(table2)
        return widget

    def action_ok(self):
        self.close()

    def get_dataset(self):
        return self.parent.datasetTable.df


class PopupRowDistinct(QWidget):
    """
    数据去重，对话框

    参考  https://zhuanlan.zhihu.com/p/667980876
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(200, 500)
        container_layout = QVBoxLayout(self)
        container_layout.setContentsMargins(0,0,0,0)
        container_layout.setSpacing(0)

        main_widget = QFrame()
        main_widget.setFixedHeight(150)
        container_layout.addWidget(main_widget)
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # 左侧是表头列表，单选
        left_frame = QFrame()
        left_frame.setFixedWidth(50)
        main_layout.addWidget(left_frame)
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(0,0,0,0)
        left_layout.setSpacing(0)
        left_layout.addWidget(QLabel('可以多选'))
        self.column_names = QListWidget()
        self.column_names.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        left_layout.addWidget(self.column_names)
        ##################################################################
        # 中间是内容
        center_frame = QFrame()
        main_layout.addWidget(center_frame)
        center_layout = QVBoxLayout(center_frame)

        ### 第1行
        center_layout.addWidget(QLabel('行去重的时候，需要指定按照哪些列进行去重'))

        # 第2行
        row2 = QFrame()
        center_layout.addWidget(row2)
        row2layout = QHBoxLayout(row2)
        row2layout.addWidget(QLabel('相似度阈值'))

        slider_horizon = QSlider(Qt.Horizontal)
        slider_horizon.setMinimum(1)
        slider_horizon.setMaximum(100)
        slider_horizon.setSingleStep(1)
        slider_horizon.setValue(90)
        slider_horizon.setTickPosition(QSlider.TicksBelow)
        slider_horizon.setTickInterval(5)

        row2layout.addWidget(slider_horizon)

        vaLable = QLabel('90')
        slider_horizon.valueChanged.connect(lambda: self.value_changed(vaLable, slider_horizon.value()))
        vaLable.setFixedWidth(20)
        row2layout.addWidget(vaLable)


        ### 第3行
        self.label_msg = QLabel()
        self.label_msg.setStyleSheet("color:red;")
        center_layout.addWidget( self.label_msg)

        ### 第4行
        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        btn_ok.clicked.connect(lambda :self.action_ok(slider_horizon.value()))
        center_layout.addWidget(btn_ok)


        #####################################################
        ## 最下面是表格工具栏
        table_toolbar = QFrame()
        table_toolbar_layout = QHBoxLayout(table_toolbar)
        table_toolbar_layout.setContentsMargins(0,10,0,0)
        container_layout.addWidget(table_toolbar)

        btn1 = QPushButton('删除该分组')
        btn2 = QPushButton('合并该分组')
        btn3 = QPushButton('合并所有分组')
        btn1.clicked.connect(self.action_not_combine)
        btn2.clicked.connect(self.action_combine_current_group)
        btn3.clicked.connect(self.action_combine_all)
        table_toolbar_layout.addWidget(btn1)
        table_toolbar_layout.addWidget(btn2)
        table_toolbar_layout.addWidget(btn3)
        #  最下面是表格
        self.group_dataset = []
        self.group_table = QTableWidget()
        self.group_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.group_table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.group_table.verticalHeader().hide()
        container_layout.addWidget(self.group_table)
    def action_not_combine(self):
        logger.info('删除该分组，不合并')
        rows = [item.row() for item in self.group_table.selectedItems()]
        if not rows:
            QMessageBox.critical(self, '错误', '请选择一行')
            return
        row_no = rows[0]
        self.__delete_group_table(row_no, False)

    def __delete_group_table(self, row_no, can_delete):
        group_name = self.group_table.item(row_no, 1).text()
        original_nos = [row[0] for row in self.group_dataset if row[1] == group_name]
        self.group_dataset = [row for row in self.group_dataset if row[0] not in original_nos]
        self.__fill_table_data()
        if can_delete:
            df = self.get_df()
            df.drop(original_nos[1:], inplace=True)
            self.set_df(df)
    def action_combine_current_group(self):
        logger.error('合并该分组')
        rows = [item.row() for item in self.group_table.selectedItems()]
        if not rows:
            QMessageBox.critical(self, '错误', '请选择一行')
            return
        row_no = rows[0]
        self.__delete_group_table(row_no, True)


    def action_combine_all(self):
        logger.error('合并所有分组')

        if self.group_table.rowCount()==0:
            QMessageBox.critical(self, '错误', '请选进行分组，再执行合并')
            return

        temp_group_name = ''
        original_nos = []
        for row in self.group_dataset:
            if row[1] != temp_group_name:
                original_nos.append(row[0])
                temp_group_name = row[1]

        self.group_table.setRowCount(0)
        df = self.get_df()
        df = df.iloc[original_nos, :]
        self.set_df(df)

    def action_ok(self, limited:int):
        logger.error('行去重，这里还有大问题，多次点击ok有问题')
        names = [item.text() for item in self.column_names.selectedItems()]

        t1 = time.time()
        words = []
        df = self.get_df()
        for i in range(df.shape[0]):
            # 取一行多列
            dd = df.loc[i, names].tolist()
            dd = [line.split(Cfg.seperator) for line in dd]
            # list拉平
            dd = sum(dd, [])
            # TODO 结巴分词，分词后，相似度比较效果不好
            # dd = [list(jieba.cut(i.strip(), cut_all=False)) for i in dd if i.strip()]
            # dd = sum(dd, [])
            words.append(' '.join(set(dd)))

        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(words)
        cosine_sim = cosine_similarity(X, X)
        ll = len(cosine_sim)

        pairs = []
        for i in range(ll):
            for j in range(i+1,ll):
                v = cosine_sim[i,j]
                if v*100 >=limited:
                    pairs.append([i,j,v])
        # 封装一下
        primary_data = []

        for i, item in enumerate(pairs):
            # 分别是行号、组名、相似度
            row0 = [item[0], f'{i}组',  '{:.1f}'.format(item[2]*100)]
            row0.extend(  df.loc[item[0], names].tolist())
            primary_data.append(row0)
            # 分别是行号、组名、相似度
            row1 = [item[1], f'{i}组', '{:.1f}'.format(item[2]*100)]
            row1.extend(df.loc[item[1], names].tolist())
            primary_data.append(row1)


        # 合并组，以前是两两分组，现在多个分成一组
        self.color_map = {}
        self.regroup(primary_data, self.color_map)


        # 表格的列名
        table_headers = ['原行号', '组名','相似度']
        table_headers.extend(names)
        # 在表格中显示分组
        self.group_table.setColumnCount(len(table_headers))
        self.group_table.setHorizontalHeaderLabels(table_headers)
        self.group_table.setRowCount(len(self.group_dataset))
        self.group_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.__fill_table_data()

        t2 = time.time()
        msg = '分析{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(names), round(t2 - t1, 2))
        self.label_msg.setText(msg)

    def __fill_table_data(self):
        for i in range(self.group_table.rowCount()):
            self.group_table.removeRow(i)
        for i in range(len(self.group_dataset)):
            for j in range(len(self.group_dataset[i])):
                if j == 0:  # 行号默认从0开始，手工+1
                    self.group_table.setItem(i, j, QTableWidgetItem(str(self.group_dataset[i][j] + 1)))
                else:
                    self.group_table.setItem(i, j, QTableWidgetItem(str(self.group_dataset[i][j])))
                if j == 1:
                    c = self.color_map[self.group_dataset[i][1]]
                    self.group_table.item(i, j).setForeground(QBrush(QColor(c[0], c[1], c[2])))
                self.group_table.item(i, j).setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

    def regroup(self, primary_data, color_map):
        if len(primary_data) == 0:
            return
        # 取top 2加入队列
        self.group_dataset.append(primary_data[0])
        self.group_dataset.append(primary_data[1])
        first = primary_data[0]
        future_deleted = [first[1]] # 组名
        color_map[first[1]] = Utils.generate_random_color()
        for i in range(2, len(primary_data), 2):
            item = primary_data[i]
            if first[0]==item[0]:   # 原列号相同
                primary_data[i + 1][1] = first[1]   # 修改组号
                self.group_dataset.append(primary_data[i + 1]) # 配对的第2个
                future_deleted.append(item[1])  #加入组名
        primary_data = [item for item in primary_data if item[1] not in future_deleted]
        self.regroup(primary_data, color_map)



    def set_column_names(self, names):
        if names is not None:
            self.column_names.clear()
            self.column_names.addItems(names)
            self.column_names.setCurrentRow(0)

    def get_df(self):
        return self.parent.datasetTable.df

    def set_df(self, df):
        self.parent.datasetTable.set_df(df)

    def value_changed(self, lbl, val):
        lbl.setText(str(val))

class PopupSplitColumn(QFrame):
    """
    拆分列，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(500, 200)
        main_layout = QHBoxLayout(self)

        # 左侧是表头列表，单选
        left_frame = QFrame()
        main_layout.addWidget(left_frame)
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(0,0,0,0)
        left_layout.setSpacing(0)
        left_layout.addWidget(QLabel('只能单选'))
        self.column_names = QListWidget()
        self.column_names.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        left_layout.addWidget(self.column_names)
        ##################################################################
        # 右侧是内容
        right_frame = QFrame()
        main_layout.addWidget(right_frame)

        right_layout = QVBoxLayout(right_frame)

        # 第0行
        right_layout.addWidget(QLabel('按分隔符，后面填写字符；按字符数，后面填写数字'))

        # 第1行
        row1 = QFrame()
        right_layout.addWidget(row1)
        row1layout = QHBoxLayout(row1)

        row1layout.addWidget(QLabel('拆分方式'))

        cb1 = QComboBox()
        cb1.addItems(['按分隔符', '按字符数'])
        row1layout.addWidget(cb1)

        le1 = QLineEdit()
        row1layout.addWidget(le1)

        # 第2行
        row2 = QFrame()
        right_layout.addWidget(row2)
        row2layout = QHBoxLayout(row2)

        row2layout.addWidget(QLabel('拆分结果'))
        cb2 = QComboBox()
        cb2.addItems(['前N个列', '第N个列'])
        row2layout.addWidget(cb2)

        le2 = QLineEdit()
        row2layout.addWidget(le2)

        # 第3行
        self.label_msg = QLabel()
        self.label_msg.setStyleSheet("color:red;")
        right_layout.addWidget( self.label_msg)

        # 第4行

        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        btn_ok.clicked.connect(lambda :self.action_ok(cb1.currentText().strip(), le1.text(), cb2.currentText().strip(), le2.text().strip()))
        right_layout.addWidget(btn_ok)

    def action_ok(self, split_style, le1, get_style, le2):
        """
        split_style 表示按分隔符还是按字符数
        le1 表示具体的分隔符还是具体的字符数
        get_style 表示
        """

        logger.error('拆分列')
        names = [item.text() for item in self.column_names.selectedItems()]
        name = names[0]


        m = re.compile(r'^[1-9]\d*$')
        if '字符' in split_style and not m.match(le1):
            QMessageBox.critical(self, '错误', '拆分方式是按字符数，后面请填写正整数')
            return

        if not m.match(le2):
            QMessageBox.critical(self, '错误', '拆分结果后面请填写正整数')
            return

        le2 = int(le2)
        df = self.get_df()


        t1 = time.time()
        if '分隔符' in split_style:
            df['xxxyyyzzz'] = df[name].apply(lambda x: x.split(le1))
        if '字符' in split_style:
            df['xxxyyyzzz'] = df[name].apply(lambda x: self.split_string_by_length(x, le1))

        new_names = []
        if '前' in get_style:
            for i in range(le2):
                new_name = f'{name}-{i+1}'
                new_names.append(new_name)
                df[new_name] = df['xxxyyyzzz'].map(lambda x: self.get_from_limit(i, x, le2))
        if '第' in get_style:
            new_name = f'{name}-1'
            new_names.append(new_name)
            df[new_name] = df['xxxyyyzzz'].map(lambda x: self.get_from_limit(le2, x, le2))

        df.drop('xxxyyyzzz', axis=1, inplace=True)
        old_names = df.columns.tolist()
        # 下面的new_names一定要倒序
        old_names = Utils.resort_columns(old_names, sorted(new_names, reverse=True))
        df = df[old_names]
        self.set_df(df)
        t2 = time.time()
        error = '分隔符含有中文或中文字符\r\n' if Utils.has_Chinese_or_punctuation(le1) else ''
        msg = error+'拆分{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], 1, round(t2 - t1, 2))
        self.label_msg.setText(msg)

    def split_string_by_length(self, string, length):
        """
        按照数量，拆分字符串
        """
        pattern = f".{{1,{length}}}"
        result = re.findall(pattern, string)
        return result

    def get_from_limit(self, i:int, arr:List[str], limit:int):
        if limit<=len(arr):
            return arr[i]
        else:
            if i<len(arr):
                return arr[i]
            else:
                return ''
    def set_column_names(self, names):
        if names is not None:
            self.column_names.clear()
            self.column_names.addItems(names)
            self.column_names.setCurrentRow(0)

    def get_df(self):
        return self.parent.datasetTable.df

    def set_df(self, df):
        self.parent.datasetTable.set_df(df)


class PopupReplaceValue(QFrame):
    """
    替换值，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(300, 200)
        main_layout = QHBoxLayout(self)

        # 左侧是表头列表
        left_frame = QFrame()
        main_layout.addWidget(left_frame)
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(0,0,0,0)
        left_layout.setSpacing(0)
        left_layout.addWidget(QLabel('可以多选'))
        self.column_widget = QListWidget()
        self.column_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        left_layout.addWidget(self.column_widget)
        ##################################################################
        # 右侧是内容
        right_frame = QFrame()
        main_layout.addWidget(right_frame)

        right_layout = QVBoxLayout(right_frame)

        tabwidget = QTabWidget(self)
        right_layout.addWidget(tabwidget)

        ### 方式1  ###################################################3
        tab1 = QWidget()
        tab1_layout = QVBoxLayout(tab1)
        tabwidget.addTab(tab1, '方式1')

        ### 第0行

        row0 = QFrame()
        tab1_layout.addWidget(row0)
        row0layout = QHBoxLayout(row0)

        old_lbl = QLabel('原值')

        row0layout.addWidget(old_lbl)

        old_lineEdit = QLineEdit()
        old_lineEdit.setText(',')
        row0layout.addWidget(old_lineEdit)
        ####第1行

        row1 = QFrame()
        tab1_layout.addWidget(row1)
        row1layout = QHBoxLayout(row1)

        new_lbl = QLabel('新值')

        row1layout.addWidget(new_lbl)

        new_lineEdit = QLineEdit()
        new_lineEdit.setText(Cfg.seperator)
        row1layout.addWidget(new_lineEdit)

        #### 方式2 #########################################################
        tab2 = QWidget()
        tab2_layout = QVBoxLayout(tab2)
        tabwidget.addTab(tab2, '方式2')

        row00 = QFrame()
        tab2_layout.addWidget(row00)
        row00layout = QHBoxLayout(row00)

        row00layout.addWidget(QLabel('字符'))
        other_linedit = QLineEdit()
        row00layout.addWidget(other_linedit)

        row11 = QFrame()
        tab2_layout.addWidget(row11)
        row11layout = QHBoxLayout(row11)

        btg11 = QButtonGroup(self)
        rbt00 = QRadioButton('保留')
        rbt11 = QRadioButton('舍弃')
        rbt00.setChecked(True)
        btg11.addButton(rbt00, 1)
        btg11.addButton(rbt11, 2)
        row11layout.addWidget(rbt00)
        row11layout.addWidget(rbt11)
        ###第3行 ###############################################################
        row3 = QFrame()
        right_layout.addWidget(row3)
        row1layout = QHBoxLayout(row3)

        btg = QButtonGroup(self)
        rbt0 = QRadioButton('替换当前列')
        rbt1 = QRadioButton('添加新列')
        rbt0.setChecked(True)
        btg.addButton(rbt0, 1)
        btg.addButton(rbt1, 2)
        row1layout.addWidget(rbt0)
        row1layout.addWidget(rbt1)


        # 第4行
        self.label_msg = QLabel()
        self.label_msg.setStyleSheet("color:red;")
        right_layout.addWidget( self.label_msg)

        # 第5行
        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");

        btn_ok.clicked.connect(lambda :self.action_ok(tabwidget.currentIndex(), old_lineEdit.text(),new_lineEdit.text(), rbt1.isChecked(), other_linedit.text(), rbt00.isChecked()))
        right_layout.addWidget(btn_ok)



    def action_ok(self, current_tab_index, old_sep, new_sep, is_new, other_char, is_reserved):
        logger.info('替换值')
        names = [item.text() for item in self.column_widget.selectedItems()]
        if names:
            df = self.get_df()

            t1 = time.time()
            for col in names:
                new_col = col + '-new' if is_new else col
                if current_tab_index == 0:
                    df[new_col] = df[col].astype(str).str.replace(old_sep, new_sep).fillna(df[col])
                if current_tab_index == 1:
                    if is_reserved:
                        # 只保留该字符
                        df[new_col] = df[col].apply(lambda x: other_char if other_char in x else x)
                    else:
                        # 删除该字符
                        df[new_col] = df[col].astype(str).str.replace(other_char, '').fillna(df[col])
            self.set_df(df)
            t2 = time.time()

            error1 = '原值含有中文或中文字符\r\n' if Utils.has_Chinese_or_punctuation(old_sep) else ''
            error2 = error1 + '新值含有中文或中文字符\r\n' if Utils.has_Chinese_or_punctuation(new_sep) else ''
            msg = error2 + '替换{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(names), round(t2 - t1, 2))
            self.label_msg.setText(msg)



    def set_column_names(self, names):
        if names is not None:
            self.column_widget.clear()
            self.column_widget.addItems(names)
            self.column_widget.setCurrentRow(0)

    def get_df(self):
        return self.parent.datasetTable.df

    def set_df(self, df):
        self.parent.datasetTable.set_df(df)


class PopupCopyColumn(QFrame):
    """
    复制列，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(300, 200)
        main_layout = QHBoxLayout(self)

        # 左侧是表头列表，单选
        left_frame = QFrame()
        main_layout.addWidget(left_frame)
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(0,0,0,0)
        left_layout.setSpacing(0)
        left_layout.addWidget(QLabel('可以多选'))
        self.column_names = QListWidget()
        self.column_names.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        left_layout.addWidget(self.column_names)
        ##################################################################
        # 右侧是内容
        right_frame = QFrame()
        main_layout.addWidget(right_frame)

        right_layout = QVBoxLayout(right_frame)

        # 第1行
        right_layout.addWidget(QLabel('新的列名是在原列名后面带有-new'))
        # 第2行
        self.label_msg = QLabel()
        self.label_msg.setStyleSheet("color:red;")
        right_layout.addWidget( self.label_msg)
        # 第3行
        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        btn_ok.clicked.connect(self.action_ok)
        right_layout.addWidget(btn_ok)

    def action_ok(self):
        logger.info('复制列')
        t1 = time.time()
        names = [item.text() for item in self.column_names.selectedItems()]
        df = self.get_df()
        new_names = []
        for col in names:
            new_names.append(col+'-new')
            df[col+'-new'] = df[col]

        old_names = df.columns.tolist()
        old_names = Utils.resort_columns(old_names, new_names)
        df = df[old_names]

        self.set_df(df)
        t2 = time.time()

        msg = '复制{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(names), round(t2 - t1, 2))
        self.label_msg.setText(msg)
    def set_column_names(self, names):
        if names is not None:
            self.column_names.clear()
            self.column_names.addItems(names)
            self.column_names.setCurrentRow(0)

    def get_df(self):
        return self.parent.datasetTable.df

    def set_df(self, df):
        self.parent.datasetTable.set_df(df)


class PopupRenameColumn(QFrame):
    """
    复制列，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(300, 500)
        main_layout = QVBoxLayout(self)

        self.column_names_table = QTableWidget()
        main_layout.addWidget(self.column_names_table)

        self.label_msg = QLabel()
        self.label_msg.setStyleSheet("color:red;")
        main_layout.addWidget( self.label_msg)

        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        btn_ok.clicked.connect(self.action_ok)
        main_layout.addWidget(btn_ok)

    def action_ok(self):
        logger.info('重命名列')
        rowCount = self.column_names_table.rowCount()

        t1 = time.time()
        user_header = {}
        for i in range(rowCount):
            user_header[self.column_names_table.item(i, 0).text()] = self.column_names_table.item(i, 1).text()
        self.set_user_header(user_header)
        t2 = time.time()

        msg = '重命名列，耗时{0}秒'.format(round(t2 - t1, 2))
        self.label_msg.setText(msg)

    def set_user_header(self, user_header):
        self.parent.datasetTable.user_headers = user_header
        self.parent.datasetTable.flush_user_headers()

    def set_column_names(self, names):
        if names is not None:
            self.column_names_table.verticalHeader().hide()
            self.column_names_table.setColumnCount(2)
            self.column_names_table.setHorizontalHeaderLabels(['当前名称', '新的名称'])
            self.column_names_table.setRowCount(len(names))
            for i, row in enumerate(names):
                item = QTableWidgetItem(str(row))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled)
                self.column_names_table.setItem(i,0, item)

                item = QTableWidgetItem('')
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.column_names_table.setItem(i, 1, item)

    def get_df(self):
        return self.parent.datasetTable.df

    def set_df(self, df):
        self.parent.datasetTable.set_df(df)


class PopupCombineSynonym(QFrame):
    """
    同义词合并，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(300, 200)
        main_layout = QHBoxLayout(self)

        # 左侧是表头列表，单选
        left_frame = QFrame()
        main_layout.addWidget(left_frame)
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(0,0,0,0)
        left_layout.setSpacing(0)
        left_layout.addWidget(QLabel('可以多选'))
        self.column_names = QListWidget()
        self.column_names.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        left_layout.addWidget(self.column_names)
        ##################################################################
        # 右侧是内容
        right_frame = QFrame()
        main_layout.addWidget(right_frame)

        right_layout = QVBoxLayout(right_frame)


        ####第1行
        row1 = QFrame()
        right_layout.addWidget(row1)
        row1_layout = QHBoxLayout(row1)
        row1_layout.setContentsMargins(0,0,0,0)
        row1_layout.setSpacing(0)
        row1_layout.addWidget(QLabel('词典'))
        le1 = QLineEdit()
        le1.setReadOnly(True)
        row1_layout.addWidget(le1)
        btn1 = QPushButton('...')
        btn1.setFixedWidth(30)
        row1_layout.addWidget(btn1)
        btn1.clicked.connect(lambda :self.action_btn1(le1))


        ####第2行
        row2 = QFrame()
        right_layout.addWidget(row2)
        row2_layout = QHBoxLayout(row2)

        btg = QButtonGroup(self)

        rbt0 = QRadioButton('替换当前列')
        rbt1 = QRadioButton('添加新列')
        rbt0.setChecked(True)
        btg.addButton(rbt0, 1)
        btg.addButton(rbt1, 2)
        row2_layout.addWidget(rbt0)
        row2_layout.addWidget(rbt1)

        #### 第3行
        self.label_msg = QLabel()
        self.label_msg.setStyleSheet("color:red;")
        right_layout.addWidget( self.label_msg)

        #### 第4行
        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        btn_ok.clicked.connect(lambda :self.action_ok(le1.text(), rbt1.isChecked()))
        right_layout.addWidget(btn_ok)

        main_layout.setStretch(0,1)
        main_layout.setStretch(1, 3)
    def action_ok(self, dict_path, is_new:bool):
        logger.info('同义词合并')
        names = [item.text() for item in self.column_names.selectedItems()]
        if dict_path is None or dict_path.strip() == "":
            QMessageBox.critical(self, '错误', '请选择词典')
            return
        t1 = time.time()
        # key是被替换的词，value是新词【第1个】
        words_dict = {}
        with open(dict_path, encoding='utf-8') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines if not line.strip().startswith('#')]
            for line in lines:
                words = line.split(';')
                # 一行一个词，那么长度是1
                if len(words)>1:
                    tgt = words[0]
                    for org in words[1:]:
                        words_dict[org] = tgt

        df = self.get_df()
        # 遍历每一列，对每一列的每一个值，进行替换处理
        for col in names:
            col_new = col+'-new' if is_new else col
            df[col_new] = df[col].apply(lambda x:self.__replace(x, words_dict))
        self.set_df(df)
        t2 = time.time()

        msg = '合并{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(names), round(t2 - t1, 2))
        self.label_msg.setText(msg)
    def __replace(self, line, words_dict):
        keys = words_dict.keys()
        words = [str(words_dict[w]) if w in keys else w for w in line.split(Cfg.seperator)]
        return ';'.join(words)
    def action_btn1(self, input):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择词典",  # 标题
            Cfg.dicts,  # 起始目录
            "文件类型 (*.csv *.txt *.xls *.xlsx)"  # 选择类型过滤项，过滤内容在括号中
        )
        logger.error(filePath)
        input.setText(filePath)
    def set_column_names(self, names):
        if names is not None:
            self.column_names.clear()
            self.column_names.addItems(names)
            self.column_names.setCurrentRow(0)

    def get_df(self):
        return self.parent.datasetTable.df

    def set_df(self, df):
        self.parent.datasetTable.set_df(df)


class PopupStopWords(QFrame):
    """
    停用词，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(300, 200)
        main_layout = QHBoxLayout(self)

        # 左侧是表头列表，单选
        left_frame = QFrame()
        main_layout.addWidget(left_frame)
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(0,0,0,0)
        left_layout.setSpacing(0)
        left_layout.addWidget(QLabel('可以多选'))
        self.column_names = QListWidget()
        self.column_names.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        left_layout.addWidget(self.column_names)
        ##################################################################
        # 右侧是内容
        right_frame = QFrame()
        main_layout.addWidget(right_frame)

        right_layout = QVBoxLayout(right_frame)


        ####第1行
        row1 = QFrame()
        right_layout.addWidget(row1)
        row1_layout = QHBoxLayout(row1)
        row1_layout.setContentsMargins(0,0,0,0)
        row1_layout.setSpacing(0)
        row1_layout.addWidget(QLabel('词典'))
        le1 = QLineEdit()
        le1.setReadOnly(True)
        row1_layout.addWidget(le1)
        btn1 = QPushButton('...')
        btn1.setFixedWidth(30)
        row1_layout.addWidget(btn1)
        btn1.clicked.connect(lambda :self.action_btn1(le1))


        ####第2行
        row2 = QFrame()
        right_layout.addWidget(row2)
        row2_layout = QHBoxLayout(row2)

        btg = QButtonGroup(self)

        rbt0 = QRadioButton('替换当前列')
        rbt1 = QRadioButton('添加新列')
        rbt0.setChecked(True)
        btg.addButton(rbt0, 1)
        btg.addButton(rbt1, 2)
        row2_layout.addWidget(rbt0)
        row2_layout.addWidget(rbt1)

        #### 第3行
        self.label_msg = QLabel()
        self.label_msg.setStyleSheet("color:red;")
        right_layout.addWidget( self.label_msg)

        ####  第4行
        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        btn_ok.clicked.connect(lambda :self.action_ok(le1.text(), rbt1.isChecked()))
        right_layout.addWidget(btn_ok)

        main_layout.setStretch(0,1)
        main_layout.setStretch(1, 3)
    def action_ok(self, dict_path, is_new:bool):
        logger.info('停用词')
        names = [item.text() for item in self.column_names.selectedItems()]
        if dict_path is None or dict_path.strip() == "":
            QMessageBox.critical(self, '错误', '请选择词典')
            return
        t1 = time.time()
        # key是被替换的词，value是新词【第1个】
        words_set = set()
        with open(dict_path, encoding='utf-8') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines if not line.strip().startswith('#')]
            for line in lines:
                words_set.update(line.split(';'))

        df = self.get_df()
        # 遍历每一列，对每一列的每一个值，进行替换处理
        for col in names:
            col_new = col+'-new' if is_new else col
            df[col_new] = df[col].apply(lambda x:self.__replace(x, words_set))
        self.set_df(df)
        t2 = time.time()

        msg = '处理{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(names), round(t2 - t1, 2))
        self.label_msg.setText(msg)

    def __replace(self, line, words_set):
        words = [w for w in line.split(Cfg.seperator) if w not in words_set]
        return ';'.join(words)
    def action_btn1(self, input):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择词典",  # 标题
            Cfg.dicts,  # 起始目录
            "文件类型 (*.csv *.txt *.xls *.xlsx)"  # 选择类型过滤项，过滤内容在括号中
        )
        logger.error(filePath)
        input.setText(filePath)
    def set_column_names(self, names):
        if names is not None:
            self.column_names.clear()
            self.column_names.addItems(names)
            self.column_names.setCurrentRow(0)

    def get_df(self):
        return self.parent.datasetTable.df

    def set_df(self, df):
        self.parent.datasetTable.set_df(df)



class PopupCompareColumns(QFrame):
    """
    列对比，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(300, 200)
        main_layout = QHBoxLayout(self)

        # 左侧是表头列表，单选
        left_frame = QFrame()
        main_layout.addWidget(left_frame)
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(0,0,0,0)
        left_layout.setSpacing(0)
        left_layout.addWidget(QLabel('只能选择两列'))
        self.column_names = QListWidget()
        self.column_names.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        left_layout.addWidget(self.column_names)
        ##################################################################
        # 右侧是内容
        right_frame = QFrame()
        main_layout.addWidget(right_frame)

        right_layout = QVBoxLayout(right_frame)


        ####第1行
        btn_reset = QPushButton('恢复颜色')
        btn_reset.clicked.connect(self.action_reset)
        right_layout.addWidget(btn_reset)

        ####第2行
        right_layout.addWidget(QLabel('只能对两个列进行对比，不同值使用颜色标注'))

        #### 第3行
        self.label_msg = QLabel()
        self.label_msg.setStyleSheet("color:red;")
        right_layout.addWidget( self.label_msg)


        ####  第4行
        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        btn_ok.clicked.connect(self.action_ok)
        right_layout.addWidget(btn_ok)

    def action_reset(self):
        logger.info('列对比')
        indexes = [item.row() for item in self.column_names.selectedIndexes()]

        t1 = time.time()
        df = self.get_df()
        table = self.get_table()
        for i in range(df.shape[0]):
            for col in indexes:
                table.item(i, col).setBackground(QBrush(QColor(255,255,255)))

        t2 = time.time()
        msg = '清除{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(indexes), round(t2 - t1, 2))
        self.label_msg.setText(msg)
    def action_ok(self):
        logger.info('列对比')
        indexes = [item.row() for item in self.column_names.selectedIndexes()]
        if len(indexes) !=2:
            QMessageBox.critical(self, '错误', '只能选择2列')
            return

        t1 = time.time()
        df = self.get_df()
        table = self.get_table()
        for i in range(df.shape[0]):
            if df.iloc[i, indexes[0]] != df.iloc[i, indexes[1]]:
                table.item(i, indexes[1]).setBackground(QBrush(QColor(192,192,192)))
        t2 = time.time()
        msg = '对比{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(indexes), round(t2 - t1, 2))
        self.label_msg.setText(msg)

    def __replace(self, line, words_set):
        words = [w for w in line.split(Cfg.seperator) if w not in words_set]
        return ';'.join(words)
    def action_btn1(self, input):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择词典",  # 标题
            Cfg.dicts,  # 起始目录
            "文件类型 (*.csv *.txt *.xls *.xlsx)"  # 选择类型过滤项，过滤内容在括号中
        )
        logger.error(filePath)
        input.setText(filePath)
    def set_column_names(self, names):
        if names is not None:
            self.column_names.clear()
            self.column_names.addItems(names)
            self.column_names.setCurrentRow(0)

    def get_df(self):
        return self.parent.datasetTable.df
    def get_table(self):
        return self.parent.datasetTable
    def set_df(self, df):
        self.parent.datasetTable.set_df(df)


class PopupModifyValue(QFrame):
    """
    修改值，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(300, 200)
        main_layout = QVBoxLayout(self)

        ####第1行
        main_layout.addWidget(QLabel('处于修改状态时，拖拽或者选择操作会出现错误'))
        main_layout.addWidget(QLabel('修改完毕，请禁用修改'))

        #### 第2行
        self.label_msg = QLabel()
        self.label_msg.setStyleSheet("color:red;")
        main_layout.addWidget( self.label_msg)

        ####  第3行
        ff = QFrame()
        ff_layout = QHBoxLayout(ff)
        main_layout.addWidget(ff)

        btn_reset = QPushButton('保存修改')
        btn_reset.clicked.connect(self.action_reset)
        ff_layout.addWidget(btn_reset)

        btn_ok = QPushButton('允许修改')
        btn_ok.clicked.connect(self.action_ok)
        ff_layout.addWidget(btn_ok)


    def action_reset(self):
        logger.info('列对比')
        df = self.get_df()
        table = self.get_table()
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                table.item(i, j).setFlags(Qt.ItemFlag.ItemIsEnabled)
                if df.iloc[i, j]!=table.item(i,j).text():
                    df.iloc[i, j] = table.item(i,j).text()
        self.set_df(df)


        msg = '禁止修改'
        self.label_msg.setText(msg)
    def action_ok(self):
        logger.info('列对比')

        table = self.get_table()

        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                table.item(i, j).setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable)

        msg = '允许修改'
        self.label_msg.setText(msg)


    def get_df(self):
        return self.parent.datasetTable.df
    def get_table(self):
        return self.parent.datasetTable
    def set_df(self, df):
        self.parent.datasetTable.set_df(df)

class PopupOneclick(QFrame):
    """
    一键清洗，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(300, 200)
        main_layout = QVBoxLayout(self)

        main_layout.addWidget(QLabel('一键清洗'))

        self.label_msg = QLabel()
        self.label_msg.setStyleSheet("color:red;")
        main_layout.addWidget( self.label_msg)

        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        btn_ok.clicked.connect(self.action_ok)
        main_layout.addWidget(btn_ok)

    def action_ok(self):
        logger.error('一键清洗')

        # msg = '清除{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(indexes), round(t2 - t1, 2))
        # self.label_msg.setText(msg)

class PopupHistory(QFrame):
    """
    操作历史，对话框
    """

    def __init__(self, parent=None, title=''):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(title)

        self.resize(300, 500)
        main_layout = QVBoxLayout(self)

        listWidget = QListWidget()
        with open('./clean.log', encoding='utf-8') as reader:
            for line in reader.readlines():
                tt = line[:19]
                msg = line.split(' - ')[1].strip()
                listWidget.addItem(tt+'  '+msg)
        main_layout.addWidget(listWidget)

        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(28, 177, 245);");
        btn_ok.clicked.connect(self.action_ok)
        main_layout.addWidget(btn_ok)

    def action_ok(self):
        logger.info('操作历史')
        self.close()
class DatasetTable(QTableWidget):
    signal_statusbar = Signal(str)

    def __init__(self):
        super().__init__()
        self.df:DataFrame = None

        self.user_headers = None
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_body_context_menu)
        self.setSortingEnabled(True)
        self.horizontalHeader().setSectionsMovable(True)


    def set_df(self, df: DataFrame):
        self.df = df
        self.__fillData()

    def flush_user_headers(self):
        if self.user_headers:
            headers = []

            for k in self.df.columns:
                v = self.user_headers[k]
                # 如果v是空，取k
                v = v if v.strip() != '' else k
                headers.append(v)

            self.setHorizontalHeaderLabels(headers)
    def __fillData(self):
        """
        填充数据，并显示统计信息
        """
        self.df.reset_index(drop=True, inplace=True)
        self.setColumnCount(self.df.shape[1])
        self.setRowCount(self.df.shape[0])
        self.setHorizontalHeaderLabels(self.df.columns)
        for i, row in self.df.iterrows():
            for j, _ in enumerate(row):
                item = QTableWidgetItem(str(self.df.iloc[i, j]))
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.setItem(i, j, item)

    def show_body_context_menu(self):
        """
        显示数据的右键菜单
        """
        body_menu = QMenu(self)

        self.act_column_chooseall = QAction('选中列')
        self.act_column_chooseall.triggered.connect(self.action_column_chooseall)
        body_menu.addAction(self.act_column_chooseall)

        self.act_row_delete = QAction('删除行')
        self.act_row_delete.triggered.connect(self.action_row_delete)
        body_menu.addAction(self.act_row_delete)

        self.act_column_delete = QAction('删除列')
        self.act_column_delete.triggered.connect(self.action_column_delete)
        body_menu.addAction(self.act_column_delete)

        body_menu.move(QtGui.QCursor().pos())
        body_menu.show()

    def action_column_chooseall(self):
        cols = [index.column() for index in self.selectedIndexes()]
        self.selectColumn(cols[0])

    def action_row_delete(self):
        rows = sorted([index.row() for index in self.selectedIndexes()], reverse=True)
        self.df.drop(rows, inplace=True)
        self.__fillData()
        self.signal_statusbar.emit('删除行 ' + ' , '.join([str(i) for i in rows]))

    def action_column_delete(self):
        cols = sorted([index.column() for index in self.selectedIndexes()], reverse=True)
        col_names = [self.df.columns[i] for i in cols]
        col_names = list(set(col_names))
        self.df.drop(col_names, axis=1, inplace=True)
        self.__fillData()
        self.signal_statusbar.emit('删除列 ' + ' , '.join(col_names))

    def update_table_cell(self):

        # items 是一个列表，每个元素是QTableWidgetItem
        items = self.selectedItems()
        if len(items) == 0:
            return
        item = items[0]
        self.df.iloc[item.row(), item.column()] = item.text()
        self.signal_statusbar.emit('更新数据 ' + item.text())

class DatasetFrame(QWidget):
    signal_statusbar = Signal(str)

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.datasetTable = DatasetTable()
        self.datasetTable.signal_statusbar.connect(self.show_statusbar)

        main_layout.addWidget(self.build_toolbar())
        main_layout.addWidget(self.datasetTable)

    def set_main(self, main):
        self.main = main

    def build_toolbar(self):
        top_toolbar = QToolBar(self)

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '元数据', self.action_metadata))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '重命名', self.action_rename_column))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '复制列', self.action_copy_column))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '拆分列', self.action_split_column))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '替换值', self.action_replace_column))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '合并词', self.action_combine_synonym))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '停用词', self.action_stop_words))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '列对比', self.action_compare_columns))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '修改值', self.action_modify_value))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '行去重', self.action_distinct))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '一键清洗', self.action_oneclick))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/riqi.png', '操作历史', self.action_history))

        top_toolbar.addWidget(QLabel('     '))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/biaodaochu.png', '保存', self.action_model_save))

        top_toolbar.addWidget(self._gen_toolbutton('./icons/shujufenxi.png', '下载', self.action_download))

        return top_toolbar

    def _gen_toolbutton(self, icon, text, action):
        """
        生成工具按钮
        """
        btn1 = QToolButton(self)
        btn1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        btn1.setIcon(QIcon(icon))
        btn1.setText(text)
        btn1.clicked.connect(action)
        return btn1

    def action_metadata(self):
        logger.info('元数据')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return
        self.popupMetadata = PopupMetadata(self, '元数据')
        self.popupMetadata.show()

    def action_model_save(self):
        logger.info('保存模型')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据，无法保存')
            return

        filePath, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "保存模型文件",  # 标题
            Cfg.models,  # 起始目录
            "模型文件 (*.pkl)"  # 选择类型过滤项，过滤内容在括号中
        )
        if filePath:
            self.get_df().to_pickle(filePath, compression="gzip")
            self.signal_statusbar.emit('成功保存模型')

    def action_download(self):
        logger.info('下载数据')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据，无法下载')
            return

        filePath, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "下载数据文件",  # 标题
            os.path.join(os.path.expanduser("~"), 'Desktop'),  # 起始目录
            "Excel (*.xlsx)"  # 选择类型过滤项，过滤内容在括号中
        )
        if filePath:
            self.get_df().to_excel(filePath, index=False)
            self.signal_statusbar.emit('成功下载数据')

    def action_rename_column(self):
        logger.info('重命名列')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return
        self.popupRenameColumn = PopupRenameColumn(self, '重命名')
        self.popupRenameColumn.set_column_names(self.get_df().columns)
        self.popupRenameColumn.show()

    def action_copy_column(self):
        logger.info('复制列')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return
        self.popupCopyColumn = PopupCopyColumn(self, '复制列')
        self.popupCopyColumn.set_column_names(self.get_df().columns)
        self.popupCopyColumn.show()

    def action_split_column(self):
        logger.info('拆分列')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return
        self.popupSplitColumn = PopupSplitColumn(self, '拆分列')
        self.popupSplitColumn.set_column_names(self.get_df().columns)
        self.popupSplitColumn.show()
    def action_replace_column(self):
        logger.info('替换值')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return
        self.popupReplaceValue = PopupReplaceValue(self, '替换值')
        self.popupReplaceValue.set_column_names(self.get_df().columns)
        self.popupReplaceValue.show()
    def action_combine_synonym(self):
        logger.info('合并同义词')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return
        self.popupCombineSynonym = PopupCombineSynonym(self, '合并词')
        self.popupCombineSynonym.set_column_names(self.get_df().columns)
        self.popupCombineSynonym.show()

    def action_stop_words(self):
        logger.info('停用词')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return
        self.popupStopWords = PopupStopWords(self, '停用词')
        self.popupStopWords.set_column_names(self.get_df().columns)
        self.popupStopWords.show()

    def action_compare_columns(self):
        logger.info('列对比')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return
        self.popupCompareColumns = PopupCompareColumns(self, '列对比')
        self.popupCompareColumns.set_column_names(self.get_df().columns)
        self.popupCompareColumns.show()

    def action_modify_value(self):
        logger.info('修改值')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return

        self.popupModifyValue = PopupModifyValue(self, '修改值')
        self.popupModifyValue.show()
    def action_distinct(self):
        logger.info('行去重')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return
        self.popupRowDistinct = PopupRowDistinct(self, '行去重')
        self.popupRowDistinct.set_column_names(self.get_df().columns)
        self.popupRowDistinct.show()
    def action_oneclick(self):
        logger.info('一键清洗')
        if self.get_df() is None:
            QMessageBox.critical(self, '错误', '下面表格没有数据')
            return
        self.popupOneclick = PopupOneclick(self, '一键清洗')
        self.popupOneclick.show()

    def action_history(self):
        logger.info('操作历史')
        self.popupHistory = PopupHistory(self, '操作历史')
        self.popupHistory.show()
    def set_df(self, df):
        self.datasetTable.set_df(df)

    def get_df(self):
        return self.datasetTable.df

    def show_statusbar(self, msg):
        self.signal_statusbar.emit(msg)


class DataConfigWidget(QWidget):
    def __init__(self):
        super(DataConfigWidget, self).__init__()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)

        main_splitter = QSplitter(Qt.Horizontal, self)
        main_layout.addWidget(main_splitter)
        left_frame = QFrame(main_splitter)
        right_showtext = QTextEdit(main_splitter)
        main_splitter.addWidget(left_frame)
        main_splitter.addWidget(right_showtext)
        main_splitter.setSizes([50, 50])

        # 左侧的配置项
        left_layout = QVBoxLayout()
        left_frame.setLayout(left_layout)

        stop_linedit = self.__add_row_file(left_layout, '停用词', right_showtext)
        tongyi_linedit = self.__add_row_file(left_layout, '同义词', right_showtext)


        # 弹簧条
        left_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def __add_row_input(self, left_layout, text):

        row1 = DataConfigWidget.__build_config_row(left_layout)
        # 按钮

        label1 = QPushButton()
        label1.setFixedWidth(80)
        label1.setText(text)
        row1.addWidget(label1)
        # 文本框
        lineedit1 = QLineEdit()
        row1.addWidget(lineedit1)

        return lineedit1
    def __add_row_file(self, left_layout, text, right_showtext=None):

        row1 = DataConfigWidget.__build_config_row(left_layout)
        # 按钮

        label1 = QPushButton()
        label1.setFixedWidth(80)
        label1.setText(text)
        if right_showtext is not None:
            label1.clicked.connect(lambda: DataConfigWidget.__show_text(self, lineedit1.text(), right_showtext))
        row1.addWidget(label1)
        # 文本框
        lineedit1 = QLineEdit()
        row1.addWidget(lineedit1)
        lineedit1.setReadOnly(True)
        # 按钮
        btn1 = QPushButton('...')
        btn1.setFixedWidth(30)
        btn1.clicked.connect(lambda: DataConfigWidget.__choose_file_from_dialog(self, Cfg.dicts, lineedit1))
        row1.addWidget(btn1)

        return lineedit1
    @staticmethod
    def __build_config_row(parent):
        container = QWidget()
        parent.addWidget(container)

        lo = QHBoxLayout()
        lo.setContentsMargins(0, 0, 0, 0)
        lo.setSpacing(0)
        container.setLayout(lo)

        return lo

    @staticmethod
    def __show_text(parent, path, target):
        if not path:
            QMessageBox.critical(parent, '错误', '请指定路径')
            return

        with open(path, encoding='utf-8') as f:
            for line in f.readlines():
                target.append(line.strip())

    @staticmethod
    def __choose_file_from_dialog(parent, pdir, input):
        filePath, _ = QFileDialog.getOpenFileName(
            parent,  # 父窗口对象
            "选择文件",  # 标题
            pdir,  # 起始目录
            "文件类型 (*.csv *.txt *.xls *.xlsx)"  # 选择类型过滤项，过滤内容在括号中
        )
        logger.error(filePath)
        input.clear()
        input.setText(filePath)


class CleanWidget(QMainWindow):
    """
    专门用于清洗的主要组件
    """

    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 10, 0, 0)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.resize(1000, 700)

        # 中间的拖动分割器
        main_splitter = QSplitter(self)
        main_layout.addWidget(main_splitter)
        left_frame = QFrame(main_splitter)
        left_frame.setMaximumWidth(200)
        main_splitter.addWidget(left_frame)
        center_frame = QFrame(main_splitter)
        main_splitter.addWidget(center_frame)

        # 左侧窗口
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        left_frame.setLayout(left_layout)
        left_splitter = QSplitter(self)
        left_splitter.setOrientation(Qt.Vertical)
        # 数据文件
        datafile_widget = DataFileWidget(left_splitter)
        datafile_widget.setMain(self)
        datafile_widget.signal_dataset.connect(self.show_df)
        datafile_widget.signal_statusbar.connect(self.showStatusbarMessage)
        # 数据模型
        datamodel_widget = DataModelWidget(left_splitter)
        datamodel_widget.setMain(self)
        datamodel_widget.signal_dataset.connect(self.show_df)
        datamodel_widget.signal_statusbar.connect(self.showStatusbarMessage)

        left_splitter.addWidget(datafile_widget)
        left_splitter.addWidget(datamodel_widget)
        left_layout.addWidget(left_splitter)

        # 中间主窗口
        center_layout = QVBoxLayout()
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(0)
        center_frame.setLayout(center_layout)

        # 中间的tabwidget
        center_widget = QTabWidget(self)
        center_layout.addWidget(center_widget)
        self.tab_dataset = DatasetFrame()
        self.tab_dataset.set_main(self)
        self.tab_dataset.signal_statusbar.connect(self.showStatusbarMessage)
        center_widget.addTab(self.tab_dataset, '数据')
        self.tab_config = DataConfigWidget()
        center_widget.addTab(self.tab_config, '配置')
        # 默认选中的tab
        center_widget.setCurrentIndex(0)

    def show_df(self, df: DataFrame):
        self.df = df
        self.tab_dataset.set_df(df)
        self.showStatusbarMessage('解析 {0} 条记录'.format(df.shape[0]))

    def showStatusbarMessage(self, val):
        self.statusBar().setStyleSheet("color: red;font-weight: bold;font-size: 16px;")
        self.statusBar().showMessage(val, 10000)

        # 绑定多线程
        self.work = Worker()
        self.work.valve.connect(self.showStatusbarMessage)
        # 应该有个按钮，操控doWork
        # self.start_btn.clicked.connect(self.doWork)

    def doWork(self):

        if self.work.a == 9999:
            self.work.a = 0
        if self.work.isFinished():
            self.work.start()
        # 使用嵌套 if最省事，但不容易看懂
        if self.start_btn.text() == "开始":
            self.start_btn.setText("停止")
            self.work.pause = False
            self.work.a = 0
            self.work.start()

            self.start_parse()
            return
        elif self.start_btn.text() == "停止":
            self.start_btn.setText("开始")
            self.work.pause = True
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)

    cleanWidget = CleanWidget()
    cleanWidget.show()

    app.exec()
