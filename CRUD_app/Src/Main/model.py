__author__ = 'rkourav'


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False, unique=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, nullable=False, unique=True)
    include_columns = ['id', 'username', 'name', 'email']

    def __repr__(self):
        return '<User %r>' % self.name


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    u_id = db.Column(db.Integer, ForeignKey=True)
    text = db.Column(db.String(1024))
    profiles = db.relationship('Profile', backref=db.backref('blogs'))
    include_columns = ['id', 'username', 'email']
