import os


on_heroku = False
if 'ENVIRONNEMENT' in os.environ:
  on_heroku = True


def is_on_heroku():
    return on_heroku