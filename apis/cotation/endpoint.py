from http import HTTPStatus
from flask import current_app
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, fields

from models import db
from models.crypto import Crypto


from services.coinmarketcapService import CoinMarketCapService

ns = Namespace('cotation', description='opérations relatives aux cotation')

cotation = ns.model('Cotation', {
    'crypto': fields.String(required=True, description='Crypto de la cotation'),
    'date': fields.Date(required=True, description='Date de la cotation'),
    'prix': fields.Fixed(required=True, description='Prix de la crypto'),
    'change': fields.Fixed(required=False, description='Evolution de crypto'),
})


@ns.route('/')
class TachesList(Resource):
    @ns.doc('list_cotation')
    @ns.marshal_list_with(cotation)
    def get(self):
        """
        Retourne l'ensemble des cotation
        """

        CMC = CoinMarketCapService(current_app.config['CMC_API_URL'], current_app.config['CMC_API_KEY'])

        cryptos = db.session.query(Crypto).all()

        cotations = CMC.getQuotes(cryptos)

        return cotations
