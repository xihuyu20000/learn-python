# 表格，测试

from lxml import etree

from basic import tpl_builder


def test_simple_table():
    tbl_config = [
        {'fname': 'id', 'label': '编号', 'width': 20},
        {'fname': 'name', 'label': '姓名', 'width': 40},
        {'fname': 'age', 'label': '年龄', 'width': 20},
    ]
    tbl_data = [
        {'id': 1, 'name': '张三', 'age': 23},
        {'id': 2, 'name': '李四', 'age': 24},
        {'id': 3, 'name': '王五', 'age': 25},
    ]

    context = {"project_title": "simple-table", "tbl_config": tbl_config, "tbl_data": tbl_data}
    content = tpl_builder.build_tpl(tpl_path=f"tables/simple-table.html", context=context)
    print(content)
    root = etree.HTML(content)

    assert root.xpath('//title/text()') == ['simple-table']
    assert len(root.xpath('//table/thead//td')) == 3
    assert len(root.xpath('//table/tbody//tr')) == 3
