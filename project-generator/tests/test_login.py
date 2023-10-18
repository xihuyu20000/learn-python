# 登录页，测试

from lxml import etree

from basic import tpl_builder


def test_01():
    for i in [1,2,3,4,5,6]:
        _test_login(i)

def _test_login(i):
    content = tpl_builder.build_tpl(tpl_path=f"login/login0{i}.html", context={"project_title": "我的地盘我做主", "username": "test@qq.com", "password": "admin"})
    root = etree.HTML(content)
    assert root.xpath('//title/text()') == ['我的地盘我做主']
    assert root.xpath('//*[@id="form2"]/@action') == ['/login']
    assert root.xpath('//*[@id="form2"]/@method') == ['post']
    assert root.xpath('//*[@name="username"]/@value') == ['test@qq.com']
    assert root.xpath('//*[@name="password"]/@value') == ['admin']
