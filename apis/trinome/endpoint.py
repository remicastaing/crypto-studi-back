from http import HTTPStatus
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, fields

from apis.trinome.dao import TrinomeDAO
from apis.trinome.parser import trinome_reqparser

ns = Namespace('trinomes', description='opérations relatives aux trinomes')

trinome = ns.model('Trinome', {
    'id': fields.String(required=True, description='Reponse'),
    'actuel': fields.Boolean,
    'couts_carbu': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_pneu': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_entretien': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_peage': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'salaires': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'cotisations': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'indemnites': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'autres_couts': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'hh_totales': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'assurances': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'taxes': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_structure': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'nbre_vehicules': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'nbre_jours_roulage': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_journaliers_autres': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_forces_fms': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_forces_horaires': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_forces_journaliers': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_kms': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_horaires': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'couts_journaliers': fields.Fixed(decimals=5, required=True, description='Reponse'),
})

DAO = TrinomeDAO()


@ns.route('/')
class TrinomesList(Resource):
    @ns.doc('list_trinomes')
    @ns.marshal_list_with(trinome)
    def get(self):
        """
        Retourne l'ensemble des trinomes
        """
        return DAO.getAll()

    @ns.doc('create_trinomes')
    @ns.marshal_with(trinome)
    @ns.expect(trinome_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "Un trinome a été créé.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    @ns.response(int(HTTPStatus.CONFLICT), "L'trinome existe déjà.")
    def post(self):
        """ Crée un trinome"""

        trinome_dict = trinome_reqparser.parse_args()

        return DAO.create(trinome_dict)


@ns.route('/<string:id>')
@ns.response(404, "Le trinome n'a pas été trouvé")
@ns.param('id', "L'uuid du trinome")
class Utilisateur(Resource):

    @ns.doc('get_trinome')
    @ns.marshal_with(trinome)
    def get(self, id):
        '''Retourne un trinome'''
        return DAO.get(id)

    @ns.doc('delete_trinome')
    @ns.response(204, 'Trinome supprimé')
    def delete(self, id):
        '''Supprime un trinome'''
        DAO.delete(id)
        return '', 204

    @ns.doc('update_trinomes')
    @ns.marshal_with(trinome)
    @ns.expect(trinome_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "Le trinome a été modifié.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    def put(self, id):
        """ Modifie un trinome"""

        trinome_dict = trinome_reqparser.parse_args()

        return DAO.update(id, trinome_dict)
