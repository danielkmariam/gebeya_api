import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from instance.config import app_config
from src.resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config.from_object(app_config[os.getenv('APP_ENV')])
app.config.from_pyfile('instance/config.py')

api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from src.db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
