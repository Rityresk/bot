import argparse
from data.users import Jobs, User, LoginForm, News, RegisterForm, AddJob
from data import db_session
from flask import Flask, render_template, redirect, request
import os
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/')
def bootstrap():
    db_session.global_init("db/user.db")
    job = Jobs()
    db_sess = db_session.create_session()
    a = []
    for user in db_sess.query(Jobs).all():
        a.append(user)
        print(user.team_leader)
    s = []
    for i in a:
        w = i.team_leader
        for user in db_sess.query(User).filter(User.id == w):
            s.append(f"{user.name} {user.surname}")
    return render_template('3.html', a=a, s=s)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('2.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('2.html', title='Авторизация', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('4.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('4.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        if request.method == 'POST':
            return redirect('/login')
    return render_template('4.html', title='Регистрация', form=form)


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    form = AddJob()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        e = False if form.is_finished.data == "False" else True
        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            is_finished=e
        )
        db_sess.add(job)
        db_sess.commit()
        if request.method == 'POST':
            return redirect('/')
    return render_template('5.html', title='Регистрация', form=form)


@app.route('/job/<int:id>', methods=['GET', 'POST'])
def edit_news(id):
    form = AddJob()
    if request.method == "POST":
        db_sess = db_session.create_session()
        j = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if j:
            e = False if form.is_finished.data == "False" else True
            j.team_leader = form.team_leader.data
            j.job = form.job.data
            j.work_size = form.work_size.data
            j.collaborators = form.collaborators.data
            j.start_date = form.start_date.data
            j.end_date = form.end_date.data
            j.is_finished = e
            db_sess.commit()
            return redirect('/')
    return render_template('5.html',
                           form=form)


@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).filter(Jobs.id == id).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(port=80, host='127.0.0.1')