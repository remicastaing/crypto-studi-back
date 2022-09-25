from flask_restx import Api

from .hello.endpoint import ns as ns_hello
from .cotation.endpoint import ns as ns_cotation
from .transaction.endpoint import ns as ns_transaction
from .valuation.endpoint import ns as ns_valuation
from .cumul.endpoint import ns as ns_cumul


api = Api(
    title='API Crypto Studi',
    version='0.1',
    description="API de l'application Crypto Studi",
)

api.add_namespace(ns_hello)
api.add_namespace(ns_cotation)
api.add_namespace(ns_transaction)
api.add_namespace(ns_valuation)
api.add_namespace(ns_cumul)
