class ProjectConfig:
    """
    项目：
    """

    def __init__(self):
        self.project_name: str = ''
        self.display_name: str = ''


class PageConfig:
    """
    页面：
    """

    def __init__(self):
        self.page_name: str = ''  # 名称
        self.menuable: bool = False  # 是否菜单
        self.parent: str = ''  # 父窗口


class Widget:
    """
    组件
    """

    def __init__(self):
        ...


class TableWidget(Widget):
    """
    表格组件
    """

    def __init__(self):
        self.treeable: bool = False  # 树表格
        self.pagable: bool = False  # 分页
        self.single_choose_row: bool = False  # 单选行
        self.multi_choose_row: bool = False  # 多选行

        self.btn_add: bool = False  # 插入按钮
        self.btn_remove: bool = False  # 删除按钮
        self.btn_modify: bool = False  # 修改按钮
        self.btn_show: bool = False  # 显示按钮


class FormWidget(Widget):
    """
    表单组件
    """

    def __init__(self):
        ...


class ColumnConfig:
    """
    列
    """

    def __init__(self):
        self.column_name: str = ''  # 列名
        self.display_name: str = ''  # 显示名
        self.order_index: str = ''  # 排序
        self.field_style: str = ''  # 数据类型
        self.show_format = ''  # 显示格式
        self.width = ''  # 宽度
        self.just_style = ''  # 对齐方式
        self.hidable = ''  # 是否隐藏
        self.cal_style = ''  # 合计类型
