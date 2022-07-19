from http import HTTPStatus
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, fields

from apis.utilisateur.dao import UtilisateurDAO
from apis.tache.dao import TacheDAO

from apis.tache.endpoint import tache

from apis.utilisateur.parser import create_utilisateur_reqparser, update_utilisateur_reqparser

ns = Namespace('utilisateurs', description='opérations relatives aux utilisateurs')

utilisateur = ns.model('Utilisateur', {
    'id': fields.String(required=True, description='Reponse'),
    'prenom': fields.String(required=True, description='Reponse'),
    'nom': fields.String(required=True, description='Reponse'),
    'email': fields.String(required=True, description='Reponse'),
})

DAO = UtilisateurDAO()
TDAO = TacheDAO()


@ns.route('/')
class UtilisateursList(Resource):
    @ns.doc('list_utilisateurs')
    @ns.marshal_list_with(utilisateur)
    def get(self):
        """
        Retourne l'ensemble des utilisateurs
        """
        return DAO.getAll()

    @ns.doc('create_utilisateurs')
    @ns.marshal_with(utilisateur)
    @ns.expect(create_utilisateur_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "Un utilisateur a été créé.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    @ns.response(int(HTTPStatus.CONFLICT), "L'utilisateur existe déjà.")
    def post(self):
        """ Crée un utilisateur"""

        utilisateur_dict = create_utilisateur_reqparser.parse_args()
        prenom = utilisateur_dict['prenom']
        nom = utilisateur_dict['nom']
        email = utilisateur_dict['email']
        return DAO.create(prenom, nom, email)


@ns.route('/<string:id>')
@ns.response(404, "L'utilisateur n'a pas été trouvé")
@ns.param('id', "L'uuid de l'utilisateur")
class Utilisateur(Resource):

    @ns.doc('get_utilisateur')
    @ns.marshal_with(utilisateur)
    def get(self, id):
        '''Retourne un utilisateur'''
        return DAO.get(id)

    @ns.doc('delete_utilisateur')
    @ns.response(204, 'Utilisateur supprimé')
    def delete(self, id):
        '''Supprime un utilisateur'''
        DAO.delete(id)
        return '', 204

    @ns.doc('update_utilisateurs')
    @ns.marshal_with(utilisateur)
    @ns.expect(update_utilisateur_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "L'utilisateur a été modifié.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    def put(self, id):
        """ Modifie un utilisateur"""

        utilisateur_dict = update_utilisateur_reqparser.parse_args()

        prenom = utilisateur_dict['prenom']
        nom = utilisateur_dict['nom']
        email = utilisateur_dict['email']
        return DAO.update(id, prenom, nom, email)

@ns.route('/<string:id>/taches')
@ns.response(404, "L'utilisateur n'a pas été trouvé")
@ns.param('id', "L'uuid de l'utilisateur")
class Tache(Resource):

    @ns.doc('list_taches_par_utilisateur')
    @ns.marshal_list_with(tache)
    def get(self, id):
        """
        Retourne l'ensemble des utilisateurs
        """
        return TDAO.getAllFor(id)