from tgbot.models.db import db


class Operator(db.Model):
    __tablename__ = 'operators'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Unicode(), default='noname')
