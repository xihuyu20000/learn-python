from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def index():
    code ="<script>window.close();</script>"
    return render_template('index.html', code=code)