from flask_restx import Api

from .hello.endpoint import ns as ns_hello
from .utilisateur.endpoint import ns as ns_utilisateurs
from .liste.endpoint import ns as ns_liste
from .tache.endpoint import ns as ns_tache


api = Api(
    title='API Lalalist',
    version='0.1',
    description="La super géniale API de Lalalist",
)

api.add_namespace(ns_hello)
api.add_namespace(ns_utilisateurs)
api.add_namespace(ns_liste)
api.add_namespace(ns_tache)
