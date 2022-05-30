import uuid
from xml.etree.ElementPath import prepare_parent

from sqlalchemy import ForeignKey
from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


temps_travail_journalier = 8

class Operation(db.Model):

    __tablename__ = 'operations'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    trinome = db.Column(UUID(as_uuid=True), ForeignKey("trinomes.id"))
    commercial = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date, nullable=False)

    avant_kms = db.Column(db.Numeric, nullable=False)
    avant_peages = db.Column(db.Numeric, nullable=False)
    avant_tps = db.Column(db.Numeric, nullable=False)

    aller_kms = db.Column(db.Numeric, nullable=False)
    aller_peages = db.Column(db.Numeric, nullable=False)
    aller_tps = db.Column(db.Numeric, nullable=False)

    retour_kms = db.Column(db.Numeric, nullable=False)
    retour_peages = db.Column(db.Numeric, nullable=False)
    retour_tps = db.Column(db.Numeric, nullable=False)

    apres_kms = db.Column(db.Numeric, nullable=False)
    apres_peages = db.Column(db.Numeric, nullable=False)
    apres_tps = db.Column(db.Numeric, nullable=False)

    chargement_tps = db.Column(db.Numeric, nullable=False)
    dechargement_tps = db.Column(db.Numeric, nullable=False)

    chargement_unite = db.Column(db.Numeric, nullable=False)
    chargement_qtt_totale = db.Column(db.Numeric, nullable=False)
    chargement_par_tour = db.Column(db.Numeric, nullable=False)



    def __repr__(self):
        return (
            f"<Operation id={self.id}, date={self.date}>"
        )

    @property
    def nbr_tours_possibles(self):
        return round((temps_travail_journalier - self.avant_tps - self.apres_tps + self.retour_tps) / (self.chargement_tps + self.aller_tps + self.dechargement_tps + self.retour_tps))



    @property
    def km_total(self):
        return self.avant_kms + self.nbr_tours_possibles * self.aller_kms + (self.nbr_tours_possibles - 1) * self.retour_kms + self.apres_kms

    @property
    def tps_service_necessaire(self):
        return self.avant_tps + self.nbr_tours_possibles * (self.chargement_tps + self.aller_tps + self.dechargement_tps)\
            + (self.nbr_tours_possibles - 1) * self.retour_tps + self.apres_tps

