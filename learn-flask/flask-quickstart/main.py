from flask import Flask, render_template

app = Flask(__name__)
print('模板的搜索路径',app.jinja_loader.searchpath)
@app.route('/')
def index():
    return render_template('index.html')