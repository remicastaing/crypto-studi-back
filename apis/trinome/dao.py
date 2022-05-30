
from models import db
from models.trinome import Trinome
from datetime import date

arguments = [
               'en_vigeur',
               'couts_carbu',
               'couts_pneu',
               'couts_entretien',
               'couts_peage',
               'salaires',
               'cotisations',
               'indemnites',
               'autres_couts',
               'hh_totales',
               'assurances',
               'taxes',
               'couts_structure',
               'nbre_vehicules',
               'nbre_jours_roulage',
               'couts_journaliers_autres',
               'couts_forces_fms',
               'couts_forces_horaires',
               'couts_forces_journaliers']

class TrinomeDAO():

    def getAll(self):
        return Trinome.query.all()

    def get(self, id):
        res = Trinome.query.get(id)
        print(res)
        return res

    def create(self, data):

        trinome = Trinome()
        trinome.date =date.today()
        for key, value in data.items():
            if key in arguments:
                setattr(trinome, key, value)

        db.session.add(trinome)
        db.session.commit()
        db.session.refresh(trinome)
        return trinome

    def delete(self, id):

        Trinome.query.get(id).delete()
        db.session.commit()

    def update(self, id, data):

        trinome = Trinome.query.get(id)

        trinome.date_creation = date.today()

        for key, value in data.items():
            if key in arguments:
                setattr(trinome, key, value)

        db.session.commit()
        db.session.refresh(trinome)
        return trinome
