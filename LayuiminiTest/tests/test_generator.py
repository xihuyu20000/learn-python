from basic.dbmgr import DBStyle
from basic.dbmgr.generator import DbAction, CreateTableRunner, AlterTableRunner
from basic.log import debug
from tests import BaseTest


class TestDbActionGenerator:
    def test_001_table_new(self):
        new_config = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {
                'id':{'label':'主键', 'datatype':'integer', 'length':10, 'pk':1}
            }
        }
        old_config = None
        steps = DbAction.generate_steps(new_config=new_config, old_config=old_config)
        assert len(steps) == 1
        assert steps[0]['action_style'] == DbAction.TABLE_CREATE

    def test_002_table_update(self):
        new_config = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {
                'id':{'label':'主键', 'datatype':'integer', 'length':10, 'pk':1}
            }
        }
        old_config = {
            'table_name': 'test11', 'table_desc': '测试表',
            'fields': {
                'id':{'label':'主键', 'datatype':'integer', 'length':10, 'pk':1}
            }
        }
        steps = DbAction.generate_steps(new_config=new_config, old_config=old_config)
        assert len(steps) == 1
        assert steps[0]['action_style'] == DbAction.TABLE_ALTER

    def test_003_table_drop(self):
        # todo 不知道怎么写
        ...

    def test_010_field_add(self):
        new_config = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {
                'id':{'label':'主键', 'datatype':'integer', 'length':10, 'pk':1},
                'name': {'label': '姓名', 'datatype': 'string', 'length':10},
                'sex': {'label': '性别', 'datatype': 'string', 'length':10},
            }
        }
        old_config = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {
                'id':{'label':'主键', 'datatype':'integer', 'length':10, 'pk':1}
            }
        }
        steps = DbAction.generate_steps(new_config=new_config, old_config=old_config)
        assert len(steps) == 2
        assert steps[0]['action_style'] == DbAction.FIELD_ADD

        fields = set()
        fields.add(steps[0]['field_name'])
        fields.add(steps[1]['field_name'])
        fields2 = set()
        fields2.add('name')
        fields2.add('sex')
        assert fields == fields2

    def test_011_field_delete(self):
        new_config = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {
                'id':{'label':'主键', 'datatype':'integer', 'length':10, 'pk':1},
            }
        }
        old_config = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {
                'id':{'label':'主键', 'datatype':'integer', 'length':10, 'pk':1},
                'name': {'label': '姓名', 'datatype': 'string', 'length':10},
                'sex': {'label': '性别', 'datatype': 'string', 'length':10},
            }
        }
        steps = DbAction.generate_steps(new_config=new_config, old_config=old_config)
        assert len(steps) == 2
        assert steps[0]['action_style'] == DbAction.FIELD_DELETE

        fields = set()
        fields.add(steps[0]['field_name'])
        fields.add(steps[1]['field_name'])
        fields2 = set()
        fields2.add('name')
        fields2.add('sex')
        assert fields == fields2

    def test_015_field_update(self):
        new_config = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {
                'id': {'label': '主键', 'datatype': 'integer', 'length':10, 'pk': 1},
                'name': {'label': '姓名1', 'datatype': 'string', 'length':10},
                'sex': {'label': '性别', 'datatype': 'integer', 'length':10},
            }
        }
        old_config = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {
                'id': {'label': '主键', 'datatype': 'integer', 'length':10, 'pk': 1},
                'name': {'label': '姓名', 'datatype': 'string', 'length':10},
                'sex': {'label': '性别', 'datatype': 'string', 'length':10},
            }
        }
        steps = DbAction.generate_steps(new_config=new_config, old_config=old_config)
        assert len(steps) == 2
        assert steps[0]['action_style'] == DbAction.FIELD_UPDATE

        fields = set()
        fields.add(steps[0]['field_name'])
        fields.add(steps[1]['field_name'])
        fields2 = set()
        fields2.add('name')
        fields2.add('sex')
        assert fields == fields2


class TestNewTableRunner:
    default_config = {
        'mysql8_default_engine' : 'Innodb',
        'mysql8_default_charset' : 'utf8mb4'
    }
    table_config = {
        'table_name': 'test', 'table_desc': '测试表',
        'fields': {
            'id': {'label': '主键', 'datatype': 'integer', 'length': 10, 'pk': 1},
            'name': {'label': '姓名', 'datatype': 'string', 'length': 10},
            'sex': {'label': '性别', 'datatype': 'string', 'length': 10},
        }
    }

    steps = DbAction.generate_steps(new_config=table_config)
    def test_001_sqlite(self):
        print(TestNewTableRunner.steps)
        runner = CreateTableRunner(DBStyle.SQLite, default_config=TestNewTableRunner.default_config)
        sql = runner.run(TestNewTableRunner.table_config)
        debug('自动生成的SQL' ,sql)
        assert 'CREATE TABLE' in sql

    def test_002_mysql5(self):
        runner = CreateTableRunner(DBStyle.MySQL5, default_config=TestNewTableRunner.default_config)
        sql = runner.run(TestNewTableRunner.table_config)
        debug('自动生成的SQL' ,sql)
        assert 'CREATE TABLE' in sql

    def test_003_mysql8(self):
        runner = CreateTableRunner(DBStyle.MySQL8, default_config=TestNewTableRunner.default_config)
        sql = runner.run(TestNewTableRunner.table_config)
        debug('自动生成的SQL' ,sql)
        assert 'CREATE TABLE' in sql


class TestAlterTableRunner:
    default_config = {
        'mysql8_default_engine' : 'Innodb',
        'mysql8_default_charset' : 'utf8mb4'
    }
    new_config = {
        'table_name': 'test', 'table_desc': '测试表',
        'fields': {
            'id': {'label': '主键', 'datatype': 'integer', 'length': 10, 'pk': 1}
        }
    }
    old_config = {
        'table_name': 'test11', 'table_desc': '测试表',
        'fields': {
            'id': {'label': '主键', 'datatype': 'integer', 'length': 10, 'pk': 1}
        }
    }

    steps = DbAction.generate_steps(new_config=new_config, old_config=old_config)
    def test_001_sqlite(self):
        print(TestAlterTableRunner.steps)
    #     runner = AlterTableRunner(DBStyle.SQLite, default_config=TestAlterTableRunner.default_config)
    #     sql = runner.run(TestAlterTableRunner.table_config)
    #     debug('自动生成的SQL' ,sql)
    #     assert 'ALTER TABLE' in sql