from flask import Flask
from apis import api
from core.env import is_on_heroku

app = Flask(__name__)
api.init_app(app)
print('test 2')
app.run(debug=not(is_on_heroku()))
