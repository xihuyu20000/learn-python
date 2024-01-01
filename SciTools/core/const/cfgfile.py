import collections
import os
from typing import Dict

from PySide2.QtCore import QSettings

from core.log import logger

abs_path = os.path.expanduser("~")

CfgItem = collections.namedtuple('CfgItem', ['label', 'key', 'value'])


class CfgHandler:
    def __init__(self):
        # 配置文件路径
        self.cfg_save_path = os.path.join(abs_path, ".clean-cfg.db")
        # 配置字典
        self.load_dict: Dict[str, str] = collections.defaultdict(str)

        # cfg.db文件存在，则读取内容
        if os.path.exists(self.cfg_save_path):
            setting = QSettings(self.cfg_save_path, QSettings.IniFormat)
            for key in setting.allKeys():
                if len(setting.value(key)) > 0:
                    self.load_dict[key] = setting.value(key)

        # 工作空间文件夹
        self.workspace = CfgItem(label='workspace', key='workspace', value=os.path.abspath(os.curdir))
        self.__init_value(self.workspace)

        # 数据文件文件夹
        self.datafiles: CfgItem = CfgItem(label='datafiles', key='datafiles',
                                          value=os.path.join(self.workspace.value, "datafiles"))
        self.__init_value(self.datafiles)

        # 词典文件夹
        self.dicts = CfgItem(label='dicts', key='dicts', value=os.path.join(self.workspace.value, "dicts"))
        self.__init_value(self.dicts)

        ####################################################################################################

        # 停用词表
        self.stop_words = CfgItem(label="停用词表", key='stop_words',
                                  value=os.path.join(self.dicts.value, "停用词表.txt"))
        self.__init_value(self.stop_words)

        # 合并词表
        self.combine_words = CfgItem(label="合并词表", key='combine_words',
                                     value=os.path.join(self.dicts.value, "合并词表.txt"))
        self.__init_value(self.combine_words)

        # 受控词表
        self.controlled_words = CfgItem(label="受控词表", key='controlled_words',
                                        value=os.path.join(self.dicts.value, "受控词表.txt"))
        self.__init_value(self.controlled_words)

        # 分组词表
        self.group_words = CfgItem(label="分组词表", key='group_words',
                                   value=os.path.join(self.dicts.value, "分组词表.txt"))
        self.__init_value(self.group_words)

        ####################################################################################################

        # 表头颜色
        self.table_header_bgcolor = CfgItem(label='table_header_bgcolor', key='table_header_bgcolor', value='lightblue')
        self.__init_value(self.table_header_bgcolor)

        # 文件默认的分隔符
        self.seperator = CfgItem(label='seperator', key='seperator', value=';')
        self.__init_value(self.seperator)

        # 读取csv文件时，的分隔符
        self.csv_seperator = CfgItem(label='csv_seperator', key='csv_seperator', value=',')
        self.__init_value(self.csv_seperator)

        # 程序运行的计时器，精确度
        self.precision_point = CfgItem(label='precision_point', key='precision_point', value='4')
        self.__init_value(self.precision_point)

        # 打开时，弹出窗口，可以关闭，当天不显示
        self.popup_startup = CfgItem(label='popup_startup', key='popup_startup', value='')
        self.__init_value(self.popup_startup)

        logger.debug('配置信息 {}', self.load_dict)

    def get(self, key):
        return self.load_dict[key]

    def set(self, key, value):
        logger.debug('保存配置信息{}={}', key, value)
        self.load_dict[key] = value

        setting = QSettings(self.cfg_save_path, QSettings.IniFormat)
        setting.setValue(key, value)

    def __init_value(self, item: CfgItem):
        if len(self.load_dict[item.key]) > 0:
            setattr(self, item.key, item._replace(value=self.load_dict[item.key]))
        else:
            setattr(self, item.key, item)


Cfg = CfgHandler()
