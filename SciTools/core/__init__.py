"""

"""
import os
import sys
from typing import Any

import psutil
import requests
from loguru import logger
from lxml import etree

import settings

ROOT_DIR = os.path.abspath(os.path.dirname('SciTools'))


def abs_path(filename: str) -> str:
    if not os.path.isabs(filename):
        filename = os.path.join(ROOT_DIR, filename)
    Logger.info(f'文件路径 {filename}')
    assert os.path.exists(filename)
    return filename

logger.remove()
logger.add(sys.stderr, level=settings.LOG_LEVEL)
class Logger():

    @staticmethod
    def trace(msg:str):
        logger.trace(msg)

    @staticmethod
    def debug(msg:str):
        logger.debug(msg)

    @staticmethod
    def info(msg:str):
        logger.info(msg)

    @staticmethod
    def error(msg:str):
        logger.error(msg)


class OS:
    @staticmethod
    def __GetRegValue(key: str, subkey: str, value: str) -> Any:
        '''
        获取系统注册表信息

        Parameters
        ----------
        key : str
            类型.
        subkey : str
            路径.
        value : str
            key.

        Returns
        -------
        value : Any
            DESCRIPTION.

        '''
        import winreg
        key = getattr(winreg, key)
        handle = winreg.OpenKey(key, subkey)
        (value, type) = winreg.QueryValueEx(handle, value)
        return value

    @staticmethod
    def GetSystemVersionWindows() -> str:
        '''
        获取操作系统版本（windows）
        Returns 返回值带有Windows 10字眼，带有x64
        -------
        str
            DESCRIPTION.

        '''
        try:
            import platform
            bit: str = 'x86';
            if 'PROGRAMFILES(X86)' in os.environ: bit = 'x64'

            def get(key: str):
                return OS.__GetRegValue(
                    "HKEY_LOCAL_MACHINE",
                    "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
                    key
                )

            osName = get('ProductName')
            build = get('CurrentBuildNumber')

            version: str = '{} (build {}) {} (Py{})'.format(
                osName, build, bit, platform.python_version())
            return version
        except Exception as ex:
            print('获取系统版本失败，错误：' + str(ex))
            return '未知系统版本.'

    @staticmethod
    def __ToSizeInt(byte: int, target: str) -> int:
        '''
        将字节大小转换为目标单位的大小

        Parameters
        ----------
        byte : int
            int格式的字节大小（bytes size）
        target : str
            目标单位，str.

        Returns
        -------
        int
            转换为目标单位后的字节大小.

        '''
        return int(byte / 1024 ** (('KB', 'MB', 'GB', 'TB').index(target) + 1))

    @staticmethod
    def GetMemInfoWindows() -> dict:
        '''
        获取内存信息（windows）

        Returns
        -------
        dict
            DESCRIPTION.

        '''
        mem = psutil.virtual_memory()
        memInfo: dict = {
            'memTotal': OS.__ToSizeInt(mem.total, 'MB'),
            'memFree': OS.__ToSizeInt(mem.free, 'MB'),
            'memRealUsed': OS.__ToSizeInt(mem.used, 'MB'),
            'menUsedPercent': mem.used / mem.total * 100
        }

        return memInfo


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
