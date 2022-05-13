from flask_restx import Namespace, Resource, fields

ns = Namespace('hello', description='endpoint de test')

hello = ns.model('Hello', {
    'hello': fields.String(required=True, description='Reponse'),
})

@ns.route('/')
class HelloWorld(Resource):
    @ns.doc('Hello world')
    @ns.marshal_list_with(hello)
    def get(self):
        return {'hello': 'world'}
