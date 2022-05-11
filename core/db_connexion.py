import psycopg2
import os
from .env import is_on_heroku


if is_on_heroku():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn  = psycopg2.connect(DATABASE_URL, sslmode='require')
else:
    conn = psycopg2.connect(
        host="localhost",
        database="transcodb",
        user="postgres")

def get_connexion():
  
    return conn

