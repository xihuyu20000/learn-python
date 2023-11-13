from basic.dbmgr import SchemaValidator
from tests import BaseTest


class TestSchemaValidator(BaseTest):
    def test_001(self):
        d001 = [
        ]
        flag, msg = SchemaValidator.check(d001)
        assert not flag
        assert msg == SchemaValidator.err001

    def test_002(self):
        d002 = {
        }
        flag, msg = SchemaValidator.check(d002)
        assert not flag
        assert msg == SchemaValidator.err002

    def test_003(self):
        d003 = {
            'table_name': 'test',
            'fields': {}
        }
        flag, msg = SchemaValidator.check(d003)
        assert not flag
        assert msg == SchemaValidator.err003
    def test_004(self):
        d004 = {
            'table_name': 'test',
            'table_desc': '测试表',
        }
        flag, msg = SchemaValidator.check(d004)
        assert not flag
        assert msg == SchemaValidator.err004


    def test_100(self):
        d100 = {
            'table_name': 'test',
            'table_desc': '测试表',
            'fields': []
        }
        flag, msg = SchemaValidator.check(d100)
        assert not flag
        assert msg == SchemaValidator.err100

    def test_101(self):
        d101 = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {'id':[]}
        }
        flag, msg = SchemaValidator.check(d101)
        assert not flag
        assert msg == SchemaValidator.err101

    def test_102(self):
        d102 = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {'id':{}}
        }
        flag, msg = SchemaValidator.check(d102)
        assert not flag
        assert msg == SchemaValidator.err102

    def test_103(self):
        d103 = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {'id':{'label':''}}
        }
        flag, msg = SchemaValidator.check(d103)
        assert not flag
        assert msg == SchemaValidator.err103

    def test_104(self):
        d104 = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {'id':{'label':'编号'}}
        }
        flag, msg = SchemaValidator.check(d104)
        assert not flag
        assert msg == SchemaValidator.err104

    def test_105(self):
        d105 = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {'id':{'label':'编号', 'datatype':''}}
        }
        flag, msg = SchemaValidator.check(d105)
        assert not flag
        assert msg == SchemaValidator.err105

    def test_106(self):
        d106 = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {'id':{'label':'编号', 'datatype':'int'}}
        }
        flag, msg = SchemaValidator.check(d106)
        assert not flag
        assert msg == SchemaValidator.err106

    def test_107(self):
        d107 = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {'id':{'label':'编号', 'datatype':'integer'}}
        }
        flag, msg = SchemaValidator.check(d107)
        assert not flag
        assert msg == SchemaValidator.err107

    def test_201(self):
        d201 = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {'id':{'label':'编号', 'datatype':'integer', 'length':10},
                       'name':{'label':'姓名', 'datatype':'string', 'length':10}}
        }
        flag, msg = SchemaValidator.check(d201)
        assert not flag
        assert msg == SchemaValidator.err201
    def test_202(self):
        d202 = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {'id':{'label':'编号', 'datatype':'integer', 'length':10, 'pk':1},
                       'name':{'label':'姓名', 'datatype':'string', 'length':10, 'pk':1}}
        }
        flag, msg = SchemaValidator.check(d202)
        assert not flag
        assert msg == SchemaValidator.err202

    def test_10000(self):
        d10000 = {
            'table_name': 'test', 'table_desc': '测试表',
            'fields': {'id':{'label':'编号', 'datatype':'integer', 'length':10, 'pk':1},
                       'name':{'label':'姓名', 'datatype':'string', 'length':10}}
        }
        flag, msg = SchemaValidator.check(d10000)
        assert flag
        assert msg is None

