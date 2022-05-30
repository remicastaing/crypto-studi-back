from flask_restx import Api

from .hello.endpoint import ns as ns_hello
from .utilisateur.endpoint import ns as ns_utilisateurs
from .trinome.endpoint import ns as ns_trinome
from .operation.endpoint import ns as ns_operation


api = Api(
    title='API TransCompétence',
    version='0.1',
    description="La super géniale API de la ChocolaTeam",
)

api.add_namespace(ns_hello)
api.add_namespace(ns_utilisateurs)
api.add_namespace(ns_trinome)
api.add_namespace(ns_operation)
