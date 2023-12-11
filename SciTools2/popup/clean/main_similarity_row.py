import re
import time
from typing import List, Set, Dict

import pandas as pd
from PySide2.QtWidgets import QDialog
from log import logger

from helper import Utils, ssignal
from popup.clean.uipy import ui_similarity_row
from toolkit import PandasTableModel


class PopupSimilarityRows(QDialog, ui_similarity_row.Ui_Form):
    GROUP_LABEL_TEXT = '组号'
    ORIGINAL_LABEL_TEXT = '原行号'
    def __init__(self, parent):
        super(PopupSimilarityRows, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.column_names.addItems(self.get_clean_columns())
        self.column_names.setCurrentRow(0)

        self.group_table_model = PandasTableModel()
        self.group_table.setModel(self.group_table_model)
        self.slider_horizon.valueChanged.connect(lambda :self.value_changed(self.vaLable, self.slider_horizon.value()))
        self.btn_ok.clicked.connect(lambda: self.action_ok(self.slider_horizon.value()))

        self.btn_combine_current_group.clicked.connect(self.action_combine_current_group)
        self.btn_save_current_group.clicked.connect(self.action_save)

    def action_ok(self, limited):
        logger.info('相似度')
        column_names = self.column_names.selectedItems()
        if len(column_names) == 0:
            return
        column_names = [item.text() for item in column_names]
        # 保存阈值
        self.limited = limited
        # 在分组表中，删除的分组号
        self.deleted_group_nos = []
        t1 = time.time()
        #############################################################################3
        # 对df的每一行的选中的列，拆分成set，放入到words_list中。这里不需要进行jieba分词，但是需要数据清洗

        df = self.get_df()
        # words_list的长度与df的行数相同
        words_list: List[Set[str]] = []
        # 遍历ds所有行
        for i in range(df.shape[0]):
            # 取一行多列
            dd = df.loc[i, column_names].tolist()
            # TODO 需要对cut使用停用词表
            stop_words = [';']
            dd = [[item.strip() for item in re.split(r'\s+|;', line) if item.strip() not in stop_words] for line in dd]
            # list拉平
            dd = sum(dd, [])
            words_list.append(set(dd))
        ###############################################################################
        # 计算相似度
        # pairs是list，每一项是list，有3项，分别是行号、组号、相似度
        pairs_dict = []

        self.__calc_similarity(df, words_list, pairs_dict)

        ######################################################################################
        # 封装成DataFrame
        group_dataset = []
        for item in pairs_dict:
            # 分别是行号、组名、相似度
            row0 = item.copy()
            # 取出原始列，插入到集合中
            row0.extend(df.loc[item[0], column_names].tolist())
            # print('row0', row0)
            group_dataset.append(row0)

        header_names = [PopupSimilarityRows.ORIGINAL_LABEL_TEXT, PopupSimilarityRows.GROUP_LABEL_TEXT,
                        '相似度(%)'] + column_names

        group_df = pd.DataFrame(columns=header_names, data=group_dataset)

        #########################################################################################
        # 对原始数据集，增加分组列，方便后续更新
        self.df_bak = self.get_df()
        # key是行号，vale是组号
        index_group_dict = {item[0]: item[1] for item in group_dataset}
        self.df_bak['group'] = [index_group_dict[i] if i in index_group_dict else '' for i in
                                range(self.df_bak.shape[0])]

        #########################################################################################
        # 展示表格
        self.group_table_model.pub_set_dataset(group_df)

        t2 = time.time()
        msg = '分析{0}条记录，{1}个列，耗时{2}秒'.format(df.shape[0], len(column_names), round(t2 - t1, 2))
        ssignal.info.send(msg)

    def __calc_similarity(self, df, words_list, pairs_dict):
        group_no = 0
        for source_i, source_words in enumerate(words_list):
            # 第1个不取，形成三角矩阵，不包括对角线
            used_indexes = [p[0] for p in pairs_dict]
            # 注意下面的判断逻辑：
            # 1、index>i表示只处理后面的句子
            # 2、index not in used_indexes表示不在 前面相似选择出来的范围内
            # 符合以上一个条件，返回本身；否则，返回空串。这样的目的，是为了保持句子的原始顺序号不变化
            targets: List[Set[str]] = []
            # 以下的代码不能合并到一起，必须保持这样
            for index, words in enumerate(words_list):
                if index > source_i:
                    if index not in used_indexes:
                        targets.append(words)
                    else:
                        targets.append(set())
                else:
                    targets.append(set())
            # print('比较完成的index',used_indexes)
            # print('待比较的句子', sentences)

            # 计算出相似度
            threshold = int(self.limited) / 100
            assert threshold <= 1 and threshold > 0
            result: Dict[int, float] = Utils.calculate_jaccard_similarity(threshold, source_words, targets)
            # print(threshold, result, source_words, targets)
            # print('比较结果', result)
            if result:
                # 组号+1
                group_no += 1
                # 把当前的句子放进去，第3个表示当前句子，使用None表示不跟自己比较相似度
                pairs_dict.append([source_i, group_no, '100'])
                for target_index, simil in result.items():
                    pairs_dict.append([target_index, group_no, '{:.1f}'.format(simil * 100)])
        # logger.info(pairs_dict)

    def action_combine_current_group(self):
        logger.info('合并该分组')

        row_nos = self.group_table.selectedIndexes()
        if len(row_nos) == 0:
            ssignal.error.send('请选择一行')
            return

        row_nos = [index.row() for index in self.group_table.selectedIndexes()]

        df = self.group_table_model.pub_get_dataset()

        # 更新当前分组表
        group_nos = df.loc[row_nos, PopupSimilarityRows.GROUP_LABEL_TEXT].tolist()
        # 添加到删除表中
        self.deleted_group_nos.extend(group_nos)
        boolean_df = df[PopupSimilarityRows.GROUP_LABEL_TEXT].isin(group_nos)
        df.drop(df[boolean_df].index, inplace=True)
        self.group_table_model.pub_set_dataset(df)

    def action_save(self):
        logger.info('保存修改')
        """
        根据self.deleted_group_nos的值，更新原始表
        """
        no_changed = self.df_bak[~self.df_bak['group'].isin(self.deleted_group_nos)]
        will_changed = self.df_bak[self.df_bak['group'].isin(self.deleted_group_nos)].copy()
        will_changed.drop_duplicates(subset=['group'], keep='first', inplace=True)
        changed = pd.concat([no_changed, will_changed], axis=0, ignore_index=True)
        changed.drop(columns=['group'], inplace=True)

        # print(no_changed)
        # print(will_changed)
        # print(changed)

        self.set_df(changed)


    def value_changed(self, lbl, val):
        lbl.setText(str(val))

    def get_clean_columns(self):
        return self.parent.master_get_clean_columns()

    def get_df(self):
        return self.parent.master_get_clean_df()

    def set_df(self, df):
        self.parent.master_set_clean_df(df)