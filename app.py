from flask import Flask
from apis import api


def create_app():
    app = Flask(__name__)
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    api.init_app(app)
    return app


if __name__ == '__main__':
    application = create_app()
    application.run(host="0.0.0.0", port=8080, debug=True)
