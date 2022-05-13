import re
# from flask_restx import inputs
from flask_restx.reqparse import RequestParser


def utilisateur_nom(nom):
    """Methode pour valider le format d'un nom ou prénom (lettre, tiret et apostrophe)"""
    if not re.compile(r"/^[a-z ,.'-]+$/i").match(nom):
        raise ValueError(
            f"'{nom}' ne correspond pas à un nom ou un prénom."
        )
    return nom


create_utilisateur_reqparser = RequestParser(bundle_errors=True)

create_utilisateur_reqparser.add_argument(
    "nom",
    type=str,
    location="form",
    required=True,
    nullable=False,
    case_sensitive=True,
)
create_utilisateur_reqparser.add_argument(
    "prenom",
    type=str,
    location="form",
    required=True,
    nullable=False,
    case_sensitive=True,
)
create_utilisateur_reqparser.add_argument(
    "email",
    # type=inputs.email,
    location="form",
    required=True,
    nullable=False,
)
