import collections
import os
import sys

import strenum

abs_path = (
    os.path.expanduser("~")
    if getattr(sys, "frozen", False)
    else os.path.abspath(os.curdir)
)


class FileFormat(strenum.StrEnum):
    CNKI = "知网"
    WEIPU = "维普"
    WANFANG = "万方"
    CNKI_PATENT = "知网专利"
    WOS = "WOS"
    CSV = "CSV"
    EXCEL = "EXCEL"
    PICKLE = "PICKLE"


Field = collections.namedtuple("Field", ['cn_name', 'en_name', 'order'])

# 内部字段字典
INNER_FIELDS_DICT = collections.defaultdict(Field)
INNER_FIELDS_DICT['doctype'] = Field('文献类型', 'doctype', 100)
INNER_FIELDS_DICT['authors'] = Field('全部作者', 'authors', 20)
INNER_FIELDS_DICT['pubyear'] = Field('年份', 'pubyear', 1)
INNER_FIELDS_DICT['org'] = Field('作者单位', 'org', 30)
INNER_FIELDS_DICT['kws'] = Field('关键字', 'keywords', 40)
INNER_FIELDS_DICT['title'] = Field('标题', 'title', 10)
INNER_FIELDS_DICT['abs'] = Field('摘要', 'abstract', 60)
INNER_FIELDS_DICT['source'] = Field('来源', 'source', 50)

# CNKI期刊论文字段字典
CNKI_FIELDS_DICT = collections.defaultdict(Field)
CNKI_FIELDS_DICT["RT"]=INNER_FIELDS_DICT['doctype']  # 文献类型
CNKI_FIELDS_DICT["A1"]=INNER_FIELDS_DICT['authors']  # 作者
CNKI_FIELDS_DICT["AD"]=INNER_FIELDS_DICT['org']  # 工作单位
CNKI_FIELDS_DICT["T1"]=INNER_FIELDS_DICT['title']  # 题名
CNKI_FIELDS_DICT["JF"]=INNER_FIELDS_DICT['source']  # 来源
CNKI_FIELDS_DICT["YR"]=INNER_FIELDS_DICT['pubyear']  # 出版年
CNKI_FIELDS_DICT["K1"]=INNER_FIELDS_DICT['kws']  # 关键词
CNKI_FIELDS_DICT["AB"]=INNER_FIELDS_DICT['abs']  # 摘要

class FieldMapping:
    @staticmethod
    def cnki2core():
        return {k:v.cn_name for k,v in CNKI_FIELDS_DICT.items() }


class NormStyle(strenum.StrEnum):
    """
    归一化的方法
    """
    ochiia = 'ochiia'


class HierachyClusterStyle(strenum.StrEnum):
    """
    层次聚类的参数
    """
    average = 'average'
    ward = 'ward'


class DistanceStyle(strenum.StrEnum):
    """
    聚类计算方法
    """
    correlation = 'correlation'
    euclidean = 'euclidean'
    cosine = 'cosine'
