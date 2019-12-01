from flask import Flask
from apis import api

app = Flask(__name__)
api.init_app(app)

app.run(port=8080, debug=True)
