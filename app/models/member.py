from ..extensions import db
from flask_restful import fields


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    