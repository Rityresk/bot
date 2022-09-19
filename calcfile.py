import argparse
from data.users import Jobs, User, RegisterForm
from data import db_session
from flask import Flask, render_template, redirect, request, make_response, session
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
@app.route("/")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")

if __name__ == "__main__":
    app.run(port=80, host='127.0.0.1')