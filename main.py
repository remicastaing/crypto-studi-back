from config import ProductionConfig, DevelopmentConfig
from flask import Flask
from models import db
from apis import api
from core.env import is_on_heroku
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


if not(is_on_heroku()):
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
api.init_app(app)

if not(is_on_heroku()):
    app.run(host='0.0.0.0', port=80, debug=True)
