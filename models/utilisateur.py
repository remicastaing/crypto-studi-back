import uuid
from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Utilisateur(db.Model):

    __tablename__ = 'utilisateurs'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prenom = db.Column(db.String(), nullable=False)
    nom = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return (
            f"<Utilisateur id={self.id}, prenom={self.prenom}, nom={self.nom}, email={self.email}>"
        )
