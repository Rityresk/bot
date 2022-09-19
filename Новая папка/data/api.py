import flask
import json
from . import db_session
from flask import request
from .users import Jobs, User
from io import BytesIO
import requests
from PIL import Image

blueprint = flask.Blueprint(
    'api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/user_delete/<int:id>/')
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(User).filter(User.id == id).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    return '1'


@blueprint.route('/api/users', methods=['POST', 'GET'])
def get_news():
    db_session.global_init("db/user.db")
    db_sess = db_session.create_session()
    if flask.request.method == "POST":
        q = ''
        for user in db_sess.query(User).filter(Jobs.id == c):
            q = user
        if q:
            return "Id already exists"
        news = User(surname=request.json['surname'],
                    name=request.json['name'],
                    age=request.json['age'],
                    position=request.json['position'],
                    speciality=request.json['speciality'],
                    address=request.json['address'],
                    email=request.json['email'],
                    hashed_password=request.json['hashed_password'],
                    modified_date=request.json['modified_date']
                    )
        db_sess.add(news)
        db_sess.commit()
    a = []
    for user in db_sess.query(User).all():
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
    return flask.jsonify(a)


@blueprint.route('/api/user/<int:id>')
def get_1(id):
    db_session.global_init("db/user.db")
    db_sess = db_session.create_session()
    t = db_sess.query(User).all()
    if id > len(t):
        return 'Неверный номер'
    for user in db_sess.query(User).filter(User.id == id):
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
    return flask.jsonify(q)


@blueprint.route('/api/redact/<int:id>/', methods=['POST', 'GET'])
def redact(id):
    db_session.global_init("db/user.db")
    db_sess = db_session.create_session()
    j = db_sess.query(User).filter(User.id == id).first()
    surname = request.json['surname']
    name = request.json['name']
    age = request.json['age']
    position = request.json['position']
    speciality = request.json['speciality']
    address = request.json['address']
    email = request.json['email']
    hashed_password = request.json['hashed_password']
    modified_date = request.json['modified_date']
    db_sess.commit()
    return 1

@blueprint.route('/users_show/<int:id>')
def a(id):
    db_session.global_init("db/user.db")
    db_sess = db_session.create_session()
    for user in db_sess.query(User).filter(User.id == id):
        q = user.city_from
        x = user.name + ' ' + user.surname
    if q:
        toponym_to_find = q
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponym_to_find,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        if not response:
            pass
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
        delta = "0.5"
        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": ",".join([delta, delta]),
            "l": "map"
        }
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=map_params)
        map_file = "data/static/map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    return flask.render_template("9.html", user=x, img=map_file)