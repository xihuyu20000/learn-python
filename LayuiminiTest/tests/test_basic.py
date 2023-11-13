from tests import BaseTest


class TestCore(BaseTest):
    def test_001(self):
        resp = self.client.get('/helloworld')
        assert resp.data == b'Hello World!'
