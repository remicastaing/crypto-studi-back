from http import HTTPStatus
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, fields

from apis.operation.dao import OperationDAO
from apis.operation.parser import operation_reqparser

ns = Namespace('operations', description='opérations relatives aux operations')

operation = ns.model('Operation', {
    'id': fields.String(required=True, description='Reponse'),
    'trinome': fields.String(required=True, description='Reponse'),
    'commercial': fields.String(required=True, description='Reponse'),
    'date': fields.DateTime(dt_format='rfc822'),
    'avant_kms': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'avant_peages': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'avant_tps': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'aller_kms': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'aller_peages': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'aller_tps': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'retour_kms': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'retour_peages': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'retour_tps': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'apres_kms': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'apres_peages': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'apres_tps': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'chargement_tps': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'dechargement_tps': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'chargement_unite': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'chargement_qtt_totale': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'chargement_par_tour': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'nbr_tours_possibles': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'km_total': fields.Fixed(decimals=5, required=True, description='Reponse'),
    'tps_service_necessaire': fields.Fixed(decimals=5, required=True, description='Reponse'),
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
