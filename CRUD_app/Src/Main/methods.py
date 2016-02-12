__author__ = 'rkourav'

import flask.ext.restless
from model import db, app, Profile, Blog

db.create_all()
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Profile, methods=['GET', 'POST', 'DELETE', 'PUT'])
manager.create_api(Blog, methods=['GET', 'POST', 'DELETE', 'PUT'], results_per_page=15)
app.run(threaded=True)
