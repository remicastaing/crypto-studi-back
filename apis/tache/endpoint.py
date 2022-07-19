from http import HTTPStatus
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, fields

from apis.tache.dao import TacheDAO
from apis.tache.parser import create_tache_reqparser, update_tache_reqparser

ns = Namespace('taches', description='opérations relatives aux taches')

tache = ns.model('Tache', {
    'id': fields.String(required=True, description='ID de la tâche'),
    'liste': fields.String(required=True, description='ID de la liste'),
    'nom': fields.String(required=True, description='Nom de la tâche'),
    'date': fields.Date(required=True, description='Date de création de la tâche'),
    'statut': fields.Boolean,
    'attribution': fields.String(required=True, description='Personne en charge de la tache'),
})

DAO = TacheDAO()


@ns.route('/')
class TachesList(Resource):
    @ns.doc('list_taches')
    @ns.marshal_list_with(tache)
    def get(self):
        """
        Retourne l'ensemble des taches
        """
        return DAO.getAll()

    @ns.doc('create_taches')
    @ns.marshal_with(tache)
    @ns.expect(create_tache_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "Un tache a été créé.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    @ns.response(int(HTTPStatus.CONFLICT), "La tache existe déjà.")
    def post(self):
        """ Crée un tache"""

        tache_dict = create_tache_reqparser.parse_args()
        nom = tache_dict['nom']
        liste = tache_dict['liste']
        statut = tache_dict['statut']
        attribution = tache_dict['attribution']
        return DAO.create(liste, nom, statut, attribution)


@ns.route('/<string:id>')
@ns.response(404, "La tache n'a pas été trouvée")
@ns.param('id', "L'uuid de la tache")
class Tache(Resource):

    @ns.doc('get_tache')
    @ns.marshal_with(tache)
    def get(self, id):
        '''Retourne un tache'''
        return DAO.get(id)

    @ns.doc('delete_tache')
    @ns.response(204, 'Tache supprimée')
    def delete(self, id):
        '''Supprime un tache'''
        DAO.delete(id)
        return '', 204

    @ns.doc('update_taches')
    @ns.marshal_with(tache)
    @ns.expect(update_tache_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "La tache a été modifiée.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    def put(self, id):
        """ Modifie un tache"""

        tache_dict = update_tache_reqparser.parse_args()

        nom = tache_dict['nom']
        statut = tache_dict['statut']
        attribution = tache_dict['attribution']
        return DAO.update(id, nom, statut, attribution)
