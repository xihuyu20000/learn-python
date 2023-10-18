import os

from jinja2 import Environment, FileSystemLoader, Template

from loguru import logger as log

def get_project_path():
    """
    获取项目的根目录的绝对路径
    :return:
    """
    return os.path.dirname(os.path.abspath(__name__))


class Builder:
    def build_str(self, tpl_str:str, data:dict) -> str:
        """
        解析字符串模板
        :param tpl_str:
        :param data:
        :return:
        """
        tpl = Template(tpl_str)
        assert tpl
        content = tpl.render(data)
        assert content
        return content

    def build_tpl(self, tpl_path:str, context:dict) -> str:
        """
        解析html模板
        :param tpl_path: 模板路径
        :param context: 上下文数据
        :return: 解析后的字符串
        """
        # 项目根目录
        tpl_root_dir = os.path.join(get_project_path(), 'templates')
        assert os.path.exists(tpl_root_dir)
        # jinja2上下文环境
        env = Environment(loader=FileSystemLoader(tpl_root_dir))
        log.info('模板列表\r\n===> '+' \r\n===> '.join(env.loader.list_templates()))
        # 读取模板
        tpl = env.get_template(tpl_path)
        # 解析成str
        content = tpl.render(context)
        assert len(content)>0
        return content


tpl_builder = Builder()