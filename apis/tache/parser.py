from flask_restx.reqparse import RequestParser


create_tache_reqparser = RequestParser(bundle_errors=True)

create_tache_reqparser.add_argument(
    "nom",
    type=str,
    location='json',
    required=True,
    nullable=False,
    case_sensitive=True,
)
create_tache_reqparser.add_argument(
    "liste",
    type=str,
    location='json',
    required=True,
    nullable=False,
    case_sensitive=True,
)
create_tache_reqparser.add_argument(
    "statut",
    type=bool,
    location='json',
    required=True,
    nullable=False,
    case_sensitive=True,
)
create_tache_reqparser.add_argument(
    "attribution",
    type=str,
    location='json',
    required=True,
    nullable=False,
)


update_tache_reqparser = RequestParser(bundle_errors=True)

update_tache_reqparser.add_argument(
    "nom",
    type=str,
    location='json',
)
update_tache_reqparser.add_argument(
    "statut",
    type=bool,
    location='json',
)
update_tache_reqparser.add_argument(
    "attribution",
    type=str,
    location='json',
)
