"""
这是工具模块，这里的代码，一定不能依赖其他项目模块
"""
import collections
import itertools
import os
import re
import secrets
import sys
import time
import uuid
from typing import Dict, Union, Set
from typing import Tuple, List

import arrow
import jieba
import numpy as np
import pandas as pd
import requests
import wmi
from lxml import etree
from scipy.stats import zscore
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from zhon.hanzi import punctuation

from core.const import Config
from core.log import logger


def is_running_as_exe():
    return getattr(sys, 'frozen', False)

class DictReader:
    @staticmethod
    def combine_words_file(abs_paths: Union[str, List[str]]) -> Dict[str, str]:
        """
        合并字典的返回值是dict，key是需要替换的词，value是保留的词
        abs_paths: 字典的绝对路径
        """
        if isinstance(abs_paths, str):
            abs_paths = [abs_paths]

        words_dict = collections.defaultdict(str)
        for abs_path in abs_paths:
            with open(abs_path, "r", encoding="utf-8") as f:
                # 去掉空行
                lines = [line.strip() for line in f.readlines() if line.strip()]
                # 去掉注释行
                lines = [line for line in lines if not line.startswith('#')]
                for line in lines:
                    words = line.split(';')
                    first = words[0]
                    for w in words[1:]:
                        words_dict[w] = first

        return words_dict


    @staticmethod
    def stop_words_file(abs_paths: Union[str, List[str]]) ->Set[str]:
        """
        停用词典
        """
        if isinstance(abs_paths, str):
            abs_paths = [abs_paths]

        words_set = set()
        for abs_path in abs_paths:
            with open(abs_path, "r", encoding="utf-8") as f:
                # 去掉空行
                lines = [line.strip() for line in f.readlines() if line.strip()]
                # 去掉注释行
                lines = [line for line in lines if not line.startswith('#')]
                for line in lines:
                    for w in line.split(';'):
                        words_set.add(w)
        return words_set

    @staticmethod
    def controlled_words_file(abs_paths: Union[str, List[str]]) ->Set[str]:
        """
        受控词典
        """
        if isinstance(abs_paths, str):
            abs_paths = [abs_paths]

        words_set = set()
        for abs_path in abs_paths:
            with open(abs_path, "r", encoding="utf-8") as f:
                # 去掉空行
                lines = [line.strip() for line in f.readlines() if line.strip()]
                # 去掉注释行
                lines = [line for line in lines if not line.startswith('#')]
                for line in lines:
                    for w in line.split(';'):
                        words_set.add(w)

        return words_set


