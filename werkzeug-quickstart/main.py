from werkzeug import run_simple, Response


class Application:
    def __call__(self, env, start_response):
        resp = Response()
        return resp(env, start_response)

# app是一个callable对象
app = Application()
run_simple('0.0.0.0', 5000, app)