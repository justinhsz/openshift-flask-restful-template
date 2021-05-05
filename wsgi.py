from flask import Flask
from apis import api


def create_app():
    app = Flask(__name__)
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    api.init_app(app)
    return app


application = create_app()

if __name__ == '__main__':
    application.run('0.0.0.0', 8080, debug=True)
    pass
