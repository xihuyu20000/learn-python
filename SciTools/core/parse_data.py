import re
from typing import Dict, List

import pandas as pd

from core import abs_path

"""
专门解析各种数据来源的文件，输出的格式必须统一是BiblioModel
"""


# 作者，机构，关键词

# = namedtuple('BiblioModel', ['doctype', 'authors', 'orgs', 'title', 'source', 'pubyear', 'kws', 'abs'])

class BiblioModel:
    def __init__(self, doctype='', authors='', orgs='', title='', source='', pubyear='', kws='', abs=''):
        self.doctype = doctype
        self.authors = authors
        self.orgs = orgs
        self.title = title
        self.source = source
        self.pubyear = pubyear
        self.kws = kws
        self.abs = abs

    def to_dict(self):
        return {'doctype': self.doctype, 'authors': self.authors, 'orgs': self.orgs, 'title': self.title,
                'source': self.source, 'pubyear': self.pubyear, 'kws': self.kws, 'abs': self.abs}

    @staticmethod
    def from_cnki_gbt7714_2015(raw: Dict):
        # 'doctype', 'authors', 'orgs', 'title', 'source', 'pubyear', 'kws', 'abs'
        doctype = raw['doctype']
        authors = ','.join([a.strip() for a in raw['authors'].strip().split(',') if a.strip()])
        orgs = ''
        title = raw['title']
        source = raw['source']
        pubyear = ''
        kws = ''
        abs = ''

        return BiblioModel(doctype=doctype, authors=authors, orgs=orgs, title=title, source=source, pubyear=pubyear,
                           kws=kws, abs=abs)

    @staticmethod
    def from_cnki_refworks(raw: Dict):
        # 'doctype', 'authors', 'orgs', 'title', 'source', 'pubyear', 'kws', 'abs'
        doctype = raw['RT']
        authors = ','.join([a.strip() for a in raw['A1'].strip().split(';') if a.strip()])
        orgs = ','.join([a.strip() for a in raw['AD'].strip().split(';') if a.strip()])
        title = raw['T1']
        source = raw['JF']
        pubyear = ''
        kws = ','.join([a.strip() for a in raw['K1'].strip().split(',') if a.strip()])
        abs = raw['AB']

        if len(raw['YR']) > 0:
            pubyear = raw['YR']
        elif len(raw['FD']) > 0:
            pubyear = raw['FD'][:4]

        return BiblioModel(doctype=doctype, authors=authors, orgs=orgs, title=title, source=source, pubyear=pubyear,
                           kws=kws, abs=abs)


class ParserData:

    @staticmethod
    def parse_save_excel(ds, excelname: str):
        """

        :param ds:
        :param excelname:
        """
        # 转为dict类型
        ds = [model.to_dict() for model in ds]
        df = pd.DataFrame(ds)
        # index从1开始
        df.index += 1
        writer = pd.ExcelWriter(excelname)
        df.to_excel(writer)
        writer._save()


class cnki_gbt_7714_2015(ParserData):
    # 在线文献的类型
    ONLINE_MEDIAS = ['DB/OL', 'DB/MT', 'DB/CD', 'M/CD', 'CP/DK', 'J/OL', 'EB/OL']

    @staticmethod
    def __match_doctype(line: str):
        # *后面的？表示非贪婪模式
        return re.search(r'\[.*?\].', line)

    @staticmethod
    def __refdoc_style(line: str):
        m = cnki_gbt_7714_2015.__match_doctype(line)
        if m:
            # 去除前后的中括号
            return m.group().replace('[', '').replace('].', '')
        return ''

    @staticmethod
    def __pubdate(doctype, line: str):
        """
        电子文献与非电子文献，出版日期的著录方式不一样
        :param doctype:
        :param line:
        :return:
        """
        if doctype in cnki_gbt_7714_2015.ONLINE_MEDIAS:
            m = re.search(r'\[\d{4}', line)
            if m:
                return m.group()[1:]
            else:
                return ''
        else:
            return line[:4]

    @staticmethod
    def parse_line(line) -> BiblioModel:
        dataset = dict()
        dataset['line'] = line.strip()

        # 1 序号
        target = re.search(r'^\[\d+\]', line)
        dataset['no'] = int(target.group()[1:-1])
        # 去掉序号后的行
        line: str = line.replace(target.group(), '')

        # 2 文献类型
        dataset['doctype'] = cnki_gbt_7714_2015.__refdoc_style(line)

        # 3 主要责任者
        authors = line[:line.find('.')]
        authors = authors[:-1] if authors[-1] == '等' else authors
        dataset['authors'] = authors
        # 去掉责任者后的行
        line = line[line.find('.') + 1:]

        # 4 题名
        m = cnki_gbt_7714_2015.__match_doctype(line)
        dataset['title'] = line[: m.span()[0]]
        # 去掉责任者后的行
        line = line[m.span()[1]:]

        # 5 来源
        source = line[:line.find(',')]
        dataset['source'] = source
        # 去掉责任者后的行
        line = line[line.find(',') + 1:]

        # 6 出版年
        dataset['pubyear'] = cnki_gbt_7714_2015.__pubdate(dataset['doctype'], line)

        return BiblioModel.from_cnki_gbt7714_2015(dataset)

    @staticmethod
    def parse_file(filename: str) -> List[BiblioModel]:
        """
        解析cnki的GBT 7714-2015格式文件
        :param filename:
        :return:
        """
        filename = abs_path(filename)

        datasets = []
        with open(filename, encoding='utf-8') as f:
            for line in f.readlines():
                assert line
                if line.strip():
                    line = line.strip()
                    datasets.append(cnki_gbt_7714_2015.parse_line(line))
        return datasets


class cnki_refworks(ParserData):
    """
    导出txt时，文件末尾多2个空行
    """
    CORE_ITEMS = ('RT'  # 文献类型
                  , 'A1'  # 作者
                  , 'AD'  # 工作单位
                  , 'T1'  # 题名
                  , 'JF'  # 来源
                  , 'YR'  # 出版年
                  , 'FD'  # 出版日期
                  , 'K1'  # 关键词
                  , 'AB'  # 摘要
                  )

    @staticmethod
    def parse_file(filename: str):
        filename = abs_path(filename)

        ds = []
        with open(filename, 'r', encoding='utf-8') as f:
            NO = 1
            values: Dict[str, int | str] = {'NO': NO, 'RT': '', 'A1': '', 'AD': '', 'T1': '', 'JF': '', 'YR': '',
                                            'FD': '',
                                            'K1': '',
                                            'AB': ''}
            for linone, line in enumerate(f.readlines()):
                # 前2个字母是具体的key
                name = line[:2].strip()
                if name in cnki_refworks.CORE_ITEMS:
                    values[name] = line[2:].strip()

                # 空行，表示上一条结束，新的一条开始
                if len(line.strip()) == 0:
                    if values and len(values['RT']) > 0:
                        ds.append(BiblioModel.from_cnki_refworks(values))
                    # 每次初始化数据
                    NO += 1
                    values = {'NO': NO, 'RT': '', 'A1': '', 'AD': '', 'T1': '', 'JF': '', 'YR': '', 'FD': '', 'K1': '',
                              'AB': ''}

        return ds


if __name__ == '__main__':
    pass
