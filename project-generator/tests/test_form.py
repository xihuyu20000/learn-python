# 表格，测试

from lxml import etree

from basic import tpl_builder


def test_simple_form():
    form_config = [
        {'fname': 'id', 'label': '编号', 'width': 20},
        {'fname': 'name', 'label': '姓名', 'width': 40},
        {'fname': 'age', 'label': '年龄', 'width': 20},
    ]
    form_data = [
        {'id': 1, 'name': '张三', 'age': 23},
        {'id': 2, 'name': '李四', 'age': 24},
        {'id': 3, 'name': '王五', 'age': 25},
    ]

    context = {"project_title": "simple-form", "form_config": form_config, "form_data": form_data}
    content = tpl_builder.build_tpl(tpl_path=f"forms/simple-form.html", context=context)
    print(content)
    root = etree.HTML(content)

    assert root.xpath('//title/text()') == ['simple-form']

