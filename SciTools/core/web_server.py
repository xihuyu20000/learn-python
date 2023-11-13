from flask import Flask, render_template

import settings

"""
web服务器，显示组件和大屏
"""
app = Flask(__name__, template_folder='../assets/templates', static_folder='../assets/static')
print(app.jinja_loader.list_templates())


@app.route('/')
def index():
    option = {
        'darkMode': 'auto',
        'colorBy': 'series',
        'title': {
          'text': 'ECharts 入门示例'
        },
        'tooltip': {},
        'legend': {
          'data': ['销量']
        },
        'xAxis': {
          'data': ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
        },
        'yAxis': {},
        'series': [
          {
            'name': '销量',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
          }
        ]
      };
    return render_template('index.html', option=option)


if __name__ == '__main__':
    app.run(debug=True, port=settings.WEB_SERVER_PORT)
