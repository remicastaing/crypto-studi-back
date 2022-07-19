from flask_restx.reqparse import RequestParser


create_liste_reqparser = RequestParser(bundle_errors=True)

create_liste_reqparser.add_argument(
    "nom",
    type=str,
    location='json',
    required=True,
    nullable=False,
    case_sensitive=True,
)



update_liste_reqparser = RequestParser(bundle_errors=True)

update_liste_reqparser.add_argument(
    "nom",
    type=str,
    location='json',
)

