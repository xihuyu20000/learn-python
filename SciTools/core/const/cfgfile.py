import collections
import json
import os
import sys
from typing import Dict

from core.log import logger

abs_path = (
    os.path.expanduser("~")
    if getattr(sys, "frozen", False)
    else os.path.abspath(os.curdir)
)

CfgItem = collections.namedtuple('CfgItem', ['label', 'key', 'value'])


class CfgHandler:
    def __init__(self):
        self.cfg_save_path = os.path.join(abs_path, "clean.db")
        self.load_dict: Dict[str, str] = collections.defaultdict(str)
        try:
            with open(self.cfg_save_path, encoding="utf-8") as load_f:
                dataform = str(load_f.read()).strip("'<>() ").replace('\'', '\"')
                self.load_dict.update(json.loads(dataform))
                logger.debug(self.load_dict)
        except Exception as e:
            logger.exception(e)

        # 工作空间文件夹
        self.workspace = CfgItem(label='workspace', key='workspace', value=os.path.abspath(os.curdir))

        # 数据文件文件夹
        self.datafiles = CfgItem(label='datafiles', key='datafiles',
                                 value=os.path.join(self.workspace.value, "datafiles"))

        # 词典文件夹
        self.dicts = CfgItem(label='dicts', key='dicts', value=os.path.join(self.workspace.value, "dicts"))
        ####################################################################################################
        # 停用词表
        self.stop_words = CfgItem(label="停用词表", key='stopwords',
                                  value=os.path.join(self.dicts.value, "停用词表.txt"))
        self.stop_words = self.stop_words._replace(value=self.load_dict[self.stop_words.key])
        # 合并词表
        self.combine_words = CfgItem(label="合并词表", key='combinewords',
                                     value=os.path.join(self.dicts.value, "合并词表.txt"))
        self.combine_words = self.combine_words._replace(value=self.load_dict[self.combine_words.key])
        # 受控词表
        self.controlled_words = CfgItem(label="受控词表", key='controlledwords',
                                        value=os.path.join(self.dicts.value, "受控词表.txt"))
        self.controlled_words = self.controlled_words._replace(value=self.load_dict[self.controlled_words.key])
        # 分组词表
        self.group_words = CfgItem(label="分组词表", key='stopwords',
                                   value=os.path.join(self.dicts.value, "分组词表.txt"))
        self.group_words = self.group_words._replace(value=self.load_dict[self.group_words.key])
        ####################################################################################################
        # 表头颜色
        self.table_header_bgcolor = CfgItem(label='table_header_bgcolor', key='table_header_bgcolor', value='lightblue')
        self.table_header_bgcolor = self.table_header_bgcolor._replace(
            value=self.load_dict[self.table_header_bgcolor.key])
        # 全局字体大小
        self.global_font_size = CfgItem(label='global_font_size', key='global_font_size', value='12')
        self.global_font_size = self.global_font_size._replace(value=self.load_dict[self.global_font_size.key])
        # 文件默认的分隔符
        self.seperator = CfgItem(label='seperator', key='seperator', value=';')
        self.seperator = self.seperator._replace(value=self.load_dict[self.seperator.key])
        # 读取csv文件时，的分隔符
        self.csv_seperator = CfgItem(label='csv_seperator', key='csv_seperator', value=',')
        self.csv_seperator = self.csv_seperator._replace(value=self.load_dict[self.csv_seperator.key])
        # 程序运行的计时器，精确度
        self.precision_point = CfgItem(label='precision_point', key='precision_point', value='4')
        self.precision_point = self.precision_point._replace(value=self.load_dict[self.precision_point.key])
        # 打开时，弹出窗口，可以关闭，当天不显示
        self.popup_startup = CfgItem(label='popup_startup', key='popup_startup', value='')
        self.popup_startup = self.popup_startup._replace(value=self.load_dict[self.popup_startup.key])

        logger.debug("初始化执行结束 {}", self.cfg_save_path)

    def get(self, key):
        return self.load_dict[key]

    def set(self, key, value):
        self.load_dict[key] = value

        try:
            with open(self.cfg_save_path, 'w', encoding="utf-8") as write_f:
                json.dump(self.load_dict, write_f, indent=4, ensure_ascii=False)
        except Exception as e:
            logger.exception(e)


cfg = CfgHandler()
