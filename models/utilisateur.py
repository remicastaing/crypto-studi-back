from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()


class Utilisateur(Base):

    __tablename__ = 'utilisateur'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prenom = Column(String(), nullable=False)
    nom = Column(String(), nullable=False)

    def __repr__(self):
        return (
            f"<Utilisateur id={self.id}, prenom={self.prenom}, nom={self.nom}>"
        )
