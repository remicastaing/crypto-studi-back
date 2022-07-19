import uuid
from . import db

import uuid


from sqlalchemy import select, func, text, true
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import column_property
from sqlalchemy.ext.hybrid import hybrid_property

from models.tache import Tache

textual_get_avg = text(
    "select floor(avg( (t.statut  = true)::int )*100) as completion from taches t")


class Liste(db.Model):

    __tablename__ = 'listes'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date, nullable=False)

    completion = column_property(
        select(func.count(Tache.id)).
        where(Tache.liste==id).
        where(Tache.statut==True).
        correlate_except(Tache).
        scalar_subquery()
    )

    nb_tache = column_property(
        select(func.count(Tache.id)).
        where(Tache.liste==id).
        correlate_except(Tache).
        scalar_subquery()
    )

    

    def __repr__(self):
        return (
            f"<Liste id={self.id}, nom={self.nom}, date={self.date} completion={self.completion}>"
        )

    # @hybrid_property
    # def completion(self):
    #     return 0
