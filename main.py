import os
from flask import Flask
from apis import api
from core.env import is_on_heroku


app = Flask(__name__)
api.init_app(app)
if is_on_heroku():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
else:
    app.run(host='0.0.0.0', port=80, debug=True)
