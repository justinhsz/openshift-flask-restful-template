from flask_restplus import Api

from .time import time_api

api = Api(
    title='Basic API',
    version='1.0',
    description='A set of API',
)

api.add_namespace(time_api)
