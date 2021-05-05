from flask import Response
from flask_restplus import Namespace, Resource, fields

from core.command import read_git_log, env_dependency_file

api = Namespace(name='info',
                     description='The set of API to demonstrate the RESTful API information')

commit = api.model('Commit', {
    'commit': fields.String(required=True, description='Commit id'),
    'author': fields.String(required=True, description='Author name'),
    'date': fields.DateTime(required=True, description='Commit date'),
    'message': fields.String(required=True, description='Commit message')
})


@api.route('/changelog/<int:number>')
class Changelog(Resource):
    @staticmethod
    @api.marshal_with(commit)
    def get(number: int = 20):
        """Show changelog as JSON format."""
        return read_git_log(number)


@api.route('/env')
class Environment(Resource):
    @staticmethod
    @api.produces(['text/yaml'])
    def get():
        """Show environment file"""
        return Response(env_dependency_file(), mimetype='text/yaml')
