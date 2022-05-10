from flask import Flask
from flask_restx import Resource, Api
import os
import psycopg2

on_heroku = False
if 'ENVIRONNEMENT' in os.environ:
  on_heroku = True


if on_heroku:
  DATABASE_URL = os.environ['DATABASE_URL']
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
else:
  conn = psycopg2.connect(
    host="localhost",
    database="transcodb",
    user="postgres")

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/environnement')
class GetMain(Resource):
    def get(self):
        return {'prod': on_heroku}

if __name__ == '__main__':
    app.run(debug=True)