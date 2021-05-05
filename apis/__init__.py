from flask_restplus import Api

from .time import time_api
from .info import api as info_api

api = Api(
    title='Basic API',
    version='1.0',
    description='A set of API',
)

api.add_namespace(time_api)
api.add_namespace(info_api)
