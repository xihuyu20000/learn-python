from flask import Flask, render_template

import settings

"""
web服务器，显示组件和大屏
"""
app = Flask(__name__, template_folder='../assets/templates', static_folder='../assets/static')
print(app.jinja_loader.list_templates())


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=settings.WEB_SERVER_PORT)
