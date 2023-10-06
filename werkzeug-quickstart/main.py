from collections import defaultdict

import jinja2
from werkzeug import run_simple, Response, Request

url_map = defaultdict(str)
url_map['/'] = 'index.html'
url_map['/user'] = 'user.html'

class Application:
    def __init__(self):
        self.jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'), autoescape=True)
        print('模板', self.jinja_env.loader.list_templates())

    def __call__(self, env, start_response):
        req = Request(env)
        print('请求路径', req.path)
        template_name = url_map.get(req.path, 'index.html')
        text = self.jinja_env.get_template(template_name).render()
        resp = Response(text, mimetype='text/html')
        return resp(env, start_response)

app = Application()
run_simple('0.0.0.0', 5000, app)