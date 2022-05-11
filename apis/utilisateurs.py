from flask_restx import Namespace, Resource, fields

from DAO.utilisateurs_DAO import UtilisateurDAO

ns = Namespace('utilisateurs', description='opérations relatives aux utilisateurs')

utilisateur = ns.model('Utilisateur', {
    'id': fields.String(required=True, description='Reponse'),
    'prenom': fields.String(required=True, description='Reponse'),
    'nom': fields.String(required=True, description='Reponse'),
    'email': fields.String(required=True, description='Reponse'),
})

DAO = UtilisateurDAO()


@ns.route('/')
class UtilisateursList(Resource):
    @ns.doc('list_utilisateurs')
    @ns.marshal_list_with(utilisateur)
    def get(self):
        """
        Retourne l'ensemble des utilisateurs
        """
        return DAO.getAll()


@ns.route('/<string:id>')
@ns.response(404, "L'uilisateur n'a pas été trouvé")
@ns.param('id', "L'uuid de l'utilisateur")
class Utilisateur(Resource):
    '''Retourne un seul utilisateur'''
    @ns.doc('get_utilisateur')
    @ns.marshal_with(utilisateur)
    def get(self, id):
        '''Retourne un utilisateur'''
        return DAO.get(id)

    # @ns.doc('delete_todo')
    # @ns.response(204, 'Todo deleted')
    # def delete(self, id):
    #     '''Delete a task given its identifier'''
    #     DAO.delete(id)
    #     return '', 204

    # @ns.expect(todo)
    # @ns.marshal_with(todo)
    # def put(self, id):
    #     '''Update a task given its identifier'''
    #     return DAO.update(id, api.payload)
