"""

"""

from core.parse_data import cnki_gbt_7714_2015, cnki_refworks, BiblioModel


def test001():
    """
    解析期刊
    :return:
    """
    line = "[500]曾妮,张安.基于Cite Space的国外海洋渔村文化研究进展分析[J].城市建筑,2023,20(17):196-201.DOI:10.19892/j.cnki.csjz.2023.17.43"
    ds: BiblioModel = cnki_gbt_7714_2015.parse_line(line)
    assert ds.authors == '曾妮,张安'
    assert ds.title == '基于Cite Space的国外海洋渔村文化研究进展分析'
    assert ds.doctype == 'J'
    assert ds.source == '城市建筑'


def test002():
    """
    解析在线文献
    :return:
    """
    line = "[479]何莎莎,刘芳宇,金悦婷等.“肺与大肠相表里”研究文献可视化分析[J/OL].中国中医药信息杂志,1-8[2023-11-11]https://doi.org/10.19879/j.cnki.1005-5304.202301193."

    ds: BiblioModel = cnki_gbt_7714_2015.parse_line(line)
    assert ds.authors == '何莎莎,刘芳宇,金悦婷'
    assert ds.title == '“肺与大肠相表里”研究文献可视化分析'
    assert ds.doctype == 'J/OL'
    assert ds.source == '中国中医药信息杂志'


def test100():
    filename = 'files/CNKI-GBT 7714-2015 格式引文(新).txt'
    ds = cnki_gbt_7714_2015.parse_file(filename)
    assert len(ds) == 500
    cnki_gbt_7714_2015.parse_save_excel(ds, 'output/a.xlsx')


def test200():
    filename = 'files/CNKI-refworks.txt'
    ds = cnki_refworks.parse_file(filename)
    assert len(ds) == 500
    cnki_refworks.parse_save_excel(ds, 'output/b.xlsx')


def test201():
    filename = 'files/CNKI-refworks3.txt'
    ds = cnki_refworks.parse_file(filename)
    assert len(ds) == 500
    cnki_refworks.parse_save_excel(ds, 'output/c.xlsx')
