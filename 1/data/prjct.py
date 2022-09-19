import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin


class Place(SqlAlchemyBase):
    __tablename__ = 'my_list'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=False)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    coords = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    notes = sqlalchemy.Column(sqlalchemy.String, nullable=True)