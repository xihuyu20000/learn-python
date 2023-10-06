from werkzeug import run_simple, Response


class Application:
    def __call__(self, env, start_response):
        text = '<strong>hello world</strong>'
        resp = Response(text, mimetype='text/html')
        return resp(env, start_response)

app = Application()
run_simple('0.0.0.0', 5000, app)