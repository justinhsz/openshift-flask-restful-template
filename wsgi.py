from flask import Flask
from apis import api


def create_app():
    app = Flask(__name__)
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    api.init_app(app)
    return app


application = create_app()

if __name__ == '__main__':
    application.run('127.0.0.1', 8080, debug=True)
    pass
