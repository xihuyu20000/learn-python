import importlib
import os

from flask import Flask

from basic import log
from basic.config import config
from basic.database import db

basedir = os.path.abspath(os.path.dirname(__name__))
def auto_load_plugins(app):
    """
    自动导入插件
    :param app:
    :return:
    """
    base_plugins = os.path.join(basedir, 'plugins')
    notin = ('__init__.py', '__pycache__')
    plugins = [plugin_name for plugin_name in os.listdir(base_plugins) if plugin_name not in notin]
    for plugin in plugins:
        plugin_module = importlib.import_module(f'plugins.{plugin}.routes')
        log.debug('插件', plugin_module.__name__)
        app.register_blueprint(plugin_module.bp)

def create_app(config_name=None):
    """
    创建app的工厂，全局唯一
    :param config_name:
    :return:
    """
    app = Flask('LayuiminiTest')
    log.debug('项目根目录', app.root_path)
    app.config.from_object(config[config_name]())
    db.init_app(app)
    auto_load_plugins(app)
    log.debug('模板路径', app.jinja_loader.list_templates())


    @app.route('/helloworld')
    def helloworld():
        return 'Hello World!'

    return app


