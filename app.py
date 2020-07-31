import os

from flask import Flask
from flask_restful import Api

from instance.config import app_config
from src.resources.user import UserRegister

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.from_object(app_config[os.getenv('APP_ENV')])
app.config.from_pyfile('instance/config.py')

api = Api(app)

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
