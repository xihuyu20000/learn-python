from typing import Tuple, Dict

from basic.log import error


class SchemaValidator:
    """
    表结构、字段结构的schema校验器
    """
    err001 = '不是有效的dict类型'
    err002 = 'root必须含有table_name属性'
    err003 = 'root必须含有table_desc属性'
    err004 = 'root必须含有fields属性'

    err100 = 'fields的值类型必须是dict'
    err101 = '每一个field的值类型必须是dict'
    err102 = 'field必须有属性label'
    err103 = 'field的属性label的值，不能是空串'
    err104 = 'field必须有属性datatype'
    err105 = 'field的属性datatype的值，不能是空串'
    err106 = 'field的属性datatype的值，不是有效的数据类型'
    err107 = 'field必须有属性length'

    err201 = '必须有一个列是主键'
    err202 = '只能有一个列是主键，不能多个列都设置主键'

    @staticmethod
    def check(json_instance: Dict) -> Tuple[bool, str | None]:
        if not isinstance(json_instance, dict):
            error(SchemaValidator.err001)
            return False, SchemaValidator.err001
        if 'table_name' not in json_instance.keys():
            error(SchemaValidator.err002)
            return False, SchemaValidator.err002
        if 'table_desc' not in json_instance.keys():
            error(SchemaValidator.err003)
            return False, SchemaValidator.err003
        if 'fields' not in json_instance.keys():
            error(SchemaValidator.err004)
            return False, SchemaValidator.err004

        if not (isinstance(json_instance['fields'], dict)):
            error(SchemaValidator.err100)
            return False, SchemaValidator.err100

        fields: Dict[str, Dict] = json_instance['fields']
        has_pk = 0
        for field_name, field_config in fields.items():
            if not isinstance(field_config, dict):
                error(SchemaValidator.err101)
                return False, SchemaValidator.err101

            if 'label' not in field_config.keys():
                error(SchemaValidator.err102)
                return False, SchemaValidator.err102

            label_value = str(field_config['label']).strip()
            if len(label_value) == 0:
                error(SchemaValidator.err103)
                return False, SchemaValidator.err103

            if 'datatype' not in field_config.keys():
                error(SchemaValidator.err104)
                return False, SchemaValidator.err104

            datatype_value = str(field_config['datatype']).strip()
            if len(datatype_value) == 0:
                error(SchemaValidator.err105)
                return False, SchemaValidator.err105

            if datatype_value not in DataStyle.values():
                error(SchemaValidator.err106)
                return False, SchemaValidator.err106
            # 必须有length属性
            if 'length' not in field_config.keys():
                error(SchemaValidator.err107)
                return False, SchemaValidator.err107
            # 如果有is_pk属性，只有能1个
            if 'pk' in field_config.keys():
                if int(field_config['pk']) == 1:
                    if has_pk:
                        error(SchemaValidator.err202)
                        return False, SchemaValidator.err202
                    else:
                        has_pk = True
        # 如果没有is_pk属性，报错
        if not has_pk:
            error(SchemaValidator.err201)
            return False, SchemaValidator.err201

        return True, None


class DBStyle:
    """
    数据库类型
    """
    SQLite = "sqlite"
    MySQL5 = "mysql5"
    MySQL8 = "mysql8"

    @staticmethod
    def values() -> Tuple[str, ...]:
        return DBStyle.SQLite, DBStyle.MySQL5, DBStyle.MySQL8


class DataStyle:
    """
    数据类型
    """
    STRING = "string"
    INTEGER = "integer"
    DATE = "date"
    TIME = "time"
    DATETIME = "datetime"

    sqlite_mapping = {
        STRING: "TEXT",
        INTEGER: "INTEGER",
        DATE: "DATE",
        TIME: "DATE",
        DATETIME: "DATETIME"
    }
    mysql5_mapping = {
        STRING: "VARCHAR",
        INTEGER: "INT",
        DATE: "DATE",
        TIME: "TIME",
        DATETIME: "DATETIME"
    }
    mysql8_mapping = {
        STRING: "VARCHAR",
        INTEGER: "INT",
        DATE: "DATE",
        TIME: "TIME",
        DATETIME: "DATETIME"
    }

    @staticmethod
    def real_datatype(db_style: str, key: str) -> str:
        if db_style == DBStyle.SQLite:
            return DataStyle.sqlite_mapping.get(key)
        elif db_style == DBStyle.MySQL5:
            return DataStyle.mysql5_mapping.get(key)
        elif db_style == DBStyle.MySQL8:
            return DataStyle.mysql8_mapping.get(key)
        assert '不支持的数据库类型'

    @staticmethod
    def values() -> Tuple[str, ...]:
        return DataStyle.STRING, DataStyle.INTEGER, DataStyle.DATE, DataStyle.TIME, DataStyle.DATETIME
