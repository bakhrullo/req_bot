from tgbot.models.db import db
from datetime import datetime


class Operator(db.Model):
    __tablename__ = 'operators'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Unicode(), default='noname')


class Counter(db.Model):
    __tablename__ = 'counter'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Unicode(), default='counter')
    count = db.Column(db.Integer(), default=1)
    day = db.Column(db.Integer(), default=int(datetime.now().strftime("%d")))
