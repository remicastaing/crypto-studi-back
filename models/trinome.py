import uuid
from xml.etree.ElementPath import prepare_parent
from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Trinome(db.Model):

    __tablename__ = 'trinomes'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = db.Column(db.Date, nullable=False)
    actuel = db.Column(db.Boolean, nullable=False)
    couts_carbu = db.Column(db.Numeric, nullable=False)
    couts_pneu = db.Column(db.Numeric, nullable=False)
    couts_entretien = db.Column(db.Numeric, nullable=False)
    couts_peage = db.Column(db.Numeric, nullable=False)
    salaires = db.Column(db.Numeric, nullable=False)
    cotisations = db.Column(db.Numeric, nullable=False)
    indemnites = db.Column(db.Numeric, nullable=False)
    autres_couts = db.Column(db.Numeric, nullable=False)
    hh_totales = db.Column(db.Numeric, nullable=False)
    assurances = db.Column(db.Numeric, nullable=False)
    taxes = db.Column(db.Numeric, nullable=False)
    couts_structure = db.Column(db.Numeric, nullable=False)
    nbre_vehicules = db.Column(db.Numeric, nullable=False)
    nbre_jours_roulage = db.Column(db.Numeric, nullable=False)

    couts_journaliers_autres = db.Column(db.Numeric, nullable=False)
    couts_forces_fms = db.Column(db.Numeric, nullable=False)
    couts_forces_horaires = db.Column(db.Numeric, nullable=False)
    couts_forces_journaliers = db.Column(db.Numeric, nullable=False)

    def __repr__(self):
        return (
            f"<Trinome id={self.id}, date={self.date}, actuel={self.en_vigeur}>"
        )

    @property
    def couts_kms(self):
        return self.couts_pneu + self.couts_carbu + self.couts_entretien + self.couts_peage

    @property
    def couts_horaires(self):
        return (self.salaires + self.cotisations + self.indemnites + self.autres_couts) / self.hh_totales

    @property
    def couts_journaliers(self):
        return (self.assurances + self.taxes + self.couts_structure) / self.nbre_vehicules / self.nbre_jours_roulage
