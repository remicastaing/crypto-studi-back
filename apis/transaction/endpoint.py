from http import HTTPStatus
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, fields

from apis.transaction.dao import TransactionDAO
from apis.transaction.parser import create_transaction_reqparser, update_transaction_reqparser

ns = Namespace('transaction', description='opérations relatives aux transaction')

transaction = ns.model('Transaction', {
    'id': fields.String(required=True, description='ID de la transaction'),
    # 'utilisateur': fields.String(required=True, description='ID de l\'utilisateur'),
    'crypto': fields.String(required=True, description='Crypto de la transaction'),
    'date': fields.Date(required=True, description='Date de création de la transaction'),
    'quantite': fields.Fixed(required=True, description='Quantite de crypto transaction'),
    'prix': fields.String(required=True, description='Prix de la transaction'),
})

DAO = TransactionDAO()


@ns.route('/')
class TachesList(Resource):
    @ns.doc('list_transaction')
    @ns.marshal_list_with(transaction)
    def get(self):
        """
        Retourne l'ensemble des transaction
        """
        return DAO.getAll()

    @ns.doc('create_taches')
    @ns.marshal_with(transaction)
    @ns.expect(create_transaction_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "Un transaction a été créé.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    @ns.response(int(HTTPStatus.CONFLICT), "La transaction existe déjà.")
    def post(self):
        """ Crée un transaction"""

        transaction_dict = create_transaction_reqparser.parse_args()
        # utilisateur = transaction_dict['utilisateur']
        utilisateur = '7b3afe16-4a50-42f2-a6fa-32016c3cae07'
        crypto = transaction_dict['crypto']
        date = transaction_dict['date']
        quantite = transaction_dict['quantite']
        prix = transaction_dict['prix']
        return DAO.create(utilisateur, date, crypto, quantite, prix)


@ns.route('/<string:id>')
@ns.response(404, "La transaction n'a pas été trouvée")
@ns.param('id', "L'uuid de la transaction")
class Tache(Resource):

    @ns.doc('get_transaction')
    @ns.marshal_with(transaction)
    def get(self, id):
        '''Retourne un transaction'''
        return DAO.get(id)

    @ns.doc('delete_transaction')
    @ns.response(204, 'Tache supprimée')
    def delete(self, id):
        '''Supprime un transaction'''
        DAO.delete(id)
        return '', 204

    @ns.doc('update_transaction')
    @ns.marshal_with(transaction)
    @ns.expect(update_transaction_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "La transaction a été modifiée.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    def put(self, id):
        """ Modifie un transaction"""

        transaction_dict = update_transaction_reqparser.parse_args()

        utilisateur = '7b3afe16-4a50-42f2-a6fa-32016c3cae07'
        crypto = transaction_dict['crypto']
        quantite = transaction_dict['quantite']
        prix = transaction_dict['prix']
        return DAO.update(id, utilisateur, crypto, quantite, prix)