class Utils:
    @staticmethod
    def resort_columns(old_names: List[str], new_names: List[str]):
        """
        新插入的列，位于原有列的后面。
        新的列名，是原列名后面加上了“-new”。其他格式不支持
        """
        for new1 in new_names:
            old_names.remove(new1)

        for new1 in new_names:
            i = old_names.index(new1[: new1.rfind("-")])
            old_names.insert(i + 1, new1)

        return old_names

    @staticmethod
    def calculate_jaccard_similarity(threshold, l1, sentences) -> Dict[int, float]:
        """
        threshold 在 [0.0, 1.0]
        """
        set1 = set(l1)
        result = {}
        for index, l2 in enumerate(sentences):
            set2 = set(l2)
            intersection = len(set1.intersection(set2))
            union = len(set1.union(set2))
            if union == 0:
                return 0
            if union:
                val = intersection / union
                if val >= threshold:
                    result[index] = val
        return result

    @staticmethod
    def jaccard_similarity(set1: Set[str], set2: Set[str]) -> float:
        """
        计算杰卡德相似度
        :param set1: set类型
        :param set2:
        :return: 在[0,1]之间的值
        """
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union

    @staticmethod
    def generate_random_color():
        """
        生成任意颜色
        """
        red = secrets.randbelow(256)
        green = secrets.randbelow(256)
        blue = secrets.randbelow(256)
        # return red, green, blue

        red = str(hex(red))[-2:].replace("x", "0").upper()
        green = str(hex(green))[-2:].replace("x", "0").upper()
        blue = str(hex(blue))[-2:].replace("x", "0").upper()
        return "#" + red + green + blue

    @staticmethod
    def replace(line, words_dict:Dict[str, str]):
        """
        假设line是'aa;bb;cc;dd'，words_dict是{'aa':1,'cc':2}，返回值是1;bb;2;dd
        :param line:
        :param words_dict:
        :return:
        """
        assert isinstance(line, str)
        assert isinstance(words_dict, dict)

        keys = words_dict.keys()
        words = [
            str(words_dict[w]) if w in keys else w for w in line.split(Config.seperator.value)
        ]
        return Config.seperator.value.join(words)

    @staticmethod
    def replace2(line, words_set: Union[List[str], Set[str]]):
        """
        如果 line是aa;bb;cc;dd, words_set是['aa','bb']，那么结果是cc;dd
        :param line:
        :param words_set:
        :return:
        """
        words = [w for w in line.split(Config.seperator.value) if w not in words_set]
        return ";".join(words)

    @staticmethod
    def get_from_limit(i: int, arr: List[str], limit: int):
        if limit <= len(arr):
            return arr[i]
        else:
            if i < len(arr):
                return arr[i]
            else:
                return ""

    @staticmethod
    def split_string_by_length(string, length):
        """
        按照数量，拆分字符串
        """
        pattern = f".{{1,{length}}}"
        result = re.findall(pattern, string)
        return result

    @staticmethod
    def reserve_chars(other_char, line: str):
        rr = []
        for word in line.split(Config.seperator.value):
            if other_char in word:
                rr.append(other_char)
            else:
                rr.append(word)
        return Config.seperator.value.join(rr)

    @staticmethod
    def has_Chinese_or_punctuation(ws):
        return Utils.has_Chinese(ws) or Utils.has_punctuation(ws)

    @staticmethod
    def join_values(row, col_names: List[str]) -> Set[str]:
        """
        :param row:
        :param col_names:
        :return:
        """
        # 先合并
        joined = Config.seperator.value.join([row[col] for col in col_names])
        # 再分割
        values = [item.strip() for item in re.split(r"\s+|;", joined) if item.strip()]
        return set(values)

    @staticmethod
    def has_Chinese(ws):
        return any(
            [True if "\u4e00" <= w <= "\u9fff" else False for w in jieba.lcut(ws)]
        )

    @staticmethod
    def has_punctuation(ws):
        # 中文符号
        return any([True if w in punctuation else False for w in jieba.lcut(ws)])

    array = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    @staticmethod
    def uuid8():
        id = str(uuid.uuid4()).replace("-", "")  # 注意这里需要用uuid4
        buffer = []
        for i in range(0, 8):
            start = i * 4
            end = i * 4 + 4
            val = int(id[start:end], 16)
            buffer.append(Utils.array[val % 62])
        return "".join(buffer)

    @staticmethod
    def get_html(url):
        headers = {
            'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '_tb_token_=berT80V49uJ9PFEJKGPI; cna=IhV+FpiDqRsCAXE54OSIgfFP; v=0; t=bb1c685b877ff64669f99c9dade7042c; cookie2=1e5103120f9886062722c86a5fad8c64; uc1=cookie14=UoTbm8P7LhIRQg%3D%3D; isg=BJWVw-e2ZCOuRUDfqsuI4YF0pJFFPHuu_ffxbBc6UYxbbrVg3-JZdKMoODL97mFc; l=dBMDiW9Rqv8wgDSFBOCiVZ9JHt_OSIRAguWfypeMi_5Zl681GgQOkUvZ8FJ6VjWftBTB4tm2-g29-etki6jgwbd6TCNQOxDc.',
            'referer': 'https://item-paimai.taobao.com/pmp_item/609160317276.htm?s=pmp_detail&spm=a213x.7340941.2001.61.1aec2cb6RKlKoy',
            'sec-fetch-mode': 'cors',
            "sec-fetch-site": 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        resp = requests.get(url, headers=headers)
        assert resp.status_code == 200
        return etree.HTML(resp.text)


class MyMachineCode:
    def __init__(self):
        """
        机器码，还有授权文件，还有验证
        """
        self.m_wmi = wmi.WMI()
        self.licence_path = os.path.join(os.path.expanduser("~"), ".licence.abc")

    def __cpu(self):
        cpu_info = self.m_wmi.Win32_Processor()
        if len(cpu_info) > 0:
            return cpu_info[0].ProcessorId
        return ""

    def __mac(self):
        for network in self.m_wmi.Win32_NetworkAdapterConfiguration():
            mac_address = network.MacAddress
            if mac_address != None:
                return mac_address
        return ""

    def __mainboard(self):
        board_info = self.m_wmi.Win32_BaseBoard()
        if len(board_info) > 0:
            return board_info[0].SerialNumber.strip().strip(".")
        return ""

    def get_code(self):
        """
        获得机器码
        """
        combine_str = self.__mac() + self.__cpu() + self.__mainboard()
        combine_byte = combine_str.encode("utf-8")
        return combine_byte.upper()

    def read_licence(self):
        """
        获取授权文件内容
        """

        if os.path.exists(self.licence_path):
            with open(self.licence_path, "r", encoding="utf-8") as f:
                return "".join(f.readlines())
        return ""

    def write_licence(self, text):
        """
        写入授权文件
        """
        with open(self.licence_path, "w", encoding="utf-8") as f:
            f.write(text)
MachineCode = MyMachineCode()
