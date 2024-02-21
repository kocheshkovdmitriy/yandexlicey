import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    #OneToOne, ForeignKey, ManyToMany
    user_name = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.name"))
    user = orm.relationship('User')

    def __repr__(self):
        return f'"{self.title}" author: {self.user.name}{self.user.lastname}'