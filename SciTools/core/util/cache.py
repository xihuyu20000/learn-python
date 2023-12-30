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
        self.max_id = 0
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
        self.max_id = resultset[0]
        self.index_id = self.max_id
        cur.close()
        conn.commit()
        logger.debug('插入缓存，当前最大索引{}', self.max_id)
        ssignal.update_cache.emit()
        PandasCache.allinfo()

    def undo(self):
        """
        撤销
        """
        if self.index_id > 1:
            self.index_id -= 1
            self.current = self.get(self.index_id)
            return self.current
        PandasCache.allinfo()
        return None

    def redo(self):
        """
        恢复
        """
        if self.index_id < self.max_id:
            self.index_id += 1
            self.current = self.get(self.index_id)
            return self.current
        PandasCache.allinfo()
        return None

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
        cur.close()
        return resultset


if __name__ == '__main__':
    PandasCache.init_cache()
    cache = PandasCache()
    df1 = pd.DataFrame({"id": [1, 2], "name": ["a", "b"]})
    cache.push('aa', df1)

    df2 = pd.DataFrame({"id": [3, 4], "name": ["aa", "bb"]})
    cache.push('bb', df2)
