"""
读写数据库
"""
import os
import pickle
import sqlite3

import pandas as pd

from core.const import ssignal
from core.log import logger

_abs_path = os.path.join(os.path.expanduser("~"), '.sci.cache')
conn = sqlite3.connect(_abs_path)


class PandasCache:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.index_id = 0
        self.current: pd.DataFrame = pd.DataFrame(columns=[])

        ssignal.reset_cache.connect(PandasCache.init_cache)
        ssignal.push_cache.connect(self.push)

    def push(self, name, value: pd.DataFrame):
        """
        pickle.dumps(df)
        df = pickle.loads(df_bytes)
        """
        cur = conn.cursor()
        sql = "INSERT INTO cache(name, value) VALUES (?, ?)"
        cur.execute(sql, (name, pickle.dumps(value.copy(True)),))

        sql = "SELECT last_insert_rowid()"
        resultset = cur.execute(sql).fetchone()
        self.index_id = resultset[0]
        cur.close()
        conn.commit()
        logger.debug('插入缓存，当前最大索引{}', self.index_id)
        ssignal.update_cache.emit()
        PandasCache.allinfo()

    def get_current(self):
        return self.current

    @staticmethod
    def init_cache():
        # 缓存表
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format('cache')
        cur = conn.execute(sql)

        if len(cur.fetchall()) == 1:
            conn.execute('DROP TABLE cache')

        sql = "CREATE TABLE cache(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, value BLOB NOT NULL)"
        conn.execute(sql)

        cur.close()

        logger.debug('初始化缓存')

    @staticmethod
    def get(id: int):
        logger.debug('读取缓存 id={}', id)
        cur = conn.cursor()
        sql = "SELECT * FROM cache WHERE id=?"
        id, name, value = cur.execute(sql, (id,)).fetchone()
        cur.close()
        PandasCache.allinfo()
        return pickle.loads(value)

    @staticmethod
    def allinfo():
        cur = conn.cursor()
        sql = "SELECT id, name, value FROM cache ORDER BY id ASC"
        resultset = cur.execute(sql).fetchall()
        for row in resultset:
            logger.debug('id={}, name={}, shape={}'.format(row[0], row[1], pickle.loads(row[2]).shape))
            text1 = pickle.loads(row[2]).to_string(na_rep='', col_space=4).splitlines(keepends=True)
            with open('{}.txt'.format(row[0]), 'w', encoding='utf8') as writer:
                writer.writelines(text1)
        cur.close()
        return resultset
