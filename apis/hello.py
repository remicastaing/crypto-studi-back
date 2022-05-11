from flask_restx import Namespace, Resource, fields

api = Namespace('hello', description='endpoint de test')

hello = api.model('Cat', {
    'hello': fields.String(required=True, description='Reponse'),
})

@api.route('/')
class HelloWorld(Resource):
    @api.doc('Hello world')
    @api.marshal_list_with(hello)
    def get(self):
        return {'hello': 'world'}
