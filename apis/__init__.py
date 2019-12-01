from flask_restplus import Api

from .time import api as time

api = Api(
    title='Basic API',
    version='1.0',
    description='A set of API',
)

api.add_namespace(time)