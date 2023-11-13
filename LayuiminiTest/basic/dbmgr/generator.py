from collections import defaultdict
from typing import List, Dict, Any, Tuple

from basic.dbmgr import DBStyle, DataStyle, SchemaValidator


class DbAction:
    """
    针对数据库的操作类型
    """
    # 新建表
    TABLE_CREATE = 'table_create'
    # 修改表
    TABLE_ALTER = 'table_alter'
    # 删除表
    TABLE_DROP = 'table_drop'

    # 添加列
    FIELD_ADD = 'field_add'
    # 修改列
    FIELD_UPDATE = 'field_update'
    # 删除列
    FIELD_DELETE = 'field_delete'

    @staticmethod
    def values() -> Tuple[str, ...]:
        return DbAction.TABLE_CREATE, DbAction.TABLE_ALTER, DbAction.TABLE_DROP, DbAction.FIELD_ADD, DbAction.FIELD_UPDATE, DbAction.FIELD_DELETE

    @staticmethod
    def generate_steps(new_config:Dict, old_config:Dict=None) -> List[Dict[str, Any]]:
        flag, msg = SchemaValidator.check(new_config)
        assert flag

        steps = []
        # 没有旧配置，就是新建表
        if old_config is None:
            steps.append({'action_style': DbAction.TABLE_CREATE})
        else:
            # 表名不同，则是重命名表
            if new_config['table_name'] != old_config['table_name']:
                steps.append({'action_style': DbAction.TABLE_ALTER})
            # 获取新旧配置的所有列名
            new_config_field_names = set(new_config['fields'].keys())
            old_config_field_names = set(old_config['fields'].keys())
            # 新增列
            new_field_names = new_config_field_names.difference(old_config_field_names)
            if new_field_names:
                for field_name in new_field_names:
                    steps.append({'action_style': DbAction.FIELD_ADD, 'field_name': field_name})
            # 删除列
            delete_field_names = old_config_field_names.difference(new_config_field_names)
            if delete_field_names:
                for field_name in delete_field_names:
                    steps.append({'action_style': DbAction.FIELD_DELETE, 'field_name': field_name})
            # 同名列
            inter_field_names = new_config_field_names.intersection(old_config_field_names)
            if inter_field_names:
                for field_name in inter_field_names:
                    if new_config['fields'][field_name] != old_config['fields'][field_name]:
                        steps.append({'action_style': DbAction.FIELD_UPDATE, 'field_name': field_name})

        return steps


class CreateTableRunner():
    def __init__(self, db_style, default_config=defaultdict()):
        self.db_style = db_style
        assert self.db_style in DBStyle.values()
        self.default_config = default_config

    def _pk(self, table_config):
        for field_name, field_config in table_config['fields'].items():
            if 'pk' in field_config.keys():
                return field_name

    def _fields_sqlite(self, table_config):
        ss = []
        for field_name, field_config in table_config['fields'].items():
            field_real_datatype = DataStyle.real_datatype(self.db_style, field_config['datatype'])
            ss.append(f'{field_name} {field_real_datatype} ')
        return ss
    def _fields_mysql8(self, table_config):
        ss = []
        for field_name, field_config in table_config['fields'].items():
            field_real_datatype = DataStyle.real_datatype(self.db_style, field_config['datatype'])
            s1 = f'{field_name} {field_real_datatype}'
            if field_config['datatype'] == DataStyle.STRING or field_config['datatype'] == DataStyle.INTEGER:
                s1 = f'{field_name} {field_real_datatype}({field_config["length"]})'
                if 'pk' in field_config.keys():
                    s1 += ' PRIMARY KEY auto_increment'
            ss.append(s1)
        return ss
    def run(self, table_config) -> str:
        """
        创建表
        :param table_config:
        :return:
        """
        table_name = table_config['table_name']
        if self.db_style == DBStyle.SQLite:
            pk_field_name = self._pk(table_config)
            fields = ','.join(self._fields_sqlite(table_config))
            return f"CREATE TABLE {table_name}({fields},PRIMARY KEY {pk_field_name}) "
        if self.db_style == DBStyle.MySQL5 or self.db_style == DBStyle.MySQL8:
            fields = ','.join(self._fields_mysql8(table_config))
            return f"CREATE TABLE {table_name}({fields}) engine = {self.default_config['mysql8_default_engine']} default charset = {self.default_config['mysql8_default_charset']} comment = '{table_config['table_desc']}'"


class AlterTableRunner():
    def __init__(self, db_style, default_config=defaultdict()) ->None:
        self.db_style = db_style
        assert self.db_style in DBStyle.values()
        self.default_config = default_config

    def run(self, old_table_name, new_table_name) -> str:
        #TODO
        """
        修改表
        :param old_table_name:
        :param new_table_name:
        :return:
        """
        if self.db_style == DBStyle.SQLite:
            raise False
        if self.db_style == DBStyle.MySQL5:
            raise False
        if self.db_style == DBStyle.MySQL8:
            raise False


class DropTableRunner():
    def __init__(self, db_style, default_config=defaultdict()):
        self.db_style = db_style
        assert self.db_style in DBStyle.values()
        self.default_config = default_config

    def run(self, table_name) -> str:
        """
        删除表
        :param table_name:
        :return:
        """
        if self.db_style == DBStyle.SQLite:
            raise False
        if self.db_style == DBStyle.MySQL5:
            raise False
        if self.db_style == DBStyle.MySQL8:
            raise False


class AddFieldRunner():
    def __init__(self, db_style, default_config=defaultdict()):
        self.db_style = db_style
        assert self.db_style in DBStyle.values()
        self.default_config = default_config

    def run(self, table_name, field_name, data_type, is_nullable=None, is_unique=None, default_value=None,
            remark_value=None) -> str:
        """
        添加列
        :param table_name: 表名
        :param field_name: 列名
        :param data_type: 数据类型
        :param is_nullable: 是否空
        :param is_unique: 是否唯一
        :param default_value: 默认值
        :param remark_value: 注释
        :return:
        """
        if self.db_style == DBStyle.SQLite:
            raise False
        if self.db_style == DBStyle.MySQL5:
            raise False
        if self.db_style == DBStyle.MySQL8:
            raise False


class UpdateFieldRunner():
    def __init__(self, db_style, default_config=defaultdict()):
        self.db_style = db_style
        assert self.db_style in DBStyle.values()
        self.default_config = default_config

    def run(self, table_name, old_field_name, new_field_name) -> str:
        """
        对字段修改
        :param table_name:
        :param old_field_name:
        :param new_field_name:
        :return:
        """
        if self.db_style == DBStyle.SQLite:
            raise False
        if self.db_style == DBStyle.MySQL5:
            raise False
        if self.db_style == DBStyle.MySQL8:
            raise False


class DeleteFieldRunner():
    def __init__(self, db_style, default_config=defaultdict()):
        self.db_style = db_style
        assert self.db_style in DBStyle.values()
        self.default_config = default_config

    def run(self, table_name, field_name) -> str:
        """
        删除列
        :param table_name:
        :param field_name:
        :return:
        """
        if self.db_style == DBStyle.SQLite:
            raise False
        if self.db_style == DBStyle.MySQL5:
            raise False
        if self.db_style == DBStyle.MySQL8:
            raise False