import argparse
from data.users import Jobs, User, LoginForm, News, RegisterForm, AddJob, AddDepartment, Department, Category
from data import db_session, api, rest
from flask import Flask, render_template, redirect, request
import os
from data.rest import api as ai
from requests import get, post, delete
import flask
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify
from data.parser import parser

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)
ai = Api(app)


def abort_if_news_not_found(id):
    session = db_session.create_session()
    news = session.query(User).get(id)
    if not news:
        abort(404, message=f"{id} not found")


class UsersResource(Resource):
    def get(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        news = session.query(User).get(id)
        return jsonify({'users': news.to_dict(
            only=('surname', 'name', 'age',
                  'position', 'speciality',
                  'address', 'email', 'hashed_password', 'modified_date', 'city_from'))})

    def delete(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        news = session.query(User).get(id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        a = []
        for user in session.query(User).all():
            q = {"surname": user.surname,
                 "name": user.name,
                 "age": user.age,
                 "position": user.position,
                 "speciality": user.speciality,
                 "address": user.address,
                 "email": user.email,
                 "hashed_password": user.hashed_password,
                 "modified_date": user.modified_date
                 }
            a.append(q)
        return jsonify(a)

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = User(surname=args['surname'],
                    name=args['name'],
                    age=args['age'],
                    position=args['position'],
                    speciality=args['speciality'],
                    address=args['address'],
                    email=args['email'],
                    hashed_password=args['hashed_password'],
                    modified_date=args['modified_date']
                    )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/')
def bootstrap():
    db_session.global_init("db/user.db")
    check()
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


def check():
    db_session.global_init("db/user.db")
    db_sess = db_session.create_session()
    c = post('http://127.0.0.1:80/api/v2/users',
             json={"surname": "Jons",
                   "name": "Nick",
                   "age": 22,
                   "position": "main ch",
                   "speciality": 'favourite',
                   "address": 'qrr',
                   "email": "crit@ry",
                   "hashed_password": "12",
                   "modified_date": "33",
                   'city-from': "Saint-Petersburg"
                   })
    for i in db_sess.query(User).all():
        print(i.surname)
    print('----')
    c = delete('http://127.0.0.1:80/api/v2/users/3')
    for i in db_sess.query(User).all():
        print(i.surname)
    print('----')
    c = get('http://127.0.0.1:80/api/v2/users')
    for i in db_sess.query(User).all():
        print(i.surname)
    print('----')
    c = get('http://127.0.0.1:80/api/v2/users/2').json()
    print(c['users']['name'])


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


@app.route('/add_department', methods=['GET', 'POST'])
def add_department():
    form = AddDepartment()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Department(
            title=form.title.data,
            chief=form.chief.data,
            members=form.members.data,
            email=form.email.data
        )
        db_sess.add(job)
        db_sess.commit()
        if request.method == 'POST':
            return redirect('/department')
    return render_template('6.html', form=form)


@app.route('/department')
def dep():
    job = Department()
    db_sess = db_session.create_session()
    a = []
    for user in db_sess.query(Department).all():
        a.append(user)
        print(user.chief)
    s = []
    for i in a:
        w = i.chief
        for user in db_sess.query(User).filter(User.id == w):
            s.append(f"{user.name} {user.surname}")
    return render_template('7.html', a=a, s=s)


@app.route('/department_red/<int:id>', methods=['GET', 'POST'])
def edit_dep(id):
    form = AddDepartment()
    if request.method == "POST":
        db_sess = db_session.create_session()
        j = db_sess.query(Department).filter(Department.id == id).first()
        if j:
            j.title = form.title.data
            j.chief = form.chief.data
            j.members = form.members.data
            j.email = form.email.data
            db_sess.commit()
            return redirect('/')
    return render_template('6.html',
                           form=form)


@app.route('/department_delete/<int:id>', methods=['GET', 'POST'])
def dep_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(Department).filter(Department.id == id).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    return redirect('/department')


@app.route('/category', methods=['GET', 'POST'])
def category():
    form = Category()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == form.job.data).first()
        job.category = form.category.data
        db_sess.commit()
        if request.method == 'POST':
            return redirect('/')
    return render_template('8.html', form=form)


if __name__ == '__main__':
    ai.add_resource(rest.UsersListResource, '/api/v2/users')
    ai.add_resource(rest.UsersResource, '/api/v2/users/<int:id>')
    app.run(port=80, host='127.0.0.1')