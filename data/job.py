from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify
from . import db_session
from .parser import parser
from .users import Jobs

app = Flask(__name__)
api = Api(app)


def abort_if_news_not_found(id):
    session = db_session.create_session()
    news = session.query(Jobs).get(id)
    if not news:
        abort(404, message=f"{id} not found")


class JobsResource(Resource):
    def get(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        news = session.query(Jobs).get(id)
        return jsonify({'jobs': news.to_dict(
            only=('team_leader', 'job', 'work_size',
                  'collaborators', 'start_date',
                  'category', 'end_date', 'is_finished'))})

    def delete(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        news = session.query(Jobs).get(id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        a = []
        for user in session.query(Jobs).all():
            q = {"team_leader": user.team_leader,
                 "job": user.job,
                 "work_size": user.work_size,
                 "collaborators": user.collaborators,
                 "start_date": user.start_date,
                 'category': user.category,
                 "end_date": user.end_date,
                 "is_finished": user.is_finished
                 }
            a.append(q)
        return jsonify(a)

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = Jobs(team_leader=args['team_leader'],
                    job=args['job'],
                    work_size=args['work_size'],
                    collaborators=args['collaborators'],
                    start_date=args['start_date'],
                    category=args['category'],
                    end_date=args['end_date'],
                    is_finished=args['is_finished'])
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})