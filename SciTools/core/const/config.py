import collections
import json
import os
import sys

from PySide2 import QtCore

from core.log import logger

abs_path = (
    os.path.expanduser("~")
    if getattr(sys, "frozen", False)
    else os.path.abspath(os.curdir)
)


class FileFormat:
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
            Field('标题', 'title')
        ]


class NormStyle:
    ochiia = 'ochiia'


class HierachyClusterStyle:
    average = 'average'
    ward = 'ward'


class DistanceStyle:
    correlation = 'correlation'
    euclidean = 'euclidean'
    cosine = 'cosine'


class MySignal(QtCore.QObject):
    info = QtCore.Signal(str)
    error = QtCore.Signal(str)
    set_clean_dataset = QtCore.Signal(object)
    datafiles_changing = QtCore.Signal()
    reset_cache = QtCore.Signal()
    push_cache = QtCore.Signal(object)


ssignal = MySignal()

