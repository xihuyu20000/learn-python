from tests import BaseTest


class TestCore(BaseTest):
    def test_001(self):
        resp = self.client.get('/hello')
        assert resp.data == b'hello'

    def test_002(self):
        resp = self.client.get('/')
        assert resp.data == b'core index'