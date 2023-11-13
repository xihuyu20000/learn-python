"""

"""
import os
import re
from core import get_html


def run():
    html = get_html(r'https://scirp.org/journal/RecentlyPublishedPapers.aspx')
    root_li_list = html.xpath('//ul[@class="list-unstyled list_link"]/li')

    datasets = []

    for li in root_li_list[:2]:
        line_data = {}
        line_data['title'] = li.xpath('./div[@class="list_t"]/span/a/text()')[0].strip()
        line_data['url'] = li.xpath('./div[@class="list_t"]/span/a/@href')[0].strip()
        line_data['authors'] = li.xpath('./div[@class="txt5"]/text()')[0].strip()
        line_data['source'] = li.xpath('./div[@class="list_unit"]/a[1]/i/text()')[0].strip()
        pubdate = li.xpath('./div[@class="list_unit"]/text()')[-1]
        pubdate = re.search(r'2[0-9]{3}', pubdate).group()
        line_data['pubdate'] = pubdate
        datasets.append(line_data)

    return datasets

