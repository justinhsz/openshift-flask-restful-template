from flask_restx import Api

from .time import time_api
from .content import content_api

api = Api(
    title='Basic API',
    version='1.0',
    description='A set of API',
)

api.add_namespace(time_api)
api.add_namespace(content_api)
