from flask_restx import Api

from .hello import api as ns_hello 
from .utilisateurs import api as ns_utilisateurs


api = Api(
    title='API TransCompétence',
    version='0.1',
    description="La super géniale API de la ChocolaTeam",
)

api.add_namespace(ns_hello)
api.add_namespace(ns_utilisateurs)
