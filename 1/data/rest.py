from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify
from . import db_session
from .parser import parser
from .users import User

app = Flask(__name__)
api = Api(app)


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