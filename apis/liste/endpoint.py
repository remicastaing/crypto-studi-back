from http import HTTPStatus
from flask_restx import Namespace, Resource, fields
from flask_cors import cross_origin
from apis.liste.dao import ListeDAO
from apis.liste.parser import create_liste_reqparser, update_liste_reqparser
from apis.tache.endpoint import tache

ns = Namespace('listes', description='opérations relatives aux listes')

liste = ns.model('Liste', {
    'id': fields.String(required=True, description='ID de la liste'),
    'nom': fields.String(required=True, description='Nom de la liste'),
    'date': fields.Date(required=True, description='Date de création de la liste'),
    'nb_tache': fields.Integer(min=0, max=100, description='Nombre de taches'),
    'completion': fields.Integer(min=0, max=100, description='Nombre de taches complétées'),
})

DAO = ListeDAO()


@ns.route('/')
class ListesList(Resource):
    @ns.doc('list_listes')
    @ns.marshal_list_with(liste)
    def get(self):
        """
        Retourne l'ensemble des listes
        """
        res = DAO.getAll()
        return res

    @ns.doc('create_liste')
    @ns.marshal_with(liste)
    @ns.expect(create_liste_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "Une liste a été créée.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    @ns.response(int(HTTPStatus.CONFLICT), "La liste existe déjà.")
    def post(self):
        """ Crée un liste"""

        liste_dict = create_liste_reqparser.parse_args()
        nom = liste_dict['nom']
        return DAO.create(nom)


@ns.route('/<string:id>')
@ns.response(404, "La liste n'a pas été trouvée")
@ns.param('id', "L'uuid de la liste")
class Liste(Resource):

    @ns.doc('get_liste')
    @ns.marshal_with(liste)
    def get(self, id):
        '''Retourne une liste'''
        return DAO.get(id)

    @ns.doc('delete_liste')
    @ns.response(204, 'Liste supprimé')
    def delete(self, id):
        '''Supprime une liste'''
        DAO.delete(id)
        return '', 204

    @ns.doc('update_listes')
    @ns.marshal_with(liste)
    @ns.expect(update_liste_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "La liste a été modifiée.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    def put(self, id):
        """ Modifie une liste"""

        liste_dict = update_liste_reqparser.parse_args()

        nom = liste_dict['nom']

        return DAO.update(id, nom)


@ns.route('/<string:id>/taches')
@ns.response(404, "La liste n'a pas été trouvée")
@ns.param('id', "L'uuid de la liste")
class ListeTaches(Resource):

    @ns.doc('get_liste')
    @ns.marshal_with(tache)
    def get(self, id):
        '''Retourne une liste'''
        return DAO.getTaches(id)
