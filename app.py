import os

from flask import Flask

from instance.config import app_config

app = Flask(__name__)

app.config.from_object(app_config[os.getenv('APP_ENV')])
app.config.from_pyfile('instance/config.py')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
