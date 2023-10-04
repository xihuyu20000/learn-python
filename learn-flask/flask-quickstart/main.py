from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def index():
    code ="<script>window.close();</script>"
    return render_template('index.html', code=code)
@app.get('/login')
def login_get():
    return render_template('login.html')
@app.post('/login')
def login_post():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    print(f'用户名{username=}  密码{password=}')
    return url_for('index')

# @app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     if request.method == 'POST':
#         username = request.form.get('username', '')
#         password = request.form.get('password', '')
#         print(f'用户名{username=}  密码{password=}')
#         return None
@app.route('/user/<id>')
def user(id):
    return str(id)