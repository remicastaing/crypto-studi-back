from http import HTTPStatus
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, fields

from apis.operation.dao import OperationDAO
from apis.operation.parser import operation_reqparser

ns = Namespace('operations', description='opérations relatives aux operations')

operation = ns.model('Operation', {
    'id': fields.String(required=True, description='Reponse'),
    'prenom': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'en_vigeur': fields.Fixed(decimals=5, required=True, description='Reponse'),
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

DAO = OperationDAO()


@ns.route('/')
class OperationList(Resource):
    @ns.doc('list_operations')
    @ns.marshal_list_with(operation)
    def get(self):
        """
        Retourne l'ensemble des operations
        """
        return DAO.getAll()

    @ns.doc('create_operations')
    @ns.marshal_with(operation)
    @ns.expect(operation_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "Une operation a été créé.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    @ns.response(int(HTTPStatus.CONFLICT), "L'operation existe déjà.")
    def post(self):
        """ Crée une operation"""

        operation_dict = operation_reqparser.parse_args()

        return DAO.create(operation_dict)


@ns.route('/<string:id>')
@ns.response(404, "L'operation n'a pas été trouvé")
@ns.param('id', "L'uuid de l'operation")
class Operation(Resource):

    @ns.doc('get_operation')
    @ns.marshal_with(operation)
    def get(self, id):
        '''Retourne une operation'''
        return DAO.get(id)

    @ns.doc('delete_operation')
    @ns.response(204, 'Operation supprimé')
    def delete(self, id):
        '''Supprime une operation'''
        DAO.delete(id)
        return '', 204

    @ns.doc('update_operations')
    @ns.marshal_with(operation)
    @ns.expect(operation_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "L'operation a été modifié.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    def put(self, id):
        """ Modifie une operation"""

        operation_dict = operation_reqparser.parse_args()

        return DAO.update(id, operation_dict)
