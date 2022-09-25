from http import HTTPStatus
from flask import current_app
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, fields
from apis.cumul.dao import CumulDAO
from models.crypto import Crypto

from models import db

ns = Namespace('cumul', description='cumul des transaction')


cumul = ns.model('Cumul', {
    'date': fields.Date(required=True, description='Date de la valuation'),
    'crypto': fields.String(required=True, description='Crypto de la valuation'),
    'cotation': fields.Fixed(required=True, description='Cotation de crypto à cette date'),
    'quantite': fields.Fixed(required=True, description='Quantite de crypto à cette date'),
    'valuation': fields.Fixed(required=True, description='Valuation'),
    'achat': fields.Fixed(required=True, description='Achat cumulé à cette date'),
    'gain': fields.Fixed(required=True, description='Gain à cette date'), 
})

DAO = CumulDAO()


@ns.route('/')
class CumulList(Resource):
    @ns.doc('cumul')
    @ns.marshal_list_with(cumul)
    def get(self):
        """
        Retourne le cumuls de l'ensemble des transactions par date.
        """

        return DAO.get()


@ns.route('/<string:crypto>')
@ns.response(404, "Le cumul n'a pas été trouvée")
@ns.param('crypto', "La crypto du cumul des transactions")
class Tache(Resource):

    @ns.doc('get_transaction')
    @ns.marshal_with(cumul)
    def get(self, crypto):
        '''Retourne un transaction'''
        return DAO.getByCrypto(crypto)
