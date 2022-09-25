
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, fields

from apis.valuation.dao import ValuationDAO


from models import db

ns = Namespace('valuation', description='valuation actuelle du portefeuille de crypto')

valuation = ns.model('Valuation', {
    'crypto': fields.String(required=True, description='Crypto de la valuation'),
    'nom': fields.String(required=False, description='Nom de la crypto'),
    'quantite': fields.Fixed(required=True, description='Quantite de crypto à cette date'),
    'valuation': fields.Fixed(required=True, description='Valuation'),
    'change': fields.Fixed(required=False, description='Evolution de crypto'),
})

DAO = ValuationDAO()


@ns.route('/')
class ValuationList(Resource):
    @ns.doc('list_valuation')
    @ns.marshal_list_with(valuation)
    def get(self):
        """
        Retourne l'ensemble des valuations
        """

        return DAO.get()
