from .database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    banned = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)   # <-- this should exist
    role = db.Column(db.String(10), default='user')  # 'admin' or 'user'


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    filename = db.Column(db.String(255), nullable=False)
    similarity_score = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

