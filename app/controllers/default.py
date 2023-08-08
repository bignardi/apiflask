from flask import render_template
from app import app



@app.route('/')
def sigin():
    return render_template('sigin.html')


@app.route('/index/<user>')
@app.route('/index', defaults={'user':None})
def index(user):
    return render_template('index.html', user=user)


@app.route('/teste')
def teste():
    return render_template('teste.html')