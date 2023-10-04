import os

from flask import Flask, render_template, request, url_for, session, g, flash, redirect, abort
from markupsafe import escape

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adfadfsadf'
@app.route('/')
def index():
    code ="<font color='red'>hello world!</font>"
    request.args = {'name':'zhagnsan'}
    session['username'] = 'aaaaaaa'
    g.db = 'sqlite3'

    flash('发生一个错误，用户名出错')
    flash('发生一个错误，密码出错')


    return render_template('index.html', code=code)
@app.get('/login')
def login_get():
    return render_template('login.html')
@app.post('/login')
def login_post():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    print(f'用户名{username=}  密码{password=}')

    for fname in request.files.keys():
        request.files[fname].save(fname)
        print('文件名', fname)
    abort(501)
    return redirect(url_for('index'))

@app.errorhandler(501)
def error501(error):
    return '发生了一个501错误'

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



