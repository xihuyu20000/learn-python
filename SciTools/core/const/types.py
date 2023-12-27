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
    PARQUET = "PARQUET"


Field = collections.namedtuple("Field", ['cn_name', 'en_name'])


class FieldStyle:

    def __init__(self):
        self.fields = [
            Field('作者', 'author'),
            Field('出版年', 'pubyear'),
            Field('关键字', 'keywords'),
            Field('标题', 'title'),
            Field('摘要', 'abstract'),
        ]


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
