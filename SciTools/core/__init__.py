"""

"""
import os

import requests
from loguru import logger
from lxml import etree

ROOT_DIR = os.path.abspath(os.path.dirname('SciTools'))

def abs_path(filename: str) -> str:
    if not os.path.isabs(filename):
        filename = os.path.join(ROOT_DIR, filename)
    debug(f'文件路径{filename}')
    assert os.path.exists(filename)
    return filename

def debug(msg):
    logger.debug(msg)

def info(msg):
    logger.info(msg)

def error(msg):
    logger.error(msg)


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