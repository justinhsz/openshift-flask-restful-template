from flask import request
from flask_restx import Namespace, Resource
from werkzeug.datastructures import FileStorage

content_api = Namespace('content', description='a set of example for work with different content type.')

user = content_api.schema_model('User', {
    'properties': {
        'name': {
            'type': 'string'
        },
        'age': {
            'type': 'integer'
        },
    },
    'type': 'object'
})

user_doc = content_api.schema_model('UserDoc', {
    'type': 'object'
})


@content_api.route('/user')
class JsonContentExample(Resource):
    @content_api.expect(user)
    def post(self):
        """create a user (an example to model by json schema)"""
        if request.content_type == 'application/json':
            return request.json, 200
        else:
            return "only support content type: application/json", 415


@content_api.route('/user-document')
class XMLContentExample(Resource):
    def post(self):
        """create a user's document (an example to interact with xml content, swagger doesn't support)"""
        if request.content_type == 'application/xml':
            return request.data, 200
        else:
            return "only support content type: application/xml", 415


upload_parser = content_api.parser()
upload_parser.add_argument('xml_file', location='files', type=FileStorage, required=True)


@content_api.route('/user-document-file')
class XMLContentExample(Resource):
    @content_api.expect(upload_parser)
    def post(self):
        """create a user's document (an example to interact with xml content)"""
        file = request.files['xml_file']
        if file.content_type.endswith('/xml'):
            return "upload successful", 200
        else:
            return "only support content type: */xml", 415
