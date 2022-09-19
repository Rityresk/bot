from flask import Flask
from flask import url_for, request
app = Flask(__name__)

@app.route('/')
def a():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')