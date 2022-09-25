
from flask_restx.reqparse import RequestParser


create_transaction_reqparser = RequestParser(bundle_errors=True)

# create_transaction_reqparser.add_argument(
#     "utilisateur",
#     type=str,
#     location='json',
#     required=True,
#     nullable=False,
#     case_sensitive=True,
# )
create_transaction_reqparser.add_argument(
    "crypto",
    type=str,
    location='json',
    required=True,
    nullable=False,
    case_sensitive=True,
)
create_transaction_reqparser.add_argument(
    "date",
    type=str,
    location='json',
    required=True,
    nullable=False,
    case_sensitive=True,
)
create_transaction_reqparser.add_argument(
    "quantite",
    type=float,
    location='json',
    required=True,
    nullable=False,
    case_sensitive=True,
)
create_transaction_reqparser.add_argument(
    "prix",
    type=float,
    location='json',
    required=True,
    nullable=False,
)


update_transaction_reqparser = RequestParser(bundle_errors=True)

update_transaction_reqparser.add_argument(
    "crypto",
    type=str,
    location='json',
)
update_transaction_reqparser.add_argument(
    "date",
    type=str,
    location='json',
)
update_transaction_reqparser.add_argument(
    "quantite",
    type=float,
    location='json',
)
update_transaction_reqparser.add_argument(
    "prix",
    type=float,
    location='json',
)
