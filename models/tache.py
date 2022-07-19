import uuid
from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Tache(db.Model):

    __tablename__ = 'taches'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    liste = db.Column(UUID(as_uuid=True), db.ForeignKey('listes.id'))
    nom = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date, nullable=False)
    statut = db.Column(db.Boolean, nullable=False)
    attribution = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return (
            f"<Tache id={self.id}, nom={self.nom}, date={self.date}>, statue={self.statut}"
        )
